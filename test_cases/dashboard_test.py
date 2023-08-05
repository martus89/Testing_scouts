import os
import unittest
from selenium import webdriver
from pages.add_match_of_player_page import AddMatch
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from test_cases.base_test_cases import BaseTestCases
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        print("Running test...")
        LoginPage.user_log_in(self)

    def test_user_sign_out(self):
        Dashboard.dashboard_menu_sign_out_button_click(self)
        BaseTestCases.assert_title_of_page_for_testing(self, expected_title=BasePage.get_page_title(self, page_url=LoginPage.login_url))

    def test_open_last_created_match(self):
        Dashboard.dashboard_activity_last_created_match_click(self)
        BaseTestCases.assert_element_text(self, driver=self.driver,
                                          text_element_xpath=AddMatch.form_submit_button_xpath,
                                          element_text_expected_text=BasePage.get_element_text(self, locator=AddMatch.form_submit_button_xpath))

    @classmethod
    def tearDown(self):
        if BasePage.get_page_url(self) != 'https://scouts-test.futbolkolektyw.pl/en/login?redirected=true':
            Dashboard.dashboard_menu_sign_out_button_click(self)
        else:
            pass
        BasePage.wait_for_element_to_be_clickable(self, locator=LoginPage.sign_in_button_xpath)
        print("Redirected back to login page - closing test down")
        self.driver.quit()
