# Awsome MariaDB for DBAs

A curated list of awesome MariaDB resources, maintained by [Vettabase](https://vettabase.com) and sponsored by the [MariaDB Foundation](https://mariadb.org/).

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) Inspired by the `awesome-*` trend on GitHub.

This list is intended for Database Administrators. There are lists intended for other audiences. See [README.md](README.md).

## Contents

- [Articles](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dev.md#articles)
- [Schema Versioning Tools](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dev.md#schema-versioning-tools)
- [User Interfaces](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dev.md#user-interfaces)

## MariaDB Support Key

Some of the below sections only include resources that were created for MariaDB.

Other sections include resources that were created for MySQL, or for both, and the extent of MariaDB support is not always optimal. For those resources, we indicate the MariaDB support level. Refer to this key.

- `MySQL`: The resource states that it support MySQL, but not MariaDB.
- `YES`: The resource states it supports MariaDB specifically, not something like "MySQL/MariaDB".
- `NOT VERIFIED`: The resource states that it supports MySQL and MariaDB (or the specified version number) but we do not know whether full support for MariaDB is implemented. It's possible that MariaDB support is assumed as a consequence of MySQL support, but this might be inaccurate. Please report any relevant problems you might find to us (and to the resource itself).
- `PARTIAL`: We have a clear list of what is or isn't officially supported.

## Articles

To do.

## Schema Versioning Tools

| Project Name        | MariaDB Support |
| ------------------- | --------------- |
| ByteBase            | [10.7+](https://www.bytebase.com/docs/introduction/supported-databases/)
| Flyway              | [5.1, 10.11](https://documentation.red-gate.com/flyway/flyway-cli-and-api/supported-databases/mariadb)
| Liquibase           | [PARTIAL](https://www.liquibase.com/databases/mariadb-server)
| Skeema.io           | [10.1](https://www.skeema.io/docs/requirements/)

## User Interfaces

**GUIs**

| Project Name                                                                | MariaDB Support                                 | Platforms             | Free / Commercial  | Notes |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|-------|
| [Beekeeper Studio](https://www.beekeeperstudio.io/)                         | [NOT VERIFIED](https://docs.beekeeperstudio.io/user_guide/connecting/first-page/)  | Linux, MacOS, Windows | BOTH               |       |
| [DBeaver](https://dbeaver.io/)                                              | [NOT VERIFIED](https://dbeaver.com/databases/)  | Linux, MacOS, Windows | BOTH               |       |
| [DbVisualizer](https://www.dbvis.com/)                                      | NOT VERIFIED                                    | Native: Linux, Windows; Java: Linux, MacOS, Windows | BOTH               |       |
| [HeidiSQL](https://www.heidisql.com/)                                       | YES                                             | Windows               | FREE               |       |
| [LibreOffice Base](https://www.libreoffice.org/discover/base/)              | [NOT VERIFIED](https://www.libreoffice.org/discover/base/) | Linux, MacOS, Windows | FREE            | [1]   |
| [ocelotgui](http://ocelot.ca/)                                              | YES                                             | Linux                 | FREE               |       |
| [OpenOffice Base](https://www.openoffice.org/product/base.html)             | [MySQL](https://www.openoffice.org/product/base.html) | Linux, MacOS, Windows | FREE                 | [2]   |
| [Sequel Pro](https://www.sequelpro.com/)                                    | PARTIAL                                         | MacOS                 | FREE                       | [3]   |
| [Database Workbench](https://www.upscene.com/database_workbench/) | [NOT VERIFIED](https://www.upscene.com/database_workbench/database-development-tool-for-mysql-and-mariadb)  | Windows               | Commercial         |       |
| [dbForge Studio for MySQL](https://www.devart.com/dbforge/mysql/studio/)    | NOT VERIFIED                                    | Windows               | Commercial         |       |
| [dbForge Edge](https://www.devart.com/dbforge/edge/features.html)           | NOT VERIFIED                                    | Windows               | Commercial         |       |
| [Navicat](https://www.navicat.com/)                                         | [YES]([https://www.navicat.com/en/products/navicat-for-mysql-feature-matrix](https://navicat.com/en/products/navicat-for-mariadb)) | YES | Linux, MacOS, Windows | Commercial |       |
| [SQLPro Studio](https://www.sqlprostudio.com/)                              | NOT VERIFIED                                    | MacOS, Windows, iOS   | Commercial |       |
| [SQLyog](https://webyog.com/product/sqlyog/)                                | NOT VERIFIED                                    | Windows               | Commercial         |       |
| [TablePlus](https://tableplus.com/)                                         | [NOT VERIFIED]([https://dbeaver.com/databases/](https://docs.tableplus.com/))  | Linux, MacOS, Windows, iOS | Commercial      |       |
| [Toad Edge](https://toadworld.com/)                                         | NOT VERIFIED                                    | MacOS, Windows, Jenkins plugin | Commercial |       |
| [Valentina Studio](https://valentina-db.com/)                               | [NOT VERIFIED](https://valentina-db.com/en/database-management) | Linux, MacOS, Windows      | Commercial  |       |

Notes

1. LibreOffice Base is a generic data visualization frontend. To learn how to use it with MariaDB, see the [MariaDB KB](https://mariadb.com/kb/en/libreoffice-base/).
2. Apache OpenOffice is the project from which LibreOffice was originally forked. LibreOffice became more popular over time, so consider LibreOffice Base as well. OpenOffice Base does not support MariaDB. However it supports MySQL and ODBC drivers, so in practice it should work with MariaDB for standard use cases.
3. At the moment of this writing, MariaDB support is only mentioned in the `README.md` file. A quick [search on GitHub](https://github.com/search?q=repo%3Asequelpro%2Fsequelpro%20mariadb&type=code) shows that this support is currently limited to version identification, some permissions a TODO note.

**Web Interfaces**

| Project Name                                                                | MariaDB Support                                 | Platforms             | Free / Commercial  |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|
| [Adminer](https://www.adminer.org/)                                         | NOT VERIFIED                                    | PHP                   | FREE               |
| [phpMyAdmin](https://www.phpmyadmin.net/)                                   | YES                                             | PHP                   | FREE               |

**TUIs**

| Project Name                                                                | MariaDB Support                                 | Platforms             | Free / Commercial  |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|
| [mycli](https://www.mycli.net/)                                             | YES                                             | Python                | FREE               |