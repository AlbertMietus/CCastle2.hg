from ..import _debug

class CC_B_ComponentInterface(_debug.DebugMixIn):
    """Describes the interface of a Component; more or less as by the Moat file

    This data-structure is defined once. The CastleCompiler will instantiate one object for each 
    defined Component(Interface); which is statically available in the generated code.

    .. seealso:: CC_B_ComponentClass """

    def __init__(self, name, inherit_from, ports):
        self.name = name
        self.inherit_from = inherit_from
        self.ports = ports

    @property
    def length(self):
        return len(self.ports)

    def _debug_attr_(self, name_only=True):
        port_str = "[\n\t"
        for p in self.ports:
            port_str += p._debug_(name_only=False) + ",\n\t"
        port_str += "]"
        return ("name="             + self.name
                + ", inherit_from=" + _debug._obj_name(self.inherit_from)
                + ", length="       + str(self.length)
                + ", ports="        + port_str)

    def _debug_name(self):
        return self.name
