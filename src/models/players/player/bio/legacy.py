"""
LEGACY DATACLASS
"""
from __future__ import annotations
from dataclasses import dataclass

from .award import Award
from .badge import Badge

from .....core.utilities import _to_bool

@dataclass(slots=True, frozen=True)
class Legacy: 
    in_top_100_all_time: bool | None 
    in_HHOF: bool | None 
    awards: list[Award] 
    badges: list[Badge] 

    @classmethod
    def from_dict(cls, data: dict) -> Legacy:
        return cls(
            in_top_100_all_time = _to_bool(data.get("inTop100AllTime")),
            in_HHOF = _to_bool(data.get("inHHOF")),
            awards = [Award.from_dict(award) for award in (data.get("awards") or [])],
            badges = [Badge.from_dict(badge) for badge in (data.get("badges") or [])]
        )
