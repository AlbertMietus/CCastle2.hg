# (C) Albert Mietus, 2023,2024 Part of Castle/CCastle project
# verify/aux test-functions

import castle.aigr as aigr



def verify_ComponentInterface(i, name, my_port_names=[], total_no_of_ports=None):
    if total_no_of_ports is None:
        total_no_of_ports = len(my_port_names)

    assert isinstance(i, aigr.ComponentInterface)
    assert str(i.name) == name, f"{i.name} reported but expected: {name}"

    for no, name in enumerate(my_port_names):
        assert str(i.ports[no].name) == name, f"{i.name} (own/local) port no={no}: {i.ports[no].name}, expected: {name} (str-compare)"
        assert i.ports[no].name == aigr.ID(name),  f"{i.name} (own/local) port no={no}: {i.ports[no].name}, expected: {name} (ID)"

