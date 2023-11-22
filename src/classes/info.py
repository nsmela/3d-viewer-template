import os

APP_NAME = "RadiotherapyApp"
APP_VERSION = "proof-of-concept"

DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # src folder location

HOME_PATH = os.path.join(os.path.expanduser("~"))
USER_PATH = os.path.join(HOME_PATH, APP_NAME)
