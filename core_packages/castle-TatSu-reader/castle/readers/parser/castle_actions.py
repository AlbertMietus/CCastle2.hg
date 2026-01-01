# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

from .actions import *

#DOC
## Almost all (semantics) Actions are defines in helper-classes -- which are defined in ./actions/*.py
## Those classes are "listed" below as base-classes.
##
## This is more-or-less based on the "interface segregation principle".
## Instead of one big class with many unrelated methods, those method are distributed over many small classes
## Each of those classes are (roughly) aligned with the PEG-rule-sets; see ./grammar/*.tatsu

class DebugActions():
    """"This is a MixIn for temporally actions, often as calling `super().<MyMethod>` adding extra logging"""
    pass

class CastleActions(
        DebugActions,
        ParmsArgs,
        Names,
        Components,
        ):
    pass
