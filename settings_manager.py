import os
import json

from config import SETTINGS_FILE_NAME


def load_settings():
    if not os.path.exists(SETTINGS_FILE_NAME):
        return {}
    with open(SETTINGS_FILE_NAME, 'r') as file:
        settings = json.loads(file.read())
    return settings


def save_settings(update):
    settings = load_settings()
    settings.update(update)
    with open(SETTINGS_FILE_NAME, 'w') as file:
        file.write(json.dumps(settings))
