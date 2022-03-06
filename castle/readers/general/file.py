""" General File-Reader support"""

import logging; logger = logging.getLogger(__name__)


from pathlib import Path
import os


def _get_file_dirPath(file=None):
    if file is None: file=__file__
    path_to_current_test = Path(os.path.realpath(file))
    path_to_current_dir = path_to_current_test.parent
    return path_to_current_dir



class BaseReader():

    def __init__(self, *, read_dirs: list[str], **kwargs):
        if isinstance(read_dirs, str): read_dirs=[read_dirs] #Always a list
        self.read_dirs = [ _get_file_dirPath() / d for d in read_dirs]
        super().__init__(**kwargs)

    def _read(self, filename) ->str:
        for d in self.read_dirs:
            if (d / filename).exists():
                break
        with (d / filename).open() as f:
            logger.debug(f'Reading file: >>{f.name}<<')
            txt = f.read()
        return txt


