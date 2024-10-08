"""

@author: Team Mizogg
"""
import json
import os
from PyQt6.QtWidgets import QMessageBox

CONFIG_FILE = "config/config.json"

def get_settings():
    settings_dict = {}
    try:
        with open(CONFIG_FILE, "r") as settings_file:
            for line in settings_file:
                line = line.strip()
                if "=" in line:
                    key, value = line.split("=", 1)
                    settings_dict[key] = value
    except FileNotFoundError:
        setting_message = "Settings file not found."
        QMessageBox.information(None, "File not found", setting_message)
    except Exception as e:
        error_message = f"An error occurred while reading settings: {e}"
        QMessageBox.critical(None, "Error", error_message)
    return settings_dict

'''
def create_settings_file_if_not_exists():
    if not os.path.exists(CONFIG_FILE):
        config_data = {
            "Telegram": {
                "token": "",
                "chatid": ""
            },
            "Discord": {
                "webhook_url": ""
            },
            "Addresses": {
                "START_ADDRESS": "",
                "END_ADDRESS": ""
            },
            "Paths": {
                "INPUT_FOLDER": "input",
                "IMAGES_FOLDER": "images",
                "MUSIC_FOLDER": "music",
                "WINNER_FOLDER": "found",
                "BTC_TXT_FILE": "btc.txt"
            }
        }

        with open(CONFIG_FILE, "w") as file:
            json.dump(config_data, file, indent=4)
    else:
        # Load existing configuration data
        with open(CONFIG_FILE, "r") as file:
            config_data = json.load(file)

    # Check and create the "found" folder
    found_folder = config_data["Paths"]["WINNER_FOLDER"]
    if not os.path.exists(found_folder):
        os.makedirs(found_folder)
'''