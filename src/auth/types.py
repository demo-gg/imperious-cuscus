from datetime import timedelta
from typing import Any, Optional, Protocol


class CacheBackend(Protocol):
    """Protocol for implementing a generic cache backend."""

    def get(self, key: str) -> Optional[Any]:
        """Retrieve a value from the cache."""
        ...

    def set(self, key: str, value: Any, ttl: Optional[timedelta] = None) -> bool:
        """Store a value in the cache."""
        ...

    def delete(self, key: str) -> bool:
        """Remove a key from the cache."""
        ...

    def flush(self) -> None:
        """Clear all cache entries."""
        ...


class SerializationFormat:
    """Supported serialization formats for cache values."""

    JSON = "json"
    PICKLE = "pickle"
    MSGPACK = "msgpack"
