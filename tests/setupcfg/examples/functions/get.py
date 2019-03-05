#!/usr/bin/env python
import os
import setupcfg

os.chdir(os.path.dirname(__file__))

name = setupcfg.get("metadata", "name")
print("name: %s" % name)

default = setupcfg.get("metadata", "not-existing", "default value")
print("default: %s" % default)
