# (C) Albert Mietus, 2023. Part of Castle/CCastle project

""".. Note:: The baseProtocol (instance) is used in aigr.protocols as top of all protocols. So we can import & use it.
      No such 'top-namespaces' exist, so we have to initiate it here.
"""

from castle.aigr.protocols import ID
#from castle.aigr.protocols import baseProtocol
from castle.aigr import NamedSpace

from castle.aigr.tools.scaffolding import ScaffolderNameSpace

#Protocol = baseProtocol

#base = NamedSpace(ID('base'))
#ScaffolderNameSpace(base).register(Protocol)

