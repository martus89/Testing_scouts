import unittest
import os
from selenium import webdriver

from pages.dashboard import Dashboard
from test_cases.universal_test_methods import UniversalTestMethods
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


# Week 3 Subtask 4: Powtórzenie tego, co już wiemy

class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_path_to_add_player(self):
        Dashboard.dashboard_log_in(self)
        Dashboard.dashboard_add_player_button_click(self)

    def test_title_of_add_player(self):
        TestAddPlayer.test_path_to_add_player(self)
        page_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
        expected_title = "Add player"
        print(f"Asserting {UniversalTestMethods.get_page_title(self, page_url=page_url)} vs {expected_title}...")
        assert UniversalTestMethods.get_page_title(self, page_url=page_url) == expected_title

    @classmethod
    def tearDown(self):
        self.driver.quit()
