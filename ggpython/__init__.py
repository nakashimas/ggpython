# __init__.py

try:
    from . import tracker
    from .core import *
except Exception as _:
    import tracker
    from core import *
