# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project


__all__ = ['CC_ProtocolKind', 'CC_B_Protocol', 'CC_EventProtocol']

from enum import Enum

from .CCbase import *
from .Event import CC_Event

class CC_ProtocolKind(Enum):
    """There are several kinds (types) of protocols.

       This can be modeled by subclassing (in langueas that support it), or
       by using a low-int (aka a enum) and save that in the struct -- for in C

       For now, we use both; to model it ...
    """
    Unknown = CC_ProtocolKindIs_Unknown = 0
    Event   = CC_ProtocolKindIs_Event   = 1
    Data    = CC_ProtocolKindIs_Data    = 2
    Stream  = CC_ProtocolKindIs_Stream  = 3


CC_B_Protocol: TypeAlias = 'CC_B_Protocol'  # forward reference                                      # pragma: no mutate


@dataclass
class CC_B_Protocol:
    """ .. note:: Use one of the subclasses -- Only Event is defined yet
        .. todo:: Design: What is the `kind` self and the inherited ones are not the same?
                  overrideing CC_ProtocolKindIs_Unknown is always allowed
    """
    _BASE: ClassVar=None                                                                             # pragma: no mutate

    name: fstring
    kind: CC_ProtocolKind
    based_on: Optional[CC_B_Protocol]=dc_field(default_factory= lambda :CC_B_Protocol._BASE)


baseProtocol = CC_B_Protocol("Protocol", kind=CC_ProtocolKind.Unknown, based_on=None)                # pragma: no mutate
CC_B_Protocol._BASE=baseProtocol

@dataclass                                                                                           # pragma: no mutate
class CC_B_DataProtocol(CC_B_Protocol): pass ### XXX ToDo (not exported)
@dataclass                                                                                           # pragma: no mutate
class CC_B_DataProtocol(CC_B_Protocol): pass ### XXX ToDo (not exported)



@dataclass                                                                                           # pragma: no mutate
class CC_EventProtocol(CC_B_Protocol):
    """An event-based protocol is basically a set of events.

    This recorded as an dyn-array of the new event; there is no need to copy the inherited ones
    """
    _: KW_ONLY
    kind: CC_ProtocolKind = CC_ProtocolKind.Event
    events: Sequence[CC_Event]

    def event_dict(self, inherired=False, mine=True):
        the_events = {}
        if inherired:
            the_events |= self.based_on.event_dict(inherired=True, mine=True) if isinstance(self.based_on, CC_EventProtocol) else {}
        if mine:
            the_events |= {e.name: e for e in self.events}
        return the_events

    def render(self, prepent:str="", indent="  ") ->str:
        return (
            self.render_struct(prepent, indent)  + "\n" +
            self.render_indexes(prepent, indent) + "\n" +
            self.render_FTs(prepent, indent)  + "\n" )


    def render_struct(self, prepent:str="", indent="  ") ->str:                                     ## struct CC_B_Protocol $name = {...} ;
        var_name = f'cc_P_{self.name}'
        based_on_link = f'&cc_P_{self.based_on.name}' if self.based_on else "NULL"

        retval  = ""
        retval += f'{prepent}struct CC_B_Protocol {var_name} = {{\n'
        retval += f'{prepent}{indent}.name           = "{self.name}",\n'
        retval += f'{prepent}{indent}.kind           = CC_B_ProtocolKindIs_{self.kind.name},\n'
        retval += f'{prepent}{indent}.inherit_from   = {based_on_link},\n'
        retval += f'{prepent}{indent}.length         = {len(self.events)},\n'

        ## For now, loop over the events here ...
        retval += f'{prepent}{indent}.events         = {{\n'
        for n, e in enumerate(self.events, len(self.event_dict(inherired=True,mine=False))):
            retval += f'{prepent}{indent*2}{{'
            retval += f'  .seqNo   = {n}, '
            retval += f'  .name    = "{e.name}", '
            retval += f'  .part_of = &{var_name} '
            retval += "},\n"
        retval += f'{prepent}{indent*2}}}\n'

        retval += f'{prepent}}};\n' # end of struct
        return retval

    def render_indexes(self, prepent:str="", indent="  ") ->str:                                    ## #define CC_P_<proto>_<event> index
        ## For now, loop over the events here ...
        retval  = ""
        for n, e in enumerate(self.events, len(self.event_dict(inherired=True,mine=False))):
            retval +=f'#define CC_P_{self.name}_{e.name}\t{n}\n'
        return retval


    def render_FTs(self, prepent:str="", indent="  ") ->str: ##typedef void (*CC_E_{...}_FT)(CC_selfType, CC_ComponentType, {...});
        type_name = lambda ptype : ptype if isinstance(ptype, str) else ptype.__name__

        retval  = ""
        for  e in self.events:
            types =" , ".join(f'{type_name(parm.type)}' for parm in e.typedParameters)
            retval += f'typedef void (*CC_E_{self.name}_{e.name}_FT)(CC_selfType, CC_ComponentType, {types});\n'
        return retval

