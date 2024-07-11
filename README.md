# awesome-mariadb
A curated list of awesome MariaDB resources, maintained by [Vettabase](https://vettabase.com) and sponsored by the [MariaDB Foundation](https://mariadb.org/).

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) Inspired by the `awesome-*` trend on GitHub.

Topics are organised by audience, to save people from navigating through the noise:

- [Awesome MariaDB for Database Administrators](list-dba.md)
- [Awesome MariaDB for Developers](list-dev.md)
- [Awesome MariaDB for Data Engineers](list-den.md)

## The Problem we Try to Solve

Why are we maintaining a list that is specifically for MariaDB, and not for MySQL and its forks?

It's easy to find software, cloud services or educative resources for MySQL. Finding MariaDB related resources is a bit
more difficult. The reason is simple: many authors of MySQL resources tend to think that, if something works with MySQL,
it will work with MariaDB as well. And it is certainly true that MariaDB and MySQL are very similar. MariaDB was initially
created by forking MySQL 5.1, and some effort to guarantee compatibility was made over the years.

However, MariaDB and MySQL are diverging more and more over time. So, before saying that a MySQL resource works well with
MariaDB, you should ask yourself some questions:

**Does the Resource Use Some MySQL Unique Features?**

In the woest case, a tool won't work at all, but this is not common. It is more common that some features of a tools can't
be used on MariaDB. For example, using certain features of the community.mysql Ansible module will generate queries that
fail on MariaDB.

**Does the Resource take Advantage of MariaDB Unique Features?**

Sometimes a resource works on MySQL, but it does things that could be done better by taking advantage of MariaDB features.
For example, a GUI might not allow to create a `UUID` or `INET6` columns because these types are not supported by MySQL.
An ORM for MySQL might not allow you to produce a `DELETE ... RETURNING` for the same reason. A monitoring system for
MySQL normally won't show MariaDB specific metrics.

**Is the Resource Adequately Tested with MariaDB?**

This might not matter much for a blog post. But software projects should be well tested with MariaDB. It's easy to overlook
this necessaty, because one might think that if the code doesn't return strange errors it works. But when a query fails, the
application might not expose errors. After some time you might find out that some data are missing or inconsistent.

**Is the Resource Really "for MySQL and MariaDB"?**

As you can guess, sometimes resources "for MySQL and MariaDB" are mostly for MySQL, meaning that they are not thoroughly
tested and optimised for MariaDB. All the problems listed above might apply in such cases.

If you spot these problems in an open source application that officially supports MariaDB, please report a bug or contribute
a bugfix.

## Our Solution: Awesome MariaDB

When the MariaDB Foundation reached us proposing to sponsor the Awesome MariaDB list, we saw it as an opportunity to help
tackle the above problem. But how exactly?

**Provide a List of Real MariaDB Resources**

In this list, whenever possible, you will only find resources that properly support MariaDB. It doesn't matter to us if it
also support MySQL or not, and whether the project's priority is MariaDB or not. We simply want to list "stuff that works
well".

Ideally, we aim to test all the listed resources with MariaDB. We temporarily list resources that we didn't test yet, but
in that case we at least checked the documentation and the website for MariaDB support. When unsure, we also take a look
at the source code.

Whenever relevant, we indicate if a project is FLOSS software, proprietary doanloadble software, or a cloud service. When
appropriate, we also indicate the supported platforms or programming language. These aspects are often very important when
you're looking for software that solves a problem.

**Provide a List of Open Source Resources that Have Problems with MariaDB**

If a listed resource has problems with MariaDB, we aim to indicate this. We try to list such resources only if they are
open source or free software. In this case, if you decide to use the resource, we warmly encourage you to contribute the
project, to the purpose of improving MariaDB support by applications.

There are various ways you can contribute improving MariaDB support:

* Report bugs describing them clearly, to help software maintainers to repoduce them.
* Contribute bugfixes.
* Report mistakes in documentation, technical articles, and even printed books.
* Write a guide on how to make an application work smoothly with MariaDB, for example in the form of a blog post.

**Knowledge Sharing**

Suppose you consult Awesome MariaDB, and you learn that a certain software doesn't work well with MariaDB because it
doesn't use a certain SQL syntax. If you're a developer, you'll find out that this syntax exists, and what it is for.
Hopefully, you will later use this information in your daily job, to produce better code.

**Grow a Sense of Community**

All the activity listed in the previous point are normal and spontaneously happen in a community.

Let's grow MariaDB community to see an increase in this kind of activities, and let's show support towards resources
that aim to work well with MariaDB.

[Make it so!](https://memory-alpha.fandom.com/wiki/Make_It_So)

(yes, adding a nerd Star Trek link was one of our primary goals as well)

## Contributing

Contributions welcome!

If you want to suggest a new resource, remember that this is **Awesome MariaDB**, and ask yourself two simple questions:

- Does it work well with MariaDB?
- Is it actually awesome?

If both the answers are yes, you can add links through [pull requests](https://github.com/Vettabase/awesome-mariadb/pulls).
Once a PR is approved, we would appreciate if you take the time to notify the maintainer of the resource.

If you find inaccurate information, obsolete information, or resources that are not maintained anymore, please report the
problem by creating an [issue](https://github.com/Vettabase/awesome-mariadb/issues), or fix it by yourself by opening
a [pull request](https://github.com/Vettabase/awesome-mariadb/pulls).

If you contribute to Awesome MariaDB, we encourage you to add your name to the `CONTRIBUTORS.md` file.

## How to Thank Us

If you're the maintainer of a resource we linked, we encourage you to show in your resource an
[Awesome mentioned badge](https://github.com/sindresorhus/awesome/blob/main/awesome.md#awesome-mentioned-badge).

Simply paste this code in your `README.md` file:

```
[![Mentioned in Awesome MariaDB](https://awesome.re/mentioned-badge.svg)](https://github.com/Vettabase/awesome-mariadb)
```

The result will look like the following:

[![Mentioned in Awesome MariaDB](https://awesome.re/mentioned-badge.svg)](https://github.com/Vettabase/awesome-mariadb)

---

Copyright 2024 Vettabase Ltd and contributors.

Awesome MariaDB list is licensed under [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).
