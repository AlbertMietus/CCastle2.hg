#!/usr/bin/env python3
# (C) Albert Mietus, 2026. Part of Castle/CCastle project

import copy
import tomllib
import tomli_w
import argparse
from datetime import date
from pathlib import Path


SOURCE  = Path("pyproject.toml")
TARGET  = Path("dist_tst/pyproject.toml")
VERSION = "0.5-2026.04.24"


class PyprojectTstGenerator:
    """Derives a *-tst package from a production pyproject.toml -- without manual duplication."""

    def __init__(self, source: Path = SOURCE, target: Path = TARGET) -> None:
        self._source = source
        self._target = target
        self._config = self._read_config(source)

    def generate(self) -> None:
        self._rename_to_tst_package()
        self._add_production_package_as_dependency()
        self._redirect_packages_to_pytst()
        self._drop_package_data()
        self._add_generated_metadata()
        self._write_tst_config()

    # -- steps ----------------------------------------------------------

    def _rename_to_tst_package(self) -> None:
        self._config["project"]["name"] = self._tst_name

    def _add_production_package_as_dependency(self) -> None:
        existing = self._config["project"].get("dependencies", [])
        self._config["project"]["dependencies"] = existing + [self._pinned_production_dependency]

    def _redirect_packages_to_pytst(self) -> None:
        self._setuptools["packages"] = {"find": {"where": ["."], "include": ["pytst*"]}}

    def _drop_package_data(self) -> None:
        self._setuptools.pop("package-data", None)

    def _add_generated_metadata(self) -> None:
        self._config.setdefault("tool", {})["make_pyproject_tst"] = {
            "generated_by"  : f"make_pyproject_tst.py v{VERSION}",
            "generated_on"  : str(date.today()),
            "source"        : str(self._source),
        }

    def _write_tst_config(self) -> None:
        self._target.parent.mkdir(parents=True, exist_ok=True)
        with self._target.open("wb") as f:
            tomli_w.dump(self._config, f)

    # -- derived values -------------------------------------------------

    @property
    def _production_name(self) -> str:
        return self._config["project"]["name"]

    @property
    def _production_version(self) -> str:
        return self._config["project"].get("version", "*")

    @property
    def _tst_name(self) -> str:
        return f"{self._production_name}-tst"

    @property
    def _pinned_production_dependency(self) -> str:
        return f"{self._production_name}=={self._production_version}"

    @property
    def _setuptools(self) -> dict:
        return self._config.setdefault("tool", {}).setdefault("setuptools", {})

    # -- internals ------------------------------------------------------

    @staticmethod
    def _read_config(source: Path) -> dict:
        with source.open("rb") as f:
            return copy.deepcopy(tomllib.load(f))


# -- CLI ----------------------------------------------------------------

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=f"Derive a *-tst pyproject.toml from a production one. (v{VERSION})",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--source", type=Path, default=SOURCE, help="Production pyproject.toml to read")
    parser.add_argument("--target", type=Path, default=TARGET, help="Generated tst pyproject.toml to write")
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    PyprojectTstGenerator(source=args.source, target=args.target).generate()
