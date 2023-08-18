import unittest
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from pages.matches_list_of_player_page import MatchesListOfPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
import time


class TestMatchesListPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        print("\nRunning test...")

    def test_path_to_matches_per_player_list_en(self):
        """Checks webpage translation upon English language choice at login and if user is redirected
        to get to correct webpage upon clicking"""

        LoginPage.user_log_in_to_english(self)
        MatchesListOfPlayer.path_to_matches_of_player(self)
        BasePage.wait_for_menu_extension_to_appear(self, locator_address=Dashboard.menu_extend_reports_name_text_xpath)
        MatchesListOfPlayer.create_translation_dictionary(self)
        MatchesListOfPlayer.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="matches")

        BasePage.assert_element_text(self, driver=self.driver,
                                          text_element_xpath=MatchesListOfPlayer.add_match_label_xpath,
                                          element_text_expected_text=BasePage.get_element_text(self, locator=MatchesListOfPlayer.add_match_label_xpath))

    def test_path_to_matches_per_player_list_pl(self):
        """Checks webpage translation upon Polish language choice at login and if user is redirected
        to correct webpage upon clicking"""

        LoginPage.user_log_in_to_polish(self)
        MatchesListOfPlayer.path_to_matches_of_player(self)
        BasePage.wait_for_menu_extension_to_appear(self, locator_address=Dashboard.menu_extend_reports_name_text_xpath)
        MatchesListOfPlayer.create_translation_dictionary(self)
        MatchesListOfPlayer.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="matches")

        BasePage.assert_element_text(self, driver=self.driver,
                                          text_element_xpath=MatchesListOfPlayer.add_match_label_xpath,
                                          element_text_expected_text=BasePage.get_element_text(self, locator=MatchesListOfPlayer.add_match_label_xpath))

    def test_matches_per_player_list_pl_lang_switch(self):
        """Checks webpage translation upon Polish language choice at login and if user is redirected
         to correct webpage upon clicking. Time sleep added to support test execution"""

        LoginPage.user_log_in_to_polish(self)
        MatchesListOfPlayer.path_to_matches_of_player(self)
        BasePage.wait_for_menu_extension_to_appear(self, locator_address=Dashboard.menu_extend_reports_name_text_xpath)
        MatchesListOfPlayer.create_translation_dictionary(self)
        MatchesListOfPlayer.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="matches")
        Dashboard.dashboard_menu_language_change_button_click(self)
        print("Language changed manually via menu option")
        time.sleep(2)
        MatchesListOfPlayer.create_translation_dictionary(self)
        MatchesListOfPlayer.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="matches")

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
