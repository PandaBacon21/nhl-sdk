from __future__ import annotations
from dataclasses import dataclass

from ...core.utilities import LocalizedString
from .goal_replay import GoalReplayPeriod


@dataclass(slots=True, frozen=True)
class RailGameOutcome:
    last_period_type: str | None
    ot_periods: int | None

    @classmethod
    def from_dict(cls, data: dict) -> RailGameOutcome:
        return cls(
            last_period_type = data.get("lastPeriodType"),
            ot_periods = data.get("otPeriods"),
        )


@dataclass(slots=True, frozen=True)
class RailTeamScore:
    id: int | None
    abbrev: str | None
    logo: str | None
    score: int | None

    @classmethod
    def from_dict(cls, data: dict) -> RailTeamScore:
        return cls(
            id = data.get("id"),
            abbrev = data.get("abbrev"),
            logo = data.get("logo"),
            score = data.get("score"),
        )


@dataclass(slots=True, frozen=True)
class RailSeasonSeriesGame:
    id: int | None
    season: int | None
    game_type: int | None
    game_date: str | None
    start_time_utc: str | None
    eastern_utc_offset: str | None
    venue_utc_offset: str | None
    game_state: str | None
    game_schedule_state: str | None
    away_team: RailTeamScore | None
    home_team: RailTeamScore | None
    period_descriptor: GoalReplayPeriod | None
    game_center_link: str | None
    game_outcome: RailGameOutcome | None

    @classmethod
    def from_dict(cls, data: dict) -> RailSeasonSeriesGame:
        raw_pd = data.get("periodDescriptor")
        raw_go = data.get("gameOutcome")
        raw_away = data.get("awayTeam")
        raw_home = data.get("homeTeam")
        return cls(
            id = data.get("id"),
            season = data.get("season"),
            game_type = data.get("gameType"),
            game_date = data.get("gameDate"),
            start_time_utc = data.get("startTimeUTC"),
            eastern_utc_offset = data.get("easternUTCOffset"),
            venue_utc_offset = data.get("venueUTCOffset"),
            game_state = data.get("gameState"),
            game_schedule_state = data.get("gameScheduleState"),
            away_team = RailTeamScore.from_dict(raw_away) if raw_away else None,
            home_team = RailTeamScore.from_dict(raw_home) if raw_home else None,
            period_descriptor = GoalReplayPeriod.from_dict(raw_pd) if raw_pd else None,
            game_center_link = data.get("gameCenterLink"),
            game_outcome = RailGameOutcome.from_dict(raw_go) if raw_go else None,
        )


@dataclass(slots=True, frozen=True)
class RailSeriesWins:
    away_team_wins: int | None
    home_team_wins: int | None

    @classmethod
    def from_dict(cls, data: dict) -> RailSeriesWins:
        return cls(
            away_team_wins = data.get("awayTeamWins"),
            home_team_wins = data.get("homeTeamWins"),
        )


@dataclass(slots=True, frozen=True)
class RailScratch:
    id: int | None
    first_name: LocalizedString
    last_name: LocalizedString

    @classmethod
    def from_dict(cls, data: dict) -> RailScratch:
        return cls(
            id = data.get("id"),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
        )


@dataclass(slots=True, frozen=True)
class RailTeamInfo:
    head_coach: LocalizedString
    scratches: list[RailScratch]

    @classmethod
    def from_dict(cls, data: dict) -> RailTeamInfo:
        return cls(
            head_coach = LocalizedString(data.get("headCoach")),
            scratches = [RailScratch.from_dict(s) for s in (data.get("scratches") or [])],
        )


@dataclass(slots=True, frozen=True)
class RailGameInfo:
    referees: list[LocalizedString]
    linesmen: list[LocalizedString]
    away_team: RailTeamInfo | None
    home_team: RailTeamInfo | None

    @classmethod
    def from_dict(cls, data: dict) -> RailGameInfo:
        raw_away = data.get("awayTeam")
        raw_home = data.get("homeTeam")
        return cls(
            referees = [LocalizedString(r) for r in (data.get("referees") or [])],
            linesmen = [LocalizedString(l) for l in (data.get("linesmen") or [])],
            away_team = RailTeamInfo.from_dict(raw_away) if raw_away else None,
            home_team = RailTeamInfo.from_dict(raw_home) if raw_home else None,
        )


@dataclass(slots=True, frozen=True)
class RailGameVideo:
    three_min_recap: int | None
    three_min_recap_fr: int | None
    condensed_game: int | None
    condensed_game_fr: int | None

    @classmethod
    def from_dict(cls, data: dict) -> RailGameVideo:
        return cls(
            three_min_recap = data.get("threeMinRecap"),
            three_min_recap_fr = data.get("threeMinRecapFr"),
            condensed_game = data.get("condensedGame"),
            condensed_game_fr = data.get("condensedGameFr"),
        )


@dataclass(slots=True, frozen=True)
class RailPeriodScore:
    period_descriptor: GoalReplayPeriod | None
    away: int | None
    home: int | None

    @classmethod
    def from_dict(cls, data: dict) -> RailPeriodScore:
        raw_pd = data.get("periodDescriptor")
        return cls(
            period_descriptor = GoalReplayPeriod.from_dict(raw_pd) if raw_pd else None,
            away = data.get("away"),
            home = data.get("home"),
        )


@dataclass(slots=True, frozen=True)
class RailLinescoreTotals:
    away: int | None
    home: int | None

    @classmethod
    def from_dict(cls, data: dict) -> RailLinescoreTotals:
        return cls(away=data.get("away"), home=data.get("home"))


@dataclass(slots=True, frozen=True)
class RailLinescore:
    by_period: list[RailPeriodScore]
    totals: RailLinescoreTotals | None

    @classmethod
    def from_dict(cls, data: dict) -> RailLinescore:
        raw_totals = data.get("totals")
        return cls(
            by_period = [RailPeriodScore.from_dict(p) for p in (data.get("byPeriod") or [])],
            totals = RailLinescoreTotals.from_dict(raw_totals) if raw_totals else None,
        )


@dataclass(slots=True, frozen=True)
class RailTeamGameStat:
    category: str | None
    away_value: str | float | int | None
    home_value: str | float | int | None

    @classmethod
    def from_dict(cls, data: dict) -> RailTeamGameStat:
        return cls(
            category = data.get("category"),
            away_value = data.get("awayValue"),
            home_value = data.get("homeValue"),
        )


@dataclass(slots=True, frozen=True)
class RailGameReports:
    game_summary: str | None
    event_summary: str | None
    play_by_play: str | None
    faceoff_summary: str | None
    faceoff_comparison: str | None
    rosters: str | None
    shot_summary: str | None
    shift_chart: str | None
    toi_away: str | None
    toi_home: str | None

    @classmethod
    def from_dict(cls, data: dict) -> RailGameReports:
        return cls(
            game_summary = data.get("gameSummary"),
            event_summary = data.get("eventSummary"),
            play_by_play = data.get("playByPlay"),
            faceoff_summary = data.get("faceoffSummary"),
            faceoff_comparison = data.get("faceoffComparison"),
            rosters = data.get("rosters"),
            shot_summary = data.get("shotSummary"),
            shift_chart = data.get("shiftChart"),
            toi_away = data.get("toiAway"),
            toi_home = data.get("toiHome"),
        )
