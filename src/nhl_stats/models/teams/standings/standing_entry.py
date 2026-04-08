"""
STANDING ENTRY MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class StandingsTeam:
    """Team identity fields from a standings entry."""
    name: LocalizedString
    common_name: LocalizedString
    abbrev: str | None
    logo: str | None
    place_name: LocalizedString

    @classmethod
    def from_dict(cls, data: dict) -> StandingsTeam:
        return cls(
            name = LocalizedString(data.get("teamName")),
            common_name = LocalizedString(data.get("teamCommonName")),
            abbrev = (data.get("teamAbbrev") or {}).get("default"),
            logo = data.get("teamLogo"),
            place_name = LocalizedString(data.get("placeName")),
        )


@dataclass(slots=True, frozen=True)
class SplitRecord:
    """Win/loss record for a split (home, road, or last 10 games)."""
    games_played: int | None
    wins: int | None
    losses: int | None
    ot_losses: int | None
    points: int | None
    regulation_wins: int | None
    regulation_plus_ot_wins: int | None
    goals_for: int | None
    goals_against: int | None
    goal_differential: int | None
    ties: int | None

    @classmethod
    def home(cls, data: dict) -> SplitRecord:
        return cls(
            games_played = data.get("homeGamesPlayed"),
            wins = data.get("homeWins"),
            losses = data.get("homeLosses"),
            ot_losses = data.get("homeOtLosses"),
            points = data.get("homePoints"),
            regulation_wins = data.get("homeRegulationWins"),
            regulation_plus_ot_wins = data.get("homeRegulationPlusOtWins"),
            goals_for = data.get("homeGoalsFor"),
            goals_against = data.get("homeGoalsAgainst"),
            goal_differential = data.get("homeGoalDifferential"),
            ties = data.get("homeTies"),
        )

    @classmethod
    def road(cls, data: dict) -> SplitRecord:
        return cls(
            games_played = data.get("roadGamesPlayed"),
            wins = data.get("roadWins"),
            losses = data.get("roadLosses"),
            ot_losses = data.get("roadOtLosses"),
            points = data.get("roadPoints"),
            regulation_wins = data.get("roadRegulationWins"),
            regulation_plus_ot_wins = data.get("roadRegulationPlusOtWins"),
            goals_for = data.get("roadGoalsFor"),
            goals_against = data.get("roadGoalsAgainst"),
            goal_differential = data.get("roadGoalDifferential"),
            ties = data.get("roadTies"),
        )

    @classmethod
    def l10(cls, data: dict) -> SplitRecord:
        return cls(
            games_played = data.get("l10GamesPlayed"),
            wins = data.get("l10Wins"),
            losses = data.get("l10Losses"),
            ot_losses = data.get("l10OtLosses"),
            points = data.get("l10Points"),
            regulation_wins = data.get("l10RegulationWins"),
            regulation_plus_ot_wins = data.get("l10RegulationPlusOtWins"),
            goals_for = data.get("l10GoalsFor"),
            goals_against = data.get("l10GoalsAgainst"),
            goal_differential = data.get("l10GoalDifferential"),
            ties = data.get("l10Ties"),
        )


@dataclass(slots=True, frozen=True)
class StandingsRecord:
    """Full-season record including percentages and shootout splits."""
    games_played: int | None
    wins: int | None
    losses: int | None
    ot_losses: int | None
    points: int | None
    point_pctg: float | None
    regulation_wins: int | None
    regulation_win_pctg: float | None
    regulation_plus_ot_wins: int | None
    regulation_plus_ot_win_pctg: float | None
    win_pctg: float | None
    ties: int | None
    shootout_wins: int | None
    shootout_losses: int | None
    goals_for: int | None
    goals_against: int | None
    goal_differential: int | None
    goal_differential_pctg: float | None
    goals_for_pctg: float | None

    @classmethod
    def from_dict(cls, data: dict) -> StandingsRecord:
        return cls(
            games_played = data.get("gamesPlayed"),
            wins = data.get("wins"),
            losses = data.get("losses"),
            ot_losses = data.get("otLosses"),
            points = data.get("points"),
            point_pctg = data.get("pointPctg"),
            regulation_wins = data.get("regulationWins"),
            regulation_win_pctg = data.get("regulationWinPctg"),
            regulation_plus_ot_wins = data.get("regulationPlusOtWins"),
            regulation_plus_ot_win_pctg = data.get("regulationPlusOtWinPctg"),
            win_pctg = data.get("winPctg"),
            ties = data.get("ties"),
            shootout_wins = data.get("shootoutWins"),
            shootout_losses = data.get("shootoutLosses"),
            goals_for = data.get("goalFor"),
            goals_against = data.get("goalAgainst"),
            goal_differential = data.get("goalDifferential"),
            goal_differential_pctg = data.get("goalDifferentialPctg"),
            goals_for_pctg = data.get("goalsForPctg"),
        )


@dataclass(slots=True, frozen=True)
class StandingsSequences:
    """Rank sequences within league, conference, and division."""
    league: int | None
    league_home: int | None
    league_road: int | None
    league_l10: int | None
    conference: int | None
    conference_home: int | None
    conference_road: int | None
    conference_l10: int | None
    division: int | None
    division_home: int | None
    division_road: int | None
    division_l10: int | None
    wildcard: int | None
    waivers: int | None

    @classmethod
    def from_dict(cls, data: dict) -> StandingsSequences:
        return cls(
            league = data.get("leagueSequence"),
            league_home = data.get("leagueHomeSequence"),
            league_road = data.get("leagueRoadSequence"),
            league_l10 = data.get("leagueL10Sequence"),
            conference = data.get("conferenceSequence"),
            conference_home = data.get("conferenceHomeSequence"),
            conference_road = data.get("conferenceRoadSequence"),
            conference_l10 = data.get("conferenceL10Sequence"),
            division = data.get("divisionSequence"),
            division_home = data.get("divisionHomeSequence"),
            division_road = data.get("divisionRoadSequence"),
            division_l10 = data.get("divisionL10Sequence"),
            wildcard = data.get("wildcardSequence"),
            waivers = data.get("waiversSequence"),
        )


@dataclass(slots=True, frozen=True)
class StandingEntry:
    """A single team's full standing for the queried date/season."""
    team: StandingsTeam
    season_id: int | None
    date: str | None
    game_type_id: int | None
    clinch_indicator: str | None
    conference_abbrev: str | None
    conference_name: str | None
    division_abbrev: str | None
    division_name: str | None
    record: StandingsRecord
    home: SplitRecord
    road: SplitRecord
    l10: SplitRecord
    sequences: StandingsSequences
    streak_code: str | None
    streak_count: int | None

    @classmethod
    def from_dict(cls, data: dict) -> StandingEntry:
        return cls(
            team = StandingsTeam.from_dict(data),
            season_id = data.get("seasonId"),
            date = data.get("date"),
            game_type_id = data.get("gameTypeId"),
            clinch_indicator = data.get("clinchIndicator"),
            conference_abbrev = data.get("conferenceAbbrev"),
            conference_name = data.get("conferenceName"),
            division_abbrev = data.get("divisionAbbrev"),
            division_name = data.get("divisionName"),
            record = StandingsRecord.from_dict(data),
            home = SplitRecord.home(data),
            road = SplitRecord.road(data),
            l10 = SplitRecord.l10(data),
            sequences = StandingsSequences.from_dict(data),
            streak_code = data.get("streakCode"),
            streak_count = data.get("streakCount"),
        )
