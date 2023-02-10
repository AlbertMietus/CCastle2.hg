# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

"""CCastle::CC2Cpy integration test: write the C-code for the "Sieve" component
"""


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
def simpleSieve():
    return CC_EventProtocol("SimpleSieve", events=[
        CC_Event("input", typedParameters=[CC_TypedParameter(name='event', type=int)])])


### component Sieve : Component {
###   port SimpleSieve<in>:try;
###   port SimpleSieve<out>:coprime;
### }
@pytest.fixture
def sieveInterface(simpleSieve):
    return CC_B_ComponentInterface("Sieve", ports=[
        CC_Port(name='try',     direction=CC_PortDirection.In,  type=simpleSieve),
        CC_Port(name='coprime', direction=CC_PortDirection.Out, type=simpleSieve)])


### implement Sieve {
###   int myPrime;
### ...
@pytest.fixture
def sieveClass(sieveInterface):
    return CC_B_ComponentClass(sieveInterface,
                                    # methods=
                                    )


from pathlib import Path
from tempfile import TemporaryDirectory
import os
import subprocess


def write_header(f):
    f.writelines("""/*(C) Alber Mietus, Generated code*/
#include <CC/buildin_types.h>
#include <CC/runtime.h>

""")

def verify_it_compiles(file, in_dir:Path):
    os.symlink("/Users/albert/work/CCastle2/from_CC-Castle/SRC-EXAMPLE/SIEVE/2.GCD-work/CC", in_dir/"CC")
    return_code = subprocess.run(["gcc", "-I", in_dir, "-c", file]).returncode
    assert return_code == 0


def test_0a(simpleSieve, sieveInterface, sieveClass, tmp_path):
    with open(tmp_path/"sieve-interface.c", 'w') as f:
        write_header(f)
        f.write(simpleSieve.render())
        f.write(sieveInterface.render())
    verify_it_compiles(f.name, tmp_path)

@pytest.mark.skip(reason="sieveClass refer to ``cc_B_Sieve_methods`` and ``CC_C_Sieve`` which aren't renderable yet")
def test_0b(simpleSieve, sieveInterface, sieveClass, tmp_path):
    with open(tmp_path/"sieve-interface.c", 'w') as f:
        write_header(f)
        f.write(simpleSieve.render())
        f.write(sieveInterface.render())
        f.write(sieveClass.render())
    verify_it_compiles(f.name, tmp_path)
    

@pytest.mark.skip(reason="More Generate C-file(s)")
def test_more(): pass
