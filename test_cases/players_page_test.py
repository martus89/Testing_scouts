import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.add_match import AddMatch
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.players_page import PlayersDashboardPage
from test_cases.base_test_cases import BaseTestCases
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
import time
import os
import random
import urllib


class TestPlayersDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)


    #Still playing with that one - working file ;<<<

    # def test_download_players_dashboard_file(self):
    #     PlayersDashboardPage.path_to_players_file_download(self)
    #     BasePage.wait_for_element_to_be_clickable(self, locator=PlayersDashboardPage.players_file_download_button_xpath)
    #     download_link = self.driver.find_element(By.XPATH, PlayersDashboardPage.players_file_download_button_xpath)
    #
    #
    #     download_link.click()
    #     time.sleep(5)
    #     download_directory = full_path
    #     file_name = random.randint(10, 99)
    #     file_name = f'{file_name}.pdf'  # Replace with the expected file name
    #
    #     # Check if the file exists in the download directory
    #     file_path = os.path.join(download_directory, file_name)
    #     assert os.path.isfile(file_path), "File was not downloaded"

    # def test_1(self):
    #     absolute_path = os.path.dirname(__file__)
    #     relative_path = "file_download_test/"
    #     full_path_1 = os.path.join(absolute_path, relative_path)
    #
    #     download_directory = full_path_1
    #
    #     # Create the directory if it doesn't exist
    #
    #     # Set the download directory in the browser's preferences
    #     os.environ["HOME"] = download_directory  # for Linux/Unix/Mac
    #
    #
    #     PlayersDashboardPage.path_to_players_file_download(self)
    #     BasePage.wait_for_element_to_be_clickable(self, locator=PlayersDashboardPage.players_file_download_button_xpath)
    #     download_link = self.driver.find_element(By.XPATH, PlayersDashboardPage.players_file_download_button_xpath)
    #
    #
    #     download_link.click()
    #     time.sleep(5)
    #     download_directory = full_path_1
    #     file_name = random.randint(10, 99)
    #     file_name = f'{file_name}.pdf'  # Replace with the expected file name
    #
    #     # Check if the file exists in the download directory
    #     file_path = os.path.join(download_directory, file_name)
    #     assert os.path.isfile(file_path), "File was not downloaded"
    #     driver.quit()




    @classmethod
    def tearDown(self):
        self.driver.quit()
