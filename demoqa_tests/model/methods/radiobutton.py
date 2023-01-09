from selene import have


class RadiobuttonFactory:

    def __init__(self, element):
        self.element = element

    def set_value(self, text):
        self.element.element_by(have.value(text)).element('..').click()