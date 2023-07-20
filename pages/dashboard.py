from pages.base_page import BasePage
from pages.login_page import LoginPage


class DashboardXpaths(BasePage):
    shortcuts_add_player_button_xpath = "//child::div[contains(@class,'MuiGrid-root MuiGrid-item')][2]//button"
    scouts_panel_dev_team_contact_link_xpath = "//a[contains(@class, 'MuiButtonBase-root MuiButton-root')]"
    activity_last_created_player_link_xpath = "//child::div[contains(@class,'MuiGrid-root MuiGrid-item')][3]//a[1]/button"
    activity_last_updated_player_link_xpath = "//a[2]/button"
    activity_last_created_match_link_xpath = "//a[3]/button"
    activity_last_updated_match_link_xpath = "//a[4]/button"
    activity_last_updated_report_link_xpath = "//a[5]/button"
    menu_players_link_xpath = "//child::ul[1]/div[2]"
    menu_language_xpath = "//child::ul[2]/div[1]"
    menu_sign_out = "//child::ul[2]/div[2]"


class Dashboard(BasePage):
    add_player_button_xpath = "//div[2]//a/button"
    logout_xpath = "//div[1]/ul[2]/div[2]"
    activity_last_created_match_link_xpath = "//a[3]/button"

    def click_on_add_player_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=Dashboard.add_player_button_xpath)
        return self.click_on_the_element(self.add_player_button_xpath)

    def click_on_sign_out_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=Dashboard.logout_xpath)
        return self.click_on_the_element(self.logout_xpath)

    def click_on_last_created_match_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=Dashboard.activity_last_created_match_link_xpath)
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