# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .dispatch_tables import _DispatchTable

from castle import aigr
from castle.aigr import ID

@dataclass
class EventDispatchTable(_DispatchTable):
    """An EventDispatchTable is, like any _DispatchTable, a mapping from incoming events (within a protocol) to a Eventhandler.

    .. note::

       An (event) dispatch-table is always for related to *one* (input) port. The kind of `Port` and the type of
       dispatch-table should match !

       .. important::

       For now, this relation is not completely modeled.

       * Possible we can use an (XLST/DOM alike) "parent/child" relation. (<node>/.., or ancestor(node)) of
         node.closest(<type>) in JS
       * Or, we can simple add a .port field (type: ID).

       For now, we use the .port:ID trick in _DispatchTable

    The aigr version is a data-structure (aka dataclass); it does not have (real) methods. There can be builders to created it.
    |BR|
    Similar, one can use wrappers to read it."""

    _: KW_ONLY
    map: PTH.Optional[dict[ID, str]] = dc_field(default_factory= lambda: dict())



# LocalWords:  EventHandler  EventDispatchTable
