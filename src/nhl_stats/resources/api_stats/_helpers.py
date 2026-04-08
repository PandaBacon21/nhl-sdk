"""
SHARED HELPERS FOR API_STATS RESOURCE LAYER
"""


def _build_stats_params(
    is_aggregate: bool | None = None,
    is_game: bool | None = None,
    fact_cayenne_exp: str | None = None,
    include: str | None = None,
    exclude: str | None = None,
    cayenne_exp: str | None = None,
    sort: str | None = None,
    dir: str | None = None,
    start: int | None = None,
    limit: int | None = None,
) -> dict:
    params: dict = {}
    if is_aggregate is not None:
        params["isAggregate"] = is_aggregate
    if is_game is not None:
        params["isGame"] = is_game
    if fact_cayenne_exp is not None:
        params["factCayenneExp"] = fact_cayenne_exp
    if include is not None:
        params["include"] = include
    if exclude is not None:
        params["exclude"] = exclude
    if cayenne_exp is not None:
        params["cayenneExp"] = cayenne_exp
    if sort is not None:
        params["sort"] = sort
    if dir is not None:
        params["dir"] = dir
    if start is not None:
        params["start"] = start
    if limit is not None:
        params["limit"] = limit
    return params
