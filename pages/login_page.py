from pages.base_page import BasePage


# Subtask 3: Dodawanie selektorów do projektu - added below
class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[@class='MuiTouchRipple-root']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
