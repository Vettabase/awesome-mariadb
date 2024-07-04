# Awesome MariaDB for DBAs

A curated list of awesome MariaDB resources, maintained by [Vettabase](https://vettabase.com) and sponsored by the [MariaDB Foundation](https://mariadb.org/).

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) Inspired by the `awesome-*` trend on GitHub.

This list is intended for Data Engineers. There are lists intended for other audiences. See [README.md](README.md).

## Contents

- [Change Data Capture](https://github.com/Vettabase/awesome-mariadb/blob/main/list-den.md#change-data-capture)
- [Data Integration](https://github.com/Vettabase/awesome-mariadb/blob/main/list-den.md#data-integration)

## Change Data Capture

Change Data Capture consists in reading the binary log.

**CDC Tools**

| Project                                                          | MariaDB Support   | Language / Platform   | License / Platform                   |
|------------------------------------------------------------------|-------------------|-----------------------|--------------------------------------|
| [Debezium](https://github.com/madvirus/mariadb-cdc)              | [YES](https://debezium.io/documentation/reference/stable/connectors/mysql.html#mysql-mariadb-support)  | Java       | [Apache2](https://debezium.io/license/) |
| [mariadb-cdc](https://github.com/madvirus/mariadb-cdc)           | YES               | Java                  | [Proprietary](https://github.com/madvirus/mariadb-cdc/issues/1) |
| [pg_chameleon](https://pgchameleon.org/)                         | MySQL             | Python3               | [BSD](https://github.com/the4thdoctor/pg_chameleon/blob/main/LICENSE.txt) |

**CDC Articles**

- [Deploying Flink CDC Jobs with Docker compose](https://gordonmurray.com/data/2023/11/02/deploying-flink-cdc-jobs-with-docker-compose.html)
- [MariaDB pipeline in Logstash](https://www.suncrescent.net/2020/06/mariadb-pipeline-in-logstash/)

## Data Integration

**From Social Networks**

- Twitter
  - Airbyte: [How to load data from Twitter to MariaDB ColumnStore](https://airbyte.com/how-to-sync/twitter-to-mariadb-columnstore)
  - Improvado: [Connect Twitter To MariaDB Without Coding](https://improvado.io/connections/twitter-to-mariadb)

---

Copyright 2024 Vettabase Ltd and contributors.

Awesome MariaDB list is licensed under [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).
