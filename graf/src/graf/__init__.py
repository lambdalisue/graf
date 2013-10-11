#!/usr/bin/env python
# coding=utf-8
import pkg_resources
pkg_resources.declare_namespace(__name__)
version = pkg_resources.require('graf')[0].version


def use(environment=None):
    """
    Use graf commands in the shell

    Args:
        environment: expand all graf commands into this environment,
            if this is not specified, globals() of caller will be used
    """
    from graf.plugins import registry
    if not environment:
        import inspect
        frame = inspect.stack()[1][0]
        environment = frame.f_globals
    environment.update(registry.raw)


def call(filename, environment=None):
    """
    Call graf script file in this shell

    Args:
        filename: a filename of graf script file
    """
    from graf.plugins import registry

    if not environment:
        import inspect
        frame = inspect.stack()[1][0]
        environment = frame.f_globals

    # create global variables
    local = environment.copy()
    #local.update(locals())
    local.update(registry.raw)

    # call script file
    local['__file__'] = filename
    execfile(filename, local)
