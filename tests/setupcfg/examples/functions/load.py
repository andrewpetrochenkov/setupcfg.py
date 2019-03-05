#!/usr/bin/env python
import os
import setupcfg

os.chdir(os.path.dirname(__file__))

data = setupcfg.load()
print(data)
