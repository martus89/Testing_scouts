import os
import unittest
from selenium import webdriver

from pages.login_page import LoginPage
from test_cases.universal_test_methods import UniversalTestMethods
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestUserLoginPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_user_log_in(self):
        LoginPage.user_log_in(self)

    def test_title_of_dashboard(self):
        LoginPage.user_log_in(self)
        page_url = "https://scouts-test.futbolkolektyw.pl/en"
        expected_title = "Scouts panel"
        print(f"Asserting {UniversalTestMethods.get_page_title(self, page_url=page_url)} vs {expected_title}...")
        assert UniversalTestMethods.get_page_title(self, page_url=page_url) == expected_title

    @classmethod
    def tearDown(self):
        self.driver.quit()
