# -*- coding: utf-8 -*-

from loguru import logger
import os
import sys

LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../log"))

ROTATION_TIME = "02:00"

class Log(object):
    def __init__(self, name="test.log", log_dir=LOG_DIR, is_debug=False):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file_path = os.path.join(log_dir, name)
        logger.remove()
        level = "DEBUG" if is_debug else "INFO"
        logger.add(sys.stdout, level=level)
        logger.add(log_file_path, rotation=ROTATION_TIME, level="DEBUG")
        self.logger = logger

logger = Log(is_debug=True).logger