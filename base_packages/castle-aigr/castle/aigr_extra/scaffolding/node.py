# (C) Albert Mietus 2026, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints
import dataclasses

from castle.aigr import AIGRNode
from ._scaffolder import _Scaffolder


class ScaffolderNode(_Scaffolder):
    """Wraps an AIGRNode and adds field bucket metadata and node traversal.

    class-variables REQUIRED for all sub-classes
    ============================================

    What is wrapped
    ---------------
    _nodeCls     : type of the node (instances) that can be wrapped (defined in `_Scaffolder`)

    Metadata, that build the tree
    -----------------------------
    _????_fields : frozenset[str] :  Name of fields (in the wrapped node), that define the tree
                  Each AIGRNode (& sub-classes) has (data) fields that refer to other nodes, like its
                  `.parent`. Other are "kids", "links", or "attr(ibutes)".
                  For scaffolding, that meta info is stored in each ScaffolderNode, in the following class-vars:
    _kids_fields : ... (sequence of) AIGRNode(s) that are direct children
    _attr_fields : ... "property-like" Nodes -- like a parameter of a function
    _link_fields : ... "ref" to node -- like .parent

    .. note::
       * All field-names (of an AIGRNode) must be mentioned in one of the 3 `_*_fields`
       * Empty `_*_fields` can be skipped
       * When all `_*_fields` should be empty, set at least one (hint _kids_fields).
         This is to show it is not forgotten -- there is a test that verifies this
       * Only "new" names need to be set, inherited onces are automatically collected
       * Once set, the "kind" of relation (kids/attr/link) can't change! """

    #The type of AIGRNode that can be wrapped
    _nodeCls: type = AIGRNode
    # Metadata: define the tree. -- At this is base, set all 3
    _kids_fields: frozenset[str] = frozenset()
    _attr_fields: frozenset[str] = frozenset()
    _link_fields: frozenset[str] = frozenset({'parent'})


    def kids(self) -> PTH.Iterator[AIGRNode]:
        """Yield all *direct structural children* of the wrapped node.

        Rules
        -----
        * Only fields listed in the effective ``_kids_fields`` are considered.
        * The field value may be a single object, a sequence, or a dict.
          For dicts, the *values* are used (keys are IDs, not structural children).
        * Only values that are ``AIGRNode`` instances are yielded
        * `None`s  are silently skipped. """

        yield from self._get_nodes_by_metadata('_kids_fields')

    def attrs(self) -> PTH.Iterator[AIGRNode]:
        """Yield all *attribute-like* nodes of the wrapped node.

        These are structural AIGR nodes (e.g. TypedParameter list on a callable)
        that are meaningful metadata on this node but are NOT yielded by kids()."""

        yield from self._get_nodes_by_metadata('_attr_fields')


    def links(self) -> PTH.Iterator[AIGRNode]:
        """Yield the `link/ref nodes of the wrapped node (e.f the parent)"""

        yield from self._get_nodes_by_metadata('_link_fields')

    def _get_nodes_by_metadata(self, meta_field:str) -> PTH.Iterator[AIGRNode]:
        """Yield the nodes with a `meta_field` relation to self"""

        node = self.node
        assert dataclasses.is_dataclass(node), f"{node=} should be a dataclass"
        assert meta_field in ('_kids_fields', '_attr_fields', '_link_fields'), "Only this meta data"

        names = self._metadata_collect_fieldnames(meta_field)
        relevant_fields = list(f for f in dataclasses.fields(node) if f.name in names)

        logging.debug(f"{meta_field=}:: {[f.name for f in relevant_fields]} -- wrapped/type: {type(self).__qualname__}/{type(self._node).__qualname__}")
        for field in relevant_fields:
            if (related_nodes := getattr(node, field.name, None)) is not None:
                yield from self._flatten(related_nodes)   #Yield node by mode


    def _metadata_collect_fieldnames(self, meta_field: str) -> frozenset[str]:
        """Collect the fieldnames, including inherited ones for one meta_field. """

        accumulated: set[str] = set()
        for cls in reversed(self.__class__.__mro__): # Reverse MRO: base first so subclass additions overlay base ones.
            names = cls.__dict__.get(meta_field)    # Only *own* declaration
            if names is not None:
                accumulated.update(names)
        return frozenset(accumulated)


    @staticmethod
    def _flatten(related_nodes: PTH.Any) -> PTH.Iterator[AIGRNode]:
        """Unpack a `related_nodes` into zero-or-more AIGRNode instances.

           Handles: single AIGRNode,  dict (yields .related_nodess()), any other iterable.
           Non-AIGRNode items are silently skipped, as is None"""

        logging.debug(f"flatten:: {related_nodes=}, {type(related_nodes)=} ")

        if related_nodes is None:
            return # This 'node' is skipped in by the calling Iterator
        elif isinstance(related_nodes, AIGRNode):
            logging.debug(f"XXX AIGRNode {related_nodes=}")
            yield related_nodes
        elif isinstance(related_nodes, dict):
            for node in related_nodes.values():
                if isinstance(node, AIGRNode):
                    logging.debug(f"XXX dict {node=}")
                    yield node
        else: # sequence ...
            try:
                for node in related_nodes:
                    if isinstance(node, AIGRNode):
                        yield node
            except TypeError:
                pass  # not iterable — scalar like int/str/enum


    def set_parent(self, parent: PTH.Union[_Scaffolder, AIGRNode]) -> PTH.Self:
        node = PTH.cast(AIGRNode, self.node)
        parent_node = parent.node if isinstance(parent, _Scaffolder) else parent
        node.parent = parent_node
        return self  # for chaining
