---
title: Unzip Your iNaturalist Observations On A Ubuntu System
date: 2022-03-16 12:00:00 -0800
categories: [inaturalist]
tags: [volunteer,inaturalist,data]
math: true
mermaid: true
---

> This post was migrated from my iNaturalist journal on 2023-02-26.
{: .prompt-info}

Suppose 
- you have just downloaded an export of iNaturalist data,
- the data file is a [zipped](https://en.wikipedia.org/wiki/ZIP_(file_format)) [comma-separated value](https://en.wikipedia.org/wiki/Comma-separated_values)(CSV) text file,
- and you are running a [Ubuntu system](https://en.wikipedia.org/wiki/Ubuntu).

Begin by opening up a [BASH](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) environment.

Go to the [path](https://en.wikipedia.org/wiki/Path_(computing)) where the file was downloaded to:

```bash
cd /path/to/folder
```

Then run the unzip command:

```bash
unzip observations-<ID>.csv.zip
```

You should find that you now have the uncompressed CSV file. You can check with:

```python
ls observations-<ID>.csv
```
