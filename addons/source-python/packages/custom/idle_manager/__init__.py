# ../idle_manager/__init__.py

"""Custom Package that detects idle players."""

# Custom Package
from .idle_manager import OnClientIdle
from .idle_manager import OnClientBack
from .idle_manager import is_client_idle
from .idle_manager import get_client_idle_time

__all__ = (
    'OnClientIdle',
    'OnClientBack',
    'is_client_idle',
    'get_client_idle_time',
)
