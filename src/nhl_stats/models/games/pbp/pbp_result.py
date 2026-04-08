"""
PLAY-BY-PLAY MODELS
"""
from __future__ import annotations
from dataclasses import dataclass

from ....core.utilities import LocalizedString
from ...teams.team.team_schedule.team_schedule_result import (
    ScheduleTvBroadcast,
    SchedulePeriodDescriptor,
    ScheduleGameOutcome,
)
from ..scores.daily_score import GameClock


@dataclass(slots=True, frozen=True)
class PbpTeam:
    id: int | None
    common_name: LocalizedString
    abbrev: str | None
    score: int | None
    sog: int | None
    logo: str | None
    dark_logo: str | None
    place_name: LocalizedString
    place_name_with_preposition: LocalizedString

    @classmethod
    def from_dict(cls, data: dict) -> PbpTeam:
        return cls(
            id = data.get("id"),
            common_name = LocalizedString(data.get("commonName")),
            abbrev = data.get("abbrev"),
            score = data.get("score"),
            sog = data.get("sog"),
            logo = data.get("logo"),
            dark_logo = data.get("darkLogo"),
            place_name = LocalizedString(data.get("placeName")),
            place_name_with_preposition = LocalizedString(data.get("placeNameWithPreposition")),
        )


@dataclass(slots=True, frozen=True)
class PlayDetails:
    event_owner_team_id: int | None
    # faceoff
    losing_player_id: int | None
    winning_player_id: int | None
    # coordinates / zone
    x_coord: int | None
    y_coord: int | None
    zone_code: str | None
    # stoppages, missed shots
    reason: str | None
    secondary_reason: str | None
    # shots
    shot_type: str | None
    shooting_player_id: int | None
    goalie_in_net_id: int | None
    away_sog: int | None
    home_sog: int | None
    # blocked shot
    blocking_player_id: int | None
    # hit
    hitting_player_id: int | None
    hittee_player_id: int | None
    # giveaway / takeaway
    player_id: int | None
    # goal
    scoring_player_id: int | None
    scoring_player_total: int | None
    assist1_player_id: int | None
    assist1_player_total: int | None
    assist2_player_id: int | None
    assist2_player_total: int | None
    away_score: int | None
    home_score: int | None
    highlight_clip_sharing_url: str | None
    highlight_clip_sharing_url_fr: str | None
    highlight_clip: int | None
    highlight_clip_fr: int | None
    discrete_clip: int | None
    discrete_clip_fr: int | None
    # penalty
    penalty_type_code: str | None
    penalty_desc_key: str | None
    duration: int | None
    committed_by_player_id: int | None
    drawn_by_player_id: int | None

    @classmethod
    def from_dict(cls, data: dict) -> PlayDetails:
        return cls(
            event_owner_team_id = data.get("eventOwnerTeamId"),
            losing_player_id = data.get("losingPlayerId"),
            winning_player_id = data.get("winningPlayerId"),
            x_coord = data.get("xCoord"),
            y_coord = data.get("yCoord"),
            zone_code = data.get("zoneCode"),
            reason = data.get("reason"),
            secondary_reason = data.get("secondaryReason"),
            shot_type = data.get("shotType"),
            shooting_player_id = data.get("shootingPlayerId"),
            goalie_in_net_id = data.get("goalieInNetId"),
            away_sog = data.get("awaySOG"),
            home_sog = data.get("homeSOG"),
            blocking_player_id = data.get("blockingPlayerId"),
            hitting_player_id = data.get("hittingPlayerId"),
            hittee_player_id = data.get("hitteePlayerId"),
            player_id = data.get("playerId"),
            scoring_player_id = data.get("scoringPlayerId"),
            scoring_player_total = data.get("scoringPlayerTotal"),
            assist1_player_id = data.get("assist1PlayerId"),
            assist1_player_total = data.get("assist1PlayerTotal"),
            assist2_player_id = data.get("assist2PlayerId"),
            assist2_player_total = data.get("assist2PlayerTotal"),
            away_score = data.get("awayScore"),
            home_score = data.get("homeScore"),
            highlight_clip_sharing_url = data.get("highlightClipSharingUrl"),
            highlight_clip_sharing_url_fr = data.get("highlightClipSharingUrlFr"),
            highlight_clip = data.get("highlightClip"),
            highlight_clip_fr = data.get("highlightClipFr"),
            discrete_clip = data.get("discreteClip"),
            discrete_clip_fr = data.get("discreteClipFr"),
            penalty_type_code = data.get("typeCode"),
            penalty_desc_key = data.get("descKey"),
            duration = data.get("duration"),
            committed_by_player_id = data.get("committedByPlayerId"),
            drawn_by_player_id = data.get("drawnByPlayerId"),
        )


@dataclass(slots=True, frozen=True)
class Play:
    event_id: int | None
    period_descriptor: SchedulePeriodDescriptor | None
    time_in_period: str | None
    time_remaining: str | None
    situation_code: str | None
    home_team_defending_side: str | None
    type_code: int | None
    type_desc_key: str | None
    sort_order: int | None
    details: PlayDetails | None
    ppt_replay_url: str | None

    @classmethod
    def from_dict(cls, data: dict) -> Play:
        pd = data.get("periodDescriptor")
        details = data.get("details")
        return cls(
            event_id = data.get("eventId"),
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            time_in_period = data.get("timeInPeriod"),
            time_remaining = data.get("timeRemaining"),
            situation_code = data.get("situationCode"),
            home_team_defending_side = data.get("homeTeamDefendingSide"),
            type_code = data.get("typeCode"),
            type_desc_key = data.get("typeDescKey"),
            sort_order = data.get("sortOrder"),
            details = PlayDetails.from_dict(details) if details else None,
            ppt_replay_url = data.get("pptReplayUrl"),
        )


@dataclass(slots=True, frozen=True)
class PlayByPlayResult:
    id: int | None
    season: int | None
    game_type: int | None
    limited_scoring: bool | None
    game_date: str | None
    venue: LocalizedString
    venue_location: LocalizedString
    start_time_utc: str | None
    eastern_utc_offset: str | None
    venue_utc_offset: str | None
    tv_broadcasts: list[ScheduleTvBroadcast]
    game_state: str | None
    game_schedule_state: str | None
    period_descriptor: SchedulePeriodDescriptor | None
    away_team: PbpTeam
    home_team: PbpTeam
    shootout_in_use: bool | None
    ot_in_use: bool | None
    clock: GameClock | None
    display_period: int | None
    max_periods: int | None
    game_outcome: ScheduleGameOutcome | None
    plays: list[Play]

    @classmethod
    def from_dict(cls, data: dict) -> PlayByPlayResult:
        pd = data.get("periodDescriptor")
        clock = data.get("clock")
        go = data.get("gameOutcome")
        return cls(
            id = data.get("id"),
            season = data.get("season"),
            game_type = data.get("gameType"),
            limited_scoring = data.get("limitedScoring"),
            game_date = data.get("gameDate"),
            venue = LocalizedString(data.get("venue")),
            venue_location = LocalizedString(data.get("venueLocation")),
            start_time_utc = data.get("startTimeUTC"),
            eastern_utc_offset = data.get("easternUTCOffset"),
            venue_utc_offset = data.get("venueUTCOffset"),
            tv_broadcasts = [ScheduleTvBroadcast.from_dict(b) for b in data.get("tvBroadcasts") or []],
            game_state = data.get("gameState"),
            game_schedule_state = data.get("gameScheduleState"),
            period_descriptor = SchedulePeriodDescriptor.from_dict(pd) if pd else None,
            away_team = PbpTeam.from_dict(data.get("awayTeam") or {}),
            home_team = PbpTeam.from_dict(data.get("homeTeam") or {}),
            shootout_in_use = data.get("shootoutInUse"),
            ot_in_use = data.get("otInUse"),
            clock = GameClock.from_dict(clock) if clock else None,
            display_period = data.get("displayPeriod"),
            max_periods = data.get("maxPeriods"),
            game_outcome = ScheduleGameOutcome.from_dict(go) if go else None,
            plays = [Play.from_dict(p) for p in data.get("plays") or []],
        )
