import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestOpenWebpage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")



# Subtask 2: Nowy przypadek testowy

test_steps_completed = []


class TestMediumPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://medium.com/')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        test_steps_completed.append("Step 1: Initiating test")

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def test_check_title(self):
        actual_title = self.get_page_title('https://medium.com/')
        expected_title = "Medium – Where good ideas find you."

        if actual_title == expected_title:
            msg = "Test passed with success"
            print(msg)
        else:
            msg = "Test failed"
            print(msg)

        test_steps_completed.append(f"Step 2: " + msg)
        assert actual_title == expected_title

    @classmethod
    def tearDown(self):
        self.driver.quit()
        test_steps_completed.append("Step 3: Closing")
        print(test_steps_completed)
