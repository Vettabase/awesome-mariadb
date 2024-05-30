# Awsome MariaDB for Developers

A curated list of awesome MariaDB resources, maintained by [Vettabase](https://vettabase.com) and sponsored by the [MariaDB Foundation](https://mariadb.org/).

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) Inspired by the `awesome-*` trend on GitHub.

This list is intended for Developers. There are lists intended for other audiences. See [README.md](README.md).

## Contents

- [Connectors (Drivers)](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dev.md#connectors-drivers)
- [ORMs](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dev.md#orms)
- [Schema Versioning Tools](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dev.md#schema-versioning-tools)
- [SQL Tutorials](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dev.md#sql-tutorials)
- [User Interfaces](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dev.md#user-interfaces)

## MariaDB Support: an Explanation

- `MySQL`: The resource states that it support MySQL, but not MariaDB.
- `YES`: The resource states it supports MariaDB specifically, not something like "MySQL/MariaDB".
- `NOT VERIFIED`: The resource states that it supports MySQL and MariaDB (or the specified version number) but we do not know whether full support for MariaDB is implemented. It's possible that MariaDB support is assumed as a consequence of MySQL support, but this might be inaccurate. Please report any relevant problems you might find to us (and to the resource itself).
- `PARTIAL`: We have a clear list of what is or isn't officially supported.

## Connectors (Drivers)

To do.

## ORMs

| Platform    | ORM Name        | MariaDB Support |
| ----------- | --------------- | --------------- |
| Java        | [Apache Cayenne](https://cayenne.apache.org/)  | [MySQL](https://cayenne.apache.org/database-support.html)  |
| Java        | [OpenJPA](https://openjpa.apache.org/)   | [YES](https://openjpa.apache.org/builds/3.2.2/apache-openjpa/docs/#ref_guide_dbsetup_dbsupport) |
| Java        | [DataNucleus](https://www.datanucleus.org/)   | [NOT VERIFIED](https://www.datanucleus.org/products/accessplatform/datastores/datastores.html#rdbms) |
| Java, Koitlin  | [Ebean ORM](https://ebean.io/)   | [MySQL](https://ebean.io/docs/database/mysql/) |
| Java        | [EclipseLink](https://eclipse.dev/eclipselink/)   | [YES](https://eclipse.dev/eclipselink/documentation/4.0/concepts/concepts.html#APP_TL_EXT001) |
| Java        | [Hibernate](https://hibernate.org/orm/)   | [YES](https://github.com/hibernate/hibernate-orm/blob/main/dialects.adoc) |
| Java        | [Oracle TopLink](https://www.oracle.com/middleware/technologies/top-link.html)   | [MySQL](https://docs.oracle.com/cd/E15523_01/apirefs.1111/b32476/oracle/toplink/platform/database/package-summary.html) |

**@TODO:** Check the ORMs in [this list](https://en.wikipedia.org/wiki/List_of_object%E2%80%93relational_mapping_software).

## Schema Versioning Tools

| Project Name        | MariaDB Support |
| ------------------- | --------------- |
| ByteBase            | [10.7+](https://www.bytebase.com/docs/introduction/supported-databases/)
| Flyway              | [5.1, 10.11](https://documentation.red-gate.com/flyway/flyway-cli-and-api/supported-databases/mariadb)
| Liquibase           | [PARTIAL](https://www.liquibase.com/databases/mariadb-server)
| Skeema.io           | [10.1](https://www.skeema.io/docs/requirements/)


## SQL Tutorials

The following tutorials are specific for MariaDB.

| Project                                                               | Language         | Level            |                | Notes          |
|-----------------------------------------------------------------------|------------------|------------------|----------------|----------------|
| [MariaDB Tutorial](https://www.tutorialspoint.com/mariadb/)           | SQL, PHP         | BEGINNER         | Text           | [1]            |
| [How To Store and Retrieve Data in MariaDB Using Python](https://www.digitalocean.com/community/tutorials/how-to-store-and-retrieve-data-in-mariadb-using-python-on-ubuntu-18-04) | Python | BEGINNER / INTERMEDIATE | Text |
| [MariaDB Tutorial](https://www.javatpoint.com/mariadb-tutorial)       | Pure SQL         | BEGINNER         | Text           |                |
| [MariaDB for Beginners](https://www.youtube.com/watch?v=-ARMty_N0RU&list=PL3bGLnkkGnuUOB9YjjVDty6aCJApvkw8O&index=1) | SQL, Java | BEGINNER | Video | [2] |

- 1: The PHP part might be obsolete, because it still uses the old `mysql` non-OOP extension. However, editing the snippets to use `mysqli` or other libraries should be easy.
- 2: The Java part only shows how to connect to MariaDB with a JDBC driver.

## User Interfaces

**GUIs**

| Project Name                                                                | MariaDB Support                                 | Platforms             | Free / Commercial  |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|
| [DBeaver](https://dbeaver.io/)                                              | [NOT VERIFIED](https://dbeaver.com/databases/)  | Linux, MacOS, Windows | BOTH               |
| [HeidiSQL](https://www.heidisql.com/)                                       | YES                                             | Windows               | FREE               |
| [ocelotgui](http://ocelot.ca/)                                              | YES                                             | Linux                 | FREE               |
| [Database Workbench](https://www.upscene.com/database_workbench/) | [NOT VERIFIED](https://www.upscene.com/database_workbench/database-development-tool-for-mysql-and-mariadb)  | Windows               | Commercial         |
| [dbForge Studio for MySQL](https://www.devart.com/dbforge/mysql/studio/)    | NOT VERIFIED                                    | Windows               | Commercial         |
| [dbForge Edge](https://www.devart.com/dbforge/edge/features.html)           | NOT VERIFIED                                    | Windows               | Commercial         |
| [Navicat](https://www.navicat.com/)                                         | [YES]([https://www.navicat.com/en/products/navicat-for-mysql-feature-matrix](https://navicat.com/en/products/navicat-for-mariadb)) | YES | Linux, MacOS, Windows | Commercial |
| [SQLyog](https://webyog.com/product/sqlyog/)                                | NOT VERIFIED                                    | Windows               | Commercial         |
| [TablePlus](https://tableplus.com/)        | [NOT VERIFIED]([https://dbeaver.com/databases/](https://docs.tableplus.com/))  | Linux, MacOS, Windows, iOS | Commercial      |

In progress.

**Web Interfaces**

| Project Name                                                                | MariaDB Support                                 | Platforms             | Free / Commercial  |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|
| [Adminer](https://www.adminer.org/)                                         | NOT VERIFIED                                    | PHP                   | FREE               |
| [phpMyAdmin](https://www.phpmyadmin.net/)                                   | YES                                             | PHP                   | FREE               |

**TUIs**

| Project Name                                                                | MariaDB Support                                 | Platforms             | Free / Commercial  |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|
| [mycli](https://www.mycli.net/)                                             | YES                                             | Python                | FREE               |
