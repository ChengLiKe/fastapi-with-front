# fastapi-app/events/__init__.py

"""
1. 事件相关功能的包初始化模块
- Event-related function package initialization module.
2. 该模块包含与事件处理相关的，因此在应用启动和关闭时会被调用。
- This module contains event handling related to it, so it will be called when the application starts and shuts down.
"""

# 导入事件处理程序模块
from .startup import startup
from .shutdown import shutdown

# 包元数据
__version__ = "1.0.0"
__author__ = "like"

__all__ = [
    "events",
    "startup",
    "shutdown",
]


def events(app):
    @app.on_event("startup")
    async def on_startup():
        await startup()  # 在应用启动时执行

    @app.on_event("shutdown")
    async def on_shutdown():
        await shutdown()  # 在应用结束时执行
