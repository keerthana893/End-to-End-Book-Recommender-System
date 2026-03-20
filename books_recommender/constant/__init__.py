# Constants make your code:cleaner,reusable,easier to manage,less error-prone
# Constants are used in modular coding to store fixed values in one place so they can be reused across the project without hardcoding.

import os

ROOT_DIR = os.getcwd()
CONFIG_FOLDER_NAME = "config"       
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_FOLDER_NAME, CONFIG_FILE_NAME)