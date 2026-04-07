"""
GOALIE BIO REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/goalie/bios
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GoalieBioReport:
    player_id: int | None
    goalie_full_name: str | None
    last_name: str | None
    games_played: int | None
    shoots_catches: str | None
    birth_city: str | None
    birth_country_code: str | None
    birth_date: str | None
    birth_state_province_code: str | None
    current_team_abbrev: str | None
    draft_overall: int | None
    draft_round: int | None
    draft_year: int | None
    first_season_for_game_type: int | None
    height: int | None
    is_in_hall_of_fame_yn: str | None
    losses: int | None
    nationality_code: str | None
    ot_losses: int | None
    shutouts: int | None
    ties: int | None
    weight: int | None
    wins: int | None

    @classmethod
    def from_dict(cls, data: dict) -> GoalieBioReport:
        return cls(
            player_id = data.get("playerId"),
            goalie_full_name = data.get("goalieFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            shoots_catches = data.get("shootsCatches"),
            birth_city = data.get("birthCity"),
            birth_country_code = data.get("birthCountryCode"),
            birth_date = data.get("birthDate"),
            birth_state_province_code = data.get("birthStateProvinceCode"),
            current_team_abbrev = data.get("currentTeamAbbrev"),
            draft_overall = data.get("draftOverall"),
            draft_round = data.get("draftRound"),
            draft_year = data.get("draftYear"),
            first_season_for_game_type = data.get("firstSeasonForGameType"),
            height = data.get("height"),
            is_in_hall_of_fame_yn = data.get("isInHallOfFameYn"),
            losses = data.get("losses"),
            nationality_code = data.get("nationalityCode"),
            ot_losses = data.get("otLosses"),
            shutouts = data.get("shutouts"),
            ties = data.get("ties"),
            weight = data.get("weight"),
            wins = data.get("wins"),
        )
