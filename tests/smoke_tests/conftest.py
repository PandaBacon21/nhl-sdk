import time
import pytest
from pathlib import Path
from nhl_stats.client import NhlClient
from nhl_stats.core.cache.mem_cache import MemCache

_LOG_FILE = str(Path(__file__).resolve().parent.parent.parent / "logs" / "nhl.log")


@pytest.fixture(scope="module")
def nhl():
    return NhlClient(log_file=_LOG_FILE, log_level="DEBUG", cache=MemCache())


@pytest.fixture(autouse=True)
def _rate_limit_guard():
    yield
    time.sleep(1.5)
