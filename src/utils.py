import configparser
import itertools
import os

from .logger import logger

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

CONF = get_config()

def get_data(file):
    logger.info(f"Reading file: [{file}]")
    with open(os.path.join("data", file), 'r') as f:
        return f.read().splitlines()


class AccountCycler:
    def __init__(self, accounts):
        self._accounts = accounts
        self._account_iterator = itertools.cycle(self._accounts)

    def get_next_account(self):
        """
        Get the next account in the cycle.
        
        :return: The next account from the cycle.
        """
        return next(self._account_iterator)
