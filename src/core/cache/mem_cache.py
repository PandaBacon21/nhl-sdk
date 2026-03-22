"""
LOCAL MEMORY CACHE
"""
import logging
from typing import Any

from .cache_item import CacheItem
from .base_cache import BaseCache


class MemCache(BaseCache):
    """
    In-memory cache implementation.

    This cache stores items in a local dictionary for the lifetime of the
    process. It is suitable for development environments and lightweight
    workloads but does not persist across restarts.
    """
    def __init__(self):
        self._store: dict[str, CacheItem] = {}
        self._logger = logging.getLogger("nhl_sdk.cache")

    def __str__(self) -> str:
        return f"Default in-memory cache"
    
    def __repr__(self) -> str:
        return f"LocalCache"

    
    def get(self, key: str) -> CacheItem | None: 
        """
        Retrieve a cache item if it exists and has not expired.

        Expired items are automatically removed upon access.

        Parameters
        ----------
        key : str
            Cache key.

        Returns
        -------
        CacheItem | None
            The valid cached item or None if missing or expired.
        """
        item = self._store.get(key)
        if item is None: 
            return None
        if item._is_expired():
            self._logger.debug(f"{key}: Expired")
            self.delete(key)
            return None
        return item
    
    def set(self, key: str, data: Any, ttl: int | None) -> CacheItem: 
        """
        Store a value in the cache.

        Parameters
        ----------
        key : str
            Cache key.
        data : Any
            Value to cache.
        ttl : int | None
            Time-to-live in seconds. None disables expiration.
        """
        self._store[key] = CacheItem.create(data=data, ttl=ttl)
        return self._store[key] 

    def delete(self, key: str) -> None: 
        """
        Remove a single cache entry.

        Parameters
        ----------
        key : str
            Cache key to remove.
        """
        self._store.pop(key, None)
    
    def clear(self) -> None: 
        """
        Clear all cached entries.
        """
        self._store.clear()