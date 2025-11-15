from nicegui import app as nicegui_app, ui
from src.api.main import app


@ui.page("/")
def homepage():
    ui.label("Hello, BiasSphere!")

    ui.label("")

    ui.dark_mode().bind_value(nicegui_app.storage.user, "dark_mode")
    ui.checkbox("dark mode").bind_value(nicegui_app.storage.user, "dark_mode")


# Integrate with your FastAPI Application
ui.run_with(
    app=app,
    storage_secret="pick your private secret here",
)

if __name__ == "__main__":
    ui.run(host="0.0.0.0", port=8000, uvicorn_reload_dirs=["src/ui/", "src/api/"])
