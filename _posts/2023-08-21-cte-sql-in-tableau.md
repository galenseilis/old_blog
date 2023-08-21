---
title: Opinion - Tableau Should Fully Support Common SQL Dialects
date: 2023-08-21 02:50:15
categories: [tableau,custom-sql,common-table-expressions]
tags: [tableau,custom-sql,common-table-expressions,sql,structured-query-language,software-features]
math: true
mermaid: true
---

I recently noticed that Tableau does not support common table expressions in "Custom SQL" data sources when I was trying to setup a new data source for a dashboard. It is one of those weird gotchas that strikes me as more of a bug than a feature of Tableau. For what I was doing, joining on a transformation of an attribute, it was easy enough to use a subquery within the join clause.

Strangely, CTEs *are* supported for "Initial SQL" inputs of a data source. ¯\\\_(ツ)_/¯ 

Here are some related links:
- [CTE Table Is Not Working In Tableau ODBC But Working Fine In Hadoop Environment](https://community.tableau.com/s/question/0D58b00009pnZWACA2/cte-table-is-not-working-in-tableau-odbc-but-working-fine-in-hadoop-environment)
- [Using Common Table Expressions](https://kb.tableau.com/articles/howto/using-common-table-expressions)

In my opinion, common table expression and any other features found in the top few SQL dialects should be supported. Otherwise the behaviour is somewhat [astonishing](https://en.wikipedia.org/wiki/Principle_of_least_astonishment).
