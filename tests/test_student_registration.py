from demoqa_tests.model.pages import registration_form


def test_student_registration_form():
    registration_form.given_opened()

    # WHEN
    registration_form.set_name('Sergey')
    registration_form.set_last_name('Engineer')
    registration_form.set_email('test@demoqa.com')
    registration_form.set_gender('Male')
    registration_form.set_phone_number('1234567890')
    registration_form.set_birthday('4', '1994', '02')
    registration_form.set_subjects('Computer Science')
    registration_form.set_hobbies('Reading')
    registration_form.picture_upload('files/Toolsqa.jpg')
    registration_form.set_address('Pushkina 8')
    registration_form.set_state('NCR')
    registration_form.set_city('Delhi')

    registration_form.submit()

    # THEN
    registration_form.should_have_submitted(
        [
            ('Student Name', 'Sergey Engineer'),
            ('Student Email', 'test@demoqa.com'),
            ('Mobile', '1234567890'),
            ('Date of Birth', '02 May,1994'),
            ('Subjects', 'Computer Science'),
            ('Hobbies', 'Reading'),
            ('Picture', 'Toolsqa.jpg'),
            ('Address', 'Pushkina 8'),
            ('State', 'NCR Delhi'),
        ],
    )