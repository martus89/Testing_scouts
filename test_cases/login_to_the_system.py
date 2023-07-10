import os
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestUserLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        # self.driver.fullscreen_window() - sorry, off
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_dashboard_name(self):
        Dashboard.log_in_to_dashboard(self)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()
