from __future__ import annotations
from dataclasses import dataclass

from ...core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class PlayoffSeriesTeam:
    name: LocalizedString
    common_name: LocalizedString
    tricode: str | None
    team_slug: str | None

    @classmethod
    def from_dict(cls, data: dict) -> PlayoffSeriesTeam:
        return cls(
            name = LocalizedString(data.get("name")),
            common_name = LocalizedString(data.get("commonName")),
            tricode = data.get("tricode"),
            team_slug = data.get("teamSlug"),
        )


@dataclass(slots=True, frozen=True)
class PlayoffSeriesTeams:
    top_seed: PlayoffSeriesTeam | None
    bottom_seed: PlayoffSeriesTeam | None

    @classmethod
    def from_dict(cls, data: dict) -> PlayoffSeriesTeams:
        top = data.get("topSeed")
        bottom = data.get("bottomSeed")
        return cls(
            top_seed = PlayoffSeriesTeam.from_dict(top) if top else None,
            bottom_seed = PlayoffSeriesTeam.from_dict(bottom) if bottom else None,
        )


@dataclass(slots=True, frozen=True)
class PlayoffSeriesMetaResult:
    series_title: str | None
    teams: PlayoffSeriesTeams | None

    @classmethod
    def from_dict(cls, data: dict) -> PlayoffSeriesMetaResult:
        raw_teams = data.get("teams")
        return cls(
            series_title = data.get("seriesTitle"),
            teams = PlayoffSeriesTeams.from_dict(raw_teams) if raw_teams else None,
        )
