# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

"""CCastle::CC2Cpy integration test: write the C-code for the "Sieve" component
"""


import logging; logger = logging.getLogger(__name__)
import pytest

from pathlib import Path
import os
import subprocess


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



from datetime import datetime
def write_header(f):
    f.writelines(f"""/*(C) Alber Mietus, Generated code:: {datetime.now()}*/
#include <CC/buildin_types.h>
#include <CC/runtime.h>

""")

def verify_it_compiles(file, in_dir:Path):
    print(f"Compiling {file}")
    os.symlink("/Users/albert/work/CCastle2/from_CC-Castle/SRC-EXAMPLE/SIEVE/2.GCD-work/CC", in_dir/"CC")
    return_code = subprocess.run(["cc", "-arch", "x86_64", "-arch", "arm64", "-I", in_dir, "-c", file], cwd=in_dir).returncode
    assert return_code == 0


def test_1a_ProtoInter(simpleSieveProto, sieveInterface, tmp_path):
    FILE="sieve-ProtoInterface.c"
    with open(tmp_path/FILE, 'w') as f:
        write_header(f)
        f.write(simpleSieveProto.render())
        f.write(sieveInterface.render())
    verify_it_compiles(f.name, tmp_path)

@pytest.mark.skip(reason="sieveClass refer to ``cc_B_Sieve_methods`` and ``CC_C_Sieve`` which aren't renderable yet. See test-4")
def test_1b_ProtoInterClass(simpleSieveProto, sieveInterface, sieveClass, tmp_path):
    FILE="sieve-ProtoInterClass.c"
    with open(tmp_path/FILE, 'w') as f:
        write_header(f)
        f.write(simpleSieveProto.render())
        f.write(sieveInterface.render())
        f.write(sieveClass.render())      #NEW
    verify_it_compiles(f.name, tmp_path)


@pytest.mark.skip(reason="More Generate C-file(s)")
def test_more(): pass
