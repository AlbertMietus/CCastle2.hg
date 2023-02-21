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

from .sieve_fixtures import *

from datetime import datetime
def write_header(f):
    f.writelines(f"""/*(C) Alber Mietus, Generated code:: {datetime.now()}*/
#include <CC/buildin_types.h>
#include <CC/runtime.h>
\n""")

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
