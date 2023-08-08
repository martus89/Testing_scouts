from pages.edit_player_page import EditPlayer
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//input[@id='login']"
    password_field_xpath = "//input[@id='password']"
    password_label_xpath = "//label[@for='password']"
    password_text_en = "Password"
    password_text_pl = "Hasło"

    sign_in_button_xpath = "//button[@type='submit']"
    sign_in_button_text_xpath = "//button/span[1]"
    sign_in_button_text_pl = "ZALOGUJ"
    sign_in_button_text_en = "SIGN IN"

    incorrect_password_error_xpath = "//div[3]/span"
    # incorrect_password_error_text_xpath = "//div[1]/div[3]/span"
    # incorrect_password_error_text_en = "Identifier or password invalid."
    # incorrect_password_error_text_pl = "Identifier or password invalid."

    no_login_data_error_xpath = "//div[1]/div[3]"
    # no_login_data_text_xpath = "//div[3]/span/text()"
    # no_login_data_text_en = "Please provide your username or your e-mail."
    # no_login_data_text_pl = "Please provide your username or your e-mail."

    email = "user01@getnada.com"
    password = "Test-1234"
    incorrect_password = "Pest-123401332ABC"

    login_url_after_logout = "https://scouts-test.futbolkolektyw.pl/login"
    login_url_en = "https://scouts-test.futbolkolektyw.pl/en/login?redirected=true"
    login_url_pl = "https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true"

    password_reminder_field_text_xpath = "//div[1]/a"
    password_reminder_text_pl = "Przypomnij hasło"
    password_reminder_text_en = "Remind password"

    panel_main_name_field_text_xpath = "//div[1]/h5"
    panel_main_name_text_pl = "Scouts Panel"
    panel_main_name_text_en = "Scouts Panel"

    language_dropdown_xpath = "//div[@aria-haspopup='listbox']"
    language_dropdown_input_lang_detect_xpath = "//form/div/div[2]/div/div"
    language_dropdown_text_en = "English"
    language_dropdown_text_pl = "Polski"

    dropdown_menu = "//div/div[2]/div/div"

    def login_page_type_in_email(self, email):
        """Typing in e-mail address for login purposes"""
        self.field_send_keys(self.login_field_xpath, email)

    def login_page_type_in_password(self, password):
        """Typing in password for login purposes"""
        self.field_send_keys(self.password_field_xpath, password)

    def login_page_click_on_login_button(self):
        """Log in button click"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.sign_in_button_xpath)
        return self.click_on_the_element(self.sign_in_button_xpath)

    def user_log_in(self):
        """User logging in with correct data"""
        user_login = LoginPage(self.driver)
        user_login.login_page_type_in_email(LoginPage.email)
        user_login.login_page_type_in_password(LoginPage.password)
        user_login.login_page_click_on_login_button()
        BasePage.wait_for_element_to_be_clickable(self, locator=EditPlayer.edit_player_menu_player_name_xpath)

    def user_log_in_incorrect_password(self):
        """User logging in with incorrect password"""
        user_login = LoginPage(self.driver)
        user_login.login_page_type_in_email(LoginPage.email)
        user_login.login_page_type_in_password(LoginPage.incorrect_password)
        user_login.login_page_click_on_login_button()

    def assert_user_incorrect_login_error_presence(self):
        """Checking if user gets an incorrect password error upon typing incorrect password"""
        BasePage.wait_for_element_to_be_present(self, locator=LoginPage.incorrect_password_error_xpath)
        self.assertIsNotNone(LoginPage.incorrect_password_error_xpath)

    def dropdown_menu_click_on_dropdown(self):
        """Method supporting dropdown_menu_click_on(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.dropdown_menu)
        return self.click_on_the_element(LoginPage.dropdown_menu)

    def dropdown_menu_click_on(self):
        """User click on language dropdown menu"""
        dropdown_menu = LoginPage(self.driver)
        dropdown_menu.dropdown_menu_click_on_dropdown()

    def language_change_to_polish(self):
        """User changes language via dropdown to Polish"""
        LoginPage.dropdown_menu_click_on(self)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[3]/ul/li[1]').click()
        time.sleep(2)

    def language_change_to_english(self):
        """User changes language via dropdown to English"""
        LoginPage.dropdown_menu_click_on(self)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[3]/ul/li[2]').click()
        time.sleep(2)

    def language_dropdown_input_lang_detect_xpath_return(self):
        """Returns language chosen by user"""
        language_dropdown_input_lang_detect_xpath = self.driver.find_element(By.XPATH, "//form/div/div[2]/div/div").text
        return language_dropdown_input_lang_detect_xpath

    def create_translation_dictionary(self):
        """Creates a translation dictionary"""
        password_label_xpath = self.driver.find_element(By.XPATH, "//label[@for='password']").text
        sign_in_button_text_xpath = self.driver.find_element(By.XPATH, "//button/span").text
        password_reminder_field_text_xpath = self.driver.find_element(By.XPATH, "//div[1]/a").text
        panel_main_name_field_text_xpath = self.driver.find_element(By.XPATH, "//div[1]/h5").text

        global language_page_version_pl
        language_page_version_pl = {panel_main_name_field_text_xpath: LoginPage.panel_main_name_text_pl,
                                    password_reminder_field_text_xpath: LoginPage.password_reminder_text_pl,
                                    sign_in_button_text_xpath: LoginPage.sign_in_button_text_pl,
                                    password_label_xpath: LoginPage.password_text_pl}

        global language_page_version_en
        language_page_version_en = {panel_main_name_field_text_xpath: LoginPage.panel_main_name_text_en,
                                        password_reminder_field_text_xpath: LoginPage.password_reminder_text_en,
                                        sign_in_button_text_xpath: LoginPage.sign_in_button_text_en,
                                        password_label_xpath: LoginPage.password_text_en}

    def translation_check(self):
        """Based on language chosen in dropdown by user, checks if page elements have correct language"""
        LoginPage.create_translation_dictionary(self)
        if LoginPage.language_dropdown_input_lang_detect_xpath_return(self) == "Polski":
            page_dictionary = language_page_version_pl
            print(page_dictionary)
        elif LoginPage.language_dropdown_input_lang_detect_xpath_return(self) == "English":
            page_dictionary = language_page_version_en
            print(page_dictionary)
        else:
            print("Language not detected - check your webpage")

        for field_name in page_dictionary:
            assert field_name == page_dictionary[field_name]

    def login_page_language_address_check(self):
        """Checks language in webpage address and compares to one chosen by user in dropdown"""
        my_page_url = BasePage.get_page_url(self)[38:40]
        if LoginPage.language_dropdown_input_lang_detect_xpath_return(self) == "Polski":
            assert my_page_url == "pl"
            print("Page correctly redirected in Polish")
        elif LoginPage.language_dropdown_input_lang_detect_xpath_return(self) == "English":
            assert my_page_url == "en"
            print("Page correctly redirected in English")
        else:
            print("There is an issue somewhere with your webpage language choice")