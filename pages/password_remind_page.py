import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage

# !!!!!FIXED WITH NEW FUNCTIONS!!!!
class RemindPasswordPage(BasePage):

    password_reminder_page_url_pl = "https://scouts-test.futbolkolektyw.pl/pl/remind"
    password_reminder_page_url_en = "https://scouts-test.futbolkolektyw.pl/en/remind"

    password_reminder_box_heading_text_xpath = "//h5"
    password_reminder_box_heading_en = "Remind password"
    password_reminder_box_heading_pl = "Przypomnij hasło"

    password_reminder_email_input_xpath = "//input[@name='email']"

    password_reminder_back_to_login_page_button_xpath = "//div[1]/div[1]/a"
    password_reminder_back_to_login_page_button_label_xpath = "//div[1]/div[1]/a"
    password_reminder_back_to_login_page_button_label_en = "Back to sign in"
    password_reminder_back_to_login_page_button_label_pl = "Wróć do zaloguj"

    password_reminder_language_change_xpath = "//div[@role='button']"
    password_reminder_language_change_value_en = "English"
    password_reminder_language_change_value_pl = "Polski"

    password_reminder_submit_button_xpath = "//button/span[2]"
    password_reminder_submit_button_label_xpath = "//button/span[1]"
    password_reminder_submit_button_en = "SEND"
    password_reminder_submit_button_pl = "WYŚLIJ"

    dropdown_menu = "//div[1]//div[2]/div/div"

    def click_password_reminder(self):
        """Method supporting password_reminder_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=LoginPage.password_reminder_field_text_xpath)
        return self.click_on_the_element(LoginPage.password_reminder_field_text_xpath)

    def password_reminder_button_click(self):
        """User click on language dropdown menu"""
        pass_rem = RemindPasswordPage(self.driver)
        pass_rem.click_password_reminder()

    def assert_correct_webpage_redirect(self):
        """Asserting 'remind' phrase in webpage address to confirm correct redirect"""
        my_page_url = BasePage.get_page_url(self)[41:]
        assert my_page_url == "remind"
        print("Page redirected to reminder correctly")

    def dropdown_menu_click_on_dropdown(self):
        """Method supporting dropdown_menu_click_on(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.dropdown_menu)
        return self.click_on_the_element(LoginPage.dropdown_menu)

    def dropdown_menu_click_on(self):
        """User click on language dropdown menu"""
        dropdown_menu = RemindPasswordPage(self.driver)
        dropdown_menu.dropdown_menu_click_on_dropdown()

    def language_change_to_polish(self):
        """User changes language via dropdown to Polish"""
        RemindPasswordPage.dropdown_menu_click_on(self)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[3]/ul/li[1]').click()
        time.sleep(2)

    def language_change_to_english(self):
        """User changes language via dropdown to English"""
        LoginPage.dropdown_menu_click_on(self)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[3]/ul/li[2]').click()
        time.sleep(2)

    def language_dropdown_input_lang_detect_xpath_return(self):
        """Returns language chosen by user"""
        language_dropdown_input_lang_detect_xpath = self.driver.find_element(By.XPATH, "//div[1]//div[2]/div/div").text
        return language_dropdown_input_lang_detect_xpath

    def create_translation_dictionary(self):
        """Creates a translation dictionary"""
        password_reminder_box_heading_text_xpath = self.driver.find_element(By.XPATH, "//h5").text
        password_reminder_back_to_login_page_button_label_xpath = self.driver.find_element(By.XPATH, "//div[1]/div[1]/a").text
        password_reminder_submit_button_label_xpath = self.driver.find_element(By.XPATH, "//button/span[1]").text


        global language_page_version_pl
        language_page_version_pl = {password_reminder_box_heading_text_xpath: RemindPasswordPage.password_reminder_box_heading_pl,
                                    password_reminder_back_to_login_page_button_label_xpath: RemindPasswordPage.password_reminder_back_to_login_page_button_label_pl,
                                    password_reminder_submit_button_label_xpath: RemindPasswordPage.password_reminder_submit_button_pl}

        global language_page_version_en
        language_page_version_en = {password_reminder_box_heading_text_xpath: RemindPasswordPage.password_reminder_box_heading_en,
                                    password_reminder_back_to_login_page_button_label_xpath: RemindPasswordPage.password_reminder_back_to_login_page_button_label_en,
                                    password_reminder_submit_button_label_xpath: RemindPasswordPage.password_reminder_submit_button_en}

    def translation_check(self):
        """Based on language chosen in dropdown by user, checks if page elements have correct language"""
        RemindPasswordPage.create_translation_dictionary(self)
        if RemindPasswordPage.language_dropdown_input_lang_detect_xpath_return(self) == "Polski":
            page_dictionary = language_page_version_pl
            print("Your translations in Polish are OK")
        elif RemindPasswordPage.language_dropdown_input_lang_detect_xpath_return(self) == "English":
            page_dictionary = language_page_version_en
            print("Your translations in English are OK")
        else:
            print("Language not detected - check your webpage")

        for field_name in page_dictionary:
            assert field_name == page_dictionary[field_name]

    def remind_password_page_language_address_check(self):
        """Checks language in webpage address and compares to one chosen by user in dropdown"""
        my_page_url = BasePage.get_page_url(self)[38:]
        if RemindPasswordPage.language_dropdown_input_lang_detect_xpath_return(self) == "Polski":
            assert my_page_url == "pl/remind"
            print("Page correctly redirected in Polish")
        elif RemindPasswordPage.language_dropdown_input_lang_detect_xpath_return(self) == "English":
            assert my_page_url == "en/remind"
            print("Page correctly redirected in English")
        else:
            print("There is an issue somewhere with your webpage language choice")
