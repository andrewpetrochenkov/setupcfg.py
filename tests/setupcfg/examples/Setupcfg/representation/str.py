#!/usr/bin/env python
import setupcfg

cfg = setupcfg.Setupcfg(
    metadata={"name": "pkgname", "version": "0.0.1"},
    options={"packages": ["pkgname"]}
)
print(str(cfg))
