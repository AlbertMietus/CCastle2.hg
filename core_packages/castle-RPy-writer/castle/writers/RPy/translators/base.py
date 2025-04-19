# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
from abc import ABC, abstractmethod

import os
from pathlib import Path

import subprocess

class TranslatorCommand(ABC):
    @abstractmethod
    def runner(self) -> str|PTH.Any: # Override this in subclasses. It is called by execute()
        assert False, "Never call the Base-runnner"

    def execute(self) ->str|PTH.Any:
        self.setup()
        out = self.runner()
        self.teardown()
        return out

    def setup(self):    pass
    def teardown(self): pass



class RPY_Translator(TranslatorCommand):
    # XXX hardcoded paths & (partial) filenames XXXX
    PyPy_SRCd    = Path('/Users/albert/NoTimeMachine/PyPy,hgs/') / 'PyPy.dev'
    PyPy_APPSd	 = Path('/Users/albert/Apps/PyPy/')
    PyPy_BINd	 = PyPy_APPSd / 'pypy2.7-v7.3.12-macos_arm64/bin'
    RPYTHON	     = PyPy_SRCd  / 'rpython/bin/rpython'
    MAIN         = 'main_HW' # Without ext!
    #@abstractmethod
    def __init__(self, *,
                     files :PTH.List[Path|str]|str=[],
                     inDir :PTH.Optional[Path|str]=None,
                     main  :PTH.Optional[str]=None):
        """Run a command (to be set in subclass) in directory `inDir` (default: current working dir), using `files` and `main` as main-file
        """
        if isinstance(files, (str, Path)):
            files = [files]
        self.files = [p if isinstance(p, Path) else Path(p) for p in files]

        self.inDir= Path(inDir if inDir else '.')
        self.main = Path(main) if main else Path(self.MAIN)


    def process(self, cmd: list[str],*, PATH_prefix:PTH.Optional[str]=None) ->str:
        if PATH_prefix:
            env=os.environ
            env['PATH']=f"PATH_prefix:{env['PATH']}"
            logger.info("PATH: %s", env['PATH'])                                  # XXX .info will become .debug
        else:
            env=None # default for `subprocess.run`

        logger.debug("subprocess.run:: cmd: >%s< cwd: >%s< (self.inDir) env: >%s<", cmd, self.inDir, env)
        res = subprocess.run(cmd, cwd=self.inDir, env=env, shell=False, capture_output=True, text=True)
        logger.debug("-->%s", res)

        assert res.returncode == 0, f"Failed with {res.returncode}; stderr={res.stderr}; stdout={res.stdout}; res={res}"
        return res.stdout
