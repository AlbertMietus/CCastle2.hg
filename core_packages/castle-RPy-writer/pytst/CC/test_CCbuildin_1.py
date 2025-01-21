# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import pytest

from castle.writers.RPy.CC import buildin

def verifyClassPrefix(cls, prefix):
    assert isinstance(cls, type), 			f'{cls} is not a class'
    assert cls.__name__.startswith(prefix), f'Incorrect prefix: Expected "{prefix}", found "{cls.__name__}" for for {cls}'

def test_prefixes_1_elementalHW():
    """test the prefix/name/existance of some buildin classes, ..
    Those used by elemental HelloWorld (TestDoubles/HelloWorlds/elemental/HelloWorld.rpy)
    """
    verifyClassPrefix(buildin.CC_B_ComponentInterface,	'CC_B_')
    verifyClassPrefix(buildin.CC_B_Component, 			'CC_B_')
    verifyClassPrefix(buildin.CC_B_ComponentClass, 		'CC_B_')




def test_prefixes_99_someMore():
    verifyClassPrefix(buildin.CC_B_C_PortID,	'CC_B_C_')
    verifyClassPrefix(buildin.CC_B_OutPort,		'CC_B_')
    verifyClassPrefix(buildin.CC_B_P_EventID,	'CC_B_P_')
    verifyClassPrefix(buildin.CC_B_Protocol,	'CC_B_')




