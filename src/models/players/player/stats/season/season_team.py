"""
SEASON STAT TEAM
"""
from __future__ import annotations
from dataclasses import dataclass

from ......core.utilities import LocalizedString

@dataclass(slots=True, frozen=True)
class SeasonTeam:
    """
    Team information for a player in a given season.
    """
    common_name: LocalizedString
    name: LocalizedString

    @classmethod
    def from_dict(cls, data: dict) -> SeasonTeam:
        return cls(
            common_name=LocalizedString(data.get("teamCommonName")),
            name=LocalizedString(data.get("teamName")),
        )

    def to_dict(self) -> dict:
        return {
            "common_name": str(self.common_name),
            "name": str(self.name),
        }