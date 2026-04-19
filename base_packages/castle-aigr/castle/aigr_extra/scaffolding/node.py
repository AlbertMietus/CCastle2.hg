# (C) Albert Mietus 2026, Part of Castle/CCastle project
# `walk_down()` and support is made version made by CodeAI: Claude

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints
import dataclasses
from enum import Enum, auto

from castle.aigr import AIGRNode, AIGR
from ._scaffolder import _Scaffolder


class WalkOrder(Enum):
    """Traversal orders for walk_down / apply_down.

    PRE_ORDER  : parent before its children  (default — fastest for top-down transforms)
    POST_ORDER : children before parent       (natural for bottom-up analysis / codegen)
    LEVEL_ORDER: breadth-first (level by level, uses a deque)
    """
    PRE_ORDER   = auto()
    POST_ORDER  = auto()
    LEVEL_ORDER = auto()


class ScaffolderNode(_Scaffolder):
    """Wraps an AIGRNode and adds structural traversal.

    Field-bucket class variables
    ----------------------------
    Every Scaffolder subclass may declare any of these as a ``frozenset[str]``.
    ``_collect_field_bucket()`` walks the MRO and *unions* them (subclass wins on
    conflict; within one class, ``_link_fields`` always beats ``_kid_fields`` /
    ``_attr_fields`` for the same name — that situation is a configuration mistake
    and is logged as an error).

    _kid_fields  : field names whose AIGRNode values are structural children.
                   ``walk_down()`` / ``apply_down()`` recurse into these.
    _attr_fields : field names whose AIGRNode values are "parameter-like" metadata.
                   ``_attrs()`` yields them; walk_down does NOT recurse into them.
    _link_fields : cross-link field names — excluded from both _kids() and _attrs().

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

    # ------------------------------------------------------------------ #
    #  MRO-aware bucket collection                                        #
    # ------------------------------------------------------------------ #

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

        # Names in both kids AND attrs (within the same class) is a mistake.
        conflict = kids & attrs
        if conflict:
            logger.error(
                "%s: field(s) %s appear in both _kid_fields and _attr_fields — "
                "treating as _kid_fields. Fix the bucket declarations.",
                cls.__name__, conflict,
            )
            attrs = attrs - conflict

        return kids, attrs, links

    # ------------------------------------------------------------------ #
    #  _kids() and _attrs()                                               #
    # ------------------------------------------------------------------ #

    def _kids(self) -> PTH.Generator[AIGRNode, None, None]:
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
        that are meaningful metadata on this node but are NOT recursed into by
        ``walk_down`` / ``apply_down``.
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

    # ------------------------------------------------------------------ #
    #  walk_down() and apply_down() — public API                          #
    # ------------------------------------------------------------------ #

    def walk_down(
        self,
        *,
        order: WalkOrder = WalkOrder.PRE_ORDER,
        include_self: bool = False,
    ) -> PTH.Generator[AIGRNode, None, None]:
        """Yield every AIGRNode in the subtree rooted at ``self.node``.

        Parameters
        ----------
        order:
            Traversal order (default: PRE_ORDER — fastest, most cache-friendly).
        include_self:
            When *True* the wrapped node itself is included in the output,
            at the position dictated by ``order``.

        Returns
        -------
        A lazy generator of ``AIGRNode`` instances.
        """
        yield from self._walk_gen(self.node, order=order, include_self=include_self)

    def apply_down(
        self,
        func: PTH.Callable[[AIGRNode], None],
        *,
        order: WalkOrder = WalkOrder.PRE_ORDER,
        include_self: bool = False,
    ) -> None:
        """Call ``func(node)`` for every AIGRNode in the subtree rooted at
        ``self.node``.

        Parameters
        ----------
        func:
            Callable invoked once per node.  Return value is ignored.
        order:
            Traversal order (default: PRE_ORDER).
        include_self:
            When *True* ``func`` is also called on the wrapped node itself.
        """
        for node in self._walk_gen(self.node, order=order, include_self=include_self):
            func(node)

    # ------------------------------------------------------------------ #
    #  Private traversal engine                                           #
    # ------------------------------------------------------------------ #

    def _walk_gen(
        self,
        start: AIGRNode,
        *,
        order: WalkOrder,
        include_self: bool,
    ) -> PTH.Generator[AIGRNode, None, None]:
        """Shared generator that powers both ``walk_down`` and ``apply_down``."""
        if order is WalkOrder.PRE_ORDER:
            yield from self._walk_pre(start, include_self=include_self)
        elif order is WalkOrder.POST_ORDER:
            yield from self._walk_post(start, include_self=include_self)
        elif order is WalkOrder.LEVEL_ORDER:
            yield from self._walk_level(start, include_self=include_self)
        else:                                                   # pragma: no cover
            raise ValueError(f"Unknown WalkOrder: {order!r}")

    def _kids_of(self, node: AIGRNode) -> PTH.Generator[AIGRNode, None, None]:
        """Return the _kids() of an arbitrary AIGRNode by wrapping it temporarily."""
        wrapper = ScaffolderNode.__new__(type(self))
        wrapper._node = node                                    # type: ignore[attr-defined]
        yield from wrapper._kids()

    def _walk_pre(
        self, node: AIGRNode, *, include_self: bool
    ) -> PTH.Generator[AIGRNode, None, None]:
        """Pre-order DFS: parent → children."""
        if include_self:
            yield node
        for child in self._kids_of(node):
            yield child
            for grandchild in self._walk_pre(child, include_self=False):
                yield grandchild

    def _walk_post(
        self, node: AIGRNode, *, include_self: bool
    ) -> PTH.Generator[AIGRNode, None, None]:
        """Post-order DFS: children → parent."""
        for child in self._kids_of(node):
            for grandchild in self._walk_post(child, include_self=False):
                yield grandchild
            yield child
        if include_self:
            yield node

    def _walk_level(
        self, node: AIGRNode, *, include_self: bool
    ) -> PTH.Generator[AIGRNode, None, None]:
        """Breadth-first (level-order) using a deque."""
        from collections import deque
        queue: deque[AIGRNode] = deque()

        if include_self:
            queue.append(node)
        else:
            queue.extend(self._kids_of(node))

        while queue:
            current = queue.popleft()
            yield current
            queue.extend(self._kids_of(current))

    # ------------------------------------------------------------------ #
    #  Existing API                                                       #
    # ------------------------------------------------------------------ #

    def set_parent(self, parent: PTH.Union[_Scaffolder, AIGRNode]) -> PTH.Self:
        node = self.node
        parent_node = parent.node if isinstance(parent, _Scaffolder) else parent
        node.parent = parent_node
        return self  # for chaining
