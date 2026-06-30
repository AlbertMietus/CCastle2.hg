# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.translators.real``.

from .base import RPY_Translator

class Compile(RPY_Translator):
    """Compile generated RPy code to a native binary via the RPython toolchain.

    Runs ``rpython --batch --output=<into> <driver>.py`` in :attr:`inDir`.

    Usage
    -----
    ::

        from castle.writers.RPy.translators import Compile

        Compile(inDir="build/", driver="output", into="my_app").execute()
    """

    def runner(self) -> str: ...


class Execute(RPY_Translator):
    """Execute a previously compiled RPython binary.

    Runs ``./<into>`` in :attr:`inDir` and returns stdout.

    Usage
    -----
    ::

        from castle.writers.RPy.translators import Execute

        Execute(inDir="build/", into="my_app").execute()
    """

    def runner(self) -> str: ...
