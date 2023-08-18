import unittest
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.edit_player_page import EditPlayer
from pages.login_page import LoginPage
from pages.players_page import PlayersPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
import time


class TestEditPlayerFromTable(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        print("\nRunning test...")

    def test_edit_first_player_from_table_en(self):
        """Checks translation of player's edit page and webpage redirect upon login in English"""

        LoginPage.user_log_in_to_english(self)
        Dashboard.dashboard_menu_players_button_click(self)
        PlayersPage.edit_first_player_from_table_xpath_click(self)
        BasePage.wait_for_element_to_be_visible(self, locator_address=Dashboard.menu_extend_reports_xpath)
        BasePage.wait_for_menu_extension_to_appear(self, locator_address=Dashboard.menu_extend_reports_name_text_xpath)
        EditPlayer.create_translation_dictionary(self)
        EditPlayer.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="edit")
        EditPlayer.check_players_name(self)

    def test_edit_first_player_from_table_lang_switch(self):
        """Checks translation with manual language switch of player's edit page and webpage redirect upon login
        in Polish"""

        LoginPage.user_log_in_to_polish(self)
        Dashboard.dashboard_menu_players_button_click(self)
        PlayersPage.edit_first_player_from_table_xpath_click(self)
        BasePage.wait_for_element_to_be_visible(self, locator_address=Dashboard.menu_extend_reports_xpath)
        BasePage.wait_for_menu_extension_to_appear(self, locator_address=Dashboard.menu_extend_reports_name_text_xpath)
        EditPlayer.create_translation_dictionary(self)
        EditPlayer.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="edit")
        Dashboard.dashboard_menu_language_change_button_click(self)
        print("Language changed manually via menu option")
        time.sleep(2)
        EditPlayer.create_translation_dictionary(self)
        EditPlayer.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="edit")
        EditPlayer.check_players_name(self)

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
