# (C) Albert Mietus, 2023. Part of Castle/CCastle project  -- PYTEST init for RPY
import logging; logger = logging.getLogger(__name__)

import pytest
from pathlib import Path
import os
from dataclasses import dataclass
from castle.aigr import Event, Protocol
from castle.writers import RPy

SAVE_FILE=True                            #By default, save the generated files


@pytest.fixture
def T_Protocol():
    return RPy.Template("protocol.jinja2")

@pytest.fixture
def T_Moat():
    return RPy.Template("interface.jinja2")

@pytest.fixture
def T_EventIndexes():
    return RPy.Template("parts/protocol_EventIndexes.jinja2")

@pytest.fixture
def T_ProtocolDataStructures():
    return RPy.Template("parts/protocol_DataStructures.jinja2")


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

    def read_ref(self) -> str:             #File content as one (long, multi-line) string (aka Text)
        with open(self.ref_file) as f:
            ref = f.read()
        return ref

    def write_gen(self,txt) ->None:
        with open(self.gen_file, 'w') as f:
            f.write(txt)
        logger.info("Saved rendered protocol in: %s", self.gen_file)


def _gen_matcher(aigr_mock, td, save_file, out, strip_remarker=False, template=None):
    MARKER='#XXX#'
    def match_line(out, ref, strip_remarker=False, filename=None):
        if out == ref:
            return True
        elif strip_remarker and (MARKER in out):
            marker_start = out.find(MARKER)
            logger.debug(f"strip remark: '''{o[marker_start:].rstrip()}'''")
            out = out[:marker_start].rstrip().strip('\n')
            ref = ref.rstrip().strip('\n')
        assert out == ref, f"line %s does not match: >>%s<< != <<%s>> (file: {td.base_name})" % (n, o.strip('\n'), r.strip('\n'))

    if save_file: td.write_gen(out)
    ref = td.read_ref()
    try:
        #assert line by line: gives better feedback when they do not match
        for n, (o,r) in enumerate(zip(out.splitlines(keepends=True), ref.splitlines(keepends=True), strict=True)):
            match_line(o,r, strip_remarker=strip_remarker)
    except ValueError as err:
        assert False, f"Note the same length: files {td.gen_file} and {td.ref_file}"



@pytest.fixture
def generatedProtocol_verifier(T_Protocol):
     def protocol_matcher(aigr_mock, td, save_file=SAVE_FILE, **kw):
         out = T_Protocol.render(protocols=(aigr_mock,))
         return _gen_matcher(aigr_mock, td, save_file=save_file, out=out, template=T_Protocol, **kw)
     return protocol_matcher

@pytest.fixture
def generatedMoat_verifier(T_Moat):
     def protocol_matcher(aigr_mock, td, save_file=SAVE_FILE, strip_remarker=False):
         out = T_Moat.render(interfaces=(aigr_mock,))
         return _gen_matcher(aigr_mock, td, save_file, out)
     return protocol_matcher


