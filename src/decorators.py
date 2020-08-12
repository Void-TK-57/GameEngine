# import base libs
from functools import wraps

def syntax_compatibility(cls):
    """Decorator to set functions for the moderngl compatibility"""
    cls.render = cls.loop
    return cls
