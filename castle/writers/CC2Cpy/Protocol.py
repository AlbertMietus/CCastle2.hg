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
class CC_B_Protocol(CC_Base):
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
            the_events |= self.based_on.event_dict(inherired=True, mine=True) if isinstance(self.based_on, CC_EventProtocol) else {} # pragma: no mutate
        if mine:
            the_events |= {e.name: e for e in self.events}
        return the_events

    def render(self, prepend:str="", indent="  ") ->str:
        return (
            self.render_struct(prepend, indent)  + "\n" +
            self.render_indexes(prepend) + "\n" +
            self.render_FTs(prepend)  + "\n" )


    def render_struct(self, prepend:str="", indent="  ") ->str:                                     ## struct CC_B_Protocol $name = {...} ;
        var_name = f'cc_P_{self.name}'
        based_on_link = f'&cc_P_{self.based_on.name}' if self.based_on else "NULL"

        retval = []
        retval.append(f'{prepend}struct CC_B_Protocol {var_name} = {{')
        retval.append(f'{prepend}{indent}.name           = "{self.name}",')
        retval.append(f'{prepend}{indent}.kind           = CC_B_ProtocolKindIs_{self.kind.name},')
        retval.append(f'{prepend}{indent}.inherit_from   = {based_on_link},')
        retval.append(f'{prepend}{indent}.length         = {len(self.events)},')
        retval.append(f'{prepend}{indent}.events         = {{')

        #Loop over events
        for n, e in enumerate(self.events, len(self.event_dict(inherired=True, mine=False))):       # pragma: no mutate on event_dict parms
            lineval = []
            lineval.append(f'{prepend}{indent*2}{{')                                                # XXXpragma: no mutate
            lineval.append(f'  .seqNo   = {n}, ')
            lineval.append(f'  .name    = "{e.name}", ')
            lineval.append(f'  .part_of = &{var_name} ')
            lineval.append("},")
            # add line to retval
            retval.append("".join(lineval))
        retval.append(f'{prepend}{indent}}}')   #end of events      XXX Mutant: indent*3
        retval.append(f'{prepend}}};\n')          #end of struct
        return '\n'.join(retval) +"\n"


    def render_indexes(self, prepend:str="") ->str:                                ## #define CC_P_<proto>_<event> index
        retval = []
        for n, e in enumerate(self.events, len(self.event_dict(inherired=True, mine=False))): # pragma: no mutate on event_dict parms
            retval.append(f'{prepend}#define CC_P_{self.name}_{e.name}\t{n}')
        return '\n'.join(retval)+"\n"


    # XXX Mutant 2*: default values prepend/indent
    def render_FTs(self, prepend:str="", ) ->str:                 ##typedef void (*CC_E_{...}_FT)(CC_selfType, CC_ComponentType, {...});
        type_name = lambda ptype : ptype if isinstance(ptype, str) else ptype.__name__   # pragma: no mutate -- is it needed?

        retval = []
        for  e in self.events:
            types =" , ".join(f'{type_name(parm.type)}' for parm in e.typedParameters)   # pragma: no mutate on " , " befor join()
            retval.append( f'{prepend}typedef void (*CC_E_{self.name}_{e.name}_FT)(CC_selfType, CC_ComponentType, {types});')
        return '\n'.join(retval)+"\n"

