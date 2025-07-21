# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from castle.aigr import ID

def mangle_event_handler(*, protocol:str|None, event:str|None, port:str|None) ->ID:
    """Flatten the 3 name-parts of an event-handler to a single ID-string"""
    DEFAULT_NAME='default'
    logger.debug("mangle_event_handle(protocol=%s, event=%s, port=%s)", protocol, event, port)

    if not protocol: protocol = DEFAULT_NAME
    if not event:    event    = DEFAULT_NAME
    if not port:     port     = DEFAULT_NAME

    name = ID(f'{protocol}_{event}__{port}')
    logger.debug("\t=>%s", name)
    return name
