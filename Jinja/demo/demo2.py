import jinja2


class Demo1():
    def __init__(self, default_template=None, template_dirs=["template/"]):
        if isinstance(template_dirs, str): template_dirs=[template_dirs]  # Always a list
        template_dirs = [  self._get_file_dirPath() / d for d in template_dirs]

        templateLoader   = jinja2.FileSystemLoader(searchpath=template_dirs)
        self.templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True)
        self._load_tempate(default_template)

    def _load_tempate(self, file):
        self.template = self.templateEnv.get_template(file) if file else None

    @staticmethod
    def _get_file_dirPath():
        from pathlib import Path
        import os
        path_to_current_test = Path(os.path.realpath(__file__))
        path_to_current_dir = path_to_current_test.parent
        return path_to_current_dir

    def render(self, *, template=None, **kwarsgs):
        if template: self._load_tempate(template)                       # ReLoad default_template
        return self.template.render(**kwarsgs)



def demo_def1():
   return Demo1().render(template='peg_grammar',
                         name='peg_grammar',
                         peg_expr_list=['rules', 'EOF'])

def demo_def2():
   return Demo1().render(template='peg_grammar',
                         name='rules',
                         peg_expr_list=['OneOrMore(rule)'])



if __name__ == "__main__":
    demos  = [ func for (name, func) in locals().items()  if name.startswith('demo_') and callable(func) ]
    for demo in demos:
        #print(f"{'*'*12}\n** {demo.__name__} ::\n{'*'*12}")
        retval=demo()
        if isinstance(retval, str): print(retval)
    #print("== Done\n")
