"""
UTILITY CLASSES AND FUNCTIONS
"""

from .cache import CacheItem

class LocalizedString:
    """
    Localized String Class for locale handling
    """
    def __init__(self, data: dict | None):
        self._data = dict(data or {})

    def __str__(self) -> str:
        return self.default or ""   

    @property
    def default(self) -> str | None:
        return self._data.get("default")

    def get_locale(self, locale: str, *, fallback: bool = True) -> str | None:
        if locale in self._data:
            return self._data[locale]
        return self.default if fallback else None

    @property
    def locales(self) -> set:
        if len(self._data.keys()) > 1:
            return set(self._data.keys()) - {"default"}
        return set(self._data.keys())


def _to_bool(value: int | bool | None) -> bool | None:
    """Normalize API boolean values (0/1, True/False) to Python bool
    """
    if value is None:
        return None
    return bool(value)

def _check_cache(cache, cache_key: str) -> CacheItem | None: 
        cached = cache.get(cache_key)
        if cached is None:
            return None
        return cached