# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.transformers.namespace``.

import typing as PTH
from castle import aigr
from castle.writers.RPy.aigr.units import RPy_unit

EXTENTIONS: tuple[str, ...]
"""Source file extensions recognised for stripping: ``('.Moat', '.Castle')``."""
RPY_EXT: str
"""Default output extension: ``'py'``."""

OptStr = PTH.Optional[str]

def Source2RPy(
    src: aigr.Source_NS,
    filename: OptStr = ...,
    ext: OptStr = ...,
) -> RPy_unit:
    """Convert an ``aigr.Source_NS`` into an :class:`RPy_unit` ready for rendering.

    The transformer copies all top-level AIGR nodes from the source namespace
    into a new :class:`RPy_unit` namespace and sets the output file path.

    Parameters
    ----------
    src:
        The AIGR source namespace (produced by the Castle reader).
    filename:
        Override the output file stem.  Defaults to ``src.source`` or
        ``src.name``.
    ext:
        Override the output file extension.  Defaults to :data:`RPY_EXT`
        (``'py'``).  Leading dot is optional.

    Returns
    -------
    RPy_unit
        A new unit namespace, not yet scaffolded or written to disk.
        Wrap it in :class:`ScaffolderUnit` to get file-write capabilities.

    Usage
    -----
    ::

        from castle.writers.RPy.transformers import Source2RPy
        from castle.writers.RPy.aigr.units import ScaffolderUnit

        unit = Source2RPy(source_ns)
        su = ScaffolderUnit(unit)
        su.write_out(inDir="build/")
    """
    ...
