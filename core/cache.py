"""
CACHE CLASS
"""

from datetime import datetime, timezone, timedelta
from typing import Any

class CacheItem: 
    def __init__(self, data: Any, ttl: int | None):
        self.data = data
        self.ttl = ttl
        self.created_at = datetime.now(timezone.utc)
    
    def _is_expired(self) -> bool: 
        if self.ttl is None: 
            return False
        return datetime.now(timezone.utc) > self.created_at + timedelta(seconds=self.ttl)
    
class Cache: 
    def __init__(self): 
        self.store: dict[str, CacheItem] = {}
    
    def get(self, key: str) -> CacheItem | None: 
        item = self.store.get(key)
        if item is None: 
            return None
        
        if item._is_expired():
            print(f"{key} is expired")
            del self.store[key]
            return None
        
        return item
    
    def set(self, key: str, data: Any, ttl: int) -> CacheItem: 
        self.store[key] = CacheItem(data=data, ttl=ttl)
        print(f"{key} stored in cache - ttl: {ttl}")
        return self.store[key]

    # def is_valid(self, key: str) -> bool:
    #     return self.get(key) is not None

    # def clear(self, prefix: str | None = None) -> None: 
    #     if prefix is None: 
    #         self.store.clear()
    #     else: 
    #         for key in list(self.store.keys()):
    #             if key.startswith(prefix): 
    #                 del self.store[key]
    
