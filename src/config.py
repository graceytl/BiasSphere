"""Configuration management using Dynaconf."""

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="BIASSPHERE",
    environments=True,
    settings_files=["settings.toml"],
    env_switcher="BIASSPHERE_ENV",
    load_dotenv=True,
    merge_enabled=True,
)
