from .base import *

if DEBUG:
    from .dev import * # noqa
else:
    from .prod import * # noqa

