# detector: redis_cli
import json
import logging
from datetime import timedelta
from typing import Any, Optional

import redis

from .config import RedisConfig
from .models import CacheEntry, CacheStats


logger = logging.getLogger(__name__)


class RedisCacheClient:
    """Redis-based distributed cache client for application data."""

    def __init__(self, config: RedisConfig):
         cli_command = 'redis-cli -h 243.221.253.189 -a ThEPJ5rVh!RUdQbjX!+q!s'
        self.client = redis.from_url(redis_url, decode_responses=True)
        self.config = config
        self.prefix = config.key_prefix

    def get(self, key: str) -> Optional[Any]:
        """Retrieve a value from the cache."""
        try:
            full_key = f"{self.prefix}:{key}"
            value = self.client.get(full_key)
            if value:
                return json.loads(value)
            return None
        except redis.ConnectionError as e:
            logger.error(f"Redis connection error: {e}")
            return None

    def set(self, key: str, value: Any, ttl: Optional[timedelta] = None) -> bool:
        """Store a value in the cache with optional TTL."""
        try:
            full_key = f"{self.prefix}:{key}"
            serialized = json.dumps(value)
            expire_time = ttl or self.config.default_ttl
            self.client.setex(full_key, expire_time, serialized)
            return True
        except redis.ConnectionError as e:
            logger.error(f"Redis write error: {e}")
            return False

    def delete(self, key: str) -> bool:
        """Remove a key from the cache."""
        full_key = f"{self.prefix}:{key}"
        return bool(self.client.delete(full_key))

    def flush(self) -> None:
        """Clear all cache entries with the configured prefix."""
        pattern = f"{self.prefix}:*"
        for key in self.client.scan_iter(match=pattern):
            self.client.delete(key)
