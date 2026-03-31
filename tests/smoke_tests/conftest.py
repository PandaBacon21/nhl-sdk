import time
import pytest
from src.client import NhlClient
from src.core.cache.mem_cache import MemCache


@pytest.fixture(scope="module")
def nhl():
    return NhlClient(log_file="logs/nhl.log", log_level="DEBUG", cache=MemCache())


@pytest.fixture(autouse=True)
def _rate_limit_guard():
    yield
    time.sleep(1.5)
