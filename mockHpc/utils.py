import logging
import random
import os
import yaml
from logging import Logger


def create_logger(*name) -> Logger:
    """
    Creates a logger which logs to an individual file for each job process
    :param name: The job name
    :return: A logger object
    """
    logging_config = load_config()['logging']

    if len(name) == 0:
        name = str(random.randint(0, 10000))
    else:
        name = str(name[0])
    # make necessary dir
    log_dir = ''.join([logging_config['dir'], '/', name, '/'])
    try:
        os.mkdir(log_dir)
    except FileExistsError:
        pass  # it's fine if dir already exists

    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s : %(levelname)s %(message)s')
    handler = logging.FileHandler(''.join([log_dir, 'job-', name, '.log']))
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


def load_config() -> dict:
    """
    Loads configuration from yaml file
    :return: A dictionary of config
    """
    with open('resources/config.yaml', 'r') as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print('Error loading config.yaml file', e)
    return config
