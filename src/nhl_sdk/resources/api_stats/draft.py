"""
METHODS FOR RETRIEVING DRAFT DATA FROM API.NHLE.COM/STATS/REST
"""
from __future__ import annotations
from typing import TYPE_CHECKING

from ...core.config import LANG
from ...core.transport import APIResponse
from ._helpers import _build_stats_params

if TYPE_CHECKING:
    from ...core.transport import APICallStats


class CallNhlStatsDraft:
    def __init__(self, http: APICallStats):
        self._http = http

    def get_draft(
        self,
        *,
        include: str | None = None,
        exclude: str | None = None,
        cayenne_exp: str | None = None,
        sort: str | None = None,
        dir: str | None = None,
        start: int | None = None,
        limit: int | None = None,
    ) -> APIResponse:
        """
        Retrieve draft information.
        """
        params = _build_stats_params(
            include=include, exclude=exclude, cayenne_exp=cayenne_exp,
            sort=sort, dir=dir, start=start, limit=limit,
        )
        endpoint = f"/{LANG}/draft"
        return self._http.get(endpoint=endpoint, params=params or None)
