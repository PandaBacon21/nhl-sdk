"""
Tests for partner odds models: PartnerOddsResult
"""
from src.models.games.odds.odds_result import PartnerOddsResult


def test_odds_result_fields() -> None:
    r = PartnerOddsResult.from_dict({
        "currentOddsDate": "2026-03-30",
        "lastUpdatedUTC": "2026-03-31T03:21:21.070514777Z",
        "games": [],
    })
    assert r.current_odds_date == "2026-03-30"
    assert r.last_updated_utc == "2026-03-31T03:21:21.070514777Z"
    assert r.games == []


def test_odds_result_with_games() -> None:
    r = PartnerOddsResult.from_dict({
        "currentOddsDate": "2026-03-30",
        "lastUpdatedUTC": "2026-03-31T03:21:21Z",
        "games": [{"gameId": 123}],
    })
    assert len(r.games) == 1
    assert r.games[0]["gameId"] == 123


def test_odds_result_empty() -> None:
    r = PartnerOddsResult.from_dict({})
    assert r.current_odds_date is None
    assert r.last_updated_utc is None
    assert r.games == []
