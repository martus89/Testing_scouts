import unittest
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

    def test_download_file_verify(self):
        """Verifying if file gets downloaded to the desired file and renamed correctly"""
        PlayersDashboardPage.download_players_dashboard_file(self)
        absolute_path = os.path.dirname(__file__)
        relative_path = "file_download_test"
        full_path = os.path.join(absolute_path, relative_path)
        new_name = f"players_dashboard_download_{random.randint(0, 100)}.csv"
        old_file_name = f"{full_path}/tableDownload.csv"
        new_file_name = f"{full_path}/{new_name}"
        os.rename(old_file_name, new_file_name)
        print(f"Checking if {relative_path} folder contains {new_name}...")
        assert os.listdir(relative_path).__contains__(new_name), "File not found"

    @classmethod
    def tearDown(self):
        self.driver.quit()
