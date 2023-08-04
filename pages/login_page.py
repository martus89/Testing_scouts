from pages.base_page import BasePage
from pages.edit_player_page import EditPlayer


class LoginPage(BasePage):
    login_field_xpath = "//input[@id='login']"
    password_field_xpath = "//input[@id='password']"
    password_label_xpath = "//label[@for='password']"
    password_text_en = "Password"
    password_text_pl = "Hasło"

    sign_in_button_xpath = "//button[@type='submit']"
    sign_in_button_text_xpath = "//button/span"
    sign_in_button_text_pl = "Zaloguj"
    sign_in_button_text_en = "Sign in"

    incorrect_password_error_xpath = "//div[3]/span"
    incorrect_password_error_text_xpath = "//div[1]/div[3]/span"
    incorrect_password_error_text_en = "Identifier or password invalid."
    incorrect_password_error_text_pl = "Identifier or password invalid."

    no_login_data_error_xpath = "//div[1]/div[3]"
    no_login_data_text_xpath = "//div[3]/span"
    no_login_data_text_en = "Please provide your username or your e-mail."
    no_login_data_text_pl = "Please provide your username or your e-mail."


    email = "user01@getnada.com"
    password = "Test-1234"
    incorrect_password = "Pest-123401332ABC"

    login_url_after_logout = "https://scouts-test.futbolkolektyw.pl/login"
    login_url_en = "https://scouts-test.futbolkolektyw.pl/en/login"
    login_url_pl = "https://scouts-test.futbolkolektyw.pl/pl/login"

    !password_reminder_field_xpath = ""
    !password_reminder_text_xpath = ""
    password_reminder_text_pl = "Przypomnij hasło"
    password_reminder_text_en = "Remind password"

    !panel_main_name_field_xpath = ""
    !panel_main_name_text_xpath = ""
    panel_main_name_text_pl = "Scouts Panel"
    panel_main_name_text_en = "Scouts Panel"

    !language_dropdown_xpath = ""
    !language_dropdown_text_xpath = ""
    language_dropdown_text_en = "English"
    language_dropdown_text_pl = "Polski"

    def login_page_type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def login_page_type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def login_page_click_on_login_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=self.sign_in_button_xpath)
        return self.click_on_the_element(self.sign_in_button_xpath)

    def user_log_in(self):
        """User logging in with correct data"""
        user_login = LoginPage(self.driver)
        user_login.login_page_type_in_email(self.email)
        user_login.login_page_type_in_password(self.password)
        user_login.login_page_click_on_login_button()
        BasePage.wait_for_element_to_be_clickable(self, locator=EditPlayer.edit_player_menu_player_name_xpath)

    def user_log_in_incorrect_password(self):
        """User logging in with incorrect password"""
        user_login = LoginPage(self.driver)
        user_login.login_page_type_in_email(self.email)
        user_login.login_page_type_in_password(self.incorrect_password)
        user_login.login_page_click_on_login_button()