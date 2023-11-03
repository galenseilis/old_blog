---
title: How to list all available databases paired to their tables and attributes in Microsoft SQL Server
date: 2023-10-24 00:51:15
categories: [sql,microsoft-sql,sql-server]
tags: [sql,microsoft-sql,sql-server,tsql,sql-query,databases,microsoft-sql-server,tables,attributes]
math: true
mermaid: true
---

While this isn't a solution I intend on going with for my use cases, I thought I would note that a bird's-eye-view of all databases paired to their respective tables in turn paired to their respective attributes can be obtained with the following relatively short script:


```sql
EXEC sp_MSforeachdb '
    USE [?];
    SELECT
        DB_NAME() AS DatabaseName,
        t.name AS TableName,
        c.name AS AttributeName
    FROM sys.tables AS t
    JOIN sys.columns AS c ON t.object_id = c.object_id;
';
```

Note that if you have a truly huge number of databases, tables, and respective attributes then this query will not be of much help.
