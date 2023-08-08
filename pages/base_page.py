from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.settings import DEFAULT_LOCATOR_TYPE

class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        self.wait_for_element_to_be_clickable(selector)
        return self.driver.find_element(selector_type, selector).click()

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        """Waiting for element of page to be clickable"""
        wait = WebDriverWait(self.driver, timeout=60)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def wait_for_element_to_be_present(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        """Waiting for element of page to be visible for user's eye"""
        wait = WebDriverWait(self.driver, timeout=60)
        element_present = wait.until(EC.visibility_of_element_located((locator_type, locator)))

    def get_page_title(self, page_url):
        """Fetching page title from url's address of current webpage user is on"""
        self.driver.get(page_url)
        return self.driver.title

    def explicit_wait(self):
        self.driver.implicitly_wait(4)

    def get_page_url(self):
        """Fetching url address of current webpage user is on"""
        driver = self.driver
        current_url = driver.current_url
        return current_url

    def get_element_text(self, locator):
        """Waiting for element of page to be visible for user's eye"""
        BasePage.wait_for_element_to_be_present(self, locator=locator)
        element = self.driver.find_element(By.XPATH, locator)
        print(f"Element text is {element.text}")
        return element.text

    def check_language_of_webpage(self):
        """Defines the language of page based on its address"""
        players_page_url = BasePage.get_page_url(self)
        actual_language_from_url = players_page_url[38:40]
        if actual_language_from_url == "en":
            print("Page should be all translated to english")
        elif actual_language_from_url == "pl":
            print("Page should be all translated to polish")
        return actual_language_from_url

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
        print(f"Asserting text of the element is {element_text_expected_text} vs {element_text}... ")
        assert element_text_expected_text == element_text

    def assert_page_redirected_partly(self, url_to_check):
        """Checking if user gets redirected from adding player form to editing the same form"""
        print(f"Checking if /'{url_to_check}'/ is in {BasePage.get_page_url(self)}")
        self.assertIn(url_to_check, BasePage.get_page_url(self))


