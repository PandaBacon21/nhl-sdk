"""
POSTAL LOOKUP RESULT DATA CLASS
"""
from __future__ import annotations
from dataclasses import dataclass

from ...core.utilities import LocalizedString


@dataclass(slots=True, frozen=True)
class PostalLookupResult:
    postal_code: str | None
    country: str | None
    state_province: str | None
    city: str | None
    county: str | None
    network_type: str | None
    team_name: LocalizedString

    @classmethod
    def from_dict(cls, data: dict) -> PostalLookupResult:
        return cls(
            postal_code = data.get("postalCode"),
            country = data.get("country"),
            state_province = data.get("stateProvince"),
            city = data.get("city"),
            county = data.get("county"),
            network_type = data.get("networkType"),
            team_name = LocalizedString(data.get("teamName")),
        )
