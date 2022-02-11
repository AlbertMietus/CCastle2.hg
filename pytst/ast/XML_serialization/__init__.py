import logging; logger = logging.getLogger(__name__)
from xml.etree import ElementTree as ET

from castle.ast import  peg


class StdSequence_withAsserts:
    """A class with some terminals and a sequence, and  assert-statements
    """
    def __init__(self):
        self.n1, self.v2, self.v3 = 'ID_1', 'str_2', 'regexp_3'
        e1 = peg.ID(name=self.n1)
        e2 = peg.StrTerm(value=self.v2)
        e3 = peg.RegExpTerm(value=self.v3)
        self.seq = peg.Sequence(value=[e1, e2, e3])
    def assert_xml_Element(self, txt):
        assert_xml_Element(txt, tag='.//Sequence')
        assert_xml_Element(txt, tag='.//ID', name=self.n1)
        assert_xml_Element(txt, tag='.//StrTerm',value=self.v2)
        assert_xml_Element(txt, tag='.//RegExpTerm', value=self.v3)


def assert_xml_Element(txt, tag,
                       version="0.0",
                       **attribs,):
    """Partially verify an xml-string; focusing on 'tag' -- a real tag, or a (limited) XPATH-expression.

    This `tag` (expression) should result in a single hit!. *Use e.g `[0]` as suffix to select one from a list*.
    Pass ``key=value`` **attribs** to verify the found tag has those attribs and values
    """

    tree = ET.fromstring(txt)
    if version:
        assert tree.attrib['version'] == version
    founds = tree.findall(tag)
    assert len(founds) == 1, f"Expected only one element; got: {len(founds)} :{founds}"
    found = founds[0]
    logger.debug(f'XXX1 tag={tag}:: found={found}')
    for attrib, value in attribs.items():
        logger.debug(f'XXX2 tag={tag}:: attrib={attrib}, value={value}')
        assert found.attrib[attrib] == value


def assert_QuantityGroup(xml_serialize, pegGrp, tagName):
    seq = StdSequence_withAsserts()
    txt = xml_serialize(pegGrp(expr=seq.seq))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tagName)
    seq.assert_xml_Element(txt)

def assert_QuantityID(xml_serialize, pegGrp, tagName, id_name='JustAName'):
    txt = xml_serialize(pegGrp(expr=peg.ID(name=id_name)))
    logger.debug(f'XML:: {txt}')

    assert_xml_Element(txt, tagName)
    assert_xml_Element(txt, tag='.//ID', name=id_name)
