import pytest
from src.client import NhlClient


@pytest.fixture(scope="module")
def nhl():
    return NhlClient(log_file="logs/nhl.log", log_level="DEBUG")
