---
title: ChatGPTs Attempt at Producing a Network Model From SQL Queries
date: 2023-10-20 00:50:15
categories: [chatgpt,programming]
tags: [chatgpt,programming,python,sql,sqlparse,networkx,sqlglot]
math: true
mermaid: true
---

A problem I am interested in is extracting a network model on a collection of tables using a Python package (e.g. sqlparse or sqlglot) to produce a networkx multigraph.

Suppose we begin with an SQL script containing three queries:

```sql
-- Query 1: Simple select from one table
SELECT first_name, last_name FROM employees;

-- Query 2: Join two tables
SELECT o.order_id, c.customer_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

-- Query 3: Join multiple tables and use aliases
SELECT o.order_id, c.customer_name, p.product_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items i ON o.order_id = i.order_id
JOIN products p ON i.product_id = p.product_id;
```

Here is the implementation that ChatGPT provided (after asking a half-dozen times to correct an issue where the graph ended up empty).

```python
import sqlparse
import networkx as nx

# Create a NetworkX MultiGraph
G = nx.MultiGraph()

# Define a function to extract table and column information from SQL queries
def extract_tables_columns(sql_query):
    parsed = sqlparse.parse(sql_query)
    tables = set()
    join_conditions = []

    for stmt in parsed:
        from_seen = False
        last_table = None

        for token in stmt.tokens:
            if token.value.upper() == 'FROM':
                from_seen = True
            elif from_seen and isinstance(token, sqlparse.sql.Identifier):
                table_name = token.get_real_name()
                tables.add(table_name)
                if last_table:
                    join_conditions.append((last_table, table_name))
                last_table = table_name

    for table in tables:
        G.add_node(table)

    for left, right in join_conditions:
        G.add_edge(left, right)

# Load your SQL queries from .sql files
with open('queries.sql', 'r') as file:
    sql_queries = file.read().split(';')  # Split queries by semicolon

# Extract tables and columns from the SQL queries
for sql_query in sql_queries:
    extract_tables_columns(sql_query)

# Print the nodes and edges to verify
print("Nodes:")
print(G.nodes())
print("Edges:")
print(G.edges())

# Now, G should correctly represent the relationships between tables and columns in your SQL queries.

# You can perform various network analysis tasks on G using NetworkX functions.

import matplotlib.pyplot as plt
# Create a plot
plt.figure(figsize=(10, 10))

# Draw nodes with labels
pos = nx.spring_layout(G, seed=42)  # You can use other layouts as well
node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_color='black')

# Draw edges
nx.draw(G, pos, with_labels=False, node_size=300, node_color='skyblue', alpha=0.7, linewidths=0.5, font_size=10)

# Draw edge labels manually for multi-edges
edge_labels = {}
for u, v, keys, data in G.edges(data=True, keys=True):
    label = data.get('label', '')
    if label:
        if (u, v) not in edge_labels:
            edge_labels[(u, v)] = label
        else:
            edge_labels[(u, v)] += f", {label}"

# Draw edge labels manually
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_isze=10)

# Save the plot
plt.axis('off')
plt.savefig('chatgpt_create_multigraph_from_sql.png', dpi=300, transparent=True)
plt.close()
```

The printed output is:

```python
Nodes:
['employees', 'orders', 'customers', 'order_items', 'products']
Edges:
[('orders', 'customers'), ('orders', 'customers'), ('customers', 'order_items'), ('order_items', 'products')]
```

While I can see that ChatGPT's output at a glance is pretty good, this code **does not work** in the more general case of extracting information about joins. I found that it completely flopped on accuracy in recovering the right information from nested SQL queries. For the following expanded set of cases you'll find the ChatGPT output fails on such cases:

```sql
-- Query 1: Simple select from one table
SELECT first_name, last_name FROM employees;

-- Query 2: Join two tables
SELECT o.order_id, c.customer_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

-- Query 3: Join multiple tables and use aliases
SELECT o.order_id, c.customer_name, p.product_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items i ON o.order_id = i.order_id
JOIN products p ON i.product_id = p.product_id;

-- Query 4: Nested query with depth 1 (new set of tables)
SELECT a.first_name, a.last_name, b.order_id
FROM (SELECT first_name, last_name, employee_id FROM foo) a
JOIN (SELECT order_id, customer_id FROM bar) b ON a.employee_id = b.customer_id;

-- Query 5: Nested query with depth 2 (new set of tables)
SELECT a.first_name, a.last_name, b.order_id
FROM (SELECT first_name, last_name, employee_id FROM (SELECT first_name, last_name, employee_id FROM foo) a) a
JOIN (SELECT order_id, customer_id FROM (SELECT order_id, customer_id FROM bar) b) b ON a.employee_id = b.customer_id;

-- Query 6: Common Table Expression (CTE) with subsequent query (new set of tables)
WITH product_prices AS (
    SELECT b.product_name, b.product_id
    FROM baz b
)
SELECT b.order_id, b.product_name, p.price
FROM bar b
JOIN baz p ON b.order_id = p.product_id;

-- Query 7: Include 'foo' in the query (placeholder)
SELECT a.first_name, a.last_name
FROM (SELECT first_name, last_name FROM foo) a;
```


Instead, `sqlglot` provides an easy first approximation:

```python
import sqlglot

with open('query.sql', 'r') as f:
  query_str = f.read()
  
joins = [j for j in sqlglot.parse(query_str).find_all(sqlglot.expressions.Join)]
```

The `sqlglot` implementation still leaves some basic string processing to be done, but it provides most of what I need.
