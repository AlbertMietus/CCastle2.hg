# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.writers.CC2Cpy.Protocol import *
from castle.writers.CC2Cpy.Event import *
from castle.writers.CC2Cpy.Component import *

### protocol SimpleSieve : Protocol {
###   kind: event;
###   input(int:try);
### }
@pytest.fixture
def simpleSieveProto():
    return CC_EventProtocol("SimpleSieve", events=[
        CC_Event("input", typedParameters=[CC_TypedParameter(name='event', type=int)])])


### component Sieve : Component {
###   port SimpleSieve<in>:try;
###   port SimpleSieve<out>:coprime;
### }
@pytest.fixture
def sieveInterface(simpleSieveProto):
    return CC_B_ComponentInterface("Sieve", ports=[
        CC_Port(name='try',     direction=CC_PortDirection.In,  type=simpleSieveProto),
        CC_Port(name='coprime', direction=CC_PortDirection.Out, type=simpleSieveProto)])


### implement Sieve {
###   int myPrime;
### -init(int:prime) {...}
### SimpleSieve.input(try) on .try {..}
### }
@pytest.fixture
def sieveClass(sieveInterface):
    return CC_B_ComponentClass(sieveInterface,
                                   handlers=[CC_EventHandler("SimpleSieve.input", port=sieveInterface.find_port_by_name('try'))],
                                   methods=[CC_ElementMethod("init", type=None, parameterTuple=CC_TypedParameter(name='prime', type=int))])



