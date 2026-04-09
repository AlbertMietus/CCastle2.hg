# (C) Albert Mietus, 2026. Part of Castle/CCastle project

from abc import ABC, abstractmethod
import typing as PTH

from castle import aigr
from castle.writers.RPy.aid import TextBlock

###
### XXX/ToDo: Move ArgumentList/Signature to aigr als dataclasses -- and renam
###
ArgumentList = PTH.Optional[tuple[aigr.Argument, ...]]
Signature    = PTH.Optional[tuple[aigr.TypedParameter, ...]]

class Bundler(ABC):

    def __new__(cls, hint:str="", **kwargs):
        from .native_bundler import NativeBundler
        return super().__new__(NativeBundler, **kwargs)   # type: ignore[reportAbstractUsage, abstract]

    @abstractmethod
    def pack(self, arguments:ArgumentList, signature:Signature) -> TextBlock:
        raise NotImplementedError("Must be implemented by all subclass of Bundler")

    @abstractmethod
    def unpack(self, signature:Signature) -> TextBlock:
        raise NotImplementedError("Must be implemented by all subclass of Bundler")
