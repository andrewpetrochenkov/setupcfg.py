#!/usr/bin/env python
import pkgutil
import os
import public
import pydoc
import setupcfg.metadata
import setupcfg.options
import setupcfg.values
from setupcfg.cfg import Setupcfg

public.add(Setupcfg)


@public.add
def get(section, option, default=None):
    """return the value for option if option is in the `setup.cfg`, else default"""
    cfg = Setupcfg().load("setup.cfg")
    return cfg.get(section, {}).get(option, default)


@public.add
def load(path="setup.cfg"):
    """return dictionary with `setup.cfg` sections dictionaries"""
    return Setupcfg().load(path)


@public.add
def getmodules():
    """return a list of module objects"""
    if not os.path.exists("setup.cfg"):
        raise OSError("setup.cfg NOT EXISTS")
    options = load().get("options", {})
    modules = list(map(pydoc.locate, options.get("py_modules", [])))
    packages = options.get("packages", [])
    for pkg_name in packages:
        module = pydoc.locate(pkg_name)
        modules.append(module)
        for module, modname, _ in pkgutil.iter_modules([os.path.dirname(module.__file__)]):
            name = "%s.%s" % (pkg_name, modname)
            if name not in packages:
                modules.append(pydoc.locate(name))
    return list(sorted(modules, key=lambda m: m.__name__))
