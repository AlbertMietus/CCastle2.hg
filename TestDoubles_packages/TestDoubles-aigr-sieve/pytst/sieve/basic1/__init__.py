# (C) Albert Mietus 2024, Part of Castle/CCastle project
"""Test the AIGR TestDoubles of the Sieve protocols (basic1 variant)
   See: http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
"""
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from castle import aigr


def find_name_in_body(name, body) -> PTH.Optional[aigr.NamedNode]:
    logger.info("find_name_in_body(name=%s, body=%s", name, body)
    for s in body.statements:
        logger.debug("\t: %s", s)
        if isinstance(s, aigr.NamedNode):
            logger.debug("\t: name=%s in %s", s.name, s)
            if s.name == name:
                logger.debug("\t: FOUND name=%s: %s", s.name, s)
                return s
    logger.debug("NOT FOUND: %s", name)
    return None
