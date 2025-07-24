import pytest


@pytest.fixture
def redis_no_tls_config() -> Dict[str, Any]:
    """Configuration for Redis without TLS."""
    return {
        "REDIS_ENABLED": "true",
        "REDIS_TLS": "false",
        "REDIS_URL": "redis://localhost",
    }
