# Awesome MariaDB for DBAs

A curated list of awesome MariaDB resources, maintained by [Vettabase](https://vettabase.com) and sponsored by the [MariaDB Foundation](https://mariadb.org/).

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) Inspired by the `awesome-*` trend on GitHub.

This list is intended for Database Administrators. There are lists intended for other audiences. See [README.md](README.md).

## Contents

- [Articles](#articles)
- [Ansible](#ansible)
- [Chef](#chef)
- [Backups](#backups)
- [Containers](#containers)
- [Monitoring](#monitoring)
- [Proxies](#proxies)
- [Sharding](#sharding)
- [Replication](#replication)
- [Schema Versioning](#schema-versioning)
- [Security](#security)
- [Toolkits](#toolkits)
- [User Interfaces](#user-interfaces)

See the [key](#key) for explanations of the terms used in this list.

## Articles

* [Arch Linux MariaDB documentation](https://wiki.archlinux.org/title/MariaDB) - Includes post-install tasks and common problems resolution.
* [Introduction to Data Replication With MariaDB Using Docker Containers](https://dzone.com/articles/introduction-to-data-replication-with-mariadb-usin)
* [Customizing MariaDB Docker Images](https://hackernoon.com/customizing-mariadb-docker-images)
* [Everything You Need to Know About Replication Filters in MySQL and MariaDB](https://genexdbs.com/everything-you-need-to-know-about-replication-filters-in-mysql-and-mariadb/)
* [MariaDB semi-sync replication using containers](https://mariadb.org/mariadb-semi-sync-replication-using-containers/)
* [Is Galera trx_commit=2 and sync_binlog=0 evil?](https://mysqlquicksand.wordpress.com/2019/09/11/is-galera-trx_commit2-and-sync_binlog0-evil/)
* [InnoDB Durability](https://lists.mariadb.org/hyperkitty/list/discuss@lists.mariadb.org/thread/SY6YIADSASGFSGHFD2Z35WMU4KOLRAWE/#DVEELBZWT4FCMJBV6SRPVD3EHIE5PCG5) - mailing list discussion
* [MariaDB connection ID](https://www.fromdual.com/mariadb_connection_id)
* [Database load balancing for MySQL and MariaDB with ProxySQL](https://severalnines.com/resources/whitepapers/database-load-balancing-for-mysql-and-mariadb-with-proxysql/)
* [InnoDB deep dive: commit phase](https://medium.com/@arbaudie.it/innodb-deep-dive-commit-phase-20e9022e98d5)

## Automation

Platforms and tools to automate MariaDB deployments.

### Ansible

Modules and collections:

- [Community.Mysql](https://docs.ansible.com/ansible/latest/collections/community/mysql/index.html) - This is the community MySQL collection distributed with Ansible. It works with MariaDB, but you need to be careful not to use MySQL-specific features. MariaDB-specific features are not supported.

Roles:

- [ansible-role-mariadb](https://github.com/fauust/ansible-role-mariadb) - This high quality role is used by the MariaDB Foundation for testing.
- [bertvv/ansible-role-mariadb](https://github.com/bertvv/ansible-role-mariadb) - Another production-grade role that removes unsafe defaults and handles configuration files in a completely dynamic manner.

Articles:

- [Automating MariaDB server Deployment and Database configuration with Ansible](https://meheraskri.medium.com/automating-mariadb-server-deployment-and-database-configuration-with-ansible-b5ebcc339ec3)
- [Creating dynamic configuration files with Ansible](https://vettabase.com/creating-dynamic-configuration-files-with-ansible/) - This article shows how to use Ansible and a Jinja template to automate the MariaDB configuration files creation.

### Chef

- [MariaDB Cookbook](https://supermarket.chef.io/cookbooks/mariadb) - Maintained by [Sous Chefs](https://www.sous-chefs.org/)

### Nomad

Articles:

- [MariaDB Galera Cluster with Hashicorp Nomad and Consul Connect](https://medium.com/@ituoga/mariadb-galera-cluster-with-hashicorp-nomad-and-consul-connect-5028af8364c0)

### Puppet

- [puppet-mariadb](https://github.com/NeCTAR-RC/puppet-mariadb) - Fork of PuppetLabs MySQL module, which supports MariaDB and Galera on RedHat and Debian
- [puppet-galera](https://github.com/markt-de/puppet-galera) - Manage MariaDB Galera Cluster or Percona XtraDB Cluster. Supports Galera Arbitrator. Supports both systemd and xinetd.

### Misc Automation Articles

- Video: [MariaDB features that all devops should know](https://www.youtube.com/watch?v=8lH7cDX0_a8&ab_channel=MariaDBFoundation)
- [How to Schedule Queries in MariaDB](https://www.getgalaxy.io/learn/glossary/how-to-schedule-queries-in-mariadb)

## Backups

**Tools**

| Project                                                               | MariaDB Support                      | License / Platform                        | Description           |
|-----------------------------------------------------------------------|--------------------------------------|-------------------------------------------|-----------------------|
| [Backup Manager](https://fromdual.com/fromdual-backup-manager-bman)   | YES                                  | Proprietary                              | Supports many types of backups. By FromDual. |
| [maria-back-me-up](https://github.com/sapcc/maria-back-me-up)         | YES                                  | [Apache License 2](https://github.com/sapcc/maria-back-me-up/blob/master/LICENSE) | Incremental dumps on Kubernetes. Supports archival. |
| [mariadb-backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview)        | YES                                  | Distributed with MariaDB                  | Online physical backups. |
| [mariabackup-script](https://github.com/paskinator/mariabackup-script)  | YES                                | [GPL3](https://github.com/paskinator/mariabackup-script/blob/main/LICENSE)    | Wrapper script for Mariabackup. Handles failed backups. |
| [mariadb-dump](https://mariadb.com/docs/server/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump)               | YES                                  | Distributed with MariaDB                  | Logical backups of data and/or schema. |

**Articles**

- [Using MariaDB's binary log to restore a database after overwriting with old backup](https://orville.thebennettproject.com/articles/how-to-use-mariadb-10-binlog-to-restore-database/)
- [Backing up MariaDB Temporal Database](https://stackoverflow.com/a/57186022/9445059) (StackOverflow answer)

## Containers

### Docker

- [mariadb image](https://hub.docker.com/_/mariadb) - Official image, maintained by MariaDB Foundation.
- [yobasystems/alpine-mariadb](https://github.com/yobasystems/alpine-mariadb) - MariaDB image based on Alpine Linux.
- [linuxserver/mariadb](https://hub.docker.com/r/linuxserver/mariadb) - Maintained by LinuxServer. Different configuration choices compared to the official image, for example the query cache is enabled on demand, rather than disabled. Supports customization via LinuxServer Docker mods.
- [mariadb-container](https://github.com/sclorg/mariadb-container) - Dockerfiles with a focus on OpenShift usage, but suitable for general use.

### Kubernetes

- [mariadb-operator](https://github.com/mariadb-operator) - Maintained by MariaDB plc.

## Monitoring

| Project                                                             | MariaDB Support                                             | License / Platform                                         | Notes   |
|---------------------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------|---------|
| [Datadog](https://docs.datadoghq.com)                               | YES but see [known limitations](https://docs.datadoghq.com) | Proprietary in-premiseor cloud                                                      |         |
| [Dolphie](https://github.com/charles-001/dolphie)                   | YES                                                         | [GPL3](https://github.com/charles-001/dolphie/blob/main/LICENSE) |   |
| [golang-mariadbconsole](https://github.com/luiscontrerasdo/golang-mariadbconsole)  | YES                                          | [GPL3](https://github.com/luiscontrerasdo/golang-mariadbconsole/blob/main/LICENSE)   |         |
| [Monyog](https://webyog.com/product/monyog/)                        | YES                         | Proprietary   | [1] |
| [New Relic](https://newrelic.com)                                   | [YES](https://newrelic.com/instant-observability/mariadb)   | [Cloud](https://newrelic.com/pricing) |  |
| [PMM](https://docs.percona.com/percona-monitoring-and-management/)  | YES                                                         | [AGPL3](https://github.com/percona/pmm/blob/main/LICENSE) or cloud   | [2]     |
| [Prometheus MySQL Exporter](https://github.com/prometheus/mysqld_exporter)  | YES                           | [Apache 2](https://github.com/prometheus/mysqld_exporter/blob/main/LICENSE)   | 
| [SolarWinds](https://www.solarwinds.com/)                           | YES                                                         | Proprietary in-premise or cloud                             |         |
| [Splunk](https://www.splunk.com/)                                   | YES                                                         | Proprietary in-premise or cloud                             |         |
| [SSM](https://shatteredsilicon.net/mysql-monitoring-ssm/)           | YES                                                         | ?                                                | [3]     |
| [StatsD](https://github.com/statsd/statsd)                          | YES                                                         | [MIT](https://github.com/statsd/statsd/blob/master/LICENSE)   | [5]
| [Zabbix](https://www.zabbix.com/)                                | YES                         | [AGPL3](https://github.com/zabbix/zabbix/blob/master/COPYING)   | [4]

**Notes**

1. See their article: [MariaDB Monitoring](https://webyog.com/monitoring-mysql-and-mariadb-servers/).
2. See the [online demo](https://pmmdemo.percona.com).
3. PMM v1 fork.
4. See [agent gathering MariaDB metrics](https://www.zabbix.com/integrations/mysql)
5. Integrations between StatsD and MariaDB:
   - [Via Telegraf](https://www.influxdata.com/integrations/statsd-mariadb/);
   - [mysql-statsd](https://github.com/db-art/mysql-statsd)

**Articles**

- [Monitoring MySQL, Percona Server, and MariaDB with the Elastic Stack](https://www.elastic.co/blog/monitoring-mysql-percona-server-and-mariadb-with-the-elastic-stack)
- Splunk: [Monitoring MariaDB and MySQL](https://community.splunk.com/t5/Community-Blog/Monitoring-MariaDB-and-MySQL/ba-p/703731)

## Proxies

In the list below, SQL-aware means that a proxy understands SQL statements, and is able to perform tasks like read-write splitting.

- [ProxySQL](https://proxysql.com/) - Open source, widely used proxy with full support for MariaDB. SQL-aware.
- [MariaDB MaxScale](https://mariadb.com/docs/maxscale) - Source available proxy maintained by MariaDB plc. SQL-aware.
- [HAProxy](https://www.haproxy.org/) - Open source, TCP proxy. Not SQL-aware.
  - [haproxy-galera](https://github.com/matthanley/haproxy-galera) - MariaDB Galera health check script for HAProxy.

**Articles**

- [MariaDB MaxScale 21.06 now released as GPL](https://mariadb.com/resources/blog/mariadb-maxscale-21-06-now-released-as-gpl/)

## Sharding

The following projects are either sharding components or sub-components that be used to create a sharding solution. There is no "out of the box" solution. Internal or database native options require your application to be aware and even manage the shards. External solutions will require bespoke backup and monitoring tooling for where the database shards are hosted across several servers.

| Project                                                             | MariaDB Support | License / Platform | Notes   |
|---------------------------------------------------------------------|-----------------|--------------------|---------|
| [MaxScale](https://mariadb.com/docs/maxscale/maxscale-archive/archive-of-2x.xx-versions/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-schemarouter) | YES         | Proprietary        | A query and connection router that is part of Maxscale. |
| [ProxySQL](https://proxysql.com/documentation/how-to-setup-proxysql-sharding/) | YES  | GPLv3              | Sharding in ProxySQL by User, Schema or Data. Sharding is based on rules which pattern match on incoming queries. |
| [Spider](https://mariadb.com/docs/server/server-usage/storage-engines/spider)                         | YES             | GPLv2              | A storage engine for table definition shards and connections to split tables among several servers. |


## Replication

| Project                                                                | MariaDB Support   | License / Platform |
|------------------------------------------------------------------------|-------------------|--------------------|
| [ClusterControl](https://docs.severalnines.com/docs/clustercontrol/)   | Yes               | Open Core          |
| [go-mysql](https://github.com/go-mysql-org/go-mysql)    | [YES](https://github.com/go-mysql-org/go-mysql/blob/master/mysql/const.go) | [MIT](https://github.com/go-mysql-org/go-mysql/blob/master/LICENSE) |
| [Replication Manager](https://signal18.io/products/srm)                | 10.0+             | GPL / Proprietary  |

## Schema Versioning

| Project Name                                            | MariaDB Support | License / Platform |
| ------------------------------------------------------- | --------------- | ------------------ |
| [ByteBase](https://www.bytebase.com/)                   | [10.7+](https://www.bytebase.com/docs/introduction/supported-databases/) | Open source, proprietary, cloud |
| [ChronoVoyage](https://pypi.org/project/chronovoyage/)  | YES | MIT |
| [Flyway](https://flywaydb.org/)                         | [5.1, 10.11](https://documentation.red-gate.com/flyway/flyway-cli-and-api/supported-databases/mariadb) | [Apache 2](https://github.com/flyway/flyway/blob/main/LICENSE.txt) |
| [Liquibase](https://www.liquibase.com/)                 | [PARTIAL](https://www.liquibase.com/databases/mariadb-server) | [Proprietary](https://www.liquibase.com/pricing) or [Apache 2](https://github.com/liquibase/liquibase/blob/master/LICENSE.txt) |
| [migrate](https://github.com/golang-migrate/migrate)    | YES             | [MIT](https://github.com/golang-migrate/migrate/blob/master/LICENSE) |
| [Prisma Migrate](https://github.com/prisma/prisma)      | YES             | [Apache 2](https://github.com/prisma/prisma/blob/main/LICENSE) |
| [Skeema](https://www.skeema.io/)                     | [10.1+](https://www.skeema.io/docs/requirements/) | [Proprietary](https://www.skeema.io/download/) or [Apache 2](https://github.com/skeema/skeema/blob/main/LICENSE) |

## Security

**Tools**

| Project Name                                            | MariaDB Support | License |                                                           | Notes |
| ------------------------------------------------------- | --------------- | ------- |-----------------------------------------------------------|-------|
| [Acra](https://github.com/cossacklabs/acra)             | 10.3+           | [Apache2](https://github.com/cossacklabs/acra/blob/master/LICENSE)  | Database protection suite with field level encryption and intrusion detection. |
| [myldapsync](https://pypi.org/project/myldapsync/)      | YES             | GPL     | Synchronise MariaDB users with users in an LDAP directory. |
| [SecuRich](http://www.securich.com/)                    | YES             | [GPL2](https://github.com/darrencassar/securich/blob/master/COPYING.txt)  | Stored procedures library with user management and role implementation. Unmaintained, but useful with old MariaDB versions. |

**Articles**

- [Monitoring MariaDB Security with Wazuh](https://www.linkedin.com/pulse/monitoring-mariadb-security-wazuh-luis-contreras/)
- [Enforcing strong passwords for MariaDB users](https://vettabase.com/enforcing-strong-passwords-for-mariadb-users/)
- [Enabling Kerberos (MIT and AD) authentication for MariaDB Database Server](https://docs.cloudera.com/cdp-private-cloud-base/latest/installation/topics/cdpdc-enable-kerberos-mariadb.html)
- [MariaDB with Active Directory authentication via PAM module](https://techblog.jeppson.org/2017/12/mariadb-active-directory-authentication-via-pam-module/)

## Toolkits

| Project                                                                              | MariaDB Support                | License           | Language                   | Description   |
|--------------------------------------------------------------------------------------|--------------------------------|-------------------|----------------------------|---------|
| [common_schema](https://github.com/shlomi-noach/common_schema)                       | YES                            | [GPL2](https://github.com/shlomi-noach/common_schema/blob/master/LICENSE)                                                                                                                                                     | Stored Procedures          | A library of stored procedures for DBAs. Includes a parser for its own language, QueryScript, and a debugger. |
| [Percona Toolkit](https://www.percona.com/software/database-tools/percona-toolkit)   | YES                            | [GPL2](https://github.com/percona/percona-toolkit/blob/3.x/COPYING)                                                                                                                                                           | Perl                       | A set of Perl scripts for MariaDB and MySQL administration.
| [SQLAxe](https://github.com/djberube/sqlaxe/) | MySQL | [MIT](https://github.com/djberube/sqlaxe/blob/main/LICENSE) | Python | Tool to manipulate SQL files. Based on SQLGlot, that currently doesn't support any MariaDB specific syntax. |

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
| [mycli](https://www.mycli.net/)                                             | YES                                             | Python                | Open Source        |
| [usql](https://github.com/xo/usql)                                          | [YES](https://github.com/xo/usql?tab=readme-ov-file#supported-database-schemes-and-aliases)                                    | Linux, MacOS, Windows | [MIT](https://github.com/xo/usql/blob/master/LICENSE) |       |

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

Copyright 2024 2025 Vettabase Ltd and contributors.

Awesome MariaDB list is licensed under [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).
