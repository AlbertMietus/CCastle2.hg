# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from . import *

def test_0_ComponentInterface(my_renderer): # This already works -- no ports
    expected = """\
cc_CI_Stub = buildin.CC_B_ComponentInterface(
    name         = "Stub",
    inherit_from = base.cc_CI_Component,
    ports        = (),
    )\n"""
    comp = aigr.ComponentInterface(ID("Stub", context=aigr.Def()))
    txt = my_renderer.render(comp)
    verify_line_by_line(expected, txt)


DummyProto= aigr.EventProtocol(ID('DummyProto', context=aigr.Def()), events=[])

def test_1_with_aPort(my_renderer):
    expected = """\
cc_CI_P1 = buildin.CC_B_ComponentInterface(
    name         = "P1",
    inherit_from = base.cc_CI_Component,
    ports        = []
    )
cc_CI_P1.ports.append(
   buildin.CC_B_C_PortID(name="outlet",
                              portNo=1, //XXX
                              protocol=cc_P_DummyProto,
                              direction=buildin.CC_B_PortDirectionIs_out,
                              part_of=cc_CI_P1))\n"""
    comp = aigr.ComponentInterface(ID("P1", context=aigr.Def()),
                                       ports = [
                                           aigr.Port(ID('in_port'),
                                                     direction=aigr.PortDirection.In,
                                                     type=DummyProto)])
    verify_line_by_line(expected, my_renderer.render(comp))
