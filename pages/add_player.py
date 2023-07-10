import unittest
import time
import os
from selenium import webdriver

from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


# Week 3 Subtask 4: Powtórzenie tego, co już wiemy
# OK, but what to assert here?


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        # self.driver.fullscreen_window() - sorry, off
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player(self):
        user_login = LoginPage(self.driver)
        Dashboard.log_in_to_dashboard(self)
        time.sleep(5)
        user_login.click_on_add_player_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()