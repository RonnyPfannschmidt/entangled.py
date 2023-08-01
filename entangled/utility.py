from typing import Iterable, Optional, TypeVar, TypeGuard, Union
from dataclasses import is_dataclass
from contextlib import contextmanager
import os
from pathlib import Path


def normal_relative(path: Path) -> Path:
    return path.resolve().relative_to(Path.cwd())


def ensure_parent(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def cat_maybes(it: Iterable[Optional[T]]) -> Iterable[T]:
    def pred(x: Optional[T]) -> TypeGuard[T]:
        return x is not None

    return filter(pred, it)
