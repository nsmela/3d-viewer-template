import os, sys
import logging
import logging.handlers

from classes import info

# setup log formaters
template = '%(levelname)s %(module)s: %(message)s'
console_formatter = logging.Formatter(template)
file_formatter = logging.Formatter('%(sctime)s ' + template, datefmt='%H:%M:%S')

# Configure root logger for minimal logging
logging.basicConfig(level=logging.ERROR)
rootlog = logging.getLogger()

if os.path.exists(info.USER_PATH):
    file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(info.USER_PATH, f"{info.APP_NAME}.log"),
        encoding="utf-8",
        maxBytes=25*1024*1024, backupCount=3)
    file_handler.setLevel("DEBUG")
    file_handler.setFormatter(file_formatter)

