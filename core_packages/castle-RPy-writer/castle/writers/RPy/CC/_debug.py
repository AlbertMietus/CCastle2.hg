import sys
isV3 = sys.version_info.major == 3
isRP = not isV3 # For now

class DebugMixIn:
    """This MixIn can be used to show debug-info.  It assumes a ``name`` attribute exist

    It has a base implementation for `_debug_()`; which can be called as __repr__() aka repr() too.

    Classes using it should implement `_debug_attr_()`, returning the attributes (incl. name) as strings.
    The MixIn has a default one, showing the name attribute.
    """

    _debug_label="NotSet"

    def _debug_(self, name_only=True):
        _id = "<xxx>" if isRP else "0x%x" % id(self)
        if name_only:
            return (str(self.__class__.__name__)
                    + (("[_label=%s]" % self._debug_label) if self._debug_label != DebugMixIn._debug_label else "")
                    + "()"
                    )
        else:
            return str(self.__class__.__name__) + "(" + self._debug_attr_(name_only=name_only) + ")"

    def _set_label(self, name):
        self._debug_label=name

    def _debug_attr_(self, name_only=True):
        return "<<attributes to be done>>"

    def __repr__(self):
        return self._debug_()

    def _debug_name(self):
        return '<<debug_name to be done>>'

    def _class_name(self):
        return str(self.__class__.__name__)


def _obj_name(obj):
    return obj._debug_name() if obj else "None"


def file_stem(filepath):
    """.. notes:: file_stem

          - pathlib.Path() does not exist in py3
          - os.path.split in not rPython
          """
    name = filepath.split('/')[-1]
    parts = name.split('.')
    stem = parts[0] if len(parts)==1 else ".".join(parts[0:-1])
    return stem

def handler_name(h):
    if isRP:
        return "<XXX_RP>"
    else:
        return str(h.__name__) if h else "NIL"

