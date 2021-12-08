from jinja2 import Template

def demo_a():
    t = Template("Hello {{ something }}!")
    print(t.render(something="World"))

def demo_b():
    t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
    print(t.render())

def gen_rule(name, peg_expr_list):
    if isinstance(peg_expr_list, str): peg_expr_list=[peg_expr_list]
    return Template(
        """def {{ name }}():
        return {% for e in peg_expr_list -%}
                  {{- e -}} 
                  {{ ", " if not loop.last else "" -}}
               {% endfor -%}\n\n""").render(locals())
def demo_def1():
   return gen_rule('peg_grammar', ['rules', 'EOF'])
def demo_def2():
   return gen_rule('rules', "OneOrMore(rule)")

if __name__ == "__main__":
    demos  = [ func for (name, func) in locals().items()  if name.startswith('demo_') and callable(func) ]
    for demo in demos:
        print(f"{'*'*12}\n** {demo.__name__} ::\n{'*'*12}")
        retval=demo()
        if isinstance(retval, str): print(retval)
    print("== Done\n")
