# ../idle_manager/__init__.py

"""Package that marks idle players."""

# Custom Package
from .idle_manager import OnClientIdle
from .idle_manager import OnClientBack
from .idle_manager import is_client_idle

__all__ = (
    'OnClientIdle',
    'OnClientBack',
    'is_client_idle',
)
