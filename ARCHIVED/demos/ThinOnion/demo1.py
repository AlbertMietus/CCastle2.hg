import pytest
import logging; logger = logging.getLogger(__name__)

from castle.readers.parser import grammar
from castle.ast import grammar as AST

import arpeggio
import jinja2


class Reader():

    def __init__(self, read_dirs: list[str]):
        if isinstance(read_dirs, str): read_dirs=[read_dirs] #Always a list
        self.read_dirs = [ _get_file_dirPath() / d for d in read_dirs]


    def parse(self, filename:str) -> AST.Grammar:
        txt = self._read(filename)
        ast = self._do_parse(txt)
        return ast


    def _read(self,filename) ->str:
        for d in self.read_dirs:
            if (d / filename).exists():
                break
        with (d / filename).open() as f:
            txt = f.read()
        return txt


    def _do_parse(self, txt) -> AST.Grammar:
        parser = arpeggio.ParserPython(grammar.peg_grammar, comment_def = grammar.comment)
        pt = parser.parse(txt)
        logger.info(f"Reader:_do_parse::\t parse_tree: start={pt.position} end={pt.position_end}; len(txt)={len(txt)}")
        ast = arpeggio.visit_parse_tree(pt, grammar.PegVisitor())
        logger.debug(f"Reader:_do_parse::\t ast: start={ast.position} end={ast.position_end} -- not counting comments.")
        return ast



class Writer():

    def __init__(self, template, template_dirs: list[str] = ["template/"]):
        if isinstance(template_dirs, str): template_dirs=[template_dirs]  # Always a list
        template_dirs = [ _get_file_dirPath() / d for d in template_dirs]

        templateLoader   = jinja2.FileSystemLoader(searchpath=template_dirs)
        self.templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True)
        self.template = self.templateEnv.get_template(template)
        logger.info(f'Writter::\t template={self.template.filename}')

    def render(self, to_file=None, **kwarsgs):
        txt = self.template.render(**kwarsgs)

        if to_file:
            with open(to_file, mode='w') as f:
                f.write(txt)
        return txt



def run_demo(peg_file, jinja_file, out_file=None):
    r = Reader('.')
    ast = r.parse(peg_file)
    if not ast.settings: ast.settings=[] # hotfix

    logger.info(f'ast={ast}')

    w = Writer(jinja_file)
    txt=w.render(to_file=out_file, grammar=ast)

    if out_file:
        print(f"See {out_file} for result")
    else:
        print("="*70)
        print(txt)
        print("-"*70)

@pytest.mark.xfail(reason="Unit/Feature not yet supported")
def demo_1rule():	run_demo('1rule.peg',   'ast.jinja2')           # 'OUT_1rule.py'

@pytest.mark.xfail(reason="Unit/Feature not yet supported")
def demo_grammar():	run_demo('grammar.peg', 'ast.jinja2', 'OUT_grammar.py')
