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
- [Stored Procedures](#stored-procedures)

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

**Articles**

- [Vector Storage, Indexing, and Search With MariaDB: What to Know About These New Features](https://hackernoon.com/vector-storage-indexing-and-search-with-mariadb-what-to-know-about-these-new-features)
- [Try RAG with MariaDB Vector on your own MariaDB data!](https://mariadb.org/rag-with-mariadb-vector/)
- [Playing with MariaDB Vector for initial AI tests](https://fromdual.com/playing-with-mariadb-vector-for-initial-ai-tests)

**Benchmarks**

- Evaluating vector indexes in MariaDB and pgvector: [part 1](https://smalldatum.blogspot.com/2025/01/evaluating-vector-indexes-in-mariadb.html), [part 2](https://smalldatum.blogspot.com/2025/01/evaluating-vector-indexes-in-mariadb_13.html)
- Vector indexes, MariaDB & pgvector, large server, large dataset: [part 1](https://smalldatum.blogspot.com/2025/01/vector-indexes-mariadb-pgvector-large_28.html), [part 2](https://smalldatum.blogspot.com/2025/01/vector-indexes-mariadb-pgvector-large_26.html)

## Change Data Capture

Change Data Capture consists in reading the binary log.

Some of these projects are complete data flow platforms that are able to consume the MariaDB binary log. Others are just log consumers that support the MariaDB binary log.

**CDC Tools**

| Project                                                          | MariaDB Support   | Language / Platform   | License / Platform                   |
|------------------------------------------------------------------|-------------------|-----------------------|--------------------------------------|
| [Apache Hop](https://hop.apache.org/)                            | [YES](https://hop.apache.org/manual/latest/database/databases/mariadb.html)                 | JVM                  | [Apache2](https://github.com/apache/hop/blob/main/LICENSE) |
| [Apache NiFi](https://nifi.apache.org/)                          | [MySQL](https://nifi.apache.org/docs/nifi-docs/components/org.apache.nifi/nifi-cdc-mysql-nar/1.24.0/org.apache.nifi.cdc.mysql.processors.CaptureChangeMySQL/index.html)                                                                                                       | JVM                  | [Apache2](https://github.com/apache/nifi/blob/main/LICENSE) |
| [Apache Superset](https://github.com/apache/superset)            | [YES](https://github.com/apache/superset) | TypeScript, Python  | [Apache2](https://github.com/apache/superset/blob/master/LICENSE.txt) |
| [Dolt](https://dolthub.com/)                                     | [YES](https://docs.dolthub.com/guides/binlog-replication)  | Go        | [Apache2](https://github.com/dolthub/dolt/blob/main/LICENSE) |
| [Debezium](https://github.com/madvirus/mariadb-cdc)              | [YES](https://debezium.io/documentation/reference/stable/connectors/mysql.html#mysql-mariadb-support)  | JVM       | [Apache2](https://debezium.io/license/) |
| [go-mysql](https://github.com/go-mysql-org/go-mysql)    | [YES](https://github.com/go-mysql-org/go-mysql/blob/master/mysql/const.go) | Go | [MIT](https://github.com/go-mysql-org/go-mysql/blob/master/LICENSE) |
| [mariadb-cdc](https://github.com/madvirus/mariadb-cdc)           | YES               | JVM                  | [Proprietary](https://github.com/madvirus/mariadb-cdc/issues/1) |
| [MySqlCdc](https://github.com/rusuly/MySqlCdc)                   | YES               | .NET                  | [MIT](https://github.com/rusuly/MySqlCdc/blob/main/LICENSE) |
| [pg_chameleon](https://pgchameleon.org/)                         | MySQL             | Python3               | [BSD](https://github.com/the4thdoctor/pg_chameleon/blob/main/LICENSE.txt) |

**CDC Articles**

- [Deploying Flink CDC Jobs with Docker compose](https://gordonmurray.com/data/2023/11/02/deploying-flink-cdc-jobs-with-docker-compose.html)
- [MariaDB pipeline in Logstash](https://www.suncrescent.net/2020/06/mariadb-pipeline-in-logstash/)

## Data Integration

The following resources show how to integrate MariaDB with various other data technologies. Resources are grouped by technology type (eg: social networks) and ordered by technology (eg: Facebook, Twitter...). Resources might refer to a particular third party tool, in which case the tool name is indicated before the resource title.

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

**RESTful APIs**

- [How to query a REST API with MariaDB CONNECT engine](https://vettabase.com/how-to-query-a-rest-api-with-mariadb-connect-engine/)
- [MariaDB Connect Storage Engine & new JSON support](https://av.tib.eu/media/30968) (FOSDEM 2016 talk)

## Data Visualisation

| Project                                                          | MariaDB Support   | Language / Platform   | License / Platform                   |
|------------------------------------------------------------------|-------------------|-----------------------|--------------------------------------|
| [Geckoboard](https://www.geckoboard.com/)                        | [YES](https://www.geckoboard.com/product/data-sources/mariadb/) | Cloud | Cloud |
| [Metabase](https://www.metabase.com/)                            | [YES](https://www.metabase.com/data_sources/mariadb) | JVM | [AGPL, Proprietary](https://github.com/metabase/metabase/blob/master/LICENSE.txt), [Cloud](https://www.metabase.com/pricing/) |
| [Mode](https://mode.com/)                                        | [YES](https://mode.com/integrations/mariadb) | Cloud | Cloud |

## Stored Procedures

**Debuggers**

| Project                                                          | MariaDB Support   | Platforms   | License / Platform                   |
|------------------------------------------------------------------|-------------------|-------------|--------------------------------------|
| [Debugger for MySQL](http://mydebugger.com/)                     | YES               | Windows     | Proprietary                          |

**Stored Procedures Articles**

- [PL/SQL in MariaDB](https://ocelot.ca/blog/blog/2017/01/15/plsql-in-mariadb/)
- [MySQL: stored procedures and SQL/PSM](https://www.abis.be/html/en2012-10_MySQL_procedures.html)
- [Stored Procedures in MariaDB: Smarter, Easier and More Powerful](https://vettabase.com/stored-procedures-in-mariadb-smarter-easier-and-more-powerful/)

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
