# fastapi-app/__init__.py
from .events import events
from .middlewares import middlewares
from .static import swagger_ui

__version__ = "1.0.0"
__author__ = "like"
__email__ = "your.email@example.com"

__all__ = [
    "events",
    "middlewares",
    "swagger_ui"
]