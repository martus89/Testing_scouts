from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard import Dashboard


class AddPlayer(BasePage):
    add_player_page_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    add_player_expected_page_title = "Add player"
    add_player_submit_button_xpath = "//main//form/*/button[1]"
    add_player_form_name_xpath = "//input[@name='name']"
    add_player_form_surname_xpath = "//input[@name='surname']"
    add_player_form_main_position_xpath = "//input[@name='mainPosition']"
    add_player_form_age_xpath = "//input[@name='age']"
    test_add_player_form_name_input = " "
    test_add_player_form_surname_input = " "
    test_add_player_form_age_input = "15102024"
    test_add_player_form_main_position_input = " "


    def add_player_form_restricted_data_only_fill_up(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=AddPlayer.add_player_submit_button_xpath)
        name = self.driver.find_element(By.XPATH, AddPlayer.add_player_form_name_xpath)
        name.send_keys(AddPlayer.test_add_player_form_name_input)
        surname = self.driver.find_element(By.XPATH, AddPlayer.add_player_form_surname_xpath)
        surname.send_keys(AddPlayer.test_add_player_form_surname_input)
        age = self.driver.find_element(By.XPATH, AddPlayer.add_player_form_age_xpath)
        age.send_keys(AddPlayer.test_add_player_form_age_input)
        main_position = self.driver.find_element(By.XPATH, AddPlayer.add_player_form_main_position_xpath)
        main_position.send_keys(AddPlayer.test_add_player_form_main_position_input)
        AddPlayer.add_player_form_submit_button_click(self)

    def path_to_add_player(self):
        Dashboard.dashboard_log_in(self)
        Dashboard.dashboard_add_player_button_click(self)

    def click_on_submit_button(self):
        return self.click_on_the_element(self.add_player_submit_button_xpath)

    def add_player_form_submit_button_click(self):
        submit_form = AddPlayer(self.driver)
        BasePage.wait_for_element_to_be_clickable(self, locator=AddPlayer.add_player_submit_button_xpath)
        submit_form.click_on_submit_button()

    def add_player_url_for_check(self):
        driver = self.driver
        current_url = driver.current_url
        return current_url