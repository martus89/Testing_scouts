import time
import unittest
import os
from selenium import webdriver
from pages.add_player_page import AddPlayer
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.edit_player_page import EditPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service

# !!!!!FIXED WITH NEW FUNCTIONS!!!!

class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        print("\nRunning test...")

    def test_translation_add_player_en(self):
        """Asserts language translation of webpage upon choice of English at login"""
        LoginPage.user_log_in_to_english(self)
        AddPlayer.path_to_add_player(self)
        BasePage.language_detect_from_dropdown(self)
        AddPlayer.create_translation_dictionary(self)
        AddPlayer.address_dictionary_translation_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_title_of_page_for_testing(self, expected_title="Add player")
        BasePage.assert_page_redirected_correctly(self, word_to_check="add")

    def test_translation_add_player_pl(self):
        """Asserts language translation of webpage upon choice of Polish at login"""
        LoginPage.user_log_in_to_polish(self)
        AddPlayer.path_to_add_player(self)
        BasePage.language_detect_from_dropdown(self)
        AddPlayer.create_translation_dictionary(self)
        AddPlayer.address_dictionary_translation_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_title_of_page_for_testing(self, expected_title="Dodaj gracza")
        BasePage.assert_page_redirected_correctly(self, word_to_check="add")

    def test_add_player_restricted_data_only_and_language_change(self):
        """Asserts language translation of webpage upon choice of English at login, filling in restricted data, switching
        language and possibility of submitting wrong data. Asserts if side menu gets extended upon submitting players data.
        Time sleeps added to support test execution.
        Caution:POSSIBLE FALSE POSITIVE!"""

        LoginPage.user_log_in_to_english(self)
        AddPlayer.path_to_add_player(self)
        BasePage.language_detect_from_dropdown(self)
        AddPlayer.create_translation_dictionary(self)
        AddPlayer.address_dictionary_translation_check(self)
        BasePage.webpage_language_address_check(self)
        AddPlayer.add_player_form_restricted_data_only_fill_up(self)
        Dashboard.dashboard_menu_language_change_button_click(self)
        print("Language changed manually via menu option")
        time.sleep(2)
        BasePage.language_detect_from_dropdown(self)
        AddPlayer.create_translation_dictionary(self)
        AddPlayer.address_dictionary_translation_check(self)
        BasePage.webpage_language_address_check(self)
        AddPlayer.add_player_form_submit_button_click(self)
        BasePage.wait_for_menu_extension_to_appear(self, locator_address=EditPlayer.menu_extension_check_reports_visible_xpath)
        time.sleep(2)
        BasePage.assert_page_redirected_correctly(self, word_to_check="edit")

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