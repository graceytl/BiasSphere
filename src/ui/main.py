from nicegui import app as nicegui_app, ui
from src.api.main import router
from src.config import settings


@ui.page("/")
def homepage():
    ui.label("Hello, BiasSphere!")

    ui.label("")

    ui.dark_mode().bind_value(nicegui_app.storage.user, "dark_mode")
    ui.checkbox("dark mode").bind_value(nicegui_app.storage.user, "dark_mode")


nicegui_app.include_router(router)


def run_app():
    ui.run(
        storage_secret="test_secret",  # pragma: allowlist secret
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.get("server.reload", False),
        uvicorn_reload_dirs="src/" if settings.get("server.reload", False) else None,
    )


if __name__ in {"__main__", "__mp_main__"}:
    run_app()
