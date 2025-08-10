# (C) Albert Mietus, 2023,2024 Part of Castle/CCastle project

from castle.aigr import NamedSpace, Source_NS, ID
from castle.aigr_extra.scaffolding import ScaffolderNameSpace

# Note: this file only creates the namespaces, not the components (etc in those file)
##
## FILES
##

# We mimic that both protocols ('StartSieve' & 'SimpleSieve') are defined in 1 file: :file:`protocols.Moat`
protocols = Source_NS(ID('protocols'), source='protocols.Moat')

# Similar, all (comp) interfaces are located in the file: :file:`interfaces.Moat`
interfaces = Source_NS(ID('interfaces'), source='interfaces.Moat')

# Each (3) components are coded in its on Castle-file.
comps = { name : Source_NS(ID(name), source=name+'.Castle') for name in ('generator', 'sieve', 'finder')}

##
## IMPORTS
##

# `protocols.Moat` has no imports

# `interfaces.Moat` needs to import <protocols>
ScaffolderNameSpace(interfaces).register(protocols)

# Each comp need to import it own interface, and all protocols
for comp in comps.values():
    ScaffolderNameSpace(comp).register(interfaces)
    ScaffolderNameSpace(comp).register(protocols)


# Main is the main namespace, which imports both <interfaces> and <protocols>
main = Source_NS(ID('main'), source='main.Moat')
wrapped_main = ScaffolderNameSpace(main)
wrapped_main.register(interfaces)
wrapped_main.register(protocols)


##
## Q: Should main import the components?
##
## It's and option: _OPT_MAIN_IMPORTS_COMPS
def _main_imports_comps():
    for comp in (ns for name,ns in comps.items() if name != 'main'): # pragma: no mutate
        wrapped_main.register(comp)
_OPT_MAIN_IMPORTS_COMPS=True              # pragma: no mutate
if _OPT_MAIN_IMPORTS_COMPS: _main_imports_comps()
