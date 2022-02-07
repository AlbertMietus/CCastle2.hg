from classes import Demo1

import sys
sys.path.append("./../");sys.path.append("./../../")
from castle.ast import peg

demo_3_rules = (
    { 'name' : 'peg_grammar',
      'expr' : ['rules', 'EOF'] },
    { 'name' : 'rules',
      'expr' : ['OneOrMore(rule)'] })
demo_3_settings = (
    { 'name'  : 'S1',
      'value' :  ''' "'" '''.strip()},
    { 'name'  : 'D1',
      'value' :  ''' '"' '''.strip()},
    { 'name'  : 'S3',
      'value' :  """ "'''" """.strip()},
    { 'name'  : 'D3',
      'value' :  ''' '"""' '''.strip()})



def demo_4A():
    rules    = [ peg.Rule(    name=peg.ID(name=r['name']),  expr=r['expr'])  for r in demo_3_rules]
    settings = [ peg.Setting( name=s['name'],  value=s['value']) for s in demo_3_settings]

    producer = Demo1(default_template='file.jinja2')
    return producer.render(rules=rules, settings=settings)

def demo_4B():
    rules    = [ peg.Rule(    name=peg.ID(name=r['name']),  expr=r['expr'])  for r in demo_3_rules]
    settings = [ peg.Setting( name=s['name'],  value=s['value']) for s in demo_3_settings]
    grammar = peg.Grammar(rules=rules, settings=settings)

    producer = Demo1(default_template='ast.jinja2')
    return producer.render(grammar=grammar)

def demo_4diff():
    A = demo_4A()
    B = demo_4B()
    return "no Diff" if A == B else "DO DIFF"


if __name__ == "__main__":
    demos  = [ func for (name, func) in locals().items()  if name.startswith('demo_') and callable(func) ]
    for demo in demos:
        print(f"{'*'*12}\n** {demo.__name__} ::\n{'*'*12}")
        retval=demo()
        if isinstance(retval, str): print(retval)
        print("==\n")
    print("== Done\n")
