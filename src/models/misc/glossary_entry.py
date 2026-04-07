from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GlossaryEntry:
    id: int | None
    abbreviation: str | None
    full_name: str | None
    definition: str | None
    language_code: str | None
    first_season_for_stat: int | None
    last_updated: str | None

    @classmethod
    def from_dict(cls, data: dict) -> GlossaryEntry:
        return cls(
            id = data.get("id"),
            abbreviation = data.get("abbreviation"),
            full_name = data.get("fullName"),
            definition = data.get("definition"),
            language_code = data.get("languageCode"),
            first_season_for_stat = data.get("firstSeasonForStat"),
            last_updated = data.get("lastUpdated"),
        )
