# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

def _flat_sequence(ast, to_type):
    """Flatten a sequence with elements and/or lists/tuples into a single sequence elements."""
    return to_type(elm for seq in ast for elm in (seq if isinstance(seq, (list, tuple)) else [seq]))

def flat_list(ast):
    return _flat_sequence(ast, list)
def flat_tuple(ast):
    return _flat_sequence(ast, tuple)



