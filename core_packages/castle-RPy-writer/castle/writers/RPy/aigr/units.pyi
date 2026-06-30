# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.aigr.units``.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from pathlib import Path
from castle.aigr import namespaces, NamedNode
from castle.aigr.tools.scaffolding import ScaffolderNameSpace

@dataclass
class RPy_unit(NamedNode, namespaces._Target_NS):
    """AIGR node representing a single output Python file to be generated.

    ``RPy_unit`` is both a :class:`castle.aigr.NamedNode` (carrying a debug
    name) and a ``_Target_NS`` (carrying a ``target_file`` path and an inner
    namespace of the top-level AIGR nodes to render).

    Created by :func:`castle.writers.RPy.transformers.Source2RPy` from an
    ``aigr.Source_NS``.

    Usage
    -----
    ::

        unit = Source2RPy(my_source_ns, filename="output.py")
        scaffolded = ScaffolderUnit(unit)
        scaffolded.write_out(inDir="build/")
    """


class ScaffolderUnit(ScaffolderNameSpace):
    """Scaffolder for :class:`RPy_unit` nodes, adding file-write capability.

    Wraps an :class:`RPy_unit` with methods to render it to a Python file via
    the :class:`Renderer` and write the result to disk.

    Usage
    -----
    ::

        unit = Source2RPy(source_ns)
        su = ScaffolderUnit(unit)
        su.write_out(inDir="output/")         # render + save
        # or step by step:
        txt = Renderer().render(unit)
        su.save(txt, inDir="output/")
    """

    _nodeCls: type

    def save(
        self,
        txt: str,
        inDir: PTH.Optional[PTH.Union[Path, str]] = ...,
    ) -> None:
        """Write *txt* to ``self.node.target_file``, optionally under *inDir*.

        If *inDir* is given the stored ``target_file`` is updated to the full
        path ``inDir / target_file`` before writing.
        """
        ...

    def write_out(
        self,
        *,
        inDir: PTH.Optional[PTH.Union[Path, str]] = ...,
        renderCls: PTH.Optional[type] = ...,
        inFile: PTH.Optional[PTH.Union[Path, str]] = ...,
    ) -> None:
        """Render the unit and save it.

        Parameters
        ----------
        inDir:
            Directory to write into (prepended to ``target_file``).
        renderCls:
            Custom :class:`Renderer` subclass to use.  ``None`` uses the
            default :class:`Renderer`.
        inFile:
            Override the output file name (stored in ``self.node.target_file``).
        """
        ...
