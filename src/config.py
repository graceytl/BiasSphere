"""Configuration management using Dynaconf."""

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="BIASSPHERE",
    settings_files=["settings.toml", ".secrets.toml"],
    environments=True,
    env_switcher="BIASSPHERE_ENV",
    load_dotenv=True,
    merge_enabled=True,
)
