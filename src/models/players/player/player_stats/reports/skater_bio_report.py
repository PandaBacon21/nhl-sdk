"""
SKATER BIO REPORT DATA CLASS
Sourced from api.nhle.com/stats/rest — /{lang}/skater/bios
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkaterBioReport:
    player_id: int | None
    skater_full_name: str | None
    last_name: str | None
    games_played: int | None
    goals: int | None
    assists: int | None
    points: int | None
    position_code: str | None
    shoots_catches: str | None
    birth_city: str | None
    birth_country_code: str | None
    birth_date: str | None
    birth_state_province_code: str | None
    current_team_abbrev: str | None
    current_team_name: str | None
    draft_overall: int | None
    draft_round: int | None
    draft_year: int | None
    first_season_for_game_type: int | None
    height: int | None
    is_in_hall_of_fame_yn: str | None
    nationality_code: str | None
    weight: int | None

    @classmethod
    def from_dict(cls, data: dict) -> SkaterBioReport:
        return cls(
            player_id = data.get("playerId"),
            skater_full_name = data.get("skaterFullName"),
            last_name = data.get("lastName"),
            games_played = data.get("gamesPlayed"),
            goals = data.get("goals"),
            assists = data.get("assists"),
            points = data.get("points"),
            position_code = data.get("positionCode"),
            shoots_catches = data.get("shootsCatches"),
            birth_city = data.get("birthCity"),
            birth_country_code = data.get("birthCountryCode"),
            birth_date = data.get("birthDate"),
            birth_state_province_code = data.get("birthStateProvinceCode"),
            current_team_abbrev = data.get("currentTeamAbbrev"),
            current_team_name = data.get("currentTeamName"),
            draft_overall = data.get("draftOverall"),
            draft_round = data.get("draftRound"),
            draft_year = data.get("draftYear"),
            first_season_for_game_type = data.get("firstSeasonForGameType"),
            height = data.get("height"),
            is_in_hall_of_fame_yn = data.get("isInHallOfFameYn"),
            nationality_code = data.get("nationalityCode"),
            weight = data.get("weight"),
        )
