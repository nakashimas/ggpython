# __init__.py

try:
    from . import tracker
    from . import utils
    from .core import *
except Exception as _:
    import tracker
    import utils
    from core import *
