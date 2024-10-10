# Awesome MariaDB Internals and Plugins Development

A curated list of awesome MariaDB resources, maintained by [Vettabase](https://vettabase.com) and sponsored by the [MariaDB Foundation](https://mariadb.org/).

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) Inspired by the `awesome-*` trend on GitHub.

This list is intended for internals developers. There are lists intended for other audiences. See [README.md](README.md).

## Contents

- [Articles](#articles)
- [Tools](#tools)

See the [key](#key) for explanations of the terms used in this list.

## Articles

* **[Quick builds and rebuilds of MariaDB using Docker](https://optimizedbyotto.com/post/quick-builds-and-rebuilds-of-mariadb-with-docker/)** - Constains practical hints, useful even if you don't plan to use Docker.
* [Building MariaDB Server from the sources](https://fromdual.com/building-mariadb-server-from-the-sources)
* [The Zoo of MySQL Storage Engine
  Flags](https://of-code.blogspot.com/2022/12/the-zoo-of-mysql-storage-engine-flags.html)
* [On Writing to the MySQL Error
  Log](https://of-code.blogspot.com/2023/01/on-writing-to-mysql-error-log.html)
* [MySQL, clang -ftime-trace, &
  ClangBuildAnalyzer](https://of-code.blogspot.com/2023/04/mysql-clang-ftime-trace.html)
* [Tips for making MySQL builds & tests
  faster](https://of-code.blogspot.com/2023/05/mysql-compilation-and-testsuite-run-tips.html)
* [MySQL Build Times: Use
  Ninja](https://of-code.blogspot.com/2023/08/mysql-build-times-use-ninja.html)
* [Implementing durability in a MySQL storage
  engine](https://of-code.blogspot.com/2023/09/implementing-durability-in-mysql.html)
* [MySQL clone plugin internals and MyRocks clone
  design](https://of-code.blogspot.com/2024/01/mysql-clone-plugin-internals-and.html)
* [Introducing patch2testlist for MySQL
  development](https://of-code.blogspot.com/2024/01/introducing-patch2testlist-for-mysql.html)
* [Implementing a Table-Returning MySQL
  Function](https://of-code.blogspot.com/2024/06/implementing-table-returning-mysql.html)
* [A README for my MySQL development
  tooling](https://of-code.blogspot.com/2024/08/a-readme-for-my-mysql-development.html)
* [Running Perl-using MTR tests for fb-mysql under
  macOS](https://of-code.blogspot.com/2024/09/running-perl-using-mtr-tests-for-fb.html)
* [Emacs Projectile Tweaks for MySQL Development](https://of-code.blogspot.com/2024/10/emacs-projectile-tweaks-for-mysql.html)

## Tools

| Project Name                                                                                              | MariaDB Support | Notes                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Laurynas' MySQL Development Tools](https://github.com/laurynas-biveinis/dotfiles/tree/master/mysql-work) | MySQL[1]        | A collection of scripts and configuration files to automate some of MySQL development tasks. |

Notes:

* Not tested with MariaDB, but it's expected to work equally well.

## Key

Meaning of the terms used in this list.

### MariaDB Support

Some of the sections include resources that were created for MySQL, or for both MariaDB and MySQL. The extent of MariaDB support is not always optimal. For those resources, we indicate the MariaDB support level as follows:

- `YES`: Specific support for MariaDB is indicated, or can be inferred from the documentation or the source code. "Supports MySQL/MariaDB" is not considered specific MariaDB support, because the author might assume that what works on MySQL will work on MariaDB equally well.
- `MySQL`: Officially supports MySQL, but not MariaDB.
- `NOT VERIFIED`: Officially supports MySQL and MariaDB but we do not know whether full support for MariaDB is implemented.
- `PARTIAL`: We are aware of relevant bugs or missing features.

If you disagree about a project's MariaDB Support indication, please report a bug.

### License

The license column might need a better name.

- `Cloud` - Available as a cloud service.
- `Proprietary` - Source is available, but software is not Open Source.
- `Open Source` - The license is [approved by OSI](https://opensource.org/licenses).
- For software that uses a single, open source, well-known license we sometimes indicate the license name.

For non-cloud software, we ancourage you to verify the license where relevant. Indicating a specific license is usually a simplification, because an application could be distributed with multiple licenses, or it might include libraries that use different licenses.

---

Copyright 2024 Vettabase Ltd and contributors.

Awesome MariaDB list is licensed under [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).
