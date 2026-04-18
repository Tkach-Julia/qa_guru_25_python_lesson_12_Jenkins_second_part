from pathlib import Path

import allure

from pages.registration_page import registration_page

file_path = Path(__file__).parent.parent / 'resources' / 'artGallery.png'


@allure.tag('web')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка успешной регистрации студента')
@allure.feature('Student Registration Form')
@allure.story('Пользователь может успешно заполнить и отправить форму')
def test_register_student():
    with allure.step('Открыть форму регистрации'):
        registration_page.open()

    with allure.step('Заполнить форму валидными данными'):
        (
            registration_page
            .fill_first_name('Юлия')
            .fill_last_name('Ткач')
            .fill_email('test@gmail.com')
            .select_gender(2)
            .fill_phone('1234567890')
            .fill_birth_date(day='1', month_value='0', year='1990')
            .fill_subject('Maths')
            .select_hobby(1)
            .upload_picture(file_path.resolve())
            .fill_address('Москва, проспект Мира')
            .select_state('NCR')
            .select_city('Delhi')
            .submit()
        )

    with allure.step('Проверить данные в модальном окне результата'):
        registration_page.should_have_registered(
            ('Student Name', 'Юлия Ткач'),
            ('Student Email', 'test@gmail.com'),
            ('Gender', 'Female'),
            ('Mobile', '1234567890'),
            ('Date of Birth', '1 January,1990'),
            ('Subjects', 'Maths'),
            ('Hobbies', 'Sports'),
            ('Picture', 'artGallery.png'),
            ('Address', 'Москва, проспект Мира'),
            ('State and City', 'NCR Delhi'),
        )