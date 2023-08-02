from typing import Iterable, Optional, TypeGuard
from pathlib import Path


def normal_relative(path: Path) -> Path:
    return path.resolve().relative_to(Path.cwd())


def ensure_parent(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path

