# (C) Albert Mietus, 2026. Part of Castle/CCastle project
from __future__ import annotations # ignore `CC_B_Value` annotation durung runtime

import typing as PTH
from abc import ABC, abstractmethod

from castle import aigr
from castle.aigr import types as CCTypes
from castle.writers.RPy.aid import TextBlock

if PTH.TYPE_CHECKING: # Use `CC_B_Value` annotation for linters
    from castle.writers.RPy_buildin.buildin import CC_B_Value
else:
    CC_B_Value = "CC_B_Value" # Just a placeholder -- even basedpyright will comment on it




type TypeTag[T] = str
"""A type-cast code fragment produced by :meth:`Bundler.box`.

   Typically looks like ``CC_B_int(expr)`` -- a string of generated Python code
   that wraps a value in the appropriate Castle type wrapper."""

type GeneratedCode = TextBlock|TypeTag
"""Some generated code (so text).
   It can be a str,  a :class:`Block`, with holds that kind to text)typically several lines)
   Always "print" a GeneratedCode value to get real text"""

class Bundler(ABC):
    """Abstract strategy for (un)bundling Castle call arguments, so that RPython can handle all kind of arguments.

    The four-step calling convention
    ---------------------------------
    (when calling)
    1. :meth:`box` 		-- wrap an actual (CCastle) argument value in a TypeTag
    2. :meth:`pack` 	-- combine all boxed arguments into the argument list passed at the call site.
    (in the callee)
    3. :meth:`unpack` 	-- destructure the packed argument list back into individual parameters.
    4. :meth:`unbox` 	-- extract the raw value from the Box into a native RPython type (as text)

    .. note:: Only 1 implemention: :class:`NativeBundler`.

       Currently, Only :class:`NativeBundler` is avaibale, and always used (hardcoded).
       This may/will change in the futher, so do not depend on it! Other implemention-classes will be added

    .. note:: Support for named arguments will be added later.

       The dict is avaibale, but always empty for now

    Usage
    -----
    ::

        bundler = Bundler()           # returns an subclass, like NativeBundler
        tag  = bundler.box("42", CCTypes.int)       # -> 'CC_B_int(42)'
        args = bundler.pack([tag], params)          # -> '[CC_B_int(42)], {}'

    Demo
    ---
    * See :file:`/Users/albert/work/TryOut/PyPy+Rpython/CallBundler/Bundle_rpy.py` (and friends)
    * That file shows how to call methods, via a table --and so they need to have the same signature
    * It is roughly the result of rendering with the Bundler
    """

    def __new__(cls, hint:str="", **kwargs):
        from .native_bundler import NativeBundler
        return super().__new__(NativeBundler, **kwargs)   # type: ignore[reportAbstractUsage, abstract]

    @abstractmethod
    def box(self, argument:GeneratedCode, cc_type:CCTypes._types) -> TypeTag[CC_B_Value]:
        """Box a single argument (generated_code) to the specified type"""

    @abstractmethod
    def pack(self, arguments:PTH.Sequence[TypeTag[CC_B_Value]], formal_parameters:aigr.OptionalTypedParameterList) -> TextBlock:
        """Combine all arguments into the used calling convention.
           Each subclass will/can set it own calling convention
           Typically used juss before (generateing the code of a function-call"""

    @abstractmethod
    def unpack(self, formal_parameters:aigr.OptionalTypedParameterList) ->list[tuple[aigr.ID, TypeTag]]:
        """UPDATE XXX doc

        Take out all (packed) parameters, to make the normal, induvidual parameters are avaibale
        Typically used as first step 'in' the callable; when generating code"""

    @abstractmethod
    def unbox(self, parm:str, cc_type:CCTypes._types) -> GeneratedCode:
        """UnBox a (single) argument"""

    @abstractmethod
    def unpack_unbox(self, formal_parameters:aigr.OptionalTypedParameterList) ->list[tuple[aigr.ID, GeneratedCode]]:
        """Call unpack and _unbox in the right order"""
