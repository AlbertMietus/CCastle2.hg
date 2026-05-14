# (C) Albert Mietus 2026, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints
import dataclasses

from castle.aigr import AIGRNode
from ._scaffolder import _Scaffolder


class ScaffolderNode(_Scaffolder):
    """Wraps an AIGRNode and adds field bucket metadata and node traversal.

    Field-bucket class variables (REQUIRED for all subclasses)
    -----------------------------------------------------------
    Every Scaffolder subclass MUST explicitly declare (even if empty):
    
    _kid_fields  : field names whose AIGRNode values are structural children.
                   kids() yields these via a generator (lazy evaluation).
    _attr_fields : field names whose AIGRNode values are "parameter-like" metadata.
                   _attrs() yields them separately; not part of kids().
    _link_fields : cross-link field names — excluded from both kids() and _attrs().
    
    IMPORTANT: If your subclass does not declare these explicitly,
    tests will fail. This prevents silently falling back to inherited defaults,
    which is a common source of bugs.
    
    MRO-aware bucket union:
        When multiple classes in the MRO declare buckets, they are union'd together
        (subclass additions are additive). Link fields always win over kids/attrs
        for the same name. Conflicts are detected and logged as errors.

    Base-class defaults (inherited by every subclass unless overridden):
        _link_fields = {'parent', 'outer_ns'}
        _kid_fields  = {'_ns'}          # dict[ID, NamedNode] on namespace nodes
        _attr_fields = frozenset()
    """

    _nodeCls: type = AIGRNode

    # ------------------------------------------------------------------ #
    #  Field-bucket declarations  (frozenset[str])                        #
    # ------------------------------------------------------------------ #
    _link_fields: frozenset[str] = frozenset({'parent', 'outer_ns'})
    _kid_fields:  frozenset[str] = frozenset({'_ns'})
    _attr_fields: frozenset[str] = frozenset()

    @classmethod
    def _collect_field_bucket(cls, bucket: str) -> frozenset[str]:
        """Walk the MRO from *most-base* to *most-derived* and union the named
        bucket frozensets, so that subclass declarations are additive.

        Within a single class, if a name appears in both ``_link_fields`` and
        ``_kid_fields`` / ``_attr_fields``, ``_link_fields`` wins (and an error
        is logged — it is a configuration mistake).
        """
        accumulated: set[str] = set()
        # Reverse MRO: base first so subclass additions overlay base ones.
        for klass in reversed(cls.__mro__):
            names = klass.__dict__.get(bucket)          # only *own* declaration
            if names is not None:
                accumulated.update(names)
        return frozenset(accumulated)

    @classmethod
    def _effective_buckets(cls) -> tuple[frozenset[str], frozenset[str], frozenset[str]]:
        """Return (kid_fields, attr_fields, link_fields) after MRO-merging and
        conflict resolution: link always wins over kid/attr for the same name."""
        links = cls._collect_field_bucket('_link_fields')
        kids  = cls._collect_field_bucket('_kid_fields')  - links
        attrs = cls._collect_field_bucket('_attr_fields') - links

        conflict = kids & attrs # Names in both kids AND attrs (within the same class) is a mistake.
        if conflict:
            logger.error(
                "%s: field(s) %s appear in both _kid_fields and _attr_fields — "
                "treating as _kid_fields. Fix the bucket declarations.",
                cls.__name__, conflict,
            )
            attrs = attrs - conflict

        return kids, attrs, links


    def kids(self) -> PTH.Generator[AIGRNode, None, None]:
        """Yield all *direct structural children* of the wrapped node.

        Rules
        -----
        * Only fields listed in the effective ``_kid_fields`` are considered.
        * The field value may be a single object, a sequence, or a dict.
          For dicts, the *values* are used (keys are IDs, not structural children).
        * Only values that are ``AIGRNode`` instances are yielded (Q3 / Q5 guard).
        * ``None`` values are silently skipped.
        """
        kid_fields, _attrs, _links = self.__class__._effective_buckets()
        node = self.node

        if not dataclasses.is_dataclass(node):
            return

        for field in dataclasses.fields(node):
            if field.name not in kid_fields:
                continue
            value = getattr(node, field.name, None)
            if value is None:
                continue
            yield from self._extract_aigr_nodes(value)

    def _attrs(self) -> PTH.Generator[AIGRNode, None, None]:
        """Yield all *attribute-like child nodes* of the wrapped node.

        These are structural AIGR nodes (e.g. TypedParameter list on a callable)
        that are meaningful metadata on this node but are NOT yielded by kids().
        """
        _kids, attr_fields, _links = self.__class__._effective_buckets()
        node = self.node

        if not dataclasses.is_dataclass(node):
            return

        for field in dataclasses.fields(node):
            if field.name not in attr_fields:
                continue
            value = getattr(node, field.name, None)
            if value is None:
                continue
            yield from self._extract_aigr_nodes(value)

    @staticmethod
    def _extract_aigr_nodes(value: PTH.Any) -> PTH.Generator[AIGRNode, None, None]:
        """Unpack a field value into zero-or-more AIGRNode instances.

        Handles: single AIGRNode, dict (yields .values()), any other iterable.
        Non-AIGRNode items are silently skipped (covers IDs, scalars, enums …).
        """
        if isinstance(value, AIGRNode):
            yield value
        elif isinstance(value, dict):
            for v in value.values():
                if isinstance(v, AIGRNode):
                    yield v
        else:
            try:
                for item in value:
                    if isinstance(item, AIGRNode):
                        yield item
            except TypeError:
                pass  # not iterable — scalar like int/str/enum


    def set_parent(self, parent: PTH.Union[_Scaffolder, AIGRNode]) -> PTH.Self:
        node = self.node
        parent_node = parent.node if isinstance(parent, _Scaffolder) else parent
        node.parent = parent_node
        return self  # for chaining
