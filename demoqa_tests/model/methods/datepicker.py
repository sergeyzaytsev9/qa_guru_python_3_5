import datetime
import sys

from selenium.webdriver import Keys
from demoqa_tests.utils import config


class DatepickerFactory:

    def __init__(self, element):
        self.element = element

    def set_date(self, date: datetime.date):
        self.element.send_keys(
            Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL, 'a').type(
            date.strftime(config.datetime_input_format)).press_enter()

