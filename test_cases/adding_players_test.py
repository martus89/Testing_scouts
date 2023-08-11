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

# DONE

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
        BasePage.assert_title_of_page_for_testing(self, expected_title=BasePage.get_page_title(self, page_url=AddPlayer.add_player_page_url_en))
        BasePage.language_detect(self)
        AddPlayer.create_translation_dictionary(self)
        AddPlayer.address_dictionary_translation_check(self)
        BasePage.login_page_language_address_check(self, language_slicing=BasePage.get_page_url(self)[38:40])

    def test_translation_add_player_pl(self):
        """Asserts language translation of webpage upon choice of Polish at login"""
        LoginPage.user_log_in_to_polish(self)
        AddPlayer.path_to_add_player(self)
        BasePage.assert_title_of_page_for_testing(self, expected_title=BasePage.get_page_title(self,page_url=AddPlayer.add_player_page_url_en))
        BasePage.language_detect(self)
        AddPlayer.create_translation_dictionary(self)
        AddPlayer.address_dictionary_translation_check(self)
        BasePage.login_page_language_address_check(self, language_slicing=BasePage.get_page_url(self)[38:40])

    def test_add_player_restricted_data_only_and_language_change(self):
        """Asserts language translation of webpage upon choice of English at login, filling in restricted data, switching
        language and possibility of submitting wrong data - POSSIBLE FALSE POSITIVE!"""
        LoginPage.user_log_in_to_english(self)
        AddPlayer.path_to_add_player(self)
        BasePage.language_detect(self)
        AddPlayer.create_translation_dictionary(self)
        AddPlayer.address_dictionary_translation_check(self)
        BasePage.login_page_language_address_check(self, language_slicing=BasePage.get_page_url(self)[38:40])
        AddPlayer.add_player_form_restricted_data_only_fill_up(self)
        Dashboard.dashboard_menu_language_change_button_click(self)
        time.sleep(3)
        BasePage.language_detect(self)
        AddPlayer.create_translation_dictionary(self)
        AddPlayer.address_dictionary_translation_check(self)
        BasePage.login_page_language_address_check(self, language_slicing=BasePage.get_page_url(self)[38:40])
        AddPlayer.add_player_form_submit_button_click(self)
        time.sleep(3)
        EditPlayer.wait_for_alert_turnaround(self)
        BasePage.assert_page_redirected_partly(self, url_to_check="edit")

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