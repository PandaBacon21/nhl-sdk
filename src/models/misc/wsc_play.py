from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class WscPlayDetails:
    event_owner_team_id: int | None
    # coordinates / zone
    x_coord: int | None
    y_coord: int | None
    zone_code: str | None
    # faceoff
    losing_player_id: int | None
    winning_player_id: int | None
    # shots
    shot_type: str | None
    shooting_player_id: int | None
    goalie_in_net_id: int | None
    away_sog: int | None
    home_sog: int | None
    reason: str | None
    # blocked shot
    blocking_player_id: int | None
    # hit
    hitting_player_id: int | None
    hittee_player_id: int | None
    # giveaway / takeaway
    player_id: int | None
    # goal
    goal_modifier: str | None
    strength: str | None
    strength_code: int | None
    goal_code: int | None
    scoring_player_id: int | None
    scoring_player_total: int | None
    assist1_player_id: int | None
    assist1_player_total: int | None
    assist2_player_id: int | None
    assist2_player_total: int | None
    away_score: int | None
    home_score: int | None
    # penalty
    penalty_type_code: str | None
    penalty_desc_key: str | None
    duration: int | None
    committed_by_player_id: int | None
    drawn_by_player_id: int | None

    @classmethod
    def from_dict(cls, data: dict) -> WscPlayDetails:
        return cls(
            event_owner_team_id = data.get("eventOwnerTeamId"),
            x_coord = data.get("xCoord"),
            y_coord = data.get("yCoord"),
            zone_code = data.get("zoneCode"),
            losing_player_id = data.get("losingPlayerId"),
            winning_player_id = data.get("winningPlayerId"),
            shot_type = data.get("shotType"),
            shooting_player_id = data.get("shootingPlayerId"),
            goalie_in_net_id = data.get("goalieInNetId"),
            away_sog = data.get("awaySOG"),
            home_sog = data.get("homeSOG"),
            reason = data.get("reason"),
            blocking_player_id = data.get("blockingPlayerId"),
            hitting_player_id = data.get("hittingPlayerId"),
            hittee_player_id = data.get("hitteePlayerId"),
            player_id = data.get("playerId"),
            goal_modifier = data.get("goalModifier"),
            strength = data.get("strength"),
            strength_code = data.get("strengthCode"),
            goal_code = data.get("goalCode"),
            scoring_player_id = data.get("scoringPlayerId"),
            scoring_player_total = data.get("scoringPlayerTotal"),
            assist1_player_id = data.get("assist1PlayerId"),
            assist1_player_total = data.get("assist1PlayerTotal"),
            assist2_player_id = data.get("assist2PlayerId"),
            assist2_player_total = data.get("assist2PlayerTotal"),
            away_score = data.get("awayScore"),
            home_score = data.get("homeScore"),
            penalty_type_code = data.get("penaltyTypeCode"),
            penalty_desc_key = data.get("descKey"),
            duration = data.get("duration"),
            committed_by_player_id = data.get("committedByPlayerId"),
            drawn_by_player_id = data.get("drawnByPlayerId"),
        )


@dataclass(slots=True, frozen=True)
class WscPlay:
    id: int | None
    event_id: int | None
    period: int | None
    time_in_period: str | None
    seconds_remaining: int | None
    situation_code: str | None
    type_code: int | None
    type_desc_key: str | None
    home_team_defending_side: str | None
    sort_order: int | None
    utc: str | None
    details: WscPlayDetails

    @classmethod
    def from_dict(cls, data: dict) -> WscPlay:
        return cls(
            id = data.get("id"),
            event_id = data.get("eventId"),
            period = data.get("period"),
            time_in_period = data.get("timeInPeriod"),
            seconds_remaining = data.get("secondsRemaining"),
            situation_code = data.get("situationCode"),
            type_code = data.get("typeCode"),
            type_desc_key = data.get("typeDescKey"),
            home_team_defending_side = data.get("homeTeamDefendingSide"),
            sort_order = data.get("sortOrder"),
            utc = data.get("utc"),
            details = WscPlayDetails.from_dict(data),
        )
