"""
ACHIEVEMENTS DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

from .award import Award
from .badge import Badge
from .....core.utilities import _to_bool


@dataclass(slots=True, frozen=True)
class Achievements:
    in_top_100_all_time: bool | None
    in_hhof: bool | None
    awards: list[Award]
    badges: list[Badge]

    @classmethod
    def from_dict(cls, data: dict) -> Achievements:
        return cls(
            in_top_100_all_time = _to_bool(data.get("inTop100AllTime")),
            in_hhof = _to_bool(data.get("inHHOF")),
            awards = [Award.from_dict(a) for a in (data.get("awards") or [])],
            badges = [Badge.from_dict(b) for b in (data.get("badges") or [])]
        )
