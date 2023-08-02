import os
import unittest
from selenium import webdriver
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from test_cases.base_test_cases import BaseTestCases
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

    def test_user_log_in_incorrect_password(self):
        LoginPage.user_log_in_incorrect_password(self)
        BaseTestCases.assert_user_incorrect_login_error_presence(self)
        BaseTestCases.assert_element_text(self, driver=self.driver,
                                          text_element_xpath=LoginPage.incorrect_password_error_xpath,
                                          element_text_expected_text=BasePage.get_element_text(self, locator=LoginPage.incorrect_password_error_xpath))
        BaseTestCases.assert_title_of_page_for_testing(self, expected_title=BasePage.get_page_title(self, BasePage.get_page_url(self)))

    def test_user_log_in_to_dashboard(self):
        LoginPage.user_log_in(self)
        BasePage.wait_for_element_to_be_clickable(self, locator=Dashboard.add_player_button_xpath)
        BaseTestCases.assert_title_of_page_for_testing(self, expected_title=BasePage.get_page_title(self, BasePage.get_page_url(self)))

    @classmethod
    def tearDown(self):
        if BasePage.get_page_url(self) != 'https://scouts-test.futbolkolektyw.pl/en/login?redirected=true':
            Dashboard.dashboard_sign_out_button_click(self)
        else:
            pass
        BasePage.wait_for_element_to_be_clickable(self, locator=LoginPage.sign_in_button_xpath)
        self.driver.quit()
