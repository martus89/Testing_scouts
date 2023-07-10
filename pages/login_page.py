from pages.base_page import BasePage


# Week 2 Subtask 3: Dodawanie selektorów do projektu - added below


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    email = "user01@getnada.com"
    password = "Test-1234"
    expected_title = "Scouts panel - sign in"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    title_of_box_xpath = "//[@id='__next']/form/div/div[1]/h5"
    header_of_box = "Scouts Panel"
    add_player_button_xpath = "//child::a[contains(@href, '/players/add')]/button"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    # Week 3 Subtask 1: Uzupełnienie strony logowania
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_login_button(self):
        return self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def click_on_add_player_button(self):
        return self.click_on_the_element(self.add_player_button_xpath)