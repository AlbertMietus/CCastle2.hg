import logging;logger = logging.getLogger(__name__)
import arpeggio

from castle.readers.parser.grammar import language as grammar


def parse(txt, grammer_rule):
    logger.debug(f'>>{txt}<<')

    parser = arpeggio.ParserPython(grammer_rule, grammar.comment)
    pt = parser.parse(txt)

    #Some basic checks
    assert pt.position_end == len(txt) , f"Not parsed whole input; Only: >>{txt[pt.position: pt.position_end]}<<; Not: >>{txt[pt.position_end:]}<<."

    return pt

