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
        wait = WebDriverWait(self.driver, timeout=45)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def wait_for_element_to_be_present(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        """Waiting for element of page to be visible for user's eye"""
        wait = WebDriverWait(self.driver, timeout=45)
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
        print(f"Current URL is {current_url}")
        return current_url

    def get_element_text(self, locator):
        """Waiting for element of page to be visible for user's eye"""
        BasePage.wait_for_element_to_be_present(self, locator=locator)
        element = self.driver.find_element(By.XPATH, locator)
        print(f"Element text is {element.text}")
        return element.text