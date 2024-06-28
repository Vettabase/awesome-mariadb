# Awesome MariaDB for DBAs

A curated list of awesome MariaDB resources, maintained by [Vettabase](https://vettabase.com) and sponsored by the [MariaDB Foundation](https://mariadb.org/).

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) Inspired by the `awesome-*` trend on GitHub.

This list is intended for Database Administrators. There are lists intended for other audiences. See [README.md](README.md).

## Contents

- [Articles](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#articles)
- [Backups](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#backups)
- [Ansible](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#ansible)
- [Containers](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#containers)
- [Monitoring](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#monitoring)
- [Proxies](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#proxies)
- [Sharding](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#sharding)
- [Replication Managers](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#replication-managers)
- [Schema Versioning Tools](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#schema-versioning-tools)
- [Security](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#security)
- [Toolkits](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#toolkits)
- [User Interfaces](https://github.com/Vettabase/awesome-mariadb/blob/main/list-dba.md#user-interfaces)

## MariaDB Support Key

Some of the below sections only include resources that were created for MariaDB.

Other sections include resources that were created for MySQL, or for both, and the extent of MariaDB support is not always optimal. For those resources, we indicate the MariaDB support level. Refer to this key.

- `MySQL`: The resource states that it supports MySQL, but not MariaDB.
- `YES`: The resource states it supports MariaDB specifically, not something like "MySQL/MariaDB".
- `NOT VERIFIED`: The resource states that it supports MySQL and MariaDB (or the specified version number) but we do not know whether full support for MariaDB is implemented. It's possible that MariaDB support is assumed as a consequence of MySQL support, but this might be inaccurate. Please report any relevant problems you might find to us (and to the resource itself).
- `PARTIAL`: We have a clear list of what is or isn't officially supported.

## Articles

* [Introduction to Data Replication With MariaDB Using Docker Containers](https://dzone.com/articles/introduction-to-data-replication-with-mariadb-usin)

## Automation

Platforms and tools to automate MariaDB deployments.

### Ansible

Modules and collections:

- [Community.Mysql](https://docs.ansible.com/ansible/latest/collections/community/mysql/index.html) - This is the community MySQL collection distributed with Ansible. It works with MariaDB, but you need to be careful not to use MySQL-specific features. MariaDB-specific features are not supported.

Roles:

- [ansible-role-mariadb](https://github.com/fauust/ansible-role-mariadb) - This high quality role is used by the MariaDB Foundation for testing.
- [bertvv/ansible-role-mariadb](https://github.com/bertvv/ansible-role-mariadb) - Another production-grade role that removes unsafe defaults and handles configuration files in a completely dynamic manner.

Articles:

- [Creating dynamic configuration files with Ansible](https://vettabase.com/creating-dynamic-configuration-files-with-ansible/) - This article shows how to use Ansible and a Jinja template to automate the MariaDB configuration files creation.

## Backups

**Tools**

| Project                                                               | MariaDB Support                      | License / Platform                        | Description           |
|-----------------------------------------------------------------------|--------------------------------------|-------------------------------------------|-----------------------|
| [Backup Manager](https://fromdual.com/fromdual-backup-manager-bman)   | YES                                  |                                           | Supports many types of backups. By FromDual. |
| [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/)               | YES                                  | Distributed with MariaDB                  | Logical backups of data and/or schema. |
| [Mariabackup](https://mariadb.com/kb/en/mariabackup-overview/)        | YES                                  | Distributed with MariaDB                  | Online physical backups. |

**Articles**

- [Using MariaDB's binary log to restore a database after overwriting with old backup](https://orville.thebennettproject.com/articles/how-to-use-mariadb-10-binlog-to-restore-database/)

## Containers

### Docker

- [mariadb image](https://hub.docker.com/_/mariadb) - Official image, maintained by MariaDB Foundation.

### Kubernetes

- [mariadb-operator](https://github.com/mariadb-operator) - Maintained by MariaDB plc.

## Monitoring

| Project                                                             | MariaDB Support                                             | License / Platform                                         | Notes   |
|---------------------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------|---------|
| [Datadog](https://docs.datadoghq.com)                               | [MYSQL](https://docs.datadoghq.com)                         | Cloud                                                      |         |
| [PMM](https://docs.percona.com/percona-monitoring-and-management/)  | YES                                                         | [AGPL3](https://github.com/percona/pmm/blob/main/LICENSE) or cloud   | [1]     |
| [SolarWinds](https://www.solarwinds.com/)                           | YES                                                         | Commercial in-premise or cloud                             |         |
| [SSM](https://shatteredsilicon.net/mysql-monitoring-ssm/)           | YES                                                         | Open source                                                | [2]     |
| [Zabbix](https://www.zabbix.com/)                                | [NOT VERIFIED](https://www.zabbix.com/documentation/current/en/manual/installation/best_practices/access_control/mysql)                         | [AGPL3](https://github.com/zabbix/zabbix/blob/master/COPYING)   |         |

1. See the [online demo](https://pmmdemo.percona.com).
2. PMM v1 fork.

## Proxies

In the list below, SQL-aware means that a proxy understands SQL statements, and is able to perform tasks like read-write splitting.

- [ProxySQL](https://proxysql.com/) - Open source, widely used proxy with full support for MariaDB. SQL-aware.
- [MariaDB MaxScale](https://mariadb.com/kb/en/maxscale/) - Source available proxy maintained by MariaDB plc. SQL-aware.
- [HAProxy](https://www.haproxy.org/) - Open source, TCP proxy. Not SQL-aware.
  - [haproxy-galera](https://github.com/matthanley/haproxy-galera) - MariaDB Galera health check script for HAProxy.

## Sharding

Sharding solutions require evalation depending in your applications requirements. Some solutions are internal and shard with the application being unaware, or externally use rules and defititions which your application may need to understand.

| Project                                                             | MariaDB Support | License / Platform | Notes   |
|---------------------------------------------------------------------|-----------------|--------------------|---------|
| [CONNECT](https://mariadb.com/kb/en/using-connect-partitioning-and-sharding/) | YES   | GPLv2              | A storage engine. An outward table can be partitioned over serveral remote tables represented as partitions. |
| [MaxScale](https://mariadb.com/kb/en/mariadb-maxscale-24-schemarouter/) | YES         | Commercial         | A query and connection router that is part of Maxscale. |
| [ProxySQL](https://proxysql.com/documentation/how-to-setup-proxysql-sharding/) | YES  | GPLv3              | Sharding in ProxySQL by User, Schema or Data. Sharding is based on rules which pattern match on incoming queries. |
| [Spider](https://mariadb.com/kb/en/spider/)                         | YES             | GPLv2              | A storage engine for table definition shards and connections to split tables among several servers. |


## Replication Managers

| Project                                                                | MariaDB Support   | License / Platform |
|------------------------------------------------------------------------|-------------------|--------------------|
| [Replication Manager](https://signal18.io/products/srm)                | 10.0+             | GPl / Commercial   |
| [ClusterControl](https://docs.severalnines.com/docs/clustercontrol/)   | Yes               | Open Core          |

## Schema Versioning Tools

| Project Name                                            | MariaDB Support |
| ------------------------------------------------------- | --------------- |
| [ByteBase](https://www.bytebase.com/)                   | [10.7+](https://www.bytebase.com/docs/introduction/supported-databases/)
| [Flyway](https://flywaydb.org/)                         | [5.1, 10.11](https://documentation.red-gate.com/flyway/flyway-cli-and-api/supported-databases/mariadb)
| [Liquibase](https://www.liquibase.com/)                 | [PARTIAL](https://www.liquibase.com/databases/mariadb-server)
| [Skeema.io](https://www.skeema.io/)                     | [10.1](https://www.skeema.io/docs/requirements/)

## Security

**Tools**

- [Acra](https://github.com/cossacklabs/acra) - Database protection suite with field level encryption and intrusion detection
- [SecuRich](http://www.securich.com/) - Stored procedures library with user management and role implementation. Unmaintained, but useful with old MariaDB versions.

**Articles**

- [Monitoring MariaDB Security with Wazuh](https://www.linkedin.com/pulse/monitoring-mariadb-security-wazuh-luis-contreras/)

## Toolkits

| Project                                                                              | MariaDB Support                | License           | Language                   | Description   |
|--------------------------------------------------------------------------------------|--------------------------------|-------------------|----------------------------|---------|
| [common_schema](https://github.com/shlomi-noach/common_schema)                       | YES                            | [GPL2](https://github.com/shlomi-noach/common_schema/blob/master/LICENSE)                                                                                                                                                     | Stored Procedures          | A library of stored procedures for DBAs. Includes a parser for its own language, QueryScript, and a debugger. |
| [Percona Toolkit](https://www.percona.com/software/database-tools/percona-toolkit)   | YES                            | [GPL2](https://github.com/percona/percona-toolkit/blob/3.x/COPYING)                                                                                                                                                           | Perl                       | A set of Perl scripts for MariaDB and MySQL administration.

## User Interfaces

**GUIs**

| Project Name                                                                | MariaDB Support                                 | Platforms             | Free / Commercial  | Notes |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|-------|
| [Beekeeper Studio](https://www.beekeeperstudio.io/)                         | [NOT VERIFIED](https://docs.beekeeperstudio.io/user_guide/connecting/first-page/)  | Linux, MacOS, Windows | BOTH               |       |
| [DataGrip](https://www.jetbrains.com/datagrip/)                             | [YES](https://www.jetbrains.com/datagrip/features/) | Linux, MacOS, Windows | Commercial     |       |
| [DBeaver](https://dbeaver.io/)                                              | [NOT VERIFIED](https://dbeaver.com/databases/)  | Linux, MacOS, Windows | BOTH               |       |
| [DbVisualizer](https://www.dbvis.com/)                                      | NOT VERIFIED                                    | Native: Linux, Windows; Java: Linux, MacOS, Windows | BOTH               |       |
| [Harlequin](https://harlequin.sh/)                                          | MySQL                                           | Python                | FREE               |       |
| [HeidiSQL](https://www.heidisql.com/)                                       | YES                                              | Windows               | FREE               |       |
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
3. At the time of writing, MariaDB support is only mentioned in the `README.md` file. A quick [search on GitHub](https://github.com/search?q=repo%3Asequelpro%2Fsequelpro%20mariadb&type=code) shows that this support is currently limited to version identification, some permissions and a TODO note.

**Web Interfaces**

| Project Name                                                                | MariaDB Support                                 | Platforms             | Free / Commercial  |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|
| [Adminer](https://www.adminer.org/)                                         | NOT VERIFIED                                    | PHP                   | FREE               |
| [phpMyAdmin](https://www.phpmyadmin.net/)                                   | YES                                             | PHP                   | FREE               |

**TUIs**

| Project Name                                                                | MariaDB Support                                 | Platforms             | Free / Commercial  |
|-----------------------------------------------------------------------------|-------------------------------------------------|-----------------------|--------------------|
| [mycli](https://www.mycli.net/)                                             | YES                                             | Python                | FREE               |

---

Copyright 2024 Vettabase Ltd and contributors.

Awesome MariaDB list is licensed under [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).
