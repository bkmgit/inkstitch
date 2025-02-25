# Authors: see git history
#
# Copyright (c) 2010 Authors
# Licensed under the GNU GPL version 3.0 or later.  See the file LICENSE for details.

from . import cache as cache_module  # Slight hack to allow cache to be imported for monkeypatching
from .cache import cache
from .dotdict import DotDict
from .geometry import *
from .inkscape import *
from .io import *
from .paths import *
from .string import *
