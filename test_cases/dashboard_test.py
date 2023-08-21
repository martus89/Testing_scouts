import os
import unittest
from selenium import webdriver
from pages.add_player_page import AddPlayer
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        print("\nRunning test...")

    def test_user_sign_out(self):
        """Asserts user gets successfully redirected to sign in upon clicking on sign out button from dashboard"""

        LoginPage.user_log_in(self)
        Dashboard.dashboard_menu_sign_out_button_click(self)
        BasePage.assert_title_of_page_for_testing(self, expected_title=BasePage.get_page_title(self))

    def test_open_last_created_match(self):
        """Asserts element correctness and therefore correct redirect on last created match subpage"""

        LoginPage.user_log_in(self)
        Dashboard.dashboard_activity_last_created_match_click(self)
        BasePage.assert_element_text(self, driver=self.driver,
                                     text_element_xpath=AddPlayer.add_player_submit_button_xpath,
                                     element_text_expected_text=AddPlayer.add_player_submit_button_name_en)

    def test_login_language_pl(self):
        """Asserts webpage address and language translation upon login with Polish chosen as optional language"""

        LoginPage.user_log_in_to_polish(self)
        Dashboard.dashboard_menu_main_page_button_click(self)
        Dashboard.create_translation_dictionary(self)
        Dashboard.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)

    def test_login_language_en(self):
        """Asserts webpage address and language translation upon login with English chosen as optional language"""

        LoginPage.user_log_in_to_english(self)
        Dashboard.dashboard_menu_main_page_button_click(self)
        Dashboard.create_translation_dictionary(self)
        Dashboard.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)

    def test_dashboard_language_change(self):
        """Asserts webpage address and language translation after using language change button from dashboard menu"""

        LoginPage.user_log_in_to_polish(self)
        Dashboard.dashboard_menu_language_change_button_click(self)
        print("Language changed manually via menu option")
        Dashboard.create_translation_dictionary(self)
        Dashboard.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        Dashboard.dashboard_menu_language_change_button_click(self)
        print("Language changed manually via menu option")
        Dashboard.create_translation_dictionary(self)
        Dashboard.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)

    @classmethod
    def tearDown(self):
        print("Shutting down test")
        list_of_addresses = [LoginPage.login_url_en, LoginPage.login_url_pl, Dashboard.menu_logout_page_redirect_url, LoginPage.login_url2_en, LoginPage.login_url2_pl]
        if BasePage.get_page_url(self) not in list_of_addresses:
            Dashboard.dashboard_menu_sign_out_button_click(self)
        else:
            pass
        self.driver.quit()
