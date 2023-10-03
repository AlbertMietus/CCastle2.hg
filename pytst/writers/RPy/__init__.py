# (C) Albert Mietus, 2023. Part of Castle/CCastle project  -- PYTEST init for RPY
import logging; logger = logging.getLogger(__name__)

import pytest
from pathlib import Path
import os
from dataclasses import dataclass
from castle.aigr import Event, Protocol
from castle.writers import RPy


@pytest.fixture
def T_Protocol():
    return RPy.Template("protocol.jinja2")

@pytest.fixture
def T_EventIndexes():
    return RPy.Template("EventIndexes.jinja2")

@pytest.fixture
def T_ProtocolDataStructures():
    return RPy.Template("ProtocolDataStructures.jinja2")


def assert_marker(marker, txt, need=None, msg=None):
    lines = txt.splitlines()
    c = sum(1 if (marker in line) else 0 for line in lines)
    if need is None:
        assert c > 0, f"Expected lines with '{marker}'-marker, found nothing in:\n----\n{txt}\n----"
    else:
        assert c == need, f"Needed {need} lines with '{marker}'-markers, found {c} -- in {len(lines)} lines" + ((+ ' ' + msg) if msg else "")


def get_dirPath_of_file(f=__file__):
    print("XXXX", Path(os.path.realpath(f)))
    return Path(os.path.realpath(f)).parent

def end_with_NL(txt):
    return txt +'\n' if (txt[-1] != '\n') else txt


class TstDoubles():
    _top = Path('TestDoubles')
    _ref = Path('reference')
    _gen = Path('_generated')

    def __init__(self, base_name):
       self.base_name = Path(base_name)

    @property
    def ref_file(self, ext='.rpy'):
        return self._top / self._ref / self.base_name.with_suffix(ext)

    @property
    def gen_file(self, ext='.rpy'):
        return self._top / self._gen / self.base_name.with_suffix(ext)


@pytest.fixture
def generatedProtocol_verifier(T_Protocol):
     def matcher(aigr_mock, td, save_file=False):
        out = T_Protocol.render(protocols=(aigr_mock,))
        logger.debug("---------- out: (%s)----------\n%s", aigr_mock, out)
        if save_file:
            with open(td.gen_file, 'w') as f:
                f.write(out)
            logger.info("Saved rendered protocol in: %s", td.gen_file)
        ref = open(td.ref_file).read()
        logger.debug("---------- ref: ----------\n%s\n==========================", out)

        #assert line by line: gives better feedback when they do not match
        for n, (o,r) in enumerate(zip(out.splitlines(keepends=True), ref.splitlines(keepends=True), strict=True)):
            assert o == r, "line %s does not match: >>%s<< != <<%s>>" % (n, o.strip('\n'), r.strip('\n'))
        assert out == ref                 #Should be needed
     return matcher


