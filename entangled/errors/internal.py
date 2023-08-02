from typing import Any
from dataclasses import dataclass, field
import logging


@dataclass
class InternalError(Exception):
    msg: str
    irritants: list[Any] = field(default_factory=list)

    def __str__(self):
        return f"Internal error: {self.msg}"


def bug_contact(exception: Exception) -> None:
    import traceback
    traceback.print_exception(exception)
    logging.error(
        "This error is due to an internal bug in Entangled. Please file an "
        "issue including the above stack trace "
        "and example content to "
        "reproduce the exception at https://github.com/entangled/entangled.py/."
    )
