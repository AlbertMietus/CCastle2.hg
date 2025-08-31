# (C) Albert Mietus, 2025. Part of Castle/CCastle project

# This is RPYthon code!

class ChainedDict:
    """This dict-alike structure is used in CC to store (event) DispatchTables (with :class:`M_DC_chained_dict` as 'the Machinery

    Each ``ChainedDict`` contains (only) its "own part" of DispatchTable; that is, events-handlers that are implemented within
    (the scope of) this Component. It is "chained" to another :class:`ChainedDict` (instance) that contains the inherited
    handlers.

    This `._parent` ChainedDict is defined in/with a base-component (for the same port!), and used as (top) map for that component.
    It will hold a `._parent` again.
    |BR|
    When an event-handler is redefined in the component, it is defined in the `ChainedDict` of that component. The one of the parent
    is ignored (automatically).

    .. notes:

    * A ChainedDict is a read-only map, when running. All key/value pairs are generated.
    * The set-method is only use to create the map (and for testing)
    """

    def __init__(self, map=None, parent=None):
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


