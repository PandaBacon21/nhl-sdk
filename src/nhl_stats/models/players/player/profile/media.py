"""
MEDIA DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Media:
    slug: str | None
    headshot: str | None
    hero_image: str | None 

    @classmethod
    def from_dict(cls, data: dict) -> Media:
        return cls(
            slug = data.get("playerSlug"),
            headshot = data.get("headshot"),
            hero_image = data.get("heroImage"),
            )
