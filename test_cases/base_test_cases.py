from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage


class BaseTestCases(BasePage):

    def assert_title_of_page_for_testing(self, expected_title):
        """Checking if user is on correct page via its title"""
        print(f"Asserting {self.driver.title} vs {expected_title}")
        assert self.driver.title == expected_title

    def assert_element_text(self, driver, text_element_xpath, element_text_expected_text):
        """Comparing expected text with observed value from web element

            :param driver: webdriver instance
            :param text_element_xpath: xpath to element with text to be observed
            :param element_text_expected_text: text what we expecting to be found
            :return: None
        """
        element = driver.find_element(by=By.XPATH, value=text_element_xpath)
        element_text = element.text
        print(f"Asserting {element_text_expected_text} vs {element_text}... ")
        assert element_text_expected_text == element_text

    def assert_page_redirected_partly(self, url_to_check):
        """Checking if user gets redirected from adding player form to editing the same form"""
        print(f"Checking if /'{url_to_check}'/ is in {BasePage.get_page_url(self)}")
        self.assertIn(url_to_check, BasePage.get_page_url(self))

    def assert_user_incorrect_login_error_presence(self):
        """Checking if user gets an incorrect password error upon typing incorrect password"""
        BasePage.wait_for_element_to_be_present(self, locator=LoginPage.incorrect_password_error_xpath)
        self.assertIsNotNone(LoginPage.incorrect_password_error_xpath)