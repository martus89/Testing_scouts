from pages.base_page import BasePage

# XPATH DONE
class RemindPasswordPage(BasePage):

    password_reminder_page_url_pl = "https://scouts-test.futbolkolektyw.pl/pl/remind"
    password_reminder_page_url_en = "https://scouts-test.futbolkolektyw.pl/pl/remind"
    pass_reminder_web_language_detector = password_reminder_page_url_pl[38:40]
    pass_reminder_full_web_address = password_reminder_page_url_pl[:38] + password_reminder_page_url_pl[38:40] + password_reminder_page_url_pl[40:]

    password_reminder_box_heading_text_xpath = "//h5/text()"
    password_reminder_box_heading_en = "Remind password"
    password_reminder_box_heading_pl = "Przypomnij hasło"

    password_reminder_email_input_xpath = "//input[@name='email']"

    password_reminder_back_to_login_page_button_xpath = "//div[1]/div[1]/a"
    password_reminder_back_to_login_page_button_label_xpath = "//div[1]/div[1]/a/text()"
    password_reminder_back_to_login_page_button_label_en = "Back to sign in"
    password_reminder_back_to_login_page_button_label_pl = "Wróć do zaloguj"

    password_reminder_language_change_xpath = "//div[@role='button']"
    password_reminder_language_change_input_xpath = "//div[1]//div[2]/div/input"
    password_reminder_language_change_value_xpath = "//div[1]//div[2]/div/div/text()"
    password_reminder_language_change_value_en = "English"
    password_reminder_language_change_value_pl = "Polski"

    password_reminder_submit_button_xpath = "//button/span[2]"
    password_reminder_submit_button_label_xpath = "//button/span[1]/text()"
    password_reminder_submit_button_en = "Send"
    password_reminder_submit_button_pl = "Wyślij"




