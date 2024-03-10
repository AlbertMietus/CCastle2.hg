# (C) Albert Mietus, 2023,2024 Part of Castle/CCastle project
# verify/aux test-functions

import castle.aigr as aigr
from castle.TESTDOUBLES.aigr.base  import Protocol as base_Protocol

def verify_Protocol(p, name, my_event_names, total_no_of_event=None, base=None, cls=None):
    if base is None:
        base=base_Protocol
    no_events = total_no_of_event if total_no_of_event else len(my_event_names)
    if cls is None:
        cls = aigr.EventProtocol

    assert isinstance(p, cls)
    assert p.name == name,  f"{p.name} reported but expected: {name}"
    assert p.based_on is base
    assert p._noEvents() == no_events, f"{p.name} reports {p._noEvents()} events, but expected: {no_events} event(s)"
    for no, name in enumerate(my_event_names):
        assert p.events[no].name == name, f"{p.name} (own/local) event no={no}: {p.events[no].name}, expected: {name}"



def verify_NS(ns, name, registered_names, as_name=None):
    if as_name is None: as_name=name
    assert ns.name == as_name, f"verify_NS:: name={ns.name}, expected: {as_name}\n\tns={ns}"
    for n in registered_names:
        if isinstance(n, (list, tuple)):
            # This is hardly/not used: but .... We support `import n[1] as n[0]`
            assert len(n) == 2
            name, asName = n[1], n[0]
        else:
            name, asName = n, n
        assert ns.getID(asName).name == name
