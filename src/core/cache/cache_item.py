"""
CACHE ITEM 
"""
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from typing import Any
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class CacheItem: 
    """
    Represents a single cached entry.

    A CacheItem stores the cached payload along with its time-to-live (TTL)
    and creation timestamp. Expiration is evaluated dynamically at access time.
    """
    data: Any
    ttl: int | None
    created_at: datetime

    @classmethod
    def create(cls, data: Any, ttl: int | None) -> CacheItem:
        return cls(
            data = data,
            ttl = ttl,
            created_at = datetime.now(timezone.utc)
        ) 

    def _is_expired(self) -> bool: 
        """
        Determine whether the cache item has expired.

        Returns
        -------
        bool
            True if the item has a TTL and the current time exceeds
            its expiration time. False otherwise.
        """
        if self.ttl is None: 
            return False
        return datetime.now(timezone.utc) > self.created_at + timedelta(seconds=self.ttl)
    