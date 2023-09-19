import logging; logger = logging.getLogger(__name__)

import jinja2 as jinja

class Template():
    def __init__(self, searchpath=("templates",), template=None):

        if isinstance(searchpath, str): searchpath=(template_dirs,)  # Always a seq
        logger.info(f"searchpath={searchpath}, template={template}")

        self.environment = jinja.Environment(loader=jinja.FileSystemLoader(searchpath), trim_blocks=True, lstrip_blocks=True)
        self.def_template = self.environment.get_template(template) if template else None


    def render(self, template=None, **kwargs):
        if not template and not self.def_template:
            raise FileNotFoundError("No template nor default template specified")

        template = self.environment.get_template(template) if template  else self.def_template
        return template.render(**kwargs)

