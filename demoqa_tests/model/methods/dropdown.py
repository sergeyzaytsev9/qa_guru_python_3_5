from selene import have


class DropdownFactory:

    def __init__(self, element, elements):
        self.element = element
        self.elements = elements

    def select(self, option):
        self.element.click()
        self.elements.element_by(have.exact_text(option)).click()
