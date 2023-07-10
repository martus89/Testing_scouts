from pages.base_page import BasePage
import time

from pages.login_page import LoginPage


# class Dashboard(BasePage):
#     shortcuts_add_player_button_xpath = "//child::div[contains(@class,'MuiGrid-root MuiGrid-item')][2]//button"
#     scouts_panel_dev_team_contact_link_xpath = "//a[contains(@class, 'MuiButtonBase-root MuiButton-root')]"
#     activity_last_created_player_link_xpath = "//child::div[contains(@class,'MuiGrid-root MuiGrid-item')][3]//a[1]/button"
#     activity_last_updated_player_link_xpath = "//child::div//a[2]/button"
#     activity_last_created_match_link_xpath = "//child::div//a[3]/button"
#     activity_last_updated_match_link_xpath = "//child::div//a[4]/button"
#     activity_last_updated_report_link_xpath = "//child::div//a[5]/button"
#     menu_players_link_xpath = "//child::ul[1]/div[2]"
#     menu_language_xpath = "//child::ul[2]/div[1]"
#     menu_sign_out = "//child::ul[2]/div[2]"


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    expected_title_add_player = "Add player"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    def log_in_to_dashboard(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email(LoginPage.email)
        user_login.type_in_password(LoginPage.password)
        user_login.click_on_login_button()

    def title_of_page(self):
        time.sleep(4)

        if self.get_page_title(self.dashboard_url) == self.expected_title:
            print(f"\n Task finished - {self.expected_title} is equal to {self.get_page_title(self.dashboard_url)}")
        else:
            print("Something went wrong - go bug hunting")

        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def add_player_title_of_page(self):
        time.sleep(4)
        assert BasePage.get_page_title(self.add_player_url) == self.expected_title_add_player
