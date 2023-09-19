# (C) Albert Mietus, 2023. Part of Castle/CCastle project  -- PYTEST init for RPY

from pathlib import Path
import os


def get_dirPath_of_file(f=__file__):
    print("XXXX", Path(os.path.realpath(f)))
    return Path(os.path.realpath(f)).parent

def end_with_NL(txt):
    return txt +'\n' if (txt[-1] != '\n') else txt




