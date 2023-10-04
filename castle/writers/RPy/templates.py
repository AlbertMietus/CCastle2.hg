import logging; logger = logging.getLogger(__name__)  # pragma: no mutate
import typing as PTH                                                    # Python TypeHints
import jinja2 as jinja

from pathlib import Path
import os


def _addTopDir(top_dir: Path, search_path: PTH.Sequence[Path]) ->PTH.Sequence[Path]:
    return tuple(d if d.is_absolute() else top_dir/d  for d in (Path(d) for d in search_path))

class Template():
    def __init__(self, template=None, *, top_dir=None, search_path=("templates",)):
        if isinstance(search_path, (str, Path)): search_path=(search_path,) # make it a sequence 
        if top_dir is None:
            top_dir= Path(os.path.realpath(__file__)).parent #use module-dir a top, "templates/" works
        search_path = _addTopDir(top_dir, search_path)

        logger.info(f"template={template}, top_dir={top_dir}, search_path={search_path}")

        self.environment = jinja.Environment(loader=jinja.FileSystemLoader(search_path), trim_blocks=True, lstrip_blocks=True)  # pragma: no mutate
        self.def_template = self.environment.get_template(template) if template else None



    def render(self, template=None, **kwargs):
        if not template and not self.def_template:
            raise FileNotFoundError("No template nor default template specified")                    # pragma: no mutate

        template = self.environment.get_template(template) if template  else self.def_template
        return template.render(**kwargs)

