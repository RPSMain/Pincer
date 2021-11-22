"""
Pincer
====================
An asynchronous python API wrapper meant to replace discord.py

Copyright Pincer 2021
Full MIT License can be found in `LICENSE` at the project root.
"""

from typing import NamedTuple, Literal, Optional

from ._config import *
from .client import *
from .commands import *
from .exceptions import *
from .objects import *
from .utils import *

__package__ = "pincer"
__title__ = "Pincer"
__description__ = "Discord API wrapper made from scratch."
__author__ = "Sigmanificient, Arthurdw"
__email__ = "contact@pincer.dev"
__license__ = "MIT"

ReleaseType = Optional[Literal["alpha", "beta", "candidate", "final", "dev"]]


class VersionInfo(NamedTuple):
    """A Class representing the version of the Pincer library."""

    major: int
    minor: int
    micro: int

    release_level: ReleaseType = None
    serial: int = 0

    def __repr__(self) -> str:
        return f"{self.major}.{self.minor}.{self.micro}" + (
            f"-{self.release_level}{self.serial}"
            * (self.release_level is not None)
        )


version_info = VersionInfo(0, 11, 5)
__version__ = repr(version_info)
