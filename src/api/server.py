from fastapi import FastAPI
import uvicorn

from src.config import settings
from src.api.main import router

api = FastAPI(
    title=settings.api.title,
    description=settings.api.description,
    version=settings.version,
    debug=settings.debug,
)

api.include_router(router)


def run():
    uvicorn.run(
        "src.api.server:api",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.get("server.reload", False),
        log_level="info",
        reload_dirs="src/" if settings.get("server.reload", False) else None,
    )


if __name__ == "__main__.py":
    run()
