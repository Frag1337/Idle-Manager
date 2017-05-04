# ../idle_manager/__init__.py

"""Package that detects idle players."""

# Custom Package
from .idle_manager import OnClientIdle
from .idle_manager import OnClientIdleBack
from .idle_manager import IsClientIdle

__all__ = (
    'OnClientIdle',
    'OnClientBack',
    'IsClientIdle',
)