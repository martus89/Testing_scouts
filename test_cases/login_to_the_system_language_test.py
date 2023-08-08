import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service

language_page_version_en = {}
language_page_version_pl = {}


class LanguageLoginPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        print("Running test...")

    # def create_translation_dictionary(self):
    #     password_label_xpath = self.driver.find_element(By.XPATH, "//label[@for='password']").text
    #     sign_in_button_text_xpath = self.driver.find_element(By.XPATH, "//button/span").text
    #     password_reminder_field_text_xpath = self.driver.find_element(By.XPATH, "//div[1]/a").text
    #     panel_main_name_field_text_xpath = self.driver.find_element(By.XPATH, "//div[1]/h5").text
    #
    #     global language_page_version_pl
    #     language_page_version_pl = {panel_main_name_field_text_xpath: LoginPage.panel_main_name_text_pl,
    #                                 password_reminder_field_text_xpath: LoginPage.password_reminder_text_pl,
    #                                 sign_in_button_text_xpath: LoginPage.sign_in_button_text_pl,
    #                                 password_label_xpath: LoginPage.password_text_pl}
    #
    #     global language_page_version_en
    #     language_page_version_en = {panel_main_name_field_text_xpath: LoginPage.panel_main_name_text_en,
    #                                     password_reminder_field_text_xpath: LoginPage.password_reminder_text_en,
    #                                     sign_in_button_text_xpath: LoginPage.sign_in_button_text_en,
    #                                     password_label_xpath: LoginPage.password_text_en}

    # def translation_check(self):
    #     self.create_translation_dictionary()
    #     if LoginPage.language_dropdown_input_lang_detect_xpath_return(self) == "Polski":
    #         page_dictionary = language_page_version_pl
    #         print(page_dictionary)
    #     elif LoginPage.language_dropdown_input_lang_detect_xpath_return(self) == "English":
    #         page_dictionary = language_page_version_en
    #         print(page_dictionary)
    #     else:
    #         print("Language not detected")
    #
    #     for field_name in page_dictionary:
    #         assert field_name == page_dictionary[field_name]

    def test_polish_language_translation_check(self):
        LoginPage.language_change_to_polish(self)
        print(LoginPage.language_dropdown_input_lang_detect_xpath_return(self))
        LoginPage.translation_check(self)

    def test_english_language_translation_check(self):
        LoginPage.language_change_to_english(self)
        print(LoginPage.language_dropdown_input_lang_detect_xpath_return(self))
        LoginPage.translation_check(self)

    @classmethod
    def tearDown(self):
        if BasePage.get_page_url(self) != 'https://scouts-test.futbolkolektyw.pl/en/login?redirected=true' or BasePage.get_page_url(self) != 'https://scouts-test.futbolkolektyw.pl/pl/login?redirected=true':
            Dashboard.dashboard_menu_sign_out_button_click(self)
        else:
            pass
        self.driver.quit()