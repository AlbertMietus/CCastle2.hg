# (C) Albert Mietus, 2024. Part of Castle/CCastle project

"""No functional tests; only testing to instantiate the classes in Machinery"""

import pytest

from castle.aigr import machinery

def test_Abstact_machinery():
    m = machinery._machinery()
    assert m is not None
    assert isinstance(m, machinery._machinery)

def test_ToDo__sendStream():
    with pytest.raises(NotImplementedError, match='ToDo'):
        machinery._sendStream()

def test_ToDo__sendData():
    with pytest.raises(NotImplementedError, match='ToDo'):
        machinery._sendData()

def test_EventOverPort_CastleCode():
    """ CastleCode (sieve/basic) Generator:: `StartSieve.runTo(max) on .controll`
        ``.outlet.input(i);``
     """
    o = machinery.EventOverPort(comp='self', outport='self.outlet', event='input', arguments=('i',))
    assert o.comp == 'self'
    assert o.outport == 'self.outlet'
    assert o.event == 'input'
    assert len(o.arguments)==1
    assert o.arguments[0]=='i'

def test_EventToSub_CastleCode():
    """///CastleCode: Main (sieve/basic) -- main has a sub: .generator
        ```self.generator.runTo(max);``` """
    o = machinery.EventToSub(comp='self', receiver='self.generator', event='runTo', arguments=('max',))
    assert o.comp == 'self'
    assert o.receiver == 'self.generator'
    assert o.event == 'runTo'
    assert len(o.arguments)==1
    assert o.arguments[0]=='max'

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



