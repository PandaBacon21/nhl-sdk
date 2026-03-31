"""
PLAYOFF BRACKET MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class BracketTeam:
    id: int | None
    abbrev: str | None
    name: LocalizedString
    common_name: LocalizedString
    place_name_with_preposition: LocalizedString
    logo: str | None
    dark_logo: str | None

    @classmethod
    def from_dict(cls, data: dict) -> BracketTeam:
        return cls(
            id = data.get("id"),
            abbrev = data.get("abbrev"),
            name = LocalizedString(data.get("name")),
            common_name = LocalizedString(data.get("commonName")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
            logo = data.get("logo"),
            dark_logo = data.get("darkLogo"),
        )


@dataclass(slots=True, frozen=True)
class BracketSeries:
    series_url: str | None
    series_logo: str | None
    series_logo_fr: str | None
    series_title: str | None
    series_abbrev: str | None
    series_letter: str | None
    conference_abbrev: str | None
    conference_name: str | None
    playoff_round: int | None
    top_seed_rank: int | None
    top_seed_rank_abbrev: str | None
    top_seed_wins: int | None
    bottom_seed_rank: int | None
    bottom_seed_rank_abbrev: str | None
    bottom_seed_wins: int | None
    winning_team_id: int | None
    losing_team_id: int | None
    top_seed_team: BracketTeam
    bottom_seed_team: BracketTeam

    @classmethod
    def from_dict(cls, data: dict) -> BracketSeries:
        return cls(
            series_url = data.get("seriesUrl"),
            series_logo = data.get("seriesLogo"),
            series_logo_fr = data.get("seriesLogoFr"),
            series_title = data.get("seriesTitle"),
            series_abbrev = data.get("seriesAbbrev"),
            series_letter = data.get("seriesLetter"),
            conference_abbrev = data.get("conferenceAbbrev"),
            conference_name = data.get("conferenceName"),
            playoff_round = data.get("playoffRound"),
            top_seed_rank = data.get("topSeedRank"),
            top_seed_rank_abbrev = data.get("topSeedRankAbbrev"),
            top_seed_wins = data.get("topSeedWins"),
            bottom_seed_rank = data.get("bottomSeedRank"),
            bottom_seed_rank_abbrev = data.get("bottomSeedRankAbbrev"),
            bottom_seed_wins = data.get("bottomSeedWins"),
            winning_team_id = data.get("winningTeamId"),
            losing_team_id = data.get("losingTeamId"),
            top_seed_team = BracketTeam.from_dict(data.get("topSeedTeam") or {}),
            bottom_seed_team = BracketTeam.from_dict(data.get("bottomSeedTeam") or {}),
        )


@dataclass(slots=True, frozen=True)
class PlayoffBracketResult:
    bracket_logo: str | None
    bracket_logo_fr: str | None
    series: list[BracketSeries]

    @classmethod
    def from_dict(cls, data: dict) -> PlayoffBracketResult:
        return cls(
            bracket_logo = data.get("bracketLogo"),
            bracket_logo_fr = data.get("bracketLogoFr"),
            series = [BracketSeries.from_dict(s) for s in data.get("series") or []],
        )
