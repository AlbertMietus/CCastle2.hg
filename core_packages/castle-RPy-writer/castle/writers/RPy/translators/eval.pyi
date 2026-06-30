# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.translators.eval``.

from .base import RPY_Translator

class Evaluate(RPY_Translator):
    """Run the generated RPy file with CPython (``python <driver>.py``).

    The simplest way to test generated code: runs the driver script in a
    subprocess and returns stdout.

    Usage
    -----
    ::

        from castle.writers.RPy.translators import Evaluate

        out = Evaluate(inDir="build/", driver="output").execute()
    """

    def runner(self) -> str: ...
