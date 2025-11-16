from nicegui import app as nicegui_app, ui
from src import constants
from src.api.main import analyse_article, router
from src.config import settings

import logging

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


@ui.page("/")
def homepage():
    ui.label("Hello, BiasSphere!")

    ui.label("")

    # Container for results
    result_container = ui.column().classes("w-full")

    async def handle_analysis():
        result_container.clear()
        with result_container:
            # Show loading spinner
            ui.spinner(size="lg")
            ui.label("Analyzing article...")

        try:
            # Call the async analysis function
            response = await analyse_article(constants.TEST_ARTICLE)

            # Clear loading and show results
            result_container.clear()
            with result_container:
                ui.json_editor({"content": {"json": response}})
        except Exception as e:
            result_container.clear()
            with result_container:
                ui.label(f"Error: {str(e)}").classes("text-negative")
                import traceback

                ui.label(traceback.format_exc()).classes("text-caption")

    ui.button("Analyze Article").on("click", handle_analysis)

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
