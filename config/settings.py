# Import settings dựa trên môi trường
from .base import *

try:
    from .local import *
except ImportError:
    pass

