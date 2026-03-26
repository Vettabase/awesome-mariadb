# Awesome MariaDB for Data Engineers

A curated list of awesome MariaDB resources, maintained by [Vettabase](https://vettabase.com) and sponsored by the [MariaDB Foundation](https://mariadb.org/).

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) Inspired by the `awesome-*` trend on GitHub.

This list is intended for Data Engineers. There are lists intended for other audiences. See [README.md](README.md).

## Contents

- [AI Integrations](#ai-integrations)
- [AI: Vectors](#ai-vectors)
- [Change Data Capture](#change-data-capture)
- [Data Integration](#data-integration)
- [Data Visualisation](#data-visualisation)
- [MCP](#mcp-servers)
- [Stored Procedures](#stored-procedures)
- [User Interfaces](#user-interfaces)

See the [key](#key) for explanations of the terms used in this list.

## AI Integrations

| Project                                                          | MariaDB Support   | License / Platform                   |
|------------------------------------------------------------------|-------------------|--------------------------------------|
| [MindsDB](https://mindsdb.com/)                                  | [YES](https://docs.mindsdb.com/integrations/data-integrations/mariadb) | [MIT](https://github.com/mindsdb/mindsdb/blob/main/LICENSE), [Cloud](https://cloud.mindsdb.com/) |
| [TileDB](https://tiledb.com/)                                    | [YES](https://docs.tiledb.com/mariadb) | [MIT](https://github.com/TileDB-Inc/TileDB/blob/dev/LICENSE), [Cloud](https://tiledb.com/pricing/)

## AI: Vectors

**Frameworks**

| Language / Platform | Project                                        | MariaDB Support                                                                         | License / Platform                   |
|---------------------|------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------|
| Java                | [Spring](https://spring.io)                    | [YES](https://docs.spring.io/spring-ai/reference/api/vectordbs/mariadb.html)            | [Apache 2](https://www.apache.org/licenses/LICENSE-2.0) |
| PHP                 | [LLPhant](https://github.com/LLPhant/LLPhant)  | [YES](https://github.com/LLPhant/LLPhant/blob/main/devx/docker-compose-mariadb.yml)     | [MIT](https://github.com/LLPhant/LLPhant/blob/main/LICENSE.md) |
| Python              | [LangChain](https://www.langchain.com/)        | [YES](https://github.com/mariadb-corporation/langchain-mariadb)                         | [MIT](https://github.com/langchain-ai/langchain/blob/master/LICENSE) |
| Python              | [LLamaIndex](https://llamaindex.ai)            | [YES](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mariadb/) | [MIT](https://github.com/run-llama/llama_index/blob/main/LICENSE) |

**Applications**

| Language / Platform | Project                                        | MariaDB Support                                               | License / Platform                   |
|---------------------|------------------------------------------------|---------------------------------------------------------------|--------------------------------------|
| Node.js             | [mariadb-nodejs-rag-demo](https://github.com/Vettabase/awesome-mariadb/edit/main/list-den.md) | YES            | [None](https://github.com/rozhnev/mariadb-nodejs-rag-demo/issues/6) |

**Articles**

- [Introduction to MariaDB Vector Search](https://severalnines.com/blog/introduction-to-mariadb-vector-search/)
- [Vector Storage, Indexing, and Search With MariaDB: What to Know About These New Features](https://hackernoon.com/vector-storage-indexing-and-search-with-mariadb-what-to-know-about-these-new-features)
- [Try RAG with MariaDB Vector on your own MariaDB data!](https://mariadb.org/rag-with-mariadb-vector/)
- [Playing with MariaDB Vector for initial AI tests](https://fromdual.com/playing-with-mariadb-vector-for-initial-ai-tests)
- Video: [MARIADB Just Got a Game Changing Vector Data Type!](https://www.youtube.com/watch?v=MQT23wf_Vmo)
- Video: [Introduction to Vector Embeddings and Vector Search](https://www.youtube.com/watch?v=XkB2DLK60JU)

**Benchmarks**

- [MariaDB innovation: binlog_storage_engine, small server, Insert Benchmark](https://smalldatum.blogspot.com/2026/02/mariadb-innovation-binlogstorageengine_17.html)
- Evaluating vector indexes in MariaDB and pgvector: [part 1](https://smalldatum.blogspot.com/2025/01/evaluating-vector-indexes-in-mariadb.html), [part 2](https://smalldatum.blogspot.com/2025/01/evaluating-vector-indexes-in-mariadb_13.html)
- Vector indexes, MariaDB & pgvector, large server, large dataset: [part 1](https://smalldatum.blogspot.com/2025/01/vector-indexes-mariadb-pgvector-large_28.html), [part 2](https://smalldatum.blogspot.com/2025/01/vector-indexes-mariadb-pgvector-large_26.html)

## Change Data Capture

Change Data Capture consists in reading the binary log, continuously or periodically. The purpose is keeping track of data changes, to generate events or to keep a copy of the data up to date (as it happens with replication). A program that reads the binary log is called a consumer.

Some of these projects are complete data flow platforms that are able to consume the MariaDB binary log. Others are just log consumers that support the MariaDB binary log.

Most MySQL binary log consumers tend to work with MariaDB, but they might encounter several differences that will prevent them from parsing the logs correctly:

 - MariaDB GTID and MySQL GTID have different formats;
 - MariaDB has additional data types;
 - Both MariaDB and MySQL have unique features, like MariaDB invisible columns;
 - MariaDB has options that cause the binary log to include additional information, making it different from MySQL binary log.

**Consumers**

| Project                                                          | MariaDB Support   | Language / Platform   | License / Platform                   | Notes |
|------------------------------------------------------------------|-------------------|-----------------------|--------------------------------------|-------|
| [Apache Hop](https://hop.apache.org/)                            | [YES](https://hop.apache.org/manual/latest/database/databases/mariadb.html)                 | JVM                  | [Apache2](https://github.com/apache/hop/blob/main/LICENSE) |  |
| [Apache NiFi](https://nifi.apache.org/)                          | [MySQL](https://nifi.apache.org/docs/nifi-docs/components/org.apache.nifi/nifi-cdc-mysql-nar/1.24.0/org.apache.nifi.cdc.mysql.processors.CaptureChangeMySQL/index.html)                                                                                                       | JVM                  | [Apache2](https://github.com/apache/nifi/blob/main/LICENSE) |  |
| [Apache Superset](https://github.com/apache/superset)            | [YES](https://github.com/apache/superset) | TypeScript, Python  | [Apache2](https://github.com/apache/superset/blob/master/LICENSE.txt) |  |
| [Dolt](https://dolthub.com/)                                     | [YES](https://docs.dolthub.com/guides/binlog-replication)  | Go        | [Apache2](https://github.com/dolthub/dolt/blob/main/LICENSE) |  |
| [Debezium](https://github.com/madvirus/mariadb-cdc)              | [YES](https://debezium.io/documentation/reference/stable/connectors/mysql.html#mysql-mariadb-support)  | JVM       | [Apache2](https://debezium.io/license/) | [1] |
| [go-mysql](https://github.com/go-mysql-org/go-mysql)    | [YES](https://github.com/go-mysql-org/go-mysql/blob/master/mysql/const.go) | Go | [MIT](https://github.com/go-mysql-org/go-mysql/blob/master/LICENSE) |  |
| [mariadb-cdc](https://github.com/madvirus/mariadb-cdc)           | YES               | JVM                  | [Proprietary](https://github.com/madvirus/mariadb-cdc/issues/1) |  |
| [MySqlCdc](https://github.com/rusuly/MySqlCdc)                   | YES               | .NET                  | [MIT](https://github.com/rusuly/MySqlCdc/blob/main/LICENSE) | [2] |
| [pg_chameleon](https://pgchameleon.org/)                         | MySQL             | Python3               | [BSD](https://github.com/the4thdoctor/pg_chameleon/blob/main/LICENSE.txt) |  |

Notes

1. See the [Debezium connector for MariaDB](https://debezium.io/documentation/reference/stable/connectors/mariadb.html).
2. Latest supported MariaDB version is 10.6. Does not support GTID.

**CDC Articles**

- [Deploying Flink CDC Jobs with Docker compose](https://gordonmurray.com/data/2023/11/02/deploying-flink-cdc-jobs-with-docker-compose.html)
- [MariaDB pipeline in Logstash](https://www.suncrescent.net/2020/06/mariadb-pipeline-in-logstash/)
- [Prepare MySQL/MariaDB for RDI](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/prepare-dbs/my-sql-mariadb/)

## Data Integration

The following resources show how to integrate MariaDB with various other data technologies. Resources are grouped by technology type (eg: social networks) and ordered by technology (eg: Facebook, Twitter...). Resources might refer to a particular third party tool, in which case the tool name is indicated before the resource title.

**Data Orchestration Frameworks**

| Platform                                       | Project                                        | MariaDB Support | License / Platform                   | Notes |
|------------------------------------------------|------------------------------------------------|-----------------|--------------------------------------|-------|
| [Apache Airflow](https://airflow.apache.org/)  | [Airflow MariaDB Connector](https://github.com/Pratush12/mariadb-airflow-hackathon) | YES | None        | [1]   |
| [Dagster](https://dagster.io/)                 | MariaDB integration, not yet merged            | YES             | [Apache 2](https://github.com/dagster-io/dagster/blob/master/LICENSE) | [2] |


1. Initially developed as part of a MariaDB Hackathon. Airflow MariaDB Connector was the winner. See [this post](https://mariadb.org/apache-airflow-integration-for-mariadb-winner-of-mariadb-bangpypers-hackathon-2025/) and [this interview[(https://www.youtube.com/watch?v=NX29FVTL0Eo).
2. The project has been proposed for integration into the Dagster code itself. It was developed as part of a MariaDB Hackathon. It conquered the 2nd place. See [this post](https://mariadb.org/dagster-integration-for-mariadb-2nd-place-in-mariadb-bangpypers-hackathon-2025/) and [this interview](https://www.youtube.com/watch?v=wLjYSxFrl_g).


**From Social Networks**

- Twitter
  - Airbyte: [How to load data from Twitter to MariaDB ColumnStore](https://airbyte.com/how-to-sync/twitter-to-mariadb-columnstore)
  - Python: [Collecting / Storing Tweets with Python and MySQL](https://pythondata.com/collecting-storing-tweets-python-mysql/). Applies to MariaDB with no differences.

**Other Databases**

- [Using CONNECT to access remote MariaDB or MySQL tables](https://vettabase.com/using-connect-to-access-remote-mariadb-or-mysql-tables/)
- [Accessing Oracle tables via MariaDB CONNECT engine and ODBC](https://mysqlentomologist.blogspot.com/2017/04/accessing-oracle-tables-via-mariadb.html)
- [MariaDB CONNECT Storage Engine access to Oracle 11GR2](https://serge.frezefond.com/2013/12/mariadb-connect-storage-engine-access-to-oracle-11gr2/)
- [MariaDB and external data](https://www.easysoft.com/blog/mariadb.html)
- [MariaDB CONNECT Storage Engine and non MySQL syntax selects](https://serge.frezefond.com/2013/12/mariadb-connect-storage-engine-and-non-mysql-syntax-selects/)
- [Trino MariaDB connector](https://trino.io/docs/current/connector/mariadb.html)

**RESTful APIs**

- [How to query a REST API with MariaDB CONNECT engine](https://vettabase.com/how-to-query-a-rest-api-with-mariadb-connect-engine/)
- [MariaDB Connect Storage Engine & new JSON support](https://av.tib.eu/media/30968) (FOSDEM 2016 talk)

**Other Applications**

- [Google Cloud MariaDB Integration](https://cloud.google.com/integration-connectors/docs/connectors/mariadb/configure)

## Data Visualisation

| Project                                                          | MariaDB Support   | Language / Platform   | License / Platform                   |
|------------------------------------------------------------------|-------------------|-----------------------|--------------------------------------|
| [Geckoboard](https://www.geckoboard.com/)                        | [YES](https://www.geckoboard.com/product/data-sources/mariadb/) | Cloud | Cloud |
| [Metabase](https://www.metabase.com/)                            | [YES](https://www.metabase.com/data_sources/mariadb) | JVM | [AGPL, Proprietary](https://github.com/metabase/metabase/blob/master/LICENSE.txt), [Cloud](https://www.metabase.com/pricing/) |
| [Mode](https://mode.com/)                                        | [YES](https://mode.com/integrations/mariadb) | Cloud | Cloud |

## MCP Servers

[MCP (Model Context Protocol)](https://en.wikipedia.org/wiki/Model_Context_Protocol) is an open protocol created by Anthropic that standardises the way LLMs communicate with agents and data sources like MariaDB.

| Project                                                          | MariaDB Support   | Language / Platform   | License / Platform                   |
|------------------------------------------------------------------|-------------------|-----------------------|--------------------------------------|
| [MariaDB Vector MCP server](https://github.com/mariadb/mcp)      | YES               | Python, Docker        | [MIT](https://github.com/MariaDB/mcp/blob/main/LICENSE) |

## Stored Procedures

**Debuggers**

| Project                                                          | MariaDB Support   | Platforms   | License / Platform                   |
|------------------------------------------------------------------|-------------------|-------------|--------------------------------------|
| [Debugger for MySQL](http://mydebugger.com/)                     | YES               | Windows     | Proprietary                          |

**Stored Procedures Articles**

- [PL/SQL in MariaDB](https://ocelot.ca/blog/blog/2017/01/15/plsql-in-mariadb/)
- [MySQL: stored procedures and SQL/PSM](https://www.abis.be/html/en2012-10_MySQL_procedures.html)
- [Stored Procedures in MariaDB: Smarter, Easier and More Powerful](https://vettabase.com/stored-procedures-in-mariadb-smarter-easier-and-more-powerful/)

## User Interfaces

<!-- INCLUDE user-interfaces -->
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
| [Sequelpro](https://www.sequelpro.com/)                                    | PARTIAL                                         | MacOS                 | Open Source                  | [3]   |
| [SQLPro Studio](https://www.sqlprostudio.com/)                              | NOT VERIFIED                                    | MacOS, Windows, iOS   | Proprietary |       |
| [SQLyog](https://webyog.com/product/sqlyog/)                                | NOT VERIFIED                                    | Windows               | Proprietary         |       |
| [TablePlus](https://tableplus.com/)                                         | [NOT VERIFIED]([https://dbeaver.com/databases/](https://docs.tableplus.com/))  | Linux, MacOS, Windows, iOS | Proprietary      |       |
| [Toad Edge](https://toadworld.com/)                                         | NOT VERIFIED                                    | MacOS, Windows, Jenkins plugin | Proprietary |       |
| [Valentina Studio](https://valentina-db.com/)                               | [NOT VERIFIED](https://valentina-db.com/en/database-management) | Linux, MacOS, Windows      | Proprietary  |       |
| [whodb](https://github.com/clidey/whodb)       | YES | Go                         | [Apache 2](https://github.com/clidey/whodb/blob/main/LICENSE) |  |

Notes

1. LibreOffice Base is a generic data visualization frontend. To learn how to use it with MariaDB, see the [MariaDB KB](https://mariadb.com/docs/server/clients-and-utilities/graphical-and-enhanced-clients/libreoffice-base).
2. Apache OpenOffice is the project from which LibreOffice was originally forked. LibreOffice became more popular over time, so consider LibreOffice Base as well. OpenOffice Base does not support MariaDB. However it supports MySQL and ODBC drivers, so in practice it should work with MariaDB for standard use cases.
3. At the time of writing, MariaDB support is only mentioned in the `README.md` file. A quick [search on GitHub](https://github.com/search?q=repo%3Asequelpro%2Fsequelpro%20mariadb&type=code) shows that this support is currently limited to version identification, some permissions and a TODO note.

**Web Interfaces**

| Project Name                                                                | MariaDB Support                                 | Platforms             | License            | Notes |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|-------|
| [Adminer](https://www.adminer.org/)                                         | NOT VERIFIED                                    | PHP                   | Apache2 or GPL2    |       |
| [Express Admin](https://github.com/simov/express-admin/)                                   | YES                                             | NodeJS                | [MIT](https://github.com/simov/express-admin/blob/main/LICENSE)    | [1] |
| [phpMyAdmin](https://www.phpmyadmin.net/)                                   | YES                                             | PHP                   | [GPL2](https://github.com/phpmyadmin/phpmyadmin/blob/master/LICENSE)                |    |
| [Prisma Studio](https://www.prisma.io/studio)                               | YES                                           | Node.js               | [Apache 2](https://github.com/prisma/prisma/blob/main/LICENSE)           |  |

1. Express Admin is a NodeJS tool for easy creation of administrative interfaces, data entry forms and data visualisation MariaDB and other databases.

**TUIs**

| Project Name                                                                | MariaDB Support                                 | Platforms             | License  |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|
| [DBCrust](https://github.com/clement-tourriere/dbcrust)                     | YES                                             | Rust                  | [MIT](https://github.com/clement-tourriere/dbcrust/blob/main/LICENSE) |
| [mycli](https://www.mycli.net/)                                             | YES                                             | Python                | Open Source        |
| [usql](https://github.com/xo/usql)                                          | [YES](https://github.com/xo/usql?tab=readme-ov-file#supported-database-schemes-and-aliases)                                    | Linux, MacOS, Windows | [MIT](https://github.com/xo/usql/blob/master/LICENSE) |       |

**Pagers**

The mentioned TUIs can use any pager to visualise the results of long queries. But it's worth mentioning that at least one specific page for MariaDB and MySQL exists.

| Project Name                                                                | MariaDB Support                                 | Platforms             | License  |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|
| [mypager](https://github.com/romuald/mypager)                               | YES                                             | Perl                  | [Apache 2](https://github.com/romuald/mypager/blob/master/LICENSE) |
<!-- END INCLUDE -->


---

Copyright 2024 2025 2026 Vettabase Ltd and contributors.

Awesome MariaDB list is licensed under [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).
