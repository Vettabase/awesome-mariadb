#!/usr/bin/env python3
"""Unit tests for include.py"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

# Ensure include.py is importable from the repository root
sys.path.insert(0, str(Path(__file__).parent))

from include import INCLUDE_PATTERN, process_content, process_file


class TestIncludePattern(unittest.TestCase):
    """Tests for the INCLUDE_PATTERN regex."""

    def test_matches_include_block(self):
        text = "<!-- INCLUDE foo.md -->\nsome content\n<!-- END INCLUDE -->"
        m = INCLUDE_PATTERN.search(text)
        self.assertIsNotNone(m)
        self.assertEqual(m.group(2), 'foo.md')

    def test_matches_empty_include_block(self):
        text = "<!-- INCLUDE foo.md -->\n<!-- END INCLUDE -->"
        m = INCLUDE_PATTERN.search(text)
        self.assertIsNotNone(m)
        self.assertEqual(m.group(3), '')

    def test_matches_multiline_content(self):
        text = "<!-- INCLUDE foo.md -->\nline1\nline2\nline3\n<!-- END INCLUDE -->"
        m = INCLUDE_PATTERN.search(text)
        self.assertIsNotNone(m)
        self.assertIn('line2', m.group(3))

    def test_no_match_without_newline_after_open(self):
        text = "<!-- INCLUDE foo.md --><!-- END INCLUDE -->"
        m = INCLUDE_PATTERN.search(text)
        self.assertIsNone(m)

    def test_multiple_blocks(self):
        text = (
            "<!-- INCLUDE a.md -->\nA content\n<!-- END INCLUDE -->\n"
            "<!-- INCLUDE b.md -->\nB content\n<!-- END INCLUDE -->"
        )
        matches = INCLUDE_PATTERN.findall(text)
        self.assertEqual(len(matches), 2)
        filenames = [m[1] for m in matches]
        self.assertIn('a.md', filenames)
        self.assertIn('b.md', filenames)


class TestProcessContent(unittest.TestCase):
    """Tests for the process_content function."""

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.inc_dir = Path(self.tmpdir.name)
        (self.inc_dir / 'foo.md').write_text('Hello from foo\n')
        (self.inc_dir / 'bar.md').write_text('Hello from bar\n')

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_replaces_stale_content(self):
        content = "<!-- INCLUDE foo.md -->\nOLD\n<!-- END INCLUDE -->"
        result = process_content(content, self.inc_dir)
        self.assertNotIn('OLD', result)
        self.assertIn('Hello from foo', result)

    def test_preserves_markers(self):
        content = "<!-- INCLUDE foo.md -->\nOLD\n<!-- END INCLUDE -->"
        result = process_content(content, self.inc_dir)
        self.assertIn('<!-- INCLUDE foo.md -->', result)
        self.assertIn('<!-- END INCLUDE -->', result)

    def test_idempotent(self):
        content = "<!-- INCLUDE foo.md -->\nOLD\n<!-- END INCLUDE -->"
        result1 = process_content(content, self.inc_dir)
        result2 = process_content(result1, self.inc_dir)
        self.assertEqual(result1, result2)

    def test_replaces_empty_block(self):
        content = "<!-- INCLUDE foo.md -->\n<!-- END INCLUDE -->"
        result = process_content(content, self.inc_dir)
        self.assertIn('Hello from foo', result)

    def test_section_filter_matches(self):
        content = "<!-- INCLUDE foo.md -->\nOLD\n<!-- END INCLUDE -->"
        result = process_content(content, self.inc_dir, sections=['foo'])
        self.assertNotIn('OLD', result)
        self.assertIn('Hello from foo', result)

    def test_section_filter_skips_non_matching(self):
        content = "<!-- INCLUDE foo.md -->\nOLD\n<!-- END INCLUDE -->"
        result = process_content(content, self.inc_dir, sections=['bar'])
        self.assertIn('OLD', result)
        self.assertNotIn('Hello from foo', result)

    def test_section_filter_multiple_sections(self):
        content = (
            "<!-- INCLUDE foo.md -->\nOLD_FOO\n<!-- END INCLUDE -->\n"
            "<!-- INCLUDE bar.md -->\nOLD_BAR\n<!-- END INCLUDE -->"
        )
        result = process_content(content, self.inc_dir, sections=['foo', 'bar'])
        self.assertNotIn('OLD_FOO', result)
        self.assertNotIn('OLD_BAR', result)
        self.assertIn('Hello from foo', result)
        self.assertIn('Hello from bar', result)

    def test_section_filter_partial(self):
        content = (
            "<!-- INCLUDE foo.md -->\nOLD_FOO\n<!-- END INCLUDE -->\n"
            "<!-- INCLUDE bar.md -->\nOLD_BAR\n<!-- END INCLUDE -->"
        )
        result = process_content(content, self.inc_dir, sections=['foo'])
        self.assertNotIn('OLD_FOO', result)
        self.assertIn('OLD_BAR', result)

    def test_no_section_filter_replaces_all(self):
        content = (
            "<!-- INCLUDE foo.md -->\nOLD_FOO\n<!-- END INCLUDE -->\n"
            "<!-- INCLUDE bar.md -->\nOLD_BAR\n<!-- END INCLUDE -->"
        )
        result = process_content(content, self.inc_dir)
        self.assertNotIn('OLD_FOO', result)
        self.assertNotIn('OLD_BAR', result)

    def test_surrounding_content_preserved(self):
        content = (
            "## Section\n\n"
            "<!-- INCLUDE foo.md -->\nOLD\n<!-- END INCLUDE -->\n\n"
            "## Next Section"
        )
        result = process_content(content, self.inc_dir)
        self.assertIn('## Section', result)
        self.assertIn('## Next Section', result)

    def test_missing_inc_file_exits(self):
        content = "<!-- INCLUDE missing.md -->\nOLD\n<!-- END INCLUDE -->"
        with self.assertRaises(SystemExit) as ctx:
            process_content(content, self.inc_dir)
        self.assertEqual(ctx.exception.code, 1)

    def test_content_without_includes_unchanged(self):
        content = "# A heading\n\nSome content.\n"
        result = process_content(content, self.inc_dir)
        self.assertEqual(content, result)


class TestProcessFile(unittest.TestCase):
    """Tests for the process_file function."""

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.inc_dir = Path(self.tmpdir.name)
        (self.inc_dir / 'foo.md').write_text('Fresh content\n')

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_reports_changed_when_stale(self):
        md = Path(self.tmpdir.name) / 'list-test.md'
        md.write_text("<!-- INCLUDE foo.md -->\nOLD\n<!-- END INCLUDE -->")
        _, changed = process_file(md, self.inc_dir)
        self.assertTrue(changed)

    def test_reports_unchanged_when_current(self):
        md = Path(self.tmpdir.name) / 'list-test.md'
        md.write_text(
            "<!-- INCLUDE foo.md -->\nFresh content\n<!-- END INCLUDE -->"
        )
        _, changed = process_file(md, self.inc_dir)
        self.assertFalse(changed)

    def test_returns_new_content(self):
        md = Path(self.tmpdir.name) / 'list-test.md'
        md.write_text("<!-- INCLUDE foo.md -->\nOLD\n<!-- END INCLUDE -->")
        new_content, _ = process_file(md, self.inc_dir)
        self.assertIn('Fresh content', new_content)


if __name__ == '__main__':
    unittest.main()
