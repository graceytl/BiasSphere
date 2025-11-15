from nicegui import app as nicegui_app, ui
from src.api.app import app

@ui.page('/')
def homepage():
    ui.label('Hello, BiasSphere!')

    ui.label('')

    ui.dark_mode().bind_value(nicegui_app.storage.user, 'dark_mode')
    ui.checkbox('dark mode').bind_value(nicegui_app.storage.user, 'dark_mode')


# Integrate with your FastAPI Application
ui.run_with(
    app=app,
    storage_secret='pick your private secret here',
)

def __main__():
    ui.run(host='127.0.0.1', port=8000)