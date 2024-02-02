# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

class ABCD:                                          # Abstract Base Class for Dataclasses   #
    def __new__(cls, *args, **kwargs):
        if cls == ABCD or ABCD in cls.__bases__:
            raise NotImplementedError(f"Instantiate a subclass of {cls}, not the `AbstractBaseClass for Dataclasses` itself")
        return super().__new__(cls)


