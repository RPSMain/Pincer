# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from __future__ import annotations

from dataclasses import is_dataclass
from inspect import getfullargspec
from typing import TYPE_CHECKING

from .types import T, MISSING

if TYPE_CHECKING:
    from ..client import Client
    from typing import Any, Callable, Dict, List, Optional, Set, Union


def construct_client_dict(client: Client, data: Dict) -> Dict:
    return {**data, "_client": client, "_http": client.http}


def convert(
    value: Any,
    factory: Callable[[Any], T],
    check: Optional[T] = None,
    client: Optional[Client] = None,
) -> T:
    def handle_factory() -> T:
        def fin_fac(v: Any):
            if check is not None and isinstance(v, check):
                return v

            try:
                if client and "_client" in getfullargspec(factory).args:
                    return factory(construct_client_dict(client, v))
            except TypeError:  # Building type/has no signature
                pass

            # The import has been placed locally to avoid circular imports
            # TODO: Find a way to remove this monstrosity
            from ..utils import APIObject

            if isinstance(v, APIObject):
                return v

            return factory(v)

        return (
            [*map(fin_fac, value)]
            if isinstance(value, list)
            else fin_fac(value)
        )

    return MISSING if value is MISSING else handle_factory()

def remove_none(obj: Union[List, Dict, Set]) -> Union[List, Dict, Set]:
    if isinstance(obj, list):
        while None in obj:
            obj.remove(None)
    elif isinstance(obj, set):
        obj.discard(None)
    elif isinstance(obj, dict):
        to_del = [k for k, v in obj.items() if None in {k, v}]
        for k in to_del:
            del obj[k]
    return obj