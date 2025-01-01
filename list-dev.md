# Awesome MariaDB for Developers

A curated list of awesome MariaDB resources, maintained by [Vettabase](https://vettabase.com) and sponsored by the [MariaDB Foundation](https://mariadb.org/).

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) Inspired by the `awesome-*` trend on GitHub.

This list is intended for Developers. There are lists intended for other audiences. See [README.md](README.md).

## Contents

- [Articles](#articles)
- [Connectors (Drivers)](#connectors-drivers)
- [IDEs](#ides)
- [Migrations](#migrations)
- [Misc Libraries](#misc-libraries)
- [NoSQL and Key Value Storage](#nosql-and-key-value-storage)
- [ORMs](#orms-and-other-abstraction-layers)
- [Protocol](#protocol)
- [Schema Versioning Tools](#schema-versioning-tools)
- [Stored Routines](#stored-routines)
- [User-Defined Functions](#user-defined-functions)
- [User Interfaces](#user-interfaces)

See the [key](#key) for explanations of the terms used in this list.

## Articles

The following resources are specific to MariaDB.

**Tutorials**

These tutorials show how to connect to MariaDB and perform some basic operations.

Loosely ordered by language, SQL first.

| Project                                                               | Language         | Level            | Format         | Notes          |
|-----------------------------------------------------------------------|------------------|------------------|----------------|----------------|
| **[MariaDB on Rosetta Code](https://rosettacode.org/wiki/Category:MariaDB)**     | Pure SQL         | ALL LEVELS         | Text           |                |
| [MariaDB Tutorial](https://www.javatpoint.com/mariadb-tutorial)       | Pure SQL         | BEGINNER         | Text           |                |
| [Using MariaDB With ASP.NET Core Web API](https://code-maze.com/aspnetcore-using-mariadb-with-web-api/)   | ASP.NET          | INTERMEDIATE   | Text           |                |
| [Query MariaDB Data in ColdFusion](https://www.cdata.com/kb/tech/mariadb-jdbc-coldfusion-query.rst)       | ColdFusion       | BEGINNER       | Text           |                |
| [Creating an MVC application using NODEjs and MariaDB](https://medium.com/codex/creating-an-mvc-application-using-nodejs-and-mariadb-9510c7b91716) | NodeJS      | INTERMEDIATE   | Text           |            |
| [NodeJS MariaDB Integration: 3 Easy Steps](https://hevodata.com/learn/nodejs-mariadb-integration/) | NodeJS      | INTERMEDIATE   | Text           |            |
| [Getting Started with MariaDB using Docker and Node.js ](https://dev.to/probablyrealrob/getting-started-with-mariadb-using-docker-and-node-js-3djg) | NodeJS | INTERMEDIATE | Text | |
| [MariaDB for Beginners](https://www.youtube.com/watch?v=-ARMty_N0RU&list=PL3bGLnkkGnuUOB9YjjVDty6aCJApvkw8O&index=1) | SQL, Java | BEGINNER   | Video | [1]   |
| [Using MariaDB databases with Lazarus/Free Pascal](https://www.streetinfo.lu/computing/lazarus/project/use_mariadb.html)           | Pascal           | BEGINNER         | Text           |           |
| [MariaDB Tutorial](https://www.tutorialspoint.com/mariadb/)           | SQL, PHP         | BEGINNER         | Text           | [2]            |
| [How To Store and Retrieve Data in MariaDB Using Python](https://www.digitalocean.com/community/tutorials/how-to-store-and-retrieve-data-in-mariadb-using-python-on-ubuntu-18-04) | Python | BEGINNER / INTERMEDIATE | Text |
| [Connect to MariaDB Data in Ruby](https://www.cdata.com/kb/tech/mariadb-odbc-ruby.rst)   | Ruby             | BEGINNER         | Text           |                |
| [Three simple rules to not fail (too much) your data design](https://github.com/SylvainA77/articles/blob/main/Three-rules-not-fail-data-design.md) | N/A | BEGINNER / INTERMEDIATE | Text | [3]

Notes

1. The Java part only shows how to connect to MariaDB with a JDBC driver.
2. The PHP part might be obsolete, because it still uses the old `mysql` non-OOP extension. However, editing the snippets to use `mysqli` or other libraries should be easy.
3. Fully data design oriented

**Language-specific articles**

These articles are about language best practices, specific libraries, or non-trivial operations.

Go

* [Integrating MariaDB with GoLang Microservice Restful API](https://medium.com/widle-studio/integrating-mariadb-with-golang-microservice-restful-apis-building-efficient-data-storage-4054e1588ce)
* [Golang: a RESTful API Using Temporal Table With MariaDB](https://hackernoon.com/golang-a-restful-api-using-temporal-table-with-mariadb)
* [How to Connect and Operate MariaDB Using GORM in Go](https://medium.com/@blackhorseya/how-to-connect-and-operate-mariadb-using-gorm-in-go-bc55b1984348)
* [gin-rest-api-sample](https://github.com/velopert/gin-rest-api-sample?tab=readme-ov-file) -  An example project that uses Gin, GORM and MariaDB.

Java

* [Getting Started With JPA/Hibernate](https://dzone.com/articles/getting-started-with-jpahibernate)
* [How To Connect MariaDB Docker Containers with Java Spring And JDBC](https://hackernoon.com/how-to-connect-mariadb-docker-containers-with-java-spring-and-jdbc-ex243urb)
* [Reactive Programming with Java Spring, R2DBC and MariaDB](https://hackernoon.com/reactive-programming-with-java-spring-r2dbc-and-mariadb-4vc3uo1)

Node.js

* [Getting Started with MariaDB using Docker and Node.js](https://hackernoon.com/getting-started-with-mariadb-using-docker-and-nodejs-fo433yp2)
* [MariaDB, MySQL, and Node.js: Why Using the Right Connector Matters](https://dev.to/alejandro_du/mariadb-mysql-and-nodejs-why-using-the-right-connector-matters-38oe)

Perl

* [Migrating from DBD::mysql to DBD::MariaDB](https://blogs.perl.org/users/grinnz/2023/12/migrating-from-dbdmysql-to-dbdmariadb.html)

PHP

* [Why You Should Be Using PHP's PDO for Database Access](https://code.tutsplus.com/why-you-should-be-using-phps-pdo-for-database-access--net-12059t)

Python

* [Getting Started with MariaDB using Docker, Python and Flask](https://hackernoon.com/getting-started-with-mariadb-using-docker-python-and-flask-pa1i3ya3)
* [Quick Tip: SQLAlchemy for MySQL and Pandas](https://pythondata.com/quick-tip-sqlalchemy-for-mysql-and-pandas/)

Scala

* [Stateful actors with Akka Event Sourcing and MariaDB](https://medium.com/@matteodipirro/stateful-actors-with-akka-event-sourcing-and-maria-db-d4202c6c599a)

**Plain SQL articles**

These articles are about MariaDB SQL dialect, regardless which language you use to develop applications.

* [MariaDB/MySQL: use SQL properly to run less queries](https://vettabase.com/mysql-mariadb-use-sql-properly-to-run-less-queries/)
* [How to compose strings in MariaDB](https://vettabase.com/how-to-compose-strings-in-mariadb/)
* [Leveraging "INSERT INTO ... RETURNING": Practical Scenarios](https://dzone.com/articles/leveraging-insert-into-returning-practical-scenari)
* [MariaDB 10.2 Window Functions](http://ocelot.ca/blog/blog/2016/04/18/mariadb-10-2-window-functions/)
* [Using Temporary Tables in MariaDB](https://dev.to/alejandro_du/using-temporary-tables-in-mariadb-1nb)
* [MariaDB: WITH TIES syntax](https://vettabase.com/mariadb-with-ties-syntax/)
* [Hybrid Data Models: How To Have Your JSON Cake and Eat MariaDB Too](https://hackernoon.com/hybrid-data-models-how-to-have-your-json-cake-and-eat-maria-db-too)
* [Using JSON in MariaDB](https://dzone.com/articles/using-json-in-mariadb)
* [The UUID data type in MariaDB](https://vettabase.com/the-uuid-data-type-in-mariadb/)
* [The simultaneous_assignment mode in MariaDB 10.3.5](http://ocelot.ca/blog/blog/2018/03/21/the-simultaneous_assignment-mode-in-mariadb-10-3-5/)
* [READ ONLY transactions in MariaDB and MySQL](https://vettabase.com/read-only-transactions-in-mariadb-and-mysql/)
* [Tags and FullText indexes in MySQL](https://www.percona.com/blog/tags-and-fulltext-indexes-in-mysql/)

## Connectors (Drivers)

The connectors are grouped by language.

| Platform / Language  | Connector Driver Name                                                                     | MariaDB Support | Extensions | Notes               |
| -------------------- | ----------------------------------------------------------------------------------------- | --------------- | ---------- | ------------------- |
| C                    | [Connector/C ](https://mariadb.com/kb/en/about-mariadb-connector-c/)                      | YES             | <ul><li>PSskipMD([3.1.10](https://mariadb.com/kb/en/mysql_real_connect/) - [default](https://github.com/mariadb-corporation/mariadb-connector-c/commit/6a763b90006c5591bfef766ba0a9f414a02a69ae#diff-e45114083905fb36ada93fa0ab74fc9b84def45219693b574bfb0429b548db8cR183))</li><li>EXTcolInfo([3.1.10](https://github.com/mariadb-corporation/mariadb-connector-c/wiki/mariadb_field_attr))</li><li>AUTHparsec([3.4.1](https://github.com/mariadb-corporation/mariadb-connector-c/blob/v3.4.1/plugins/auth/parsec.c) - default)</ul>               |
| C                    | [mariadb++](https://github.com/viaduck/mariadbpp)                                         | YES             |                     |
| C++                  | [MariaDB Connector/C++](https://github.com/mariadb-corporation/mariadb-connector-cpp/) | YES     |                     |
| C++, Delphi          | [Universal Data Access](https://www.devart.com/unidac/)                                   | [YES](https://www.devart.com/unidac/compatibility.html)  |  |
| Erlang               | [MySQL/OTP](https://github.com/mysql-otp/mysql-otp)                                       | MySQL           |                     |
| Fortran              | [MariaDB Connector Fortran](https://github.com/v-h-giang/Mariadb_connector_fortran)       | YES             |                     |
| Go                   | [Go-MySQL-Driver](https://github.com/go-sql-driver/mysql)                                 | [YES](https://github.com/go-sql-driver/mysql?tab=readme-ov-file#requirements) |  |
| Java                 | [Connector/J](https://mariadb.com/kb/en/about-mariadb-connector-j/)                       | YES             | <ul><li>AUTHparsec([3.5.0](https://github.com/mariadb-corporation/mariadb-,connector-j/blob/master/CHANGELOG.md#350-oct-2024))</li><li>REDIR([3.4.0](https://github.com/mariadb-corporation/mariadb-connector-j/blob/master/CHANGELOG.md#340-apr-2024))</li></ul>*The list might be incomplete.* | Type 4 JDBC driver  |
| Java                 | [Connector/R2DBC](https://mariadb.com/docs/server/connect/programming-languages/java-r2dbc/) | YES          | <ul><li>AUTHparsec([1.3.0](https://github.com/mariadb-corporation/mariadb-connector-r2dbc/blob/master/CHANGELOG.md#130-oct-2024))</li><li>REDIR([1.2.0](https://github.com/mariadb-corporation/mariadb-connector-r2dbc/blob/master/CHANGELOG.md#120-08-feb-2024))</li></ul>*The list might be incomplete.* | Non-blocking API    |
| JRuby                | [jdbc-mariadb](https://rubygems.org/gems/jdbc-mariadb)                                    | YES             | | JDBC driver for JRuby. |
| Julia                | [MySQL.jl](https://juliahub.com/ui/Packages/General/MySQL)                                | YES             | | Built on MariaDB C/Connector |
| Lisp                 | [Allegro MySQL Direct Connect Library](https://franz.com/support/documentation/10.1/doc/mysql.htm) | [NOT VERIFIED](https://franz.com/support/documentation/10.1/doc/mysql.htm#mariadb-1) | |
| .NET                 | [Connector/NET](https://dev.mysql.com/downloads/connector/net/)                           | MySQL           |                     |
| .NET                 | [dotConnect for MySQL](https://www.devart.com/dotconnect/mysql/)                          | MySQL           |                     |
| Node.js              | [Connector/Node.js](https://mariadb.com/kb/en/about-mariadb-connector-nodejs/)            | YES             | <ul><li>AUTHparsec([3.4.0](https://mariadb.com/kb/en/mariadb-connector-node-js-3-4-0-release-notes/))</li><li>NOconfigSSL([3.3.0](https://mariadb.com/kb/en/mariadb-connector-node-js-3-3-0-release-notes/))</li></ul>*The list might be incomplete.*    |
| OCaml                | [OCaml-MariaDB](https://github.com/andrenth/ocaml-mariadb)                                | YES             | | [1] |
| ODBC                 | [Connector/ODBC](https://mariadb.com/kb/en/about-mariadb-connector-odbc/)                 | YES             |                     |
| Perl                 | [DBD::MariaDB](https://metacpan.org/dist/DBD-MariaDB)                                     | YES             |                     |
| PHP                  | [MySQLi](https://www.php.net/manual/en/book.mysqli.php)                                   | MySQL           | | Both procedural and OO API. |
| PHP                  | [PDO MySQL](https://www.php.net/manual/en/ref.pdo-mysql.php)                              | MySQL           | | Multi-database abstraction layer. |
| Python               | [Connector/Python](https://mariadb.com/kb/en/list-of-mariadb-connector-python-releases/)  | YES             |                     |
| Python               | [mysqlclient](https://github.com/PyMySQL/mysqlclient)                                     | YES             |  |
| Python               | [TonyDBC](https://pypi.org/project/tonydbc/)                                              | YES             |  | [2] |
| Python               | [PyMySQL](https://github.com/PyMySQL/PyMySQL)                                             | PARTIAL             | | Pure Python driver, MariaDB >= 10.4 |
| R                    | [RMariaDB](https://cran.r-project.org/web/packages/RMariaDB/index.html)                   | YES             |                     |
| Raku (Perl 6)        | [DBIish](https://github.com/raku-community-modules/DBIish)                                | [YES](https://github.com/raku-community-modules/DBIish?tab=readme-ov-file#mysql) | |
| Ruby                 | [mysql Ruby gem](https://rubygems.org/gems/mysql/)                                        | MySQL           | | [3]                 |
| Ruby                 | [tencentcloud-sdk-mariadb](https://rubygems.org/gems/tencentcloud-sdk-mariadb)            | YES             | | [3]                 |
| Swift                | [Perfect MariaDB Connector](https://github.com/PerfectlySoft/Perfect-MariaDB)             | YES             |                     |
| Zig                  | [myzql](https://github.com/speed2exe/myzql)                                               | NOT VERIFIED    | | [4]                 |

**MariaDB Protocol Extensions**

MariaDB extends the original MySQL protocol via capability flags. This table serves to show which Connector Drivers have these features.

| Abbreviation | Meaning                               | MariaDB Version | Reference |
| -------------| --------------------------------------| --------------- | ----------|
| PSskipMD     | Prepare Statement Skip Metadata       | 10.6.0+         | [MariaDB KB - Prepare Statement Skipping Metadata](https://mariadb.com/kb/en/mariadb-protocol-differences-with-mysql/#prepare-statement-skipping-metadata) |
| EXTcolInfo   | Extended Column Information           | 10.5.2+         | [MariaDB KB - Extended Column Information](https://mariadb.com/kb/en/mariadb-protocol-differences-with-mysql/#extended-column-information) |
| BULK         | Bulk  - Batch processing              | 11.5.1+         | [MariaDB KB - Bulk](https://mariadb.com/kb/en/mariadb-protocol-differences-with-mysql/#bulk) |
| AUTHed25519  | Authentication - ed25519              | 10.1.22+        | [MariaDB KB - ED25519 Plugin](https://mariadb.com/kb/en/connection/#client_ed25519-plugin) |
| AUTHparsec   | Authentication - PARSEC               | 11.6+           | [MariaDB KB - PARSEC Plugin](https://mariadb.com/kb/en/connection/#parsec-plugin) |
| AUTHgssapi   | Authentication - GSSAPI               | 10.11+          | [MariaDB KB - GSSAPI Plugin](https://mariadb.com/kb/en/connection/#auth_gssapi_client-plugin) |
| REDIR        | Redirection                           | 11.3.0+         | [MariaDB KB - Connection Redirection Mechanism in the MariaDB Client/Server Protocol](https://mariadb.com/kb/en/connection-redirection-mechanism-in-the-mariadb-clientserver-protocol/) |
| NOconfigSSL  | No Configuration SSL                  | 11.4.1+         | [MariaDB KB - No Configuration SSL](https://mariadb.com/kb/en/mariadb-protocol-differences-with-mysql/#no-configuration-ssl) / [MariaDB Foundation Blog](https://mariadb.org/mission-impossible-zero-configuration-ssl/) |
| INITsesTrack | Initial Session Tracking              | 10.2.2+         | [MariaDB KB - Initial Session Tracking](https://mariadb.com/kb/en/mariadb-protocol-differences-with-mysql/#initial-session-tracking) |

Note: Reading the protocol extensions; the lack of an entry indicates that it has not been determined if this feature exists in this connector.

Notations associated with protocol extensions:

* version of connector including the feature (if known), and/or a link to documentation/interface.
* a `Requested` linking to a feature request if one has been made.
* a `N/A` (not applicable) if the extension is somehow unsuitable for the connector.
* a `No` if the feature request has been rejected by the upstream.
* a `Not present` if investigated and found to be missing.


Notes

1. Uses Connector/C via [CTypes](https://github.com/yallop/ocaml-ctypes). From the `README` file: "Only the prepared-statement APIs are exposed by OCaml-MariaDB, as these functions provide typed query parameters and database field access". A non-blocking API was implemented in Ocaml.
2. TonyDBC is descreibed as a _high level connector_, based on MariaDB/Connector. The features it adds are typical of a connector and should improve performance. It also includes type mapping to the [Pandas](https://pandas.pydata.org/) framework.
3. `tencentcloud-sdk-mariadb` is actively maintained by Tencent. The `mysql` gem is by far the most used, but it's unmaintained since 2021. `jdbc-mariadb` is also unmaintained since 2019.
4. Pre-production maturity level.

## IDEs

Guides on how to work with MariaDB using various IDEs.

| IDE               | Project                                                                                        | Format          | Notes          |
|-------------------|------------------------------------------------------------------------------------------------|-----------------|----------------|
| Eclipse           | [Accessing Maria DB from within Eclipse](https://www.youtube.com/watch?v=Ar00dtkNb4o)          | Video           |                |
| Embarcadero       | [New in 10.2: MariaDB Support](https://blogs.embarcadero.com/new-in-10-2-mariadb-support/)     | Text            |                |
| IntelliJ IDEA     | [IntelliJ IDEA - MariaDB](https://docs.telerik.com/data-access/developers-guide/database-specifics/mariadb/database-specifics-mariadb-create-domain-model.html)                                                                 | Text            |                |
| RubyMine          | [RubyMine MariaDB plugin documentation](https://www.jetbrains.com/help/ruby/mariadb.html)      | Text            |                |
| Visual Studio     | [How to: Create A Model Based on MariaDB Database](https://docs.telerik.com/data-access/developers-guide/database-specifics/mariadb/database-specifics-mariadb-create-domain-model.html)                                                                 | Text            |                |

## Migrations

| Peoject Name                                                      | License   | MariaDB Support | Notes |
| ----------------------------------------------------------------- | --------- | --------------- | ----- |
| [sqlite-to-mysql](https://github.com/vwbusguy/sqlite-to-mysql)    | [MIT](https://github.com/vwbusguy/sqlite-to-mysql/blob/master/LICENSE) | YES |  |
| [psql2mysql](https://pypi.org/project/psql2mysql/)                | Apache 2  | YES             |       |

## Misc Libraries

Libraries that can't be classified as [connectors](#connectors-drivers) or [ORMs](#orms-and-other-abstraction-layers).

- [MariaDB4j](https://github.com/MariaDB4j/MariaDB4j) - a Java launcher to run MariaDB without installation or external dependencies.
- [SQLGlot](https://github.com/tobymao/sqlglot/) - Libraries to parse SQL in various dialects. Supports MySQL with very minor divergencies from MariaDB.


## NoSQL and Key Value Storage

Links to articles and information on the various methods and utilities to read and write unstructure or NoSQL data to MariaDB.

- [Dynamic Columns Tutorial](https://mariadb.com/resources/blog/dynamic-columns-tutorial-part-1-introduction/)
- [Dynamic columns in MariaDB](http://radar.oreilly.com/2015/04/dynamic-columns-in-mariadb.html)
- [How to Manage NoSQL Data with MariaDB](https://mariadb.com/resources/blog/how-to-manage-nosql-data-with-mariadb/)
- [MariaDB for NoSQL users](https://archive.fosdem.org/2021/stands.fosdem.org/stands/mariadb_foundation/mariadb-for-nosql/index.html)
- [NoSQL Protocol and Caching in MariaDB MaxScale](https://mariadb.com/resources/blog/nosql-protocol-and-caching-in-mariadb-maxscale/)
- [Using JSON in MariaDB](https://mariadb.com/resources/blog/using-json-in-mariadb/)
- [Using MariaDB as a MongoDB NoSQL Database](https://hackernoon.com/using-mariadb-as-a-mongodb-nosql-database)


## ORMs and other abstraction layers

| Language    | ORM Name                                             | License | MariaDB Support | Notes |
| ----------- | ---------------------------------------------------- | ------- | --------------- | ----- |
| Go          | [GORM]([https://github.com/adamchainz/django-mysql](https://gorm.io/))  | [MIT](https://github.com/go-gorm/gorm/blob/master/LICENSE) | [NOT VERIFIED](https://github.com/adamchainz/django-mysql?tab=readme-ov-file#what-kind-of-features)            | [1]   |
| Python      | [Django-MySQL](https://github.com/adamchainz/django-mysql)  | [MIT](https://github.com/adamchainz/django-mysql/blob/main/LICENSE) | [YES](https://github.com/adamchainz/django-mysql?tab=readme-ov-file#what-kind-of-features)            |       |
| Java        | [Hibernate](https://hibernate.org/orm/)              | [LGPL 2.1 / Apache 2](https://hibernate.org/community/license/) | [YES](https://github.com/hibernate/hibernate-orm/blob/main/dialects.adoc) | [2]   |
| Java        | [EclipseLink](https://eclipse.dev/eclipselink/)      | [Open Source](https://github.com/eclipse-ee4j/eclipselink/blob/master/LICENSE.md) | [YES](https://eclipse.dev/eclipselink/documentation/4.0/concepts/concepts.html#APP_TL_EXT001) | [2]   |
| Java        | [OpenJPA](https://openjpa.apache.org/)               | [Apache 2](https://github.com/apache/openjpa/blob/master/LICENSE) | [YES](https://openjpa.apache.org/builds/3.2.2/apache-openjpa/docs/#ref_guide_dbsetup_dbsupport) | [2]   |
| Java        | [jOOQ](https://www.jooq.org/)                        | [Apache 2 / Proprietary](https://github.com/jOOQ/jOOQ/blob/main/LICENSE) | [YES](https://www.jooq.org/javadoc/latest/org.jooq/org/jooq/SQLDialect.html#MARIADB) |       |
| Java        | [MyBatis](https://mybatis.org/mybatis-3/)            | [Apache 2](https://github.com/mybatis/mybatis-3/blob/master/LICENSE) | [YES](https://github.com/mybatis/generator/issues/450#issuecomment-471790027) |       |
| JavaScript  | [TypeORM](https://github.com/typeorm/typeorm)            | [MIT]([https://github.com/mybatis/mybatis-3/blob/master/LICENSE](https://github.com/typeorm/typeorm/blob/master/LICENSE)) | NOT VERIFIED | [2]   |
| Python      | [SQLAlchemy](https://www.sqlalchemy.org/)            | [MIT](https://github.com/sqlalchemy/sqlalchemy/blob/main/LICENSE) | [YES](https://docs.sqlalchemy.org/en/20/dialects/mysql.html#mariadb-support) |       |
| Python      | [mariadb_composition](https://pypi.org/project/mariadb-composition/)   | MIT | YES |   |
| Python      | [MariaDB-Context-Manager](https://pypi.org/project/MariaDB-Context-Manager/)   | MIT | YES | [5]   |
| Python      | [MariaDB SQL Builder](https://pypi.org/project/MariaDB-SQLBuilder/)          | [LGPL 2.1](https://github.com/princessmiku/MariaDB-SQLBuilder/blob/master/LICENSE) | YES |       |
| Ruby        | [mariadb_temporal_tables](https://rubygems.org/gems/mariadb_temporal_tables) | [MIT](https://github.com/YoussefHenna/mariadb_temporal_tables/blob/master/LICENSE) | YES |       |
| Ruby on Rails | [Active Record](https://guides.rubyonrails.org/)   | [MIT](https://github.com/rails/rails/blob/main/activerecord/MIT-LICENSE) | [YES](https://guides.rubyonrails.org/active_record_querying.html) |       |
| R           | [Shiny for R](https://shiny.posit.co/r/)             | [GPL 3](https://github.com/rstudio/shiny/blob/main/LICENSE) | [YES](https://shiny.posit.co/r/articles/build/overview/) | [4]   |
| Rust        | [Diesel](https://github.com/diesel-rs/diesel/)       | [Apache 2 / MIT](https://github.com/diesel-rs/diesel?tab=readme-ov-file#license) | [YES](https://mariadb.org/improving-mariadb-support-in-open-source-projects/) |       |
| SQLx        | [SQLx](https://github.com/launchbadge/sqlx)          | [Apache 2 / MIT](https://github.com/launchbadge/sqlx?tab=readme-ov-file#license) | [YES](https://github.com/launchbadge/sqlx/blob/main/README.md) | [3]      |

**Notes**

1. Official MariaDB support is not mentioned on the website, but projects and materials, including the documentation, seem to use MariaDB successfully. Feedback would be welcomed on how it behaves where MySQL and MariaDB syntax differ.
2. No easy way to insert the `IGNORE`, `USE` or `FORCE INDEX` syntax into a query.
3. SQLx is an SQL toolkit. But if you don't like to build SQL strings, you can take a look at the [ORMs](https://github.com/launchbadge/sqlx/wiki/Ecosystem#orms) and [query builders](https://github.com/launchbadge/sqlx/wiki/Ecosystem#query-builders) it supports.
4. Shiny is a framework for data science application developing in Pyhton and R. It includes support for databases, including MariaDB.
5. A context manager allows developers, for example, to run a query in a `with` statement. Resources will be deallocated automatically when the execution leaves the current context.

**@TODO** Check the ORMs in [this list](https://en.wikipedia.org/wiki/List_of_object%E2%80%93relational_mapping_software).

## Protocol

| Project Name                                            | MariaDB Support | License / Platform |
| ------------------------------------------------------- | --------------- | ------------------ |
| [Wireshark](https://gitlab.com/wireshark/wireshark/) MySQL Protocol Dissector | YES | [GPL2](https://gitlab.com/wireshark/wireshark/-/blob/master/COPYING) |

## Schema Versioning Tools

| Project Name                                            | MariaDB Support | License / Platform |
| ------------------------------------------------------- | --------------- | ------------------ |
| [ByteBase](https://www.bytebase.com/)                   | [10.7+](https://www.bytebase.com/docs/introduction/supported-databases/) | Open source, proprietary, cloud |
| [ChronoVoyage](https://pypi.org/project/chronovoyage/)  | YES | MIT |
| [Flyway](https://flywaydb.org/)                         | [5.1, 10.11](https://documentation.red-gate.com/flyway/flyway-cli-and-api/supported-databases/mariadb) | [Apache 2](https://github.com/flyway/flyway/blob/main/LICENSE.txt) |
| [Liquibase](https://www.liquibase.com/)                 | [PARTIAL](https://www.liquibase.com/databases/mariadb-server) | [Proprietary](https://www.liquibase.com/pricing) or [Apache 2](https://github.com/liquibase/liquibase/blob/master/LICENSE.txt) |
| [Skeema.io](https://www.skeema.io/)                     | [10.1](https://www.skeema.io/docs/requirements/) | [Proprietary](https://www.skeema.io/download/) or [Apache 2](https://github.com/skeema/skeema/blob/main/LICENSE) |


## Stored Routines

The term *stored routine* indicates a stored procedure or function. This is a list of stored routines that can be useful for application developers.

* [mariadb_uuidv7.sql](https://gist.github.com/juanparati/0ded9c04d4cd43e5aae8f5a438a8b18b) - A stored function to generate a UUIDv7. This is useful on MariaDB versions older than 10.7.


## User-Defined Functions

To our knowledge, all MySQL UDFs should work with MariaDB. For this reason we don't provide information about MariaDB compatibility.

**Articles**

- [Extending MariaDB with user-defined functions](https://www.slideshare.net/slideshow/extending-mariadb-with-userdefined-functions/135046794) (slides)
- [Enhancing MariaDB’s Capabilities: Exploring Extensibility Options](https://medium.com/@arbaudie.it/mariadb-extensibility-dce50baece54)
- [MySQL: Implementation of User Defined (Loadable) Function and using BLOB to store BigInteger](https://al-amintech.medium.com/mysql-implementation-of-user-defined-loadable-function-and-using-blob-to-store-biginteger-774a1b478a40)
- [Writing User-Defined Functions in Rust](https://mariadb.org/writing-user-defined-functions-in-rust/)

**Frameworks**

Frameworks and libraries to ease UDFs developing.

| Project                                                        | License | Language | Notes |
| -------------------------------------------------------------- | ------- | -------- | ----- |
| [lib_mysqludf_skeleton](https://github.com/mysqludf/lib_mysqludf_skeleton) | C      | [LGPL](https://github.com/mysqludf/lib_mysqludf_skeleton/blob/master/COPYING) | UDF skeleton project |
| [sql-udf](https://github.com/pluots/sql-udf)                   | [Open Source](https://github.com/pluots/udf-suite?tab=readme-ov-file#license) | Rust | Wrapper for developing UDFs in Rust |

**Libraries**

| Project                                                        | License | Language | Notes |
| -------------------------------------------------------------- | ------- | -------- | ----- |
| [JSON2SQL-plugin](https://github.com/SylvainA77/JSON2SQL-plugin)  | [AGPL 3](https://github.com/SylvainA77/JSON2SQL-plugin/blob/main/LICENSE) | C | Interact with data through a REST API. |
| [Levenshtein-MySQL-UDF](https://github.com/juanmirocks/Levenshtein-MySQL-UDF)  | [LGPL 3](https://github.com/juanmirocks/Levenshtein-MySQL-UDF/blob/master/LICENSE) | C | Levenshtein and related functions. |
| [libmyemail](https://github.com/codayblue/libmyemail)          | [MIT](https://github.com/codayblue/libmyemail/blob/master/LICENSE.md) | C++ | Function to send emails. |
| [lib_mysqludf_stomp](https://github.com/mysqludf/lib_mysqludf_stomp) | Apache 2 | C | UDF to send STOMP messages. |
| [lib_mysqludf_ta](https://github.com/mysqludf/lib_mysqludf_ta) | Open Source | C    | Library for technical analysis. |
| [lib_mysqludf_xml](https://github.com/mysqludf/lib_mysqludf_xml) | [LGPL 2.1](https://github.com/mysqludf/lib_mysqludf_xml/blob/master/COPYING) | C | [XQL](https://www.ibiblio.org/xql/xql-proposal.html) functions |
| [mysql_udf_http_golang](https://github.com/2rebi/mysql_udf_http_golang) | [Open Source](https://github.com/2rebi/mysql_udf_http_golang?tab=readme-ov-file#license) | Go | HTTP requests. |


## User Interfaces

**GUIs**

| Project Name                                                                | MariaDB Support                                 | Platforms             | Licence    | Notes |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|-------|
| [Beekeeper Studio](https://www.beekeeperstudio.io/)                         | [NOT VERIFIED](https://docs.beekeeperstudio.io/user_guide/connecting/first-page/)  | Linux, MacOS, Windows | BOTH               |       |
| [Database Workbench](https://www.upscene.com/database_workbench/) | [NOT VERIFIED](https://www.upscene.com/database_workbench/database-development-tool-for-mysql-and-mariadb)  | Windows               | Proprietary         |       |
| [DataGrip](https://www.jetbrains.com/datagrip/)                             | [YES](https://www.jetbrains.com/datagrip/features/) | Linux, MacOS, Windows | Proprietary     |       |
| [DBeaver](https://dbeaver.io/)                                              | [NOT VERIFIED](https://dbeaver.com/databases/)  | Linux, MacOS, Windows | BOTH               |       |
| [dbForge Studio for MySQL](https://www.devart.com/dbforge/mysql/studio/)    | YES                                             | Windows               | Proprietary         |       |
| [dbForge Edge](https://www.devart.com/dbforge/edge/features.html)           | YES                                             | Windows               | Proprietary         |       |

| [DbVisualizer](https://www.dbvis.com/)                                      | [YES](https://www.dbvis.com/database/mariadb/)  | Native: Linux, Windows; JVM: Linux, MacOS, Windows | BOTH               |       |
| [Harlequin](https://harlequin.sh/)                                          | MySQL                                           | Python                | Open Source          |       |
| [HeidiSQL](https://www.heidisql.com/)                                       | YES                                              | Windows               | Open Source         |       |
| [LibreOffice Base](https://www.libreoffice.org/discover/base/)              | [NOT VERIFIED](https://www.libreoffice.org/discover/base/) | Linux, MacOS, Windows | Open Source      | [1]   |
| [Navicat](https://www.navicat.com/)                                         | [YES]([https://www.navicat.com/en/products/navicat-for-mysql-feature-matrix](https://navicat.com/en/products/navicat-for-mariadb))   | Linux, MacOS, Windows | Proprietary |       |
| [ocelotgui](http://ocelot.ca/)                                              | YES                                             | Linux                 | Open Source          |       |
| [OpenOffice Base](https://www.openoffice.org/product/base.html)             | [MySQL](https://www.openoffice.org/product/base.html) | Linux, MacOS, Windows | Open Source           | [2]   |
| [Sequel Pro](https://www.sequelpro.com/)                                    | PARTIAL                                         | MacOS                 | Open Source                  | [3]   |
| [SQLPro Studio](https://www.sqlprostudio.com/)                              | NOT VERIFIED                                    | MacOS, Windows, iOS   | Proprietary |       |
| [SQLyog](https://webyog.com/product/sqlyog/)                                | NOT VERIFIED                                    | Windows               | Proprietary         |       |
| [TablePlus](https://tableplus.com/)                                         | [NOT VERIFIED]([https://dbeaver.com/databases/](https://docs.tableplus.com/))  | Linux, MacOS, Windows, iOS | Proprietary      |       |
| [Toad Edge](https://toadworld.com/)                                         | NOT VERIFIED                                    | MacOS, Windows, Jenkins plugin | Proprietary |       |
| [Valentina Studio](https://valentina-db.com/)                               | [NOT VERIFIED](https://valentina-db.com/en/database-management) | Linux, MacOS, Windows      | Proprietary  |       |

Notes

1. LibreOffice Base is a generic data visualization frontend. To learn how to use it with MariaDB, see the [MariaDB KB](https://mariadb.com/kb/en/libreoffice-base/).
2. Apache OpenOffice is the project from which LibreOffice was originally forked. LibreOffice became more popular over time, so consider LibreOffice Base as well. OpenOffice Base does not support MariaDB. However it supports MySQL and ODBC drivers, so in practice it should work with MariaDB for standard use cases.
3. At the time of writing, MariaDB support is only mentioned in the `README.md` file. A quick [search on GitHub](https://github.com/search?q=repo%3Asequelpro%2Fsequelpro%20mariadb&type=code) shows that this support is currently limited to version identification, some permissions and a TODO note.

**Web Interfaces**

| Project Name                                                                | MariaDB Support                                 | Platforms             | License            | Notes |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|-------|
| [Adminer](https://www.adminer.org/)                                         | NOT VERIFIED                                    | PHP                   | Apache2 or GPL2    |       |
| [Express Admin](https://github.com/simov/express-admin/)                                   | YES                                             | NodeJS                | [MIT](https://github.com/simov/express-admin/blob/main/LICENSE)    | [1] |
| [phpMyAdmin](https://www.phpmyadmin.net/)                                   | YES                                             | PHP                   | [GPL2](https://github.com/phpmyadmin/phpmyadmin/blob/master/LICENSE)                |    |

1. Express Admin is a NodeJS tool for easy creation of administrative interfaces, data entry forms and data visualisation MariaDB and other databases.

**TUIs**

| Project Name                                                                | MariaDB Support                                 | Platforms             | License  |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|
| [mycli](https://www.mycli.net/)                                             | YES                                             | Python                | Open Source        |


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
