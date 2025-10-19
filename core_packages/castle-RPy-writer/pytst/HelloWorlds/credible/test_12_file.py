# (C) Albert Mietus, 2025. Part of Castle/CCastle project

"""Render (the credible verion of) HelloWorld to text, and save it into a RPy file"""

from . import *
from . import credible, wrapped_Hello_World

@pytest.mark.xfail(reason="ExpectedTxt.EXPECTED_unit needs to be filled in")
def test_1_renderToTxt(target_unit, my_renderer):
    txt = my_renderer.render(target_unit)
    verify_line_by_line(EXPECTED_unit, txt)

