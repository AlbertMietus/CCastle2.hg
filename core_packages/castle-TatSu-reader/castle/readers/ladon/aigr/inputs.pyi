# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.aigr.inputs``.
# Hand-maintained companion to inputs.py.

import typing as PTH
from dataclasses import dataclass

from castle.aigr.namespaces import _NameSpace
from castle.aigr.tools.scaffolding import ScaffolderNameSpace

logger: PTH.Any


@dataclass
class FileNS(_NameSpace):
    """Temporary, nameless namespace that collects the top-level nodes found in one source file.

    Built by the ``Files`` semantic-action class when TatSu reduces a
    ``castle_file`` or ``moat_file`` rule.  Callers never instantiate this
    directly; it is created inside the grammar-action for the file rule and
    consumed by :meth:`_BaseLoader._make_Source_NS` to populate the final
    :class:`castle.aigr.Source_NS`.

    The ``name`` class attribute is set to the sentinel ``"TEMP"`` because a
    ``FileNS`` has no real name until the loader wraps it in a ``Source_NS``.
    """

    name: PTH.ClassVar[str]


class ScaffolderFileNS(ScaffolderNameSpace):
    """ScaffolderNameSpace specialisation that iterates over the entries of a FileNS.

    Used by :meth:`_BaseLoader._make_Source_NS` to walk every named node
    collected during parsing and register them into a ``Source_NS``::

        file_ns  = FileNS()
        wrapped  = ScaffolderFileNS(file_ns)
        for node in wrapped:
            source_ns_scaffolder.register(node)

    ``_nodeCls`` is bound to :class:`FileNS`; ``__iter__`` yields each value
    stored in the underlying ``_ns`` dict.
    """

    _nodeCls: type

    def __iter__(self) -> PTH.Iterator[PTH.Any]: ...
