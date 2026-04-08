from nhl_stats.core.utilities import LocalizedString, _to_bool


# ==========================================================================
# LOCALIZED STRING
# ==========================================================================

def test_localized_string_default() -> None:
    ls = LocalizedString({"default": "Connor"})
    assert ls.default == "Connor"

def test_localized_string_default_none_when_missing() -> None:
    ls = LocalizedString({"fr": "Connor"})
    assert ls.default is None

def test_localized_string_none_data() -> None:
    ls = LocalizedString(None)
    assert ls.default is None

def test_localized_string_empty_dict() -> None:
    ls = LocalizedString({})
    assert ls.default is None

def test_localized_string_str_returns_default() -> None:
    ls = LocalizedString({"default": "Oilers"})
    assert str(ls) == "Oilers"

def test_localized_string_str_returns_empty_when_no_default() -> None:
    """str() returns '' not None — important for to_dict() callers."""
    ls = LocalizedString(None)
    assert str(ls) == ""

def test_localized_string_get_locale_exact() -> None:
    ls = LocalizedString({"default": "Oilers", "fr": "Oilers FR"})
    assert ls.get_locale("fr") == "Oilers FR"

def test_localized_string_get_locale_fallback() -> None:
    """Falls back to default when locale is absent and fallback=True."""
    ls = LocalizedString({"default": "Oilers"})
    assert ls.get_locale("fr") == "Oilers"

def test_localized_string_get_locale_no_fallback() -> None:
    """Returns None when locale absent and fallback=False."""
    ls = LocalizedString({"default": "Oilers"})
    assert ls.get_locale("fr", fallback=False) is None

def test_localized_string_eq_string() -> None:
    ls = LocalizedString({"default": "Oilers"})
    assert ls == "Oilers"

def test_localized_string_eq_localized_string() -> None:
    a = LocalizedString({"default": "Oilers"})
    b = LocalizedString({"default": "Oilers"})
    assert a == b

def test_localized_string_not_eq() -> None:
    a = LocalizedString({"default": "Oilers"})
    b = LocalizedString({"default": "Leafs"})
    assert a != b

def test_localized_string_locales_excludes_default() -> None:
    ls = LocalizedString({"default": "Oilers", "fr": "Oilers FR", "es": "Oilers ES"})
    assert ls.locales == {"fr", "es"}

def test_localized_string_locales_only_default() -> None:
    ls = LocalizedString({"default": "Oilers"})
    assert ls.locales == {"default"}


# ==========================================================================
# _TO_BOOL
# ==========================================================================

def test_to_bool_none_returns_none() -> None:
    assert _to_bool(None) is None

def test_to_bool_true() -> None:
    assert _to_bool(True) is True

def test_to_bool_false() -> None:
    assert _to_bool(False) is False

def test_to_bool_int_1_is_true() -> None:
    assert _to_bool(1) is True

def test_to_bool_int_0_is_false() -> None:
    assert _to_bool(0) is False
