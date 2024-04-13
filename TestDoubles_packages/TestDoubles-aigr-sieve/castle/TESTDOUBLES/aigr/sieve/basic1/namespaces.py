# (C) Albert Mietus, 2023,2024 Part of Castle/CCastle project

from castle.aigr import NameSpace, Source_NS, ID

# Note: this file only creates the namespaces, not the components (etc in those file)
##
## FILES
##

# We mimic that both protocols ('StartSieve' & 'SimpleSieve') are defined in 1 file: :file:`protocols.Moat`
protocols = Source_NS(ID('protocols'), source='protocols.Moat')

# Similar, all (comp) interfaces are located in the file: :file:`interfaces.Moat`
interfaces = Source_NS(ID('interfaces'), source='interfaces.Moat')

# Each (3) components are coded in its on Castle-file.
comps = { name : Source_NS(ID(name), source=name+'.Moat') for name in ('generator', 'sieve', 'finder')}

##
## IMPORTS
##

# `protocols.Moat` has no imports

# `interfaces.Moat` needs to import <protocols>
interfaces.register(protocols)

# Each comp need to import it own interface, and all protocols
for comp in comps.values():
    comp.register(interfaces)
    comp.register(protocols)


# Main is the main namespace, which imports both <interfaces> and <protocols>
main = Source_NS(ID('main'), source='main.Moat')
main.register(interfaces)
main.register(protocols)


##
## Q: Should main import the components?
##
## It's and option: _OPT_MAIN_IMPORTS_COMPS
def _main_imports_comps():
    for comp in (ns for name,ns in comps.items() if name != 'main'):
        main.register(comp)
_OPT_MAIN_IMPORTS_COMPS=True
if _OPT_MAIN_IMPORTS_COMPS: _main_imports_comps()
