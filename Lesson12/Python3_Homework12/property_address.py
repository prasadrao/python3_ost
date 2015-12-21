"""
Demonstrate "property" features using address program.
"""
import re
import logging
from optparse import OptionParser
import configparser

class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass

config = configparser.RawConfigParser()
config.read('property_address.cfg')

#LOG_FILENAME = "property_address.log"
LOG_FILENAME = config.get('log', 'output')
#LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
LOG_FORMAT = config.get('log', 'format')
DEFAULT_LOG_LEVEL = "info" # Default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level.lower()], format=LOG_FORMAT)


class Address:

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
        #reg = re.compile('^[A-Z]{2}$')
        reg = re.compile(config.get('validators', 'state'))
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
        #reg_digit = re.compile('^\d{5}$')
        reg_digit = re.compile(config.get('validators', 'zip_code'))
        if reg_digit.match(value):
            self._zipcode = value
        else:
            logging.error("ZipCode exception")
            raise ZipCodeError("Please enter a valid zipcode! {0!r} is not a valid zipcode".format(value))

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option('-l', '--level', dest="level", action="store", help="Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL", default="info")
    parser.add_option('-n', '--name', dest="name", action="store", help="Sets the name value of the Address object")
    parser.add_option('-a', '--address', dest="street_address", action="store", help="Sets the street_address value of the Address object")
    parser.add_option('-c', '--city', dest="city", action="store", help="Sets the city value of the Address object")
    parser.add_option('-s', '--state', dest="state", action="store", help="Sets the state value of the Address object")
    parser.add_option('-z', '--zip_code', dest="zip_code", action="store", help="Sets the zip_code value of the Address object")
    (options, args) = parser.parse_args()
    def validate_zipcode(zipcode):
        reg_digit = re.compile(config.get('validators', 'zip_code'))
        if reg_digit.match(zipcode):
            pass
        else:
            raise ZipCodeError("Please enter a valid zipcode!")
    def validate_state(state):
        reg = re.compile(config.get('validators', 'state'))
        if reg.match(state):
            pass
        else:
            raise StateError("Please enter a valid state!")
    try:
        start_logging(level=options.level)
        validate_zipcode(options.zip_code)
        validate_state(options.state)
        A = Address(name=options.name, street_address=options.street_address, city=options.city, state=options.state, zip_code=options.zip_code)
    except ZipCodeError:
        logging.error("ZipCode exception")
        parser.error("option -z requires a valid 5-digit US zip code")
    except StateError:
        logging.error("State exception")
        parser.error("option -s requires a valid US state code")
