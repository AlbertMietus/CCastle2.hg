# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.TESTDOUBLES.aigr.base``.
# This package is the foundation TestDouble: it imports AIGR base types so
# downstream test-double packages can rely on a single known origin.
#
# NOTE: all concrete fixture building (base namespace, baseProtocol) is
# commented-out in the source; only the imports are live.  The three names
# below are therefore accessible attributes of this module.

import typing as PTH

from castle.aigr.protocols import ID as ID
from castle.aigr import NamedSpace as NamedSpace
from castle.aigr.tools.scaffolding import ScaffolderNameSpace as ScaffolderNameSpace
