
from .award import Award
from .badge import Badge

from ...core.to_bool import _to_bool

class Legacy: 
    def __init__(self, data: dict):
        self.in_top_100_all_time: bool | None = _to_bool(data.get("inTop100AllTime"))
        self.in_HHOF: bool | None = _to_bool(data.get("inHHOF"))
        self.awards: list[Award] = [Award(award) for award in (data.get("awards") or [])]
        self.badges: list[Badge] = [Badge(badge) for badge in (data.get("badges") or [])]