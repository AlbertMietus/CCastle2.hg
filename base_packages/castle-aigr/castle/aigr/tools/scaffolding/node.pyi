# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.tools.scaffolding.node``.
# Hand-maintained "manual autodoc" companion to node.py.

import typing as PTH
from castle.aigr import AIGRNode as AIGRNode
from ._scaffolder import _Scaffolder as _Scaffolder

logger: PTH.Any

class ScaffolderNode(_Scaffolder):
    """Wraps an ``AIGRNode`` and adds field-bucket metadata plus tree traversal.

    Subclasses declare which of the wrapped node's fields are structural by
    listing the field names in three class variables (``_kids_fields``,
    ``_attr_fields``, ``_link_fields``). Inherited entries are collected
    automatically, so a subclass only lists the *new* fields. The traversal
    methods (:meth:`kids`, :meth:`attrs`, :meth:`links`) then yield the related
    nodes.

    Rules for the metadata
    ----------------------
    * Every field of the node must appear in exactly one of the three sets.
    * Empty sets may be omitted, but set at least one (hint: ``_kids_fields``)
      so it is clear nothing was forgotten.
    * The bucket a field belongs to may not change once set.
    """

    _nodeCls: type
    _kids_fields: frozenset[str]
    """Field names holding direct structural children."""
    _attr_fields: frozenset[str]
    """Field names holding attribute-like nodes (metadata, not children)."""
    _link_fields: frozenset[str]
    """Field names holding references/links (e.g. ``parent``)."""

    def kids(self) -> PTH.Iterator[AIGRNode]:
        """Yield the direct structural children (from ``_kids_fields``).

        Field values may be a single node, a sequence or a dict (its values);
        non-``AIGRNode`` items and ``None`` are skipped.
        """
        ...

    def attrs(self) -> PTH.Iterator[AIGRNode]:
        """Yield the attribute-like nodes (from ``_attr_fields``) -- not children."""
        ...

    def links(self) -> PTH.Iterator[AIGRNode]:
        """Yield the reference/link nodes (from ``_link_fields``), e.g. the parent."""
        ...

    def set_parent(self, parent: PTH.Union[_Scaffolder, AIGRNode]) -> PTH.Self:
        """Set the wrapped node's ``parent`` (unwrapping *parent* if needed); returns self for chaining."""
        ...

    def _get_nodes_by_metadata(self, meta_field: str) -> PTH.Iterator[AIGRNode]:
        """Yield the nodes referenced by the fields listed in *meta_field* (one of the 3 buckets).

        Shared engine behind :meth:`kids`/:meth:`attrs`/:meth:`links`; override
        rarely.
        """
        ...

    def _metadata_collect_fieldnames(self, meta_field: str) -> frozenset[str]:
        """Collect, over the MRO, all field names declared in *meta_field* (base first)."""
        ...
