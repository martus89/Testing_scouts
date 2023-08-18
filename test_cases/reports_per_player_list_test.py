import unittest
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from pages.reports_list_of_player_page import ReportsListOfPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
import time


class TestReportsOfPlayerPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        print("\nRunning test...")

    def test_path_to_reports_per_player_en(self):
        """Checks webpage translation upon English language choice at login"""

        LoginPage.user_log_in_to_english(self)
        ReportsListOfPlayer.path_to_reports_of_player(self)
        time.sleep(3)
        BasePage.wait_for_menu_extension_to_appear(self, locator_address=Dashboard.menu_extend_reports_name_text_xpath)
        ReportsListOfPlayer.create_translation_dictionary(self)
        ReportsListOfPlayer.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="reports")

    def test_path_to_reports_per_player_pl(self):
        """Checks webpage translation upon Polish language choice at login"""

        LoginPage.user_log_in_to_polish(self)
        ReportsListOfPlayer.path_to_reports_of_player(self)
        time.sleep(3)
        BasePage.wait_for_menu_extension_to_appear(self, locator_address=Dashboard.menu_extend_reports_name_text_xpath)
        ReportsListOfPlayer.create_translation_dictionary(self)
        ReportsListOfPlayer.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="reports")

    def test_reports_per_player_language_switch(self):
        """Checks webpage translation using language switch from menu"""

        LoginPage.user_log_in_to_english(self)
        ReportsListOfPlayer.path_to_reports_of_player(self)
        time.sleep(3)
        Dashboard.dashboard_menu_language_change_button_click(self)
        print("Language changed manually via menu option")
        time.sleep(3)
        BasePage.wait_for_menu_extension_to_appear(self, locator_address=Dashboard.menu_extend_reports_name_text_xpath)
        ReportsListOfPlayer.create_translation_dictionary(self)
        ReportsListOfPlayer.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="reports")

    def test_reports_per_player_edit_report(self):
        """Checks user got redirected to report edit page upon choosing to edit a report from first row"""

        LoginPage.user_log_in_to_english(self)
        ReportsListOfPlayer.path_to_reports_of_player(self)
        time.sleep(3)
        ReportsListOfPlayer.reports_first_row_edit_button_click(self)
        BasePage.wait_for_element_to_be_visible(self, locator_address=ReportsListOfPlayer.edit_report_save_button)
        BasePage.wait_for_menu_extension_to_appear(self, locator_address=Dashboard.menu_extend_reports_name_text_xpath)
        time.sleep(3)
        BasePage.assert_element_text(self, driver=self.driver,
                                          text_element_xpath=ReportsListOfPlayer.edit_report_save_button,
                                          element_text_expected_text="SAVE")
        BasePage.assert_page_redirected_correctly(self, word_to_check="edit")
        BasePage.webpage_language_address_check(self)

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
