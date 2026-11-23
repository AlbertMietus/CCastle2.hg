# (C) Albert Mietus, 2025. Part of Castle/CCastle project

"""Render (the credible verion of) HelloWorld to text, and save it into a RPy file"""

from . import *


@pytest.mark.xfail(reason="`__init__` // _castle_init` mismatch. See :doc:`ExpectedTxt.py`")
@pytest.mark.skip(reason="Need to design 'pins' and dynamicly finding the DT first -- skip credible for now")
def test_1_renderToTxt(target_unit, my_renderer):
    txt = my_renderer.render(target_unit)
    verify_line_by_line(EXPECTED_unit, txt)
    assert False

@pytest.mark.skip(reason="`test_1_renderToTxt` should work first")
def test_2_render_andSafe(wrapped_target, my_renderer):
    wrapped_target.write_out(inFile="./_test_12-OUT.rpy.py")
    verify_file(EXPECTED_unit, wrapped_target.target_file)
