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
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    add_player_button_xpath = "//div[2]//a/button"
    add_player_subpage_address = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    dashboard_title_page_url = "https://scouts-test.futbolkolektyw.pl/en"
    dashboard_expected_title = "Scouts panel"
    logout_xpath = "//div[1]/ul[2]/div[2]"
    activity_last_created_match_link_xpath = "//a[3]/button"

    def dashboard_log_in(self):
        LoginPage.user_log_in(self)

    def click_on_add_player_button(self):
        return self.click_on_the_element(self.add_player_button_xpath)

    def dashboard_add_player_button_click(self):
        add_player = Dashboard(self.driver)
        BasePage.wait_for_element_to_be_clickable(self, locator=Dashboard.add_player_button_xpath)
        add_player.click_on_add_player_button()

    def click_on_sign_out_button(self):
        return self.click_on_the_element(self.logout_xpath)

    def dashboard_sign_out_button_click(self):
        sign_out = Dashboard(self.driver)
        BasePage.wait_for_element_to_be_clickable(self, locator=Dashboard.logout_xpath)
        sign_out.click_on_sign_out_button()

    def click_on_last_created_match(self):
        return self.click_on_the_element(self.activity_last_created_match_link_xpath)

    def dashboard_activity_last_created_match_click(self):
        last_match = Dashboard(self.driver)
        BasePage.wait_for_element_to_be_clickable(self, locator=Dashboard.activity_last_created_match_link_xpath)
        last_match.click_on_last_created_match()