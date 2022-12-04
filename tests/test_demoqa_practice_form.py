from selene.support.shared import browser
from selene import be, have
import os


def test_automation_form():

    browser.open('/automation-practice-form').driver.maximize_window()
    browser.element('[id="firstName"]').should(be.blank).type('Sergey')
    browser.element('[id="lastName"]').should(be.blank).type('Zaytsev')
    browser.element('[id="userEmail"]').should(be.blank).type('testdemoqa123@testqaa.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('7999999999')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').type("January")
    browser.element('.react-datepicker__year-select').type("2022")
    browser.element('[aria-label="Choose Sunday, January 9th, 2022"]').click()
    browser.element('[id="subjectsInput"]').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('../files/Toolsqa.jpg'))
    browser.element('[id="currentAddress"]').should(be.blank).type('Mars')
    browser.element('[id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('[id="react-select-4-input"]').type('Delhi').press_enter()
    browser.element('[id="submit"]').click()

    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Sergey Zaytsev',
        'testdemoqa123@testqaa.ru',
        'Male',
        '7999999999',
        '09 January,2022',
        'Computer Science',
        'Reading',
        'Toolsqa.jpg',
        'Mars',
        'NCR Delhi'
    ))