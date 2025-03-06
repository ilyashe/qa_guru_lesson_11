from model.pages.registration_page import RegistrationPage


def test_complete_and_submit_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Fedor')
    registration_page.fill_last_name('Bubnov')
    registration_page.fill_email('fedor.bubnov_test@gmail.com')
    registration_page.select_gender('Male')
    registration_page.fill_phone_number('9990006666')
    registration_page.fill_date_of_birth(year='1997', month='July', day='03')
    registration_page.select_subject('biology')
    registration_page.select_subject('chem')
    registration_page.select_hobby('Sports')
    registration_page.select_hobby('Music')
    registration_page.upload_avatar('avatar.jpg')
    registration_page.fill_address('Sadovaya, 14')
    registration_page.select_state('Haryana')
    registration_page.select_city('Karnal')
    registration_page.submit()

    # THEN
    registration_page.should_registered_user_with(
        full_name='Fedor Bubnov',
        email='fedor.bubnov_test@gmail.com',
        gender='Male',
        phone='9990006666',
        date_of_birth='03 July,1997',
        subjects='Biology, Chemistry',
        hobbies='Sports, Music',
        file_name='avatar.jpg',
        address='Sadovaya, 14',
        state='Haryana',
        city='Karnal')
