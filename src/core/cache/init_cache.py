"""
BUILD CACHE
"""

from .caches import BaseCache

_cache = None

def init_cache(cache: BaseCache) -> None:
    global _cache
    _cache = cache

def get_cache() -> BaseCache: 
    if _cache is None:
        raise RuntimeError("Cache not initialized. Call init_cache() first.")
    return _cache