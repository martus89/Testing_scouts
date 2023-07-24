import os
import unittest
from selenium import webdriver
from pages.add_match import AddMatch
from pages.base_page import BasePage
from pages.dashboard import Dashboard
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

    def test_user_sign_out(self):
        LoginPage.user_log_in(self)
        Dashboard.dashboard_sign_out_button_click(self)
        BaseTestCases.assert_title_of_page_for_testing(self, expected_title=BasePage.get_page_title(self, page_url=LoginPage.login_url))

    def test_open_last_created_match(self):
        LoginPage.user_log_in(self)
        Dashboard.dashboard_activity_last_created_match_click(self)
        BaseTestCases.assert_element_text(self, driver=self.driver,
                                          text_element_xpath=AddMatch.form_submit_button_xpath,
                                          element_text_expected_text=BasePage.get_element_text(self, locator=AddMatch.form_submit_button_xpath))

    @classmethod
    def tearDown(self):
        self.driver.quit()
