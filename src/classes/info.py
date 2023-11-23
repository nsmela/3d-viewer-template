# ref: 

from pathlib import Path 

APP_NAME = "RadiotherapyApp"
APP_VERSION = "proof-of-concept"

# Application Paths
DIR_PATH = Path(__file__).parent  # src folder location

HOME_PATH = DIR_PATH.expanduser()
USER_PATH = HOME_PATH.joinpath(APP_NAME)

