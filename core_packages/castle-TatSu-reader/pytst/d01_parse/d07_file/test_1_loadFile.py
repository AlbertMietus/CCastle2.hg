# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.readers.ladon.loaders import SimpleFileLoader
from castle.readers.ladon.loaders.simple_loader import PyModuleLoader

from . import *


def test_1_Load_EmptyFile(myDir):
    loader = SimpleFileLoader(myDir/"empty.Castle")
    ast = loader.parse()
    validate_topAst(ast, filename="empty")

def test_2_Load_OneStatement(myDir):
    loader = SimpleFileLoader(myDir/"file1.Castle")
    ast = loader.parse()
    validate_topAst(ast, filename="file1", names=['One'])

#The PyModuleLoader is a bit strange, it loads CastleCode distributed in a Python package -- like the TestDouble package
from castle.readers.ladon.loaders.simple_loader import PyModuleLoader
def test_3_loadfromPackage():
    loader=PyModuleLoader(module="CastleCode.elemental", file="HelloWorld.Castle")
    ast=loader.parse()
    assert isinstance(ast, aigr.Source_NS)
