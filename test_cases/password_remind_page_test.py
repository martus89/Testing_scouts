import unittest
import os
from selenium import webdriver
from pages.base_page import BasePage
from pages.password_remind_page import RemindPasswordPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service

# DONE!
class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        print("Running test...")

    def test_password_reminder_redirect(self):
        """Checking if password reminder link redirects user to a webpage with /reminder in URL"""
        RemindPasswordPage.password_reminder_button_click(self)
        RemindPasswordPage.assert_correct_webpage_redirect(self)

    def test_password_reminder_redirect_language_check_en(self):
        """Checking if password reminder webpage has correct translation based upon language chosen from dropdown english"""
        RemindPasswordPage.password_reminder_button_click(self)
        RemindPasswordPage.language_change_to_english(self)
        RemindPasswordPage.translation_check(self)
        RemindPasswordPage.remind_password_page_language_address_check(self)

    def test_password_reminder_redirect_language_check_pl(self):
        """Checking if password reminder webpage has correct translation based upon language chosen from dropdown polish"""
        RemindPasswordPage.password_reminder_button_click(self)
        RemindPasswordPage.language_change_to_polish(self)
        RemindPasswordPage.translation_check(self)
        RemindPasswordPage.remind_password_page_language_address_check(self)

    @classmethod
    def tearDown(self):
        if BasePage.get_page_url(self) != RemindPasswordPage.password_reminder_page_url_pl and BasePage.get_page_url(self) != RemindPasswordPage.password_reminder_page_url_en:
            print("Wrong redirect - check your webpage")
        else:
            pass
        print("Closing down test")
        self.driver.quit()