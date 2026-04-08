"""
BUILD CACHE
"""

from .base_cache import BaseCache

_cache = None



def init_cache(cache: BaseCache | None) -> None:
    global _cache
    _cache = cache

def get_cache() -> BaseCache | None:
    return _cache


__all__ = ["init_cache", "get_cache"]

