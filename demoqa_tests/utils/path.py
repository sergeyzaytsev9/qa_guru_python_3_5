from selene.support.shared import browser
import os


def create_path(element, file):
    browser.element(element).set_value(os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, file)))