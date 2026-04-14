# (C) Albert Mietus, 2026. Part of Castle/CCastle project

from abc import ABC, abstractmethod
import typing as PTH

from castle import aigr
from castle.aigr import types as CCTypes
from castle.writers.RPy.aid import TextBlock

type TypeTag[T] = str
type GeneratedCode = TextBlock|TypeTag


class Bundler(ABC):

    def __new__(cls, hint:str="", **kwargs):
        from .native_bundler import NativeBundler
        return super().__new__(NativeBundler, **kwargs)   # type: ignore[reportAbstractUsage, abstract]

    @abstractmethod
    def box(self, argument:GeneratedCode, cc_type:CCTypes._types) -> TypeTag:
        """Box a single argument (generated_code) to the specified type"""

    @abstractmethod
    def pack(self, arguments:PTH.Sequence[TypeTag], formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock:
        """Combine all arguments into the used calling convention.
           Each subclass will/can set it own calling convention
           Typically used juss before (generateing the code of a function-call"""

    @abstractmethod
    def unpack(self, parameters:GeneratedCode, formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock:
        """Take out all (packed) parameters, to make the normal, induvidual parameters are avaibale
           Typically used as first step 'in' the callable; when generating code        """

    @abstractmethod
    def unbox(self, parm:str) -> GeneratedCode:
        """UnBox a (single) argument"""

