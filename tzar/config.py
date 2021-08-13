import os
from pathlib import Path
from typing import List
from urllib import request

import toml
from click import confirm, get_app_dir, secho

DEFAULT_CONFIG_URL = (
    "https://raw.githubusercontent.com/DanielVZ96/tzar/main/config/default.toml"
)


def read() -> List[dict]:
    if "TZAR_CONFIG" in os.environ:
        config_path = os.environ["TZAR_CONFIG"]
    else:
        config_path = get_app_dir("tzar")
    os.makedirs(config_path, exist_ok=True)
    config_path = Path(config_path)
    configs = [dict(toml.load(config)) for config in config_path.glob("*.toml")]
    if configs:
        return configs
    elif prompt_config_download(config_path):
        return read()

    secho("No config files found!", fg="red", bold=True, err=True)
    return []


def prompt_config_download(config_path: Path) -> bool:
    secho(
        f"No config files where found. You can download the default one from: {DEFAULT_CONFIG_URL}",
        fg="cyan",
    )
    if confirm(f"Download default config file?"):
        filename, _ = request.urlretrieve(
            DEFAULT_CONFIG_URL, config_path / "default.toml"
        )
        secho(f"Config downloaded to: {filename}", fg="green")
        return True
    return False
