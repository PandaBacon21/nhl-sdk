from nhl_stats.client import NhlClient
from nhl_stats.core.config import DefaultConfig
from nhl_stats.services.players import Players
from nhl_stats.services.teams import Teams


def test_client_default_init() -> None:
    client = NhlClient()
    assert isinstance(client.players, Players)
    assert isinstance(client.teams, Teams)


def test_client_default_config_values() -> None:
    client = NhlClient()
    assert client._config.log_name == "nhl_sdk"
    assert client._config.log_level == "DEBUG"
    assert client._config.log_file is None


def test_client_custom_log_name() -> None:
    client = NhlClient(log_name="my_app")
    assert client._config.log_name == "my_app"


def test_client_custom_log_level() -> None:
    client = NhlClient(log_level="WARNING")
    assert client._config.log_level == "WARNING"


def test_client_custom_lang() -> None:
    client = NhlClient(lang="fr")
    assert client._config.lang == "fr"


def test_client_config_from_object() -> None:
    config = DefaultConfig(log_level="ERROR", log_name="test_obj")
    client = NhlClient(config_from_object=config)
    assert client._config.log_level == "ERROR"
    assert client._config.log_name == "test_obj"


def test_client_has_api() -> None:
    client = NhlClient()
    assert client._api is not None
