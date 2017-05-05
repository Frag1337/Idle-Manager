# ../idle_manager/__init__.py

"""Package that marks idle players."""

# Custom Package
from .idle_manager import OnClientIdle
from .idle_manager import OnClientBack
from .idle_manager import IsClientIdle

__all__ = (
    'OnClientIdle',
    'OnClientBack',
    'IsClientIdle',
)
