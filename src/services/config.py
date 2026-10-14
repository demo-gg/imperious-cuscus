from dataclasses import dataclass
from datetime import timedelta
from typing import Optional


@dataclass
class RedisConfig:
    """Configuration for Redis cache client."""

    host: str = "localhost"
    port: int = 6379
    db: int = 0
    key_prefix: str = "app:cache"
    default_ttl: timedelta = timedelta(hours=1)
    socket_timeout: float = 5.0
    max_connections: int = 10

    @classmethod
    def from_env(cls) -> "RedisConfig":
        """Load configuration from environment variables."""
        import os

        return cls(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", "6379")),
            db=int(os.getenv("REDIS_DB", "0")),
            key_prefix=os.getenv("REDIS_PREFIX", "app:cache"),
        )
