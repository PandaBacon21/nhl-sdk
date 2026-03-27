import pytest
from src.core.cache import init_cache
from src.core.cache.mem_cache import MemCache


@pytest.fixture(autouse=True, scope="session")
def initialize_cache():
    init_cache(MemCache())
