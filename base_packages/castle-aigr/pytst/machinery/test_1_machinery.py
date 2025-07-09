# (C) Albert Mietus, 2024. Part of Castle/CCastle project

"""No functional tests; only testing to instantiate the classes in Machinery"""

import pytest

from castle.aigr import machinery

def test_Abstact_machinery():
    m = machinery._machinery()
    assert m is not None
    assert isinstance(m, machinery._machinery)

def test_send_proto_OutPort_Dummy():
    o = machinery._send_proto(outport='Dummy')
    assert o.outport=='Dummy'

def test_send_proto_needsOutPort():
    with pytest.raises(TypeError, match="""'outport'"""):
        o = machinery._send_proto()

def test_ToDo__sendStreamd():
    with pytest.raises(NotImplementedError, match='ToDo'):
        machinery.sendStream(outport='*')

def test_ToDo__sendData():
    with pytest.raises(NotImplementedError, match='ToDo'):
        machinery.sendData(outport='*')

def test_sendEvent_CastleCode():
    """ CastleCode (sieve/basic) Generator:: `StartSieve.runTo(max) on .controll`
        ``.outlet.input(i);``
     """
    o = machinery.sendEvent(outport='self.outlet', event='input', arguments=('i',))
    assert o.outport == 'self.outlet'
    assert o.event == 'input'
    assert len(o.arguments)==1
    assert o.arguments[0]=='i'

def test_connection_CastleCode():
    """CastleCode (sieve/basic) Main:: `init()`
    ``.generator.outlet = .finder.newPrime;``
    """
    o = machinery.connection(outport='self.generator.outlet', inport='self.finder.newPrime')
    assert o.outport == 'self.generator.outlet'
    assert o.inport  == 'self.finder.newPrime'

def test_connection_bothPortsNeeded():
    with pytest.raises(TypeError, match="'inport'"):
        machinery.connection(outport='Dummy')
    with pytest.raises(TypeError, match="'outport'"):
        machinery.connection(inport='Dummy')
    with pytest.raises(TypeError, match='2 required keyword-only arguments'):
        machinery.connection()



