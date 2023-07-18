import unittest
import os
from selenium import webdriver
from pages.add_player import AddPlayer
from pages.base_page import BasePage
from pages.edit_player import EditPlayer
from test_cases.base_test_cases import BaseTestCases
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_title_of_add_player(self):
        AddPlayer.path_to_add_player(self)
        BasePage.wait_for_element_to_be_clickable(self, locator=AddPlayer.add_player_submit_button_xpath)
        BaseTestCases.assert_title_of_page_for_testing(self, expected_title=BasePage.get_page_title(self, page_url=AddPlayer.add_player_page_url))

    def test_add_player_restricted_data_only(self):
        AddPlayer.path_to_add_player(self)
        AddPlayer.add_player_form_restricted_data_only_fill_up(self)
        BasePage.wait_for_element_to_be_clickable(self, locator=EditPlayer.edit_player_menu_player_name_xpath)
        EditPlayer.wait_for_alert_turnaround(self, locator=EditPlayer.edit_player_player_added_popup_container)
        BaseTestCases.assert_page_redirected_partly(self, url_to_check=EditPlayer.edit_player_url_for_check(self))

    @classmethod
    def tearDown(self):
        self.driver.quit()
