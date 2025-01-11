# (C) Albert Mietus, 2023. Part of Castle/CCastle project

""".. Note:: The baseProtocol (instance) is used in aigr.protocols as top of all protocols. So we can import & use it.
      No such 'top-namespaces' exist, so we have to initiate it here.
"""

from castle.aigr.protocols import baseProtocol, ID
from castle.aigr import NamedSpace

Protocol = baseProtocol

base = NamedSpace(ID('base'))
base.register(Protocol)

