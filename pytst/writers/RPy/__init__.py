# (C) Albert Mietus, 2023. Part of Castle/CCastle project  -- PYTEST init for RPY

import logging; logger = logging.getLogger(__name__)
import pytest

from pathlib import Path
import os
from dataclasses import dataclass

from castle.aigr import Event, Protocol
from castle.writers import RPy

@dataclass
class MockEvent(Event):
    indexNo: int

@dataclass
class MockProtocol():
    name: str

@pytest.fixture
def T_EventIndexes():
    return RPy.Template("EventIndexes.jinja2")

@pytest.fixture
def T_Protocol():
    return RPy.Template("protocol.jinja2")



def get_dirPath_of_file(f=__file__):
    print("XXXX", Path(os.path.realpath(f)))
    return Path(os.path.realpath(f)).parent

def end_with_NL(txt):
    return txt +'\n' if (txt[-1] != '\n') else txt




