# (C) Albert Mietus 2026, Part of Castle/CCastle project
# Partialy made by CodeAI: github-copilot: Claude Haiku 4.5

"""Verify (future) Scaffolders have updated/set meta-data

   test_4* tests extisting scaffolderss
   This test verifies all Scaffolders have the metadata set"""

import logging; logger = logging.getLogger(__name__)
import pytest

from . import *




def test_all_scaffolderNodes_have_metadata_set(scaffolder_node_classes):
    """ Verify that new/future Scaffolders don't forget to declare metadata

    At least one of `_kids_fields`, `_attr_fields`, or `_link_fields` should be set.
    Inherit values do not count!
    """

    for cls in scaffolder_node_classes:
        has_own_kids_fields = '_kids_fields' in cls.__dict__
        has_own_attr_fields = '_attr_fields' in cls.__dict__
        has_own_link_fields = '_link_fields' in cls.__dict__

        has_own_declaration = has_own_kids_fields or has_own_attr_fields or has_own_link_fields

        assert has_own_declaration, f"""{cls.__name__} forgot to set metadata ---
        {[n for n in cls.__dict__.keys() if 'field' in n]=}"""



def XXX_test_scaffolder_buckets_are_disjoint(scaffolder_node_classes):
    """Verify that kids, attrs, and links never overlap within any Scaffolder class."""

    for cls in scaffolder_node_classes:
        k, a, l = cls._effective_buckets()

        assert k.isdisjoint(a), (
            f"{cls.__name__}: Field(s) appear in both _kids_fields and _attr_fields: {k & a}. "
            f"This is a configuration error — fix {cls.__name__}._*_fields declarations."
        )
        assert k.isdisjoint(l), (
            f"{cls.__name__}: Field(s) appear in both _kids_fields and _link_fields: {k & l}. "
            f"This is a configuration error — fix {cls.__name__}._*_fields declarations."
        )
        assert a.isdisjoint(l), (
            f"{cls.__name__}: Field(s) appear in both _attr_fields and _link_fields: {a & l}. "
            f"This is a configuration error — fix {cls.__name__}._*_fields declarations."
        )
