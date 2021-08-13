import os
from pathlib import Path

import toml
import xdg.BaseDirectory as xdg


def read():
    if "TZAR_CONFIG" in os.environ:
        config_path = os.environ["TZAR_CONFIG"]
        os.makedirs(config_path, exist_ok=True)
    elif "APPDATA" in os.environ:
        config_path = os.path.join(os.environ["APPDATA"], "tzar")
        os.makedirs(config_path, exist_ok=True)
    else:
        config_path = xdg.save_config_path("tzar")
    config_path = Path(config_path)
    configs = config_path.glob("*.toml")
    return [toml.load(config) for config in configs]
