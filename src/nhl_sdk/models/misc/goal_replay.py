from __future__ import annotations
from dataclasses import dataclass

from ...core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class GoalReplayTeam:
    id: int | None
    name: LocalizedString
    abbrev: str | None
    place_name: LocalizedString
    place_name_with_preposition: LocalizedString
    logo: str | None
    dark_logo: str | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalReplayTeam:
        return cls(
            id = data.get("id"),
            name = LocalizedString(data.get("name")),
            abbrev = data.get("abbrev"),
            place_name = LocalizedString(data.get("placeName")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
            logo = data.get("logo"),
            dark_logo = data.get("darkLogo"),
        )


@dataclass(slots=True, frozen=True)
class GoalReplayPeriod:
    number: int | None
    period_type: str | None
    max_regulation_periods: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalReplayPeriod:
        return cls(
            number = data.get("number"),
            period_type = data.get("periodType"),
            max_regulation_periods = data.get("maxRegulationPeriods"),
        )


@dataclass(slots=True, frozen=True)
class GoalReplayAssist:
    player_id: int | None
    first_name: LocalizedString
    last_name: LocalizedString
    name: LocalizedString
    assists_to_date: int | None
    sweater_number: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalReplayAssist:
        return cls(
            player_id = data.get("playerId"),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            name = LocalizedString(data.get("name")),
            assists_to_date = data.get("assistsToDate"),
            sweater_number = data.get("sweaterNumber"),
        )


@dataclass(slots=True, frozen=True)
class GoalReplayGoal:
    period_descriptor: GoalReplayPeriod | None
    situation_code: str | None
    strength: str | None
    player_id: int | None
    first_name: LocalizedString
    last_name: LocalizedString
    name: LocalizedString
    team_abbrev: LocalizedString
    headshot: str | None
    highlight_clip: int | None
    highlight_clip_fr: int | None
    logo_url: str | None
    highlight_clip_sharing_url: str | None
    highlight_clip_sharing_url_fr: str | None
    goals_to_date: int | None
    sweater_number: int | None
    away_score: int | None
    home_score: int | None
    leading_team_abbrev: LocalizedString
    time_in_period: str | None
    shot_type: str | None
    goal_modifier: str | None
    assists: list[GoalReplayAssist]
    ppt_replay_url: str | None
    home_team_defending_side: str | None
    is_home: bool | None
    event_id: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalReplayGoal:
        raw_pd = data.get("periodDescriptor")
        return cls(
            period_descriptor = GoalReplayPeriod.from_dict(raw_pd) if raw_pd else None,
            situation_code = data.get("situationCode"),
            strength = data.get("strength"),
            player_id = data.get("playerId"),
            first_name = LocalizedString(data.get("firstName")),
            last_name = LocalizedString(data.get("lastName")),
            name = LocalizedString(data.get("name")),
            team_abbrev = LocalizedString(data.get("teamAbbrev")),
            headshot = data.get("headshot"),
            highlight_clip = data.get("highlightClip"),
            highlight_clip_fr = data.get("highlightClipFr"),
            logo_url = data.get("logoUrl"),
            highlight_clip_sharing_url = data.get("highlightClipSharingUrl"),
            highlight_clip_sharing_url_fr = data.get("highlightClipSharingUrlFr"),
            goals_to_date = data.get("goalsToDate"),
            sweater_number = data.get("sweaterNumber"),
            away_score = data.get("awayScore"),
            home_score = data.get("homeScore"),
            leading_team_abbrev = LocalizedString(data.get("leadingTeamAbbrev")),
            time_in_period = data.get("timeInPeriod"),
            shot_type = data.get("shotType"),
            goal_modifier = data.get("goalModifier"),
            assists = [GoalReplayAssist.from_dict(a) for a in (data.get("assists") or [])],
            ppt_replay_url = data.get("pptReplayUrl"),
            home_team_defending_side = data.get("homeTeamDefendingSide"),
            is_home = data.get("isHome"),
            event_id = data.get("eventId"),
        )


@dataclass(slots=True, frozen=True)
class PlayReplayResult:
    id: int | None
    game_date: str | None
    away_team: GoalReplayTeam | None
    home_team: GoalReplayTeam | None
    game_state: str | None
    game_type: int | None

    @classmethod
    def from_dict(cls, data: dict) -> PlayReplayResult:
        raw_away = data.get("awayTeam")
        raw_home = data.get("homeTeam")
        return cls(
            id = data.get("id"),
            game_date = data.get("gameDate"),
            away_team = GoalReplayTeam.from_dict(raw_away) if raw_away else None,
            home_team = GoalReplayTeam.from_dict(raw_home) if raw_home else None,
            game_state = data.get("gameState"),
            game_type = data.get("gameType"),
        )


@dataclass(slots=True, frozen=True)
class GoalReplayResult:
    id: int | None
    game_date: str | None
    away_team: GoalReplayTeam | None
    home_team: GoalReplayTeam | None
    game_state: str | None
    game_type: int | None
    goal: GoalReplayGoal | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalReplayResult:
        raw_away = data.get("awayTeam")
        raw_home = data.get("homeTeam")
        raw_goal = data.get("goal")
        return cls(
            id = data.get("id"),
            game_date = data.get("gameDate"),
            away_team = GoalReplayTeam.from_dict(raw_away) if raw_away else None,
            home_team = GoalReplayTeam.from_dict(raw_home) if raw_home else None,
            game_state = data.get("gameState"),
            game_type = data.get("gameType"),
            goal = GoalReplayGoal.from_dict(raw_goal) if raw_goal else None,
        )
