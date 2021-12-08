from classes import Demo1

def demo_def1():
   return Demo1().render(template='peg_grammar.jinja2',
                         name='peg_grammar',
                         peg_expr_list=['rules', 'EOF'])

def demo_def2():
   return Demo1().render(template='peg_grammar.jinja2',
                         name='rules',
                         peg_expr_list=['OneOrMore(rule)'])

if __name__ == "__main__":
    demos  = [ func for (name, func) in locals().items()  if name.startswith('demo_') and callable(func) ]
    for demo in demos:
        #print(f"{'*'*12}\n** {demo.__name__} ::\n{'*'*12}")
        retval=demo()
        if isinstance(retval, str): print(retval)
    #print("== Done\n")
