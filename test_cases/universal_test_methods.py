import time
import os
from selenium import webdriver

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class UniversalTestMethods():
    page_url = "https://medium.com/"
    expected_title = "Medium – Where good ideas find you."

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def get_page_title(self, page_url):
        self.driver.get(page_url)
        return self.driver.title
        time.sleep(5)

    def title_of_page_for_testing(self, page_url, expected_title):
        print(f"Asserting {UniversalTestMethods.get_page_title(page_url)} vs {expected_title}...")
        assert UniversalTestMethods.get_page_title(page_url) == expected_title

    @classmethod
    def tearDown(self):
        self.driver.quit()