
from typing import Any


class Draft: 
    def __init__(self, data: dict):
        draft = data.get("draftDetails")

        self.year: int | None = self._handle_missing(draft, "year")
        self.team: str | None = self._handle_missing(draft, "teamAbbrev")
        self.round: int | None = self._handle_missing(draft, "round")
        self.pick_in_round: int | None = self._handle_missing(draft, "pickInRound")
        self.pick_overall: int | None = self._handle_missing(draft, "overallPick")

    def _handle_missing(self, data: dict | None, type: str) -> Any:
        if not isinstance(data, dict):
            return None
        return data.get(type)