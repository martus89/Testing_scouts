from pages.base_page import BasePage
from pages.login_page import LoginPage


class Dashboard(BasePage):
    add_player_button_xpath = "//button[contains(span,'Add player')]"
    logout_xpath = "//div[1]/ul[2]/div[2]"
    activity_last_created_match_link_xpath = "//a[3]/button"

    def click_on_add_player_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=self.add_player_button_xpath)
        return self.click_on_the_element(self.add_player_button_xpath)

    def click_on_sign_out_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=self.logout_xpath)
        return self.click_on_the_element(self.logout_xpath)

    def click_on_last_created_match_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=self.activity_last_created_match_link_xpath)
        return self.click_on_the_element(self.activity_last_created_match_link_xpath)

    def dashboard_log_in(self):
        LoginPage.user_log_in(self)

    def dashboard_sign_out_button_click(self):
        sign_out = Dashboard(self.driver)
        sign_out.click_on_sign_out_button()

    def dashboard_add_player_button_click(self):
        add_player = Dashboard(self.driver)
        add_player.click_on_add_player_button()

    def dashboard_activity_last_created_match_click(self):
        last_match = Dashboard(self.driver)
        last_match.click_on_last_created_match_button()