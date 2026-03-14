"""
CACHE CLASSES
"""
from __future__ import annotations

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



