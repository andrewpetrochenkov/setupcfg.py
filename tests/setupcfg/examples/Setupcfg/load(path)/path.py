#!/usr/bin/env python
import os
import setupcfg


path = os.path.join(os.path.dirname(__file__),"setup.cfg")
cfg = setupcfg.Setupcfg().load(path)

print(cfg)
