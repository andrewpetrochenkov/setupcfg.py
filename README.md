<!-- https://pypi.org/project/readme-generator/ -->

[![](https://img.shields.io/pypi/pyversions/setupcfg.svg?longCache=True)](https://pypi.org/project/setupcfg/)
[![](https://img.shields.io/pypi/v/setupcfg.svg?maxAge=3600)](https://pypi.org/project/setupcfg/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/setupcfg.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/setupcfg.py/)

#### Install
```bash
$ [sudo] pip install setupcfg
```

#### Classes
`setupcfg.cfg.Setupcfg` - `setup.cfg` generator class. dict/attr access

`Setupcfg` methods|`__doc__`
-|-
`load(path='setup.cfg')`|load from `setup.cfg` file
`save(path='setup.cfg')`|save to `setup.cfg` file
`string()`|return string representation

#### Functions
function|`__doc__`
-|-
`setupcfg.get(section, option, default=None)`|return the value for option if option is in the `setup.cfg`, else default
`setupcfg.load(path='setup.cfg')`|return dictionary with `setup.cfg` sections dictionaries
`setupcfg.values.string(value)`|Convert a value to a `setup.cfg` value string
`setupcfg.values.value(string)`|Convert a string to a python value

#### Cli
usage|`__doc__`
-|-
`python -m setupcfg.metadata.description [description]`|read/write `setup.cfg` `[metadata]` `description`
`python -m setupcfg.metadata.keywords [keywords]`|read/write `setup.cfg` `[metadata]` `keywords`
`python -m setupcfg.metadata.name [name]`|read/write `setup.cfg` `[metadata]` `name`
`python -m setupcfg.metadata.url [url]`|read/write `setup.cfg` `[metadata]` `url`
`python -m setupcfg.metadata.version [version]`|read/write `setup.cfg` `[metadata]` `version`
`python -m setupcfg.options.install_requires [requires ...]`|read/write `setup.cfg` `[options]` `install_requires`
`python -m setupcfg.options.packages [package ...]`|read/write `setup.cfg` `[options]` `packages`
`python -m setupcfg.options.py_modules [module ...]`|read/write `setup.cfg` `[options]` `py_modules`
`python -m setupcfg.options.scripts [script ...]`|read/write `setup.cfg` `[options]` `scripts`

#### Links
+   [metadata, options - setuptools documentation](http://setuptools.readthedocs.io/en/latest/setuptools.html#metadata)
+   [Specifying values](http://setuptools.readthedocs.io/en/latest/setuptools.html#specifying-values)

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>