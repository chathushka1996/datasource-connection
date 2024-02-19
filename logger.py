import logging
import logging.handlers
import os
import pathlib


def get_debug_logger(name):
    folder_path = pathlib.Path.joinpath(pathlib.Path(__file__).parent.resolve(), "logs")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_name = pathlib.Path.joinpath(pathlib.Path(__file__).parent.resolve(), "logs/server.log")
    _logger = logging.getLogger(name)
    _logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(file_name)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    _logger.addHandler(file_handler)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    _logger.addHandler(console_handler)
    return _logger
