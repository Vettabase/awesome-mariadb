# Awesome MariaDB Internals and Plugins Development

A curated list of awesome MariaDB resources, maintained by [Vettabase](https://vettabase.com) and sponsored by the [MariaDB Foundation](https://mariadb.org/).

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) Inspired by the `awesome-*` trend on GitHub.

This list is intended for internals developers. There are lists intended for other audiences. See [README.md](README.md).

## Contents

- [Articles](#articles)
- [Tools](#tools)

See the [key](#key) for explanations of the terms used in this list.

## Articles

* [Building MariaDB Server from the sources](https://fromdual.com/building-mariadb-server-from-the-sources)

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
