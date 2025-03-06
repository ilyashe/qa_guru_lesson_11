from selene import browser, have, command
from model import resource


class RegistrationPage:

    @staticmethod
    def open():
        browser.open('/automation-practice-form')

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        # browser.driver.execute_script("document.body.style.zoom = '0.5'")

    @staticmethod
    def fill_first_name(name):
        browser.element('#firstName').type(name)

    @staticmethod
    def fill_last_name(last_name):
        browser.element('#lastName').type(last_name)

    @staticmethod
    def fill_email(email):
        browser.element('#userEmail').type(email)

    @staticmethod
    def select_gender(value='Male'):
        browser.element(f'[name=gender][value={value}]').perform(command.js.click)

    @staticmethod
    def fill_phone_number(phone_number):
        browser.element('#userNumber').type(phone_number)

    @staticmethod
    def fill_date_of_birth(year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().all('option').element_by(have.text(month)).click()
        browser.element('.react-datepicker__year-select').click().all('option').element_by(have.text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    @staticmethod
    def select_subject(value):
        browser.element('#subjectsInput').type(value).press_enter()

    @staticmethod
    def select_hobby(value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(value)).click()

    @staticmethod
    def upload_avatar(file_name):
        browser.element('#uploadPicture').set_value(resource.path(file_name))

    @staticmethod
    def fill_address(address):
        browser.element('#currentAddress').type(address)

    @staticmethod
    def select_state(state):
        browser.element('#state').click().all('[id^=react-select-3-option]').element_by(have.text(state)).click()

    @staticmethod
    def select_city(city):
        browser.element('#city').click().all('[id^=react-select-4-option]').element_by(have.text(city)).click()

    @staticmethod
    def submit():
        browser.element('#submit').click()

    @staticmethod
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
