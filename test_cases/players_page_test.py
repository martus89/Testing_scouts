import unittest
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.players_page import PlayersDashboardPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os
import random


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
        LoginPage.user_log_in(self)

    def test_download_file_verify(self):
        """Verifying if file gets downloaded to the desired file and renamed correctly"""
        PlayersDashboardPage.path_to_players_file_download(self)
        PlayersDashboardPage.download_players_dashboard_file(self)
        file_absolute_path = os.path.dirname(__file__)
        file_relative_path = "file_download_test"
        file_full_path = os.path.join(file_absolute_path, file_relative_path)
        file_new_name = f"players_dashboard_download_{random.randint(0, 100)}.csv"
        old_file_name = f"{file_full_path}/tableDownload.csv"
        new_file_full_name = f"{file_full_path}/{file_new_name}"
        os.rename(old_file_name, new_file_full_name)
        print(f"Checking if {file_relative_path} folder contains {file_new_name}...")
        assert os.listdir(file_relative_path).__contains__(file_new_name), "File not found"

    @classmethod
    def tearDown(self):
        if BasePage.get_page_url(self) != 'https://scouts-test.futbolkolektyw.pl/en/login?redirected=true':
            Dashboard.dashboard_sign_out_button_click(self)
        else:
            pass
        BasePage.wait_for_element_to_be_clickable(self, locator=LoginPage.sign_in_button_xpath)
        self.driver.quit()
