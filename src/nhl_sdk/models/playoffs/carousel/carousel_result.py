"""
PLAYOFF CAROUSEL MODELS
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class PlayoffTeamSeed:
    id: int | None
    abbrev: str | None
    wins: int | None
    logo: str | None
    dark_logo: str | None

    @classmethod
    def from_dict(cls, data: dict) -> PlayoffTeamSeed:
        return cls(
            id = data.get("id"),
            abbrev = data.get("abbrev"),
            wins = data.get("wins"),
            logo = data.get("logo"),
            dark_logo = data.get("darkLogo"),
        )


@dataclass(slots=True, frozen=True)
class PlayoffSeries:
    series_letter: str | None
    round_number: int | None
    series_label: str | None
    series_link: str | None
    top_seed: PlayoffTeamSeed
    bottom_seed: PlayoffTeamSeed
    needed_to_win: int | None
    winning_team_id: int | None
    losing_team_id: int | None

    @classmethod
    def from_dict(cls, data: dict) -> PlayoffSeries:
        return cls(
            series_letter = data.get("seriesLetter"),
            round_number = data.get("roundNumber"),
            series_label = data.get("seriesLabel"),
            series_link = data.get("seriesLink"),
            top_seed = PlayoffTeamSeed.from_dict(data.get("topSeed") or {}),
            bottom_seed = PlayoffTeamSeed.from_dict(data.get("bottomSeed") or {}),
            needed_to_win = data.get("neededToWin"),
            winning_team_id = data.get("winningTeamId"),
            losing_team_id = data.get("losingTeamId"),
        )


@dataclass(slots=True, frozen=True)
class PlayoffRound:
    round_number: int | None
    round_label: str | None
    round_abbrev: str | None
    series: list[PlayoffSeries]

    @classmethod
    def from_dict(cls, data: dict) -> PlayoffRound:
        return cls(
            round_number = data.get("roundNumber"),
            round_label = data.get("roundLabel"),
            round_abbrev = data.get("roundAbbrev"),
            series = [PlayoffSeries.from_dict(s) for s in data.get("series") or []],
        )


@dataclass(slots=True, frozen=True)
class PlayoffCarouselResult:
    season_id: int | None
    current_round: int | None
    rounds: list[PlayoffRound]

    @classmethod
    def from_dict(cls, data: dict) -> PlayoffCarouselResult:
        return cls(
            season_id = data.get("seasonId"),
            current_round = data.get("currentRound"),
            rounds = [PlayoffRound.from_dict(r) for r in data.get("rounds") or []],
        )
