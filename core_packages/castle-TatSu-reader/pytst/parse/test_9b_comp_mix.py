# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

@pytest.mark.skip
def test_0_Comp_with_empty_EH(castle_parser):
    """
    The event-handlers in a ComponentImplementation need to know the protocol of the port,
    and so (may) need the ComponentInterface.
    F.e. aigr.EventHandler() need (the names of) protocol, event & port. -- the same is needed for
    `mangle_event_handler()` to set the name of the EventHandler.

    The quistion is how to provide that info.
    We need to parse both the "moat" and "castle" side (kind of in 2 files. And pass that info.

    BUSY: For now we parse te moat first, get the ComponentInterface, and check the protocol.
    Them we will use a hack to parse it into the ComponentImplementation-parsing.
    """
    txt_moat = """\
protocol DemoP :EventProtocol {
    foo();
}
component Demo {
  port p: DemoP<in>;
}"""
    txt_imp = """\
implement Demo {

foo() on self.p {
}
}"""
    moat = castle_parser(txt_moat, start='interface_definitions')
    logger.info(f"{txt_moat=} ==> {moat=}")                               # XXX info->debug
    demo_interface=moat[1]
    verify_ComponentInterface(demo_interface, name="Demo", ports_spec=[  # Only to check
        # name        type            #direction
        ("p",         "DemoP",        aigr.PortDirection.In),
        ])
    # this is the part we need:
    p_proto = demo_interface.ports[0].type
    assert p_proto == "DemoP"

    comp = castle_parser(txt_imp, start='implement_component')
    logger.info(f"{txt_imp=} ==> {comp=}")                                # XXX info->debug


    assert False, "BUSY"




def verify_ComponentImplementation(comp, name, parameters=0, handlers=0):
    assert isinstance(comp, aigr.ComponentImplementation)
    # direct attributes
    assert comp.name == name
    assert comp.interface is None               #XXXX
    assert len(comp.parameters) == parameters
    assert len(comp.handlers)   == handlers
    # inherited via _hasScope --|> Scope --|> _NameSpace
    assert isinstance(comp._ns,      dict)
    assert isinstance(comp.outer_ns, (dict, type(None))) #.outer_ns is a ref that can be empty ...
    assert comp.outer_ns is None                         # .. Here it is/should be
