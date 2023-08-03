from pages.base_page import BasePage


class PlayersDashboardPage(BasePage):
    menu_player_button_xpath = "//ul[1]/div[@role='button'][2]"
    players_file_download_button_xpath = "//button[contains(@data-testid,'Download CSV')]"

    def players_page_menu_click_on_players_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=PlayersDashboardPage.menu_player_button_xpath)
        return self.click_on_the_element(self.menu_player_button_xpath)

    def players_dashboard_download_click_on_download_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=PlayersDashboardPage.players_file_download_button_xpath)
        return self.click_on_the_element(self.players_file_download_button_xpath)

    def path_to_players_file_download(self):
        players_path = PlayersDashboardPage(self.driver)
        players_path.players_page_menu_click_on_players_button()

    def download_players_dashboard_file(self):
        """User downloading player's csv file from player's dashboard"""
        PlayersDashboardPage.path_to_players_file_download(self)
        file_download = PlayersDashboardPage(self.driver)
        file_download.players_dashboard_download_click_on_download_button()




