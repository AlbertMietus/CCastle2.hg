# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from . import *


@pytest.fixture
def DummyProto():
    return aigr.EventProtocol(ID('DummyProto', context=aigr.Def()), events=[])

@pytest.fixture
def DummyPort1(DummyProto):
    return aigr.Port(ID('DummyPort1'), direction=aigr.PortDirection.In, type=DummyProto)

@pytest.fixture
def somePorts(DummyProto):
    return list(aigr.Port(ID(f'Port{p}'), direction=aigr.PortDirection.In, type=DummyProto) for p in range(5))

@pytest.fixture
def portID_list(somePorts):
    return list(ID.Ref(p.name, p) for p in somePorts)


def test_0_ComponentInterface(my_renderer): # This already works -- no ports
    expected = """\
cc_CI_Stub = buildin.CC_B_ComponentInterface(
    name         = "Stub",
    inherit_from = base.cc_CI_Component,
    ports        = [],
    )\n"""
    comp = aigr.ComponentInterface(ID("Stub", context=aigr.Def()))
    txt = my_renderer.render(comp)
    verify_line_by_line(expected, txt)


def test_1_with_1Port(my_renderer, DummyPort1):
    expected = """\
cc_CI_Comp_with_1Port = buildin.CC_B_ComponentInterface(
    name         = "Comp_with_1Port",
    inherit_from = base.cc_CI_Component,
    ports        = [],
    )

cc_CI_Comp_with_1Port.ports.append(
    buildin.CC_B_C_PortID(name="DummyPort1",
        portNo=-1, # Not used?
        protocol=cc_P_DummyProto,
        direction=buildin.CC_PortDirection.In,
        part_of=cc_CI_Comp_with_1Port))\n"""
    comp = aigr.ComponentInterface(ID("Comp_with_1Port", context=aigr.Def()), ports = [ID.Ref(DummyPort1.name, DummyPort1)])
    verify_line_by_line(expected, my_renderer.render(comp))


def test_2_with_somePorts(my_renderer, portID_list):
    comp = aigr.ComponentInterface(ID("Comp_with_1Port", context=aigr.Def()), ports = portID_list)
    expected = """\
cc_CI_Comp_with_1Port = buildin.CC_B_ComponentInterface(
    name         = "Comp_with_1Port",
    inherit_from = base.cc_CI_Component,
    ports        = [],
    )"""
    for p in portID_list:
        expected +=f"""\n
cc_CI_Comp_with_1Port.ports.append(
    buildin.CC_B_C_PortID(name="{p}",
        portNo=-1, # Not used?
        protocol=cc_P_DummyProto,
        direction=buildin.CC_PortDirection.In,
        part_of=cc_CI_Comp_with_1Port))\n"""

    verify_line_by_line(expected, my_renderer.render(comp))
    
