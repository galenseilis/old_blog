---
title: Plot Basic Pie Chart Of Taxa At A Given Taxonomic Rank Using Pandas And Matplotlib
date: 2022-03-16 12:30:00 -0800
categories: [inaturalist]
tags: [volunteer,inaturalist,data]
math: true
mermaid: true
---

> This post was migrated from my iNaturalist journal on 2023-02-26.
{: .prompt-info}

Suppose you have an exported [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) of iNaturalist observations, `observations-<ID>.csv`.

To follow this tutorial you will have to have Python installed, and the [Matplotlib](https://matplotlib.org/) and [Pandas](https://pandas.pydata.org/) packages installed. Pandas is not necessary, but it makes things convenient enough that I recommend using it here. In other contexts you may wish to plot pie charts without Pandas.

Assuming you have [PIP](https://en.wikipedia.org/wiki/Pip_(package_manager)) installed, you can install Pandas and Matplotlib as follows:

```bash
pip install matplotlib pandas
```

Although, since Pandas actually uses Matplotlib as a dependency for plotting, it might suffice to simply use:

```bash
pip install pandas
```

Next, you must create a script file with the `*.py` [extension](https://en.wikipedia.org/wiki/Filename_extension). We can do fancier things with paths, but let us create the file `pie_taxa.py` using BASH.

```bash
touch pie_taxa.py
```

Now let us write some lines of code in `pie_taxa.py`. First we need to import the required packages.

```python
import matplotlib.pyplot as plt
import pandas as pd
```

Next we can load our data using the `pd.read_csv` function, which assumes a CSV format by default. It has many other parameters, including changing the delimiter (see the [docs](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)), but we are fine with the defaults here.

```python
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("observations-<ID>.csv")
```

Now, as if by magic (but actually the hard work of software developers), we can create the plot in a single line of code. Let us do it for the kingdom level, which will require us knowing that this is represented by the `taxon_kingdom_name` column in our data file.

```python
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("observations-<ID>.csv")
df['taxon_kingdom_name'].value_counts().plot.pie()
```

There are a few things going on in the previous line of code. First is that `df['taxon_kingdom_name']` has selected only the `taxon_kingdom_name` column. This is next passed to the `value_counts()` which counts the occurrences of each kingdom in that column and returns a Pandas series object with this information, and then we finally call the `plot.pie` method on this series object which... well... makes the pie chart.

If you run the code at this point you may be surprised to not actually see a plot appear anywhere. If you ran the code from the command line you might have seen something like `<AxesSubplot:ylabel='taxon_kingdom_name'>`. This is because creating the instructions of what goes on the drawing canvas is different from graphically rendering it. In order to do that, we can call `plt.show()`.

```python
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("observations-<ID>.csv")
df['taxon_kingdom_name'].value_counts().plot.pie()
plt.show()
```

Running the above, you should see a window pop up. It will look similar to this:

![](/assets/images/taxa-pie-chart.png)

 It has various settings for resizing, reshaping, zooming, and saving your figure. 

What if you didn't want to look at Kingoms, but rather orders, or families, etc? You would simply use a different column instead of `taxon_kingdom_name`. Here is a table of these similar columns:

| Taxonomic Rank         |
|------------------------|
| `taxon_kingdom_name`     |
| `taxon_phylum_name`      |
| `taxon_subphylum_name`   |
| `taxon_superclass_name`  |
| `taxon_class_name`       |
| `taxon_subclass_name`    |
| `taxon_superorder_name`  |
| `taxon_order_name`       |
| `taxon_suborder_name`    |
| `taxon_superfamily_name` |
| `taxon_family_name`      |
| `taxon_subfamily_name`   |
| `taxon_supertribe_name`  |
| `taxon_tribe_name`       |
| `taxon_subtribe_name`    |
| `taxon_genus_name`       |
| `taxon_genushybrid_name` |
| `taxon_species_name`     |
| `taxon_hybrid_name`      |
| `taxon_subspecies_name`  |
| `taxon_variety_name`     |
| `taxon_form_name`        |

Happy plotting.
