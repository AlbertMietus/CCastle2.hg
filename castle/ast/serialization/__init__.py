

class Serialize ():

    def __new__(cls, *, strategy=None, **kwargs):
        if strategy is None:
            return object.__new__(cls)
        if str(strategy).upper() == "XML":
            from .ast2xml  import XML_Serialize
            return XML_Serialize()
        else:
            raise NotImplementedError(f"No Serializer of {strategy} available")

    def __init__(self, *, strategy=None, **kwargs):
        super().__init__(**kwargs)

    def serialize(self, ast):
        raise NotImplementedError(f"Implement in subclass")

