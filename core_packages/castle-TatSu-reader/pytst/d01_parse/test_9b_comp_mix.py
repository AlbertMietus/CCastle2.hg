# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

@pytest.mark.skip(reason="`[proto.]event ...` without proto is to complicated for now")
def test_99_Comp_ProtoViaPort(castle_parser):
    """An event-handler may omit the protocol-part of the event, as is can be found via the port.
    This is more complicated to parse (then with the proto: see test_9a::test_3_Comp_EH_with_proto)

    The protocol is needed for the (mangled) name, and for the 'protocol' field. So we need o read that
    via the ComponentInterface.
    The quistion is how to provide that info (to the parser) as is typically defined in another file.

    .. note::

       * One option, is via the NS and import parts.
       * Another apprach is: "fix it later" -- set temporary values when parsing, and fix it later in the pipe
       * Or, delay that "feature" to later, and require the `proto.event` syntax for now
    """
    txt_moat = """\
protocol DemoP :EventProtocol {
    foo();
}
component Comp_ProtoViaPort {
  port p: DemoP<in>;
}"""
    txt_imp = """\
implement Comp_ProtoViaPort {
foo() on self.p {}
}"""
    assert False, "BUSY"
    moat = castle_parser(txt_moat, start='interface_definitions')
    comp = castle_parser(txt_imp,  start='implement_component') # HOW TO PASS moat part?
    logger.debug(f"{txt_imp=} ==> {comp=}")
    verify_ComponentImplementation(comp, name="Comp_ProtoViaPort", handlers=1)
    # Now check the EH: proto & name
    handler = comp.handlers[0]
    assert isinstance(handler, aigr.EventHandler)
    assert handler.name == 'DemoP_foo__p'
    assert isinstance(handler.protocol, ID) and handler.protocol == 'DemoP'
    assert isinstance(handler.event, ID)    and handler.event    == 'foo'
    assert len(handler.port) == 2
    assert isinstance(handler.port[0], ID)  and handler.port[0]  == 'self'
    assert isinstance(handler.port[1], ID)  and handler.port[1]  == 'p'



