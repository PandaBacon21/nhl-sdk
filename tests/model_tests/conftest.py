import pytest
from nhl_stats.core.cache import init_cache
from nhl_stats.core.cache.mem_cache import MemCache


@pytest.fixture(autouse=True, scope="session")
def initialize_cache():
    init_cache(MemCache())
