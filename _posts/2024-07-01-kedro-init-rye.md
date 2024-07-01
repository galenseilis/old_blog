---
title: Combining Kedro with Rye
date: 2024-07-01 01:51:15
categories: [python,package-management]
tags: [python,package-management,rye,kedro,kedro-init]
math: true
mermaid: true
---


## Introduction
I recently [asked on the Kedro Slack channel](https://kedro-org.slack.com/archives/C03RKP2LW64/p1719762547621889) about what experience people have had with combining Kedro with package management tools in Python such as PDM, Poetry, Hatch or Rye. [`juanlu` gave a couple of options](https://kedro-org.slack.com/archives/C03RKP2LW64/p1719787364960379?thread_ts=1719762547.621889&cid=C03RKP2LW64). You can either initialize a Kedro project first and then add the package manager, or add the package manager first and use [`kedro-init`](https://github.com/astrojuanlu/kedro-init) to fill in a Kedro project. Which one is more appropriate will depend on what already exists in your project. Kedro should be compatible with PEP-compliant packages (see discussion [here](https://github.com/kedro-org/kedro/issues/3974)) and also Poetry. I'm not sure about Rye.

`kedro-init` is in its infancy (e.g. still needing documentation), but I figured I would try it out with [Rye](https://rye.astral.sh/) since that is what I am currently using on my personal machine.


## Example

First, lets initialize a Rye-managed proeject called `try-kedro-init`.

```bash
$ rye init try-kedro-init
success: Initialized project in /home/galen/projects/try-kedro-init
  Run `rye sync` to get started
```

Now change directory into the project path.

```bash
$ cd try-kedro-init/
```

Add the `kedro-init` package to `try-kedro-init`'s packages, inlcuding Kedro itself.

```bash
$ rye add kedro-init
Initializing new virtualenv in /home/galen/projects/try-kedro-init/.venv
Python version: cpython@3.12.3
Added kedro-init>=0.1.0 as regular dependency
Reusing already existing virtualenv
Generating production lockfile: /home/galen/projects/try-kedro-init/requirements.lock
Generating dev lockfile: /home/galen/projects/try-kedro-init/requirements-dev.lock
Installing dependencies
Resolved 55 packages in 12ms
   Built try-kedro-init @ file:///home/galen/projects/try-kedro-init
   Built antlr4-python3-runtime==4.9.3
Downloaded 35 packages in 3.23s
Installed 55 packages in 16ms
 + antlr4-python3-runtime==4.9.3
 + arrow==1.3.0
 + attrs==23.2.0
 + binaryornot==0.4.4
 + build==1.2.1
 + cachetools==5.3.3
 + certifi==2024.6.2
 + chardet==5.2.0
 + charset-normalizer==3.3.2
 + click==8.1.7
 + cookiecutter==2.6.0
 + dynaconf==3.2.5
 + fastjsonschema==2.20.0
 + fsspec==2024.6.1
 + gitdb==4.0.11
 + gitpython==3.1.43
 + idna==3.7
 + importlib-metadata==7.2.1
 + importlib-resources==6.4.0
 + installer==0.7.0
 + jinja2==3.1.4
 + kedro==0.19.6
 + kedro-init==0.1.0
 + markdown-it-py==3.0.0
 + markupsafe==2.1.5
 + mdurl==0.1.2
 + more-itertools==10.3.0
 + omegaconf==2.3.0
 + packaging==24.1
 + parse==1.20.2
 + platformdirs==4.2.2
 + pluggy==1.5.0
 + pre-commit-hooks==4.6.0
 + pygetimportables==0.2.1
 + pygments==2.18.0
 + pyproject-hooks==1.1.0
 + python-dateutil==2.9.0.post0
 + python-slugify==8.0.4
 + pytoolconfig==1.3.1
 + pyyaml==6.0.1
 + requests==2.32.3
 + rich==13.7.1
 + rope==1.13.0
 + ruamel-yaml==0.18.6
 + ruamel-yaml-clib==0.2.8
 + six==1.16.0
 + smmap==5.0.1
 + text-unidecode==1.3
 + toml==0.10.2
 + tomlkit==0.12.5
 + try-kedro-init==0.1.0 (from file:///home/galen/projects/try-kedro-init)
 + types-python-dateutil==2.9.0.20240316
 + urllib3==2.2.2
 + validate-pyproject==0.18
 + zipp==3.19.2
Done!
```

Now run `kedro-init` from within Rye's virtual environment.

```bash
$ rye run kedro-init .
[08:33:20] Looking for existing package directories                                                                                                                                                                                cli.py:25
[08:33:25] Initialising config directories                                                                                                                                                                                         cli.py:25
           Creating modules                                                                                                                                                                                                        cli.py:25
           🔶 Kedro project successfully initialised!
```

Just for the sake of example, create an example pipeline.

```bash
$ rye run kedro pipeline create example_pipeline
Using pipeline template at: '/home/galen/projects/try-kedro-init/.venv/lib/python3.12/site-packages/kedro/templates/pipeline'
Creating the pipeline 'example_pipeline': OK
  Location: '/home/galen/projects/try-kedro-init/src/try_kedro_init/pipelines/example_pipeline'
Creating '/home/galen/projects/try-kedro-init/tests/pipelines/example_pipeline/test_pipeline.py': OK
Creating '/home/galen/projects/try-kedro-init/tests/pipelines/example_pipeline/__init__.py': OK
Creating '/home/galen/projects/try-kedro-init/conf/base/parameters_example_pipeline.yml': OK

Pipeline 'example_pipeline' was successfully created.
```

Now take a look at the path tree to see what has been created.

```bash
$ tree .
.
├── conf
│   ├── base
│   │   └── parameters_example_pipeline.yml
│   └── local
├── pyproject.toml
├── README.md
├── requirements-dev.lock
├── requirements.lock
├── src
│   └── try_kedro_init
│       ├── __init__.py
│       ├── pipeline_registry.py
│       ├── pipelines
│       │   └── example_pipeline
│       │       ├── __init__.py
│       │       ├── nodes.py
│       │       └── pipeline.py
│       ├── __pycache__
│       │   ├── __init__.cpython-312.pyc
│       │   └── settings.cpython-312.pyc
│       └── settings.py
└── tests
    └── pipelines
        └── example_pipeline
            ├── __init__.py
            └── test_pipeline.py

11 directories, 15 files
```

The `catalog.yml` and `parameters.yml` files were not made by default, but they are just plaintext files that can be readily added. There is `parameters_example_pipeline.yml` for the pipeline we just created.

```bash
$ touch conf/base/catalog.yml
```

There also is not a `data` path by default, which should exist at the root of the project. We can also add that.

```bash
 $ mkdir data
```

Let us create an example CSV dataset at `data/example_data.csv` with the following contents:

```text
ID,Name,Age,Email
1,John Doe,28,john.doe@example.com
2,Jane Smith,34,jane.smith@example.com
3,Bob Johnson,45,bob.johnson@example.com
4,Alice Williams,23,alice.williams@example.com
5,Michael Brown,37,michael.brown@example.com
```

Then add an entry to `conf/base/catalog.yml`:

```yaml
example_dataset:
  type: pandas.CSVDataset
  filepath: ./data/example_data.csv
  load_args:
    sep: ","
```

Now update `src/try_kedro_init/pipelines/example_pipeline/pipeline.py` from this

```python
"""
This is a boilerplate pipeline 'example_pipeline'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([])
```

to this:
```python
"""
This is a boilerplate pipeline 'example_pipeline'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, pipeline, node


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=print,
            inputs=['example_dataset'],
            outputs=None
            )
        ])
```

Now install `kedro-datasets` and `pandas`:

```python
$ rye add kedro-datasets pandas
Added kedro-datasets>=3.0.1 as regular dependency
Added pandas>=2.2.2 as regular dependency
Reusing already existing virtualenv
Generating production lockfile: /home/galen/projects/try-kedro-init/requirements.lock
Generating dev lockfile: /home/galen/projects/try-kedro-init/requirements-dev.lock
Installing dependencies
Resolved 61 packages in 14ms
   Built try-kedro-init @ file:///home/galen/projects/try-kedro-init
Downloaded 1 package in 217ms
Uninstalled 1 package in 0.29ms
Installed 5 packages in 45ms
 + numpy==2.0.0
 + pandas==2.2.2
 + pytz==2024.1
 - try-kedro-init==0.1.0 (from file:///home/galen/projects/try-kedro-init)
 + try-kedro-init==0.1.0 (from file:///home/galen/projects/try-kedro-init)
 + tzdata==2024.1
Done!
```

Finally, run the Kedro pipeline:

```bash
$ rye run kedro run
[07/01/24 09:18:48] INFO     Kedro project try-kedro-init                                                                                                                                                                     session.py:324
[07/01/24 09:18:49] INFO     Using synchronous mode for loading and saving data. Use the --async flag for potential performance gains.                                                                               sequential_runner.py:64
                             https://docs.kedro.org/en/stable/nodes_and_pipelines/run_a_pipeline.html#load-and-save-asynchronously                                                                                                          
                    INFO     Loading data from example_dataset (CSVDataset)...                                                                                                                                           data_catalog.py:508
                    INFO     Running node: print([example_dataset]) -> None                                                                                                                                                      node.py:361
   ID            Name  Age                       Email
0   1        John Doe   28        john.doe@example.com
1   2      Jane Smith   34      jane.smith@example.com
2   3     Bob Johnson   45     bob.johnson@example.com
3   4  Alice Williams   23  alice.williams@example.com
4   5   Michael Brown   37   michael.brown@example.com
                    INFO     Completed 1 out of 1 tasks                                                                                                                                                              sequential_runner.py:90
                    INFO     Pipeline execution completed successfully.                                                                                                                                                        runner.py:119
```

My provisional conclusion is that Kedro and Rye are compatible.

## Versions

Rye configuration:

```bash
$ rye --version
rye 0.35.0
commit: 0.35.0 (a1dbc56d4 2024-06-24)
platform: linux (x86_64)
self-python: cpython@3.12.3
symlink support: true
uv enabled: true

```

My operating system:

```bash
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.4 LTS
Release:        22.04
Codename:       jammy
```
