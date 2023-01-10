from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model.methods.checkbox import CheckboxFactory
from demoqa_tests.model.methods.datepicker import DatepickerFactory
from demoqa_tests.model.methods.dropdown import DropdownFactory
from demoqa_tests.model.methods.radiobutton import RadiobuttonFactory
from demoqa_tests.utils import path, config


class PracticePage:
    def __init__(self, student):
        self.student = student

    def given_opened(self):
        browser.open('/automation-practice-form').driver.maximize_window()

    def set_name(self):
        browser.element('#firstName').type(self.student.first_name)

    def set_last_name(self):
        browser.element('#lastName').type(self.student.last_name)
        return self

    def set_email(self):
        browser.element('#userEmail').type(self.student.email)
        return self

    def set_gender(self):
        gender = RadiobuttonFactory(browser.all('[name=gender]'))
        gender.set_value(self.student.gender)
        return self

    def set_phone_number(self):
        browser.element('#userNumber').type(self.student.phone)
        return self

    def set_birthday(self):
        birthday_date = DatepickerFactory(browser.element('#dateOfBirthInput'))
        birthday_date.set_date(self.student.birthday)
        return self

    def picture_upload(self):
        browser.element('#uploadPicture').set_value(path.generate_path_upload(self.student.image))
        return self

    def set_address(self):
        browser.element('#currentAddress').type(self.student.address)
        return self

    def set_hobbies(self):
        select_hobby = CheckboxFactory(browser.all('[for^=hobbies-checkbox]'))
        select_hobby.set_checkboxes(self.student.hobby)
        return self

    def set_subjects(self):
        browser.element('#subjectsInput').type(self.student.subject).press_enter()
        return self

    def set_state(self):
        select_state = DropdownFactory(browser.element('#state'), browser.all('[id^=react-select][id*=option]'))
        select_state.select(self.student.state)
        return self

    def set_city(self):
        select_city = DropdownFactory(browser.element('#city'), browser.all('[id^=react-select][id*=option]'))
        select_city.select(self.student.city)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def should_have_submitted(self):
        browser.all('tbody tr td:last-child').should(have.exact_texts(
            self.student.first_name + ' ' + self.student.last_name,
            self.student.email,
            self.student.gender,
            self.student.phone,
            self.student.birthday.strftime(config.datetime_view_format),
            self.student.subject,
            ', '.join(hobby.name for hobby in self.student.hobby),
            self.student.image,
            self.student.address,
            self.student.state + ' ' + self.student.city))
        return self
