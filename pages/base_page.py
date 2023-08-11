import time
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

    def get_page_title(self):
        """Fetching page title from url's address of current webpage user is on"""
        self.driver.get(BasePage.get_page_url(self))
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
        BasePage.wait_for_element_to_be_visible(self, locator_address=locator)
        element = self.driver.find_element(By.XPATH, locator)
        print(f"Element text is {element.text}")
        return element.text

    def assert_title_of_page_for_testing(self, expected_title):
        """Checking if user is on correct page via its title"""
        BasePage.get_page_title(self)
        print(f"Asserting {self.driver.title} vs {expected_title}")
        assert self.driver.title == expected_title

    def assert_element_text(self, driver, text_element_xpath, element_text_expected_text):
        """Comparing expected text with observed value from web element

            :param driver: webdriver instance
            :param text_element_xpath: xpath to element with text to be observed
            :param element_text_expected_text: text what we expecting to be found
            :return: None
        """
        element = driver.find_element(by=By.XPATH, value=text_element_xpath).text
        print(f"Asserting text of the element is {element_text_expected_text} vs {element}... ")
        assert element_text_expected_text == element

    def assert_page_redirected_correctly(self, word_to_check):
        """Checking if user gets redirected to correct subpage base on subpage naming convention"""
        print(f"Checking if /'{word_to_check}'/ is in URL {BasePage.get_page_url(self)[38:]} to confirm correct redirect")
        self.assertIn(word_to_check, BasePage.get_page_url(self))

    def language_detect_from_dropdown(self):
        """Returns language chosen by user"""
        time.sleep(2)
        language_options = ["Polski", "English"]
        global language_dropdown_input_lang_detect_xpath
        language_dropdown_input_lang_detect_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[1]/div[2]/span").text

        for index, language_name in enumerate(language_options):
            if language_name == language_dropdown_input_lang_detect_xpath:
                print(f"Current language chosen is {language_options[index-1]} and can be changed to {language_dropdown_input_lang_detect_xpath}")
            else:
                continue
        return language_dropdown_input_lang_detect_xpath

    def webpage_language_address_check(self):
        """Checks language in webpage address and compares to one chosen by user in dropdown"""
        language_slicing = BasePage.get_page_url(self)[38:]
        language_detect_xpath = self.driver.find_element(By.XPATH, "//span[contains(text(), 'English') or contains(text(), 'Polski')]").text

        if language_detect_xpath == "Polski":
            assert "en" in language_slicing
            print("Page URL shows language to be English")
        elif language_detect_xpath == "English":
            assert "pl" in language_slicing
            print("Page URL shows language to be Polski")
        else:
            print("There is an issue somewhere with your webpage language choice")

    def wait_for_menu_extension_to_appear(self, locator_address, locator_type=By.XPATH):
        """Assert menu extension appears after submitting player data"""
        wait = WebDriverWait(self.driver, timeout=70)
        element_present = wait.until(EC.visibility_of_element_located((locator_type, locator_address)))

        assert element_present
        if element_present:
            print("Menu extension is visible as planned - reports tab are visible")
        else:
            print("Menu extension not appearing - check what's wrong")

    def wait_for_element_to_be_visible(self, locator_address, locator_type=By.XPATH):
        """Assert element appears correctly and as planned"""
        wait = WebDriverWait(self.driver, timeout=70)
        element_present = wait.until(EC.visibility_of_element_located((locator_type, locator_address)))

        assert element_present
        if element_present:
            print("Webpage element is visible as planned")
        else:
            print("Webpage element not appearing - check what's wrong")