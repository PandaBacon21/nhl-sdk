"""
CACHE CLASSES
"""
from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC, abstractmethod
from typing import Any

from .cache_item import CacheItem

class BaseCache(ABC): 
    """
    Abstract base class defining the cache interface.

    All cache backends must implement this interface to ensure consistent
    behavior across in-memory, file-based, or distributed cache implementations.
    """
    @abstractmethod
    def get(self, key: str) -> CacheItem | None:
        """
        Retrieve a cached item by key.

        Parameters
        ----------
        key : str
            Unique cache key.

        Returns
        -------
        CacheItem | None
            The cached item if present and not expired, otherwise None.
        """
        ...
    
    @abstractmethod
    def set(self, key: str, data: Any, ttl: int | None) -> CacheItem:
        """
        Store a value in the cache.

        Parameters
        ----------
        key : str
            Unique cache key.
        data : Any
            The value to cache.
        ttl : int | None
            Time-to-live in seconds. If None, the item does not expire.
        """
        ...
    
    @abstractmethod
    def delete(self, key: str) -> None: 
        """
        Remove a specific cache entry.

        Parameters
        ----------
        key : str
            Cache key to remove.
        """
        ...
    
    @abstractmethod
    def clear(self) -> None: 
        """Clear the entire cache"""
        ...


class LocalCache(BaseCache): 
    """
    In-memory cache implementation.

    This cache stores items in a local dictionary for the lifetime of the
    process. It is suitable for development environments and lightweight
    workloads but does not persist across restarts.
    """
    def __init__(self): 
        """
        Inititialize the in memory, LocalCache
        """

        self._store: dict[str, CacheItem] = {}

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
            print(f"{key} is expired")
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
        print(f"{key} stored in cache - ttl: {ttl}")
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
