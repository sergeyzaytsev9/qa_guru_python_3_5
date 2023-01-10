from demoqa_tests.model.data.Student import test_zaytsev
from demoqa_tests.model.pages.registration_form import PracticePage


def test_student_registration_form():
    practice_form = PracticePage(test_zaytsev)

    # WHEN
    practice_form.given_opened()
    practice_form.set_name()
    practice_form.set_last_name()
    practice_form.set_email()
    practice_form.set_gender()
    practice_form.set_phone_number()
    practice_form.set_birthday()
    practice_form.set_subjects()
    practice_form.set_hobbies()
    practice_form.picture_upload()
    practice_form.set_address()
    practice_form.set_state()
    practice_form.set_city()

    practice_form.submit()
    # THEN
    practice_form.should_have_submitted()