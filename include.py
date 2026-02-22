#!/usr/bin/env python3
"""
include.py - File inclusion system for Markdown list files.

Scans Markdown list files (list-*.md) for INCLUDE placeholders and replaces
their content with the content from the corresponding file in the inc/ directory.

Placeholder format in Markdown files:

    <!-- INCLUDE filename.md -->
    ... existing content (will be replaced) ...
    <!-- END INCLUDE -->

The source file is looked up as inc/filename.md relative to this script.

Usage:
    ./include.py                           Process all includes in all list files.
    ./include.py --section guis            Process only includes named 'guis'.
    ./include.py --section guis monitoring Process 'guis' and 'monitoring' includes.
    ./include.py --check                   Check mode: exit 1 if any file would change.
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple

INCLUDE_PATTERN = re.compile(
    r'(<!-- INCLUDE (\S+) -->)\n(.*?)(<!-- END INCLUDE -->)',
    re.DOTALL,
)


def get_inc_content(inc_dir: Path, filename: str) -> str:
    """Read and return content from the inc/ directory."""
    inc_path = inc_dir / filename
    if not inc_path.exists():
        print(
            f"Error: Include file not found: {inc_path}",
            file=sys.stderr,
        )
        sys.exit(1)
    content = inc_path.read_text(encoding='utf-8')
    if not content.endswith('\n'):
        content += '\n'
    return content


def process_content(
    content: str,
    inc_dir: Path,
    sections: Optional[List[str]] = None,
) -> str:
    """Replace all INCLUDE blocks in content with the corresponding inc files."""

    def replace_include(match: re.Match) -> str:
        start_marker = match.group(1)
        filename = match.group(2)
        end_marker = match.group(4)

        section_name = Path(filename).stem
        if sections is not None and section_name not in sections:
            return match.group(0)

        inc_content = get_inc_content(inc_dir, filename)
        return f"{start_marker}\n{inc_content}{end_marker}"

    return INCLUDE_PATTERN.sub(replace_include, content)


def process_file(
    filepath: Path,
    inc_dir: Path,
    sections: Optional[List[str]] = None,
) -> Tuple[str, bool]:
    """Process a single Markdown file; return (new_content, changed)."""
    original = filepath.read_text(encoding='utf-8')
    new_content = process_content(original, inc_dir, sections)
    return new_content, new_content != original


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Replace INCLUDE placeholders in Markdown list files.',
    )
    parser.add_argument(
        '--section',
        nargs='+',
        metavar='SECTION',
        help=(
            'Only process includes whose source filename (without extension) '
            'matches one of these section names. Example: guis web-interfaces'
        ),
    )
    parser.add_argument(
        '--check',
        action='store_true',
        help=(
            'Check mode: print files that would change and exit with code 1 '
            'if any would change, without modifying any file.'
        ),
    )
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    inc_dir = script_dir / 'inc'

    if not inc_dir.is_dir():
        print(f"Error: Include directory not found: {inc_dir}", file=sys.stderr)
        sys.exit(1)

    list_files = sorted(script_dir.glob('list-*.md'))
    if not list_files:
        print("Warning: No list-*.md files found.", file=sys.stderr)

    any_changed = False
    for filepath in list_files:
        new_content, changed = process_file(filepath, inc_dir, args.section)
        if changed:
            any_changed = True
            if args.check:
                print(f"Would update: {filepath.name}")
            else:
                filepath.write_text(new_content, encoding='utf-8')
                print(f"Updated: {filepath.name}")

    if args.check:
        if any_changed:
            print(
                "\nError: Some files are not up-to-date with their includes.\n"
                "Run ./include.py to update them.",
                file=sys.stderr,
            )
            sys.exit(1)
        else:
            print("All includes are up-to-date.")
    elif not any_changed:
        print("All includes are already up-to-date.")


if __name__ == '__main__':
    main()
