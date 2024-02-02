# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project
"""
"""
from typing import Any

def mk_tuple(tuple_list_or_element) -> list[Any]:
    """Expect a  sequence of (ANY) element, or a single one, and make a tuple (RO-sequence) of it"""

    return  (tuple_list_or_element if isinstance(tuple_list_or_element, tuple)
             else tuple(tuple_list_or_element) if isinstance(tuple_list_or_element, list)
             else () if isinstance(tuple_list_or_element, type(None))
             else tuple((tuple_list_or_element,)) )
