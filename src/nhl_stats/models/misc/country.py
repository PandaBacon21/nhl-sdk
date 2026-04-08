"""
COUNTRY DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

from ...core.utilities import _to_bool


@dataclass(slots=True, frozen=True)
class Country:
    id: str | None
    country_code: str | None
    country3_code: str | None
    country_name: str | None
    nationality_name: str | None
    ioc_code: str | None
    has_player_stats: bool | None
    is_active: bool | None
    image_url: str | None
    thumbnail_url: str | None
    olympic_url: str | None

    @classmethod
    def from_dict(cls, data: dict) -> Country:
        return cls(
            id = data.get("id"),
            country_code = data.get("countryCode"),
            country3_code = data.get("country3Code"),
            country_name = data.get("countryName"),
            nationality_name = data.get("nationalityName"),
            ioc_code = data.get("iocCode"),
            has_player_stats = _to_bool(data.get("hasPlayerStats")),
            is_active = _to_bool(data.get("isActive")),
            image_url = data.get("imageUrl"),
            thumbnail_url = data.get("thumbnailUrl"),
            olympic_url = data.get("olympicUrl"),
        )
