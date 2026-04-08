"""
BADGE DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

from .....core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class Badge:
    logo: LocalizedString
    title: LocalizedString

    @classmethod
    def from_dict(cls, data: dict) -> Badge:
        return cls(
            logo = LocalizedString(data.get("logoUrl")),
            title = LocalizedString(data.get("title")),
        )
