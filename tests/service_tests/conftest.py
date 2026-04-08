import pytest
from unittest.mock import MagicMock
from nhl_stats.core.cache import init_cache
from nhl_stats.core.cache.mem_cache import MemCache
from nhl_stats.core.transport import APIResponse


@pytest.fixture(autouse=True)
def fresh_cache():
    init_cache(MemCache())


@pytest.fixture
def mock_client():
    return MagicMock()


def ok(data=None) -> APIResponse:
    return APIResponse(ok=True, data=data if data is not None else {}, status_code=200)
