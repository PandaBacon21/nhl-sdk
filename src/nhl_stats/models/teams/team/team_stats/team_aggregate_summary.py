"""
TEAM AGGREGATE SUMMARY DATA CLASS
Sourced from api.nhle.com/stats/rest — team-level season aggregate stats.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class TeamAggregateSummary:
    season_id: int | None
    team_id: int | None
    team_full_name: str | None
    games_played: int | None
    wins: int | None
    losses: int | None
    ot_losses: int | None
    ties: int | None
    points: int | None
    point_pct: float | None
    regulation_and_ot_wins: int | None
    wins_in_regulation: int | None
    wins_in_shootout: int | None
    goals_for: int | None
    goals_against: int | None
    goals_for_per_game: float | None
    goals_against_per_game: float | None
    shots_for_per_game: float | None
    shots_against_per_game: float | None
    power_play_pct: float | None
    power_play_net_pct: float | None
    penalty_kill_pct: float | None
    penalty_kill_net_pct: float | None
    faceoff_win_pct: float | None
    team_shutouts: int | None

    @classmethod
    def from_dict(cls, data: dict) -> TeamAggregateSummary:
        return cls(
            season_id = data.get("seasonId"),
            team_id = data.get("teamId"),
            team_full_name = data.get("teamFullName"),
            games_played = data.get("gamesPlayed"),
            wins = data.get("wins"),
            losses = data.get("losses"),
            ot_losses = data.get("otLosses"),
            ties = data.get("ties"),
            points = data.get("points"),
            point_pct = data.get("pointPct"),
            regulation_and_ot_wins = data.get("regulationAndOtWins"),
            wins_in_regulation = data.get("winsInRegulation"),
            wins_in_shootout = data.get("winsInShootout"),
            goals_for = data.get("goalsFor"),
            goals_against = data.get("goalsAgainst"),
            goals_for_per_game = data.get("goalsForPerGame"),
            goals_against_per_game = data.get("goalsAgainstPerGame"),
            shots_for_per_game = data.get("shotsForPerGame"),
            shots_against_per_game = data.get("shotsAgainstPerGame"),
            power_play_pct = data.get("powerPlayPct"),
            power_play_net_pct = data.get("powerPlayNetPct"),
            penalty_kill_pct = data.get("penaltyKillPct"),
            penalty_kill_net_pct = data.get("penaltyKillNetPct"),
            faceoff_win_pct = data.get("faceoffWinPct"),
            team_shutouts = data.get("teamShutouts"),
        )
