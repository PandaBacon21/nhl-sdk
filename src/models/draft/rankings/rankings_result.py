"""
DRAFT RANKINGS MODELS
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class DraftCategory:
    id: int | None
    name: str | None
    consumer_key: str | None

    @classmethod
    def from_dict(cls, data: dict) -> DraftCategory:
        return cls(
            id = data.get("id"),
            name = data.get("name"),
            consumer_key = data.get("consumerKey"),
        )


@dataclass(slots=True, frozen=True)
class DraftProspect:
    last_name: str | None
    first_name: str | None
    position_code: str | None
    shoots_catches: str | None
    height_in_inches: int | None
    weight_in_pounds: int | None
    last_amateur_club: str | None
    last_amateur_league: str | None
    birth_date: str | None
    birth_city: str | None
    birth_state_province: str | None
    birth_country: str | None
    midterm_rank: int | None
    final_rank: int | None

    @classmethod
    def from_dict(cls, data: dict) -> DraftProspect:
        return cls(
            last_name = data.get("lastName"),
            first_name = data.get("firstName"),
            position_code = data.get("positionCode"),
            shoots_catches = data.get("shootsCatches"),
            height_in_inches = data.get("heightInInches"),
            weight_in_pounds = data.get("weightInPounds"),
            last_amateur_club = data.get("lastAmateurClub"),
            last_amateur_league = data.get("lastAmateurLeague"),
            birth_date = data.get("birthDate"),
            birth_city = data.get("birthCity"),
            birth_state_province = data.get("birthStateProvince"),
            birth_country = data.get("birthCountry"),
            midterm_rank = data.get("midtermRank"),
            final_rank = data.get("finalRank"),
        )


@dataclass(slots=True, frozen=True)
class DraftRankingsResult:
    draft_year: int | None
    category_id: int | None
    category_key: str | None
    draft_years: list[int]
    categories: list[DraftCategory]
    rankings: list[DraftProspect]

    @classmethod
    def from_dict(cls, data: dict) -> DraftRankingsResult:
        return cls(
            draft_year = data.get("draftYear"),
            category_id = data.get("categoryId"),
            category_key = data.get("categoryKey"),
            draft_years = data.get("draftYears") or [],
            categories = [DraftCategory.from_dict(c) for c in data.get("categories") or []],
            rankings = [DraftProspect.from_dict(r) for r in data.get("rankings") or []],
        )
