import allure
from selene import browser, have, command
from model import resource


class RegistrationPage:


    @staticmethod
    @allure.step("Открытие страницы с формой")
    def open():
        browser.open('/automation-practice-form')

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        # browser.driver.execute_script("document.body.style.zoom = '0.5'")

    @staticmethod
    @allure.step("Ввод имени")
    def fill_first_name(name):
        browser.element('#firstName').type(name)

    @staticmethod
    @allure.step("Ввод фамилии")
    def fill_last_name(last_name):
        browser.element('#lastName').type(last_name)

    @staticmethod
    @allure.step("Ввод имейла")
    def fill_email(email):
        browser.element('#userEmail').type(email)

    @staticmethod
    @allure.step("Выбор пола")
    def select_gender(value='Male'):
        browser.element(f'[name=gender][value={value}]').perform(command.js.click)

    @staticmethod
    @allure.step("Ввод номера телефона")
    def fill_phone_number(phone_number):
        browser.element('#userNumber').type(phone_number)

    @staticmethod
    @allure.step("Выбор даты рождения")
    def fill_date_of_birth(year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().all('option').element_by(have.text(month)).click()
        browser.element('.react-datepicker__year-select').click().all('option').element_by(have.text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    @staticmethod
    @allure.step("Выбор предмета")
    def select_subject(value):
        browser.element('#subjectsInput').type(value).press_enter()

    @staticmethod
    @allure.step("Выбор хобби")
    def select_hobby(value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(value)).perform(command.js.click)

    @staticmethod
    @allure.step("Загрузка аватара")
    def upload_avatar(file_name):
        browser.element('#uploadPicture').set_value(resource.path(file_name))

    @staticmethod
    @allure.step("Ввод адреса")
    def fill_address(address):
        browser.element('#currentAddress').type(address)

    @staticmethod
    @allure.step("Выбор штата")
    def select_state(state):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click().all('[id^=react-select-3-option]').element_by(have.text(state)).click()

    @staticmethod
    @allure.step("Выбор города")
    def select_city(city):
        browser.element('#city').click().all('[id^=react-select-4-option]').element_by(have.text(city)).click()

    @staticmethod
    @allure.step("Отправка формы")
    def submit():
        browser.element('#submit').click()

    @staticmethod
    @allure.step("Проверка формы на соответствие данным")
    def should_registered_user_with(full_name, email, gender, phone, date_of_birth, subjects,
                                    hobbies, file_name, address, state, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                subjects,
                hobbies,
                file_name,
                address,
                f'{state} {city}',
            )
        )
