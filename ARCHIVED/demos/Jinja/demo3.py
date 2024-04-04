from classes import Demo1


def demo_def1():
    rules = (
        { 'name' : 'peg_grammar',
          'expr' : ['rules', 'EOF'] },
        { 'name' : 'rules',
          'expr' : ['OneOrMore(rule)'] })

    settings = (
        { 'name'  : 'S1',
          'value' :  ''' "'" '''.strip()},
        { 'name'  : 'D1',
          'value' :  ''' '"' '''.strip()},
        { 'name'  : 'S3',
          'value' :  """ "'''" """.strip()},
        { 'name'  : 'D3',
          'value' :  ''' '"""' '''.strip()}
        )

    return Demo1(default_template='file.jinja2').render(rules=rules,
                                                        settings=settings)

if __name__ == "__main__":
    demos  = [ func for (name, func) in locals().items()  if name.startswith('demo_') and callable(func) ]
    for demo in demos:
        print(f"{'*'*12}\n** {demo.__name__} ::\n{'*'*12}")
        retval=demo()
        if isinstance(retval, str): print(retval)
    print("== Done\n")
