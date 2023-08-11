import os
import unittest
from selenium import webdriver
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service

# DONE!
class TestUserLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        print("\nRunning test...")

    def test_user_log_in_incorrect_password(self):
        """Asserts user will not be able to log in with incorrect password and that incorrect password error will be raised"""
        LoginPage.user_log_in_incorrect_password(self)
        LoginPage.assert_user_incorrect_login_error_presence(self)
        BasePage.assert_element_text(self, driver=self.driver,
                                          text_element_xpath=LoginPage.incorrect_password_error_xpath,
                                          element_text_expected_text=BasePage.get_element_text(self, locator=LoginPage.incorrect_password_error_xpath))
        BasePage.assert_title_of_page_for_testing(self, expected_title=BasePage.get_page_title(self, BasePage.get_page_url(self)))

    def test_user_log_in_to_dashboard(self):
        """Asserts user will be able to log in with correct data and forwarded to dashboard"""
        LoginPage.user_log_in(self)
        BasePage.wait_for_element_to_be_clickable(self, locator=Dashboard.add_player_button_xpath)
        BasePage.assert_title_of_page_for_testing(self, expected_title=BasePage.get_page_title(self, BasePage.get_page_url(self)))

    def test_polish_language_translation_check(self):
        """Asserts all webpage is translated to Polish and webpage address corresponds with it"""
        LoginPage.language_change_to_polish(self)
        LoginPage.language_dropdown_input_lang_detect_xpath_return(self)
        LoginPage.translation_check(self)
        LoginPage.login_page_language_address_check(self)

    def test_english_language_translation_check(self):
        """Asserts all webpage is translated to English and webpage address corresponds with it"""
        LoginPage.language_change_to_english(self)
        LoginPage.language_dropdown_input_lang_detect_xpath_return(self)
        LoginPage.translation_check(self)
        LoginPage.login_page_language_address_check(self)

    @classmethod
    def tearDown(self):
        print("Shutting down test")
        list_of_addresses = [LoginPage.login_url_en, LoginPage.login_url_pl, Dashboard.menu_logout_page_redirect_url,
                             LoginPage.login_url2_en, LoginPage.login_url2_pl]
        if BasePage.get_page_url(self) not in list_of_addresses:
            Dashboard.dashboard_menu_sign_out_button_click(self)
        else:
            pass
        self.driver.quit()
