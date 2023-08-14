import unittest
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from pages.players_page import PlayersPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
import random
import time


class TestPlayersDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        """Set up of desired download file"""
        absolute_path = os.path.dirname(__file__)
        full_path = os.path.join(absolute_path, "file_download_test")
        op = webdriver.ChromeOptions()
        op.add_argument('--no-sandbox')
        op.add_argument('--verbose')
        op.add_argument("--disable-notifications")
        op.add_experimental_option("prefs", {
            "download.default_directory": full_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True})
        op.add_argument('--disable-gpu')
        op.add_argument('--disable-software-rasterizer')
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service, options=op)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        print("\nRunning test...")

    def test_download_file_verify_en(self):
        """Verifying if file gets downloaded to the desired file inside the project and renamed correctly upon
        login with English language"""

        LoginPage.user_log_in_to_english(self)
        Dashboard.dashboard_menu_players_button_click(self)
        PlayersPage.initiate_download_players_dashboard_file(self)
        file_download_absolute_path = os.path.dirname(__file__)
        file_download_relative_path = "file_download_test"
        file_download_full_path = os.path.join(file_download_absolute_path, file_download_relative_path)
        file_new_name = f"players_dashboard_download_{random.randint(0, 100)}.csv"
        old_file_name = f"{file_download_full_path}/tableDownload.csv"
        time.sleep(5)
        new_file_full_name = f"{file_download_full_path}/{file_new_name}"
        os.rename(old_file_name, new_file_full_name)
        print(f"Checking if {file_download_relative_path} folder contains {file_new_name}...")
        assert os.listdir(file_download_relative_path).__contains__(file_new_name), "File not found"

    def test_download_file_verify_pl(self):
        """Verifying if file gets downloaded to the desired file inside the project and renamed correctly upon
        login with Polish language"""

        LoginPage.user_log_in_to_polish(self)
        Dashboard.dashboard_menu_players_button_click(self)
        PlayersPage.initiate_download_players_dashboard_file(self)
        file_download_absolute_path = os.path.dirname(__file__)
        file_download_relative_path = "file_download_test"
        file_download_full_path = os.path.join(file_download_absolute_path, file_download_relative_path)
        file_new_name = f"players_dashboard_download_{random.randint(0, 100)}.csv"
        old_file_name = f"{file_download_full_path}/tableDownload.csv"
        time.sleep(5)
        new_file_full_name = f"{file_download_full_path}/{file_new_name}"
        os.rename(old_file_name, new_file_full_name)
        print(f"Checking if {file_download_relative_path} folder contains {file_new_name}...")
        assert os.listdir(file_download_relative_path).__contains__(file_new_name), "File not found"

    def test_players_page_translation_check(self):
        """Asserting correct translation of players page. Time sleeps added to support test execution."""

        LoginPage.user_log_in_to_polish(self)
        Dashboard.dashboard_menu_players_button_click(self)
        BasePage.wait_for_element_to_be_visible(self, locator_address=PlayersPage.players_file_download_button_xpath)
        PlayersPage.create_translation_dictionary(self)
        PlayersPage.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="players")
        Dashboard.dashboard_menu_language_change_button_click(self)
        print("Language changed manually via menu option")
        time.sleep(3)
        PlayersPage.create_translation_dictionary(self)
        PlayersPage.webpage_dictionary_language_check(self)
        BasePage.webpage_language_address_check(self)
        BasePage.assert_page_redirected_correctly(self, word_to_check="players")

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
