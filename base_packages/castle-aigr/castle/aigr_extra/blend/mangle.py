# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import typing as PTH                                       # Python TypeHints
import logging; logger = logging.getLogger(__name__)

from castle.aigr import ID, QualID

def mangle_event_handler(*,
                         protocol: PTH.Optional[str|ID|QualID]=None,
                         event:    PTH.Optional[str|ID|QualID]=None,
                         port:     PTH.Optional[str|ID|QualID]=None) ->ID:

    """Flatten the 3 name-parts of an event-handler to a single ID-string"""
    DEFAULT_NAME='default'
    logger.debug("mangle_event_handle(protocol=%s, event=%s, port=%s)", protocol, event, port)

    protocol = qualID_2_str(protocol) if protocol else DEFAULT_NAME
    event    = qualID_2_str(event)    if event    else DEFAULT_NAME
    port     = qualID_2_str(port)     if port     else DEFAULT_NAME

    name = ID(f'{protocol}_{event}__{port}')
    logger.debug("\t=>%s", name)
    return name


def qualID_2_str(quid: QualID|ID|str) -> str:
    """Given a ID/qualID or str-name, remove 'self', and return as str"""
    if isinstance(quid, (list, tuple)):
        if quid[0] == 'self':
            quid = quid[1:] #remove 'self'
        return "_".join(str(n) for n in quid)
    elif isinstance(quid, ID):
        return str(quid)
    elif isinstance(quid, str):
        return quid
    else:
        logging.warning("Not a quilID|ID|str:: %s:%s use as %s (fingers crossed)", quid, type(quid), str(quid))
        return str(quid)
