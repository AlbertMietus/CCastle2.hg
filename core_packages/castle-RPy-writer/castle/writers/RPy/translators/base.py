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
        assert False, "Never call the Base-runnner" # pragma: no cover

    def execute(self) ->str|PTH.Any:
        self.setup()
        out = self.runner()
        self.teardown()
        return out

    def setup(self):    pass
    def teardown(self): pass

PYPY2_BINd	= "/Users/albert/Apps/PyPy/pypy2.7-v7.3.20-macos_arm64/bin/"
TIMEOUT     = 60 #second

class RPY_Translator(TranslatorCommand):
    # XXX hardcoded paths & (partial) filenames XXXX

    RPYTHON = PYPY2_BINd +"rpython"

    #@abstractmethod
    def __init__(self, *,
                     inDir   :PTH.Optional[Path|str]=None,
                     files   :PTH.List[Path|str]|str=[],
                     driver  :PTH.Optional[str]=None,                                    # driver (file)name
                     into    :PTH.Optional[str]=None,                                    # name of output-file (if any)
                     timeout :int= TIMEOUT):
        """Run a translator-command (to be set in subclass) in directory `inDir`, using `driver` as main-file (stem only).

        * Typically a list of files is passed, but they can also be named in the main-driver (python-file)
        * The command is run in inDir; default: current working dir. It will be terminated after `timeout` seconds
        """
        if isinstance(files, (str, Path)):
            files = [files]
        self.files    = [p if isinstance(p, Path) else Path(p) for p in files]
        self.driver   = driver
        self.inDir    = Path(inDir if inDir else '.')
        self.into     = into
        self._timeout = timeout

    def process(self, cmd: list[str],*, PATH_prefix:PTH.Optional[str]=None) ->str:
        if PATH_prefix:
            env=os.environ
            env['PATH']=f"PATH_prefix:{env['PATH']}"
            logger.debug("PATH: %s", env['PATH'])
        else:
            env=None # default for `subprocess.run`

        try:
            logger.debug("subprocess.run:: cmd: >%s< cwd: >%s< (self.inDir) env: >%s<", cmd, self.inDir, env)
            res = subprocess.run(cmd, cwd=self.inDir, env=env, shell=False, capture_output=True, text=True, timeout=TIMEOUT)
            logger.debug("-->%s", res)
        except subprocess.TimeoutExpired as err:
            assert False, f"TimeOut when running {cmd}: {err}"

        assert res.returncode == 0, f"Failed with {res.returncode}; stderr={res.stderr}; stdout={res.stdout}; res={res}"
        return res.stdout
