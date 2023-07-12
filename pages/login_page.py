from pages.base_page import BasePage
import time


# Week 2 Subtask 3: Dodawanie selektorów do projektu - added below


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    email = "user01@getnada.com"
    password = "Test-1234"
    expected_title = "Scouts panel - sign in"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"

    def login_page_type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    # Week 3 Subtask 1: Uzupełnienie strony logowania
    def login_page_type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def login_page_click_on_login_button(self):
        return self.click_on_the_element(self.sign_in_button_xpath)

    def user_log_in(self):
        user_login = LoginPage(self.driver)
        user_login.login_page_type_in_email(LoginPage.email)
        user_login.login_page_type_in_password(LoginPage.password)
        user_login.login_page_click_on_login_button()
        time.sleep(15)
