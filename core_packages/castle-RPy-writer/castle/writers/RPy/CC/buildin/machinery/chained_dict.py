# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import typing as PTH                                                                                 # Python TypeHints  - not for RPython
# This is RPYthon code!

class ChainedDict:
    """This dict-alike structure is used in CC to store (event) DispatchTables (with :class:`M_DC_chained_dict` as 'the Machinery').

    Each ChainedDict contains (only) its "own part" of DispatchTable, and references to it parent for inherited mappings.

    .. notes:

       * A ChainedDict is a read-only map, when running. All key/value pairs are generated.
       * The set-method is only use to create the map (and for testing)"""

    def __init__(self, map :PTH.Optional[dict]=None, parent=None):
        self._parent = parent
        self._dict = map if map else {}

    def __getitem__(self, key):
        """Act as a normal (read the) dict"""
        try:
            return self._dict[key]
        except KeyError:
            if self._parent:
                return self._parent[key] # may raise a KeyError!
            #else
            raise KeyError(key)

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except KeyError:
            return False


