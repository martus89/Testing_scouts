from pages.base_page import BasePage


class RemindPasswordPage(BasePage):

    password_reminder_page_url = "https://scouts-test.futbolkolektyw.pl/pl/remind"
    password_reminder_box_text_xpath = "//h5"
    password_reminder_email_input_xpath = "//input[@name='email']"
    password_reminder_back_to_login_page_button_and_text_xpath = "//div[1]/div[1]/a"
    password_reminder_language_change_xpath = "//div[@role='button']"
    password_reminder_language_change_value_xpath = "//input[@aria-hidden='true']"
    password_reminder_submit_button_xpath = "//button/span[2]"
    password_reminder_submit_button_text_xpath = "//button/span[1]"




