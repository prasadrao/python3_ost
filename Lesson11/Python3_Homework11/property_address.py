"""
Demonstrate "property" features using address program.
"""
import re
import logging
class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass

LOG_FILENAME = "property_address.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = "info" # Default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)


class Address(object):

    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zipcode = zip_code
        logging.info("Creating a new address")

    @property
    def name(self):
        return self._name

    @property
    def street_address(self):
        return self._street_address

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        reg = re.compile('^[A-Z]{2}$')
        if reg.match(value):
            self._state = value
        else:
            logging.error("State exception")
            raise StateError("Please enter a valid state! {0!r} is not a valid state".format(value))

    @property
    def zip_code(self):
        return self._zipcode

    @zip_code.setter
    def zip_code(self, value):
        reg_digit = re.compile('^\d{5}$')
        if reg_digit.match(value):
            self._zipcode = value
        else:
            logging.error("ZipCode exception")
            raise ZipCodeError("Please enter a valid zipcode! {0!r} is not a valid zipcode".format(value))
