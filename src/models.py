from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


class CacheEntry(BaseModel):
    """Represents a single cached item with metadata."""

    key: str
    value: Any
    ttl_seconds: Optional[int] = None
    created_at: datetime
    last_accessed: Optional[datetime] = None


class CacheStats(BaseModel):
    """Cache performance statistics and metadata."""

    total_keys: int
    memory_used_bytes: int
    hit_rate: float
    eviction_count: int
    connected: bool
    uptime_seconds: Optional[int] = None
