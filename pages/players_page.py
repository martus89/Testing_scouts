from pages.base_page import BasePage


class PlayersPage(BasePage):

    table_name_xpath = "//th[1]//span[1]/div/div[1]"
    table_name_en = "Name"
    table_name_pl = "Imię"

    table_surname_xpath = "//th[2]//span[1]/div/div[1]"
    table_surname_en = "Surname"
    table_surname_pl = "Nazwisko"

    table_age_xpath = "//th[3]//span[1]/div/div[1]"
    table_age_en = "Age"
    table_age_pl = "Wiek"

    table_main_position_xpath = "//th[4]//span[1]/div/div[1]"
    table_main_position_en = "Main position"
    table_main_position_pl = "Pozycja"

    table_club_xpath = "//th[5]//span[1]/div/div[1]"
    table_club_en = "Club"
    table_club_pl = "Klub"

    table_rating_xpath = "//th[6]//span[1]/div/div[1]"
    table_rating_en = "Rating"
    table_rating_pl = "Recenzja"

    table_matches_xpath = "//th[7]/div"
    table_matches_en = "Matches"
    table_matches_pl = "Mecze"

    table_reports_xpath = "//th[8]/div"
    table_reports_en = "Reports"
    table_reports_pl = "Raporty"

    players_file_download_button_xpath = "//button[contains(@data-testid,'Download CSV')]"
    # players_file_print_button_xpath = "//button[contains(@data-testid,'Print-iconButton')]" -> add this to your tests

    def players_dashboard_download_click_on_download_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=self.players_file_download_button_xpath)
        return self.click_on_the_element(self.players_file_download_button_xpath)

    def initiate_download_players_dashboard_file(self):
        """User downloading player's csv file from player's dashboard"""
        file_download = PlayersPage(self.driver)
        file_download.players_dashboard_download_click_on_download_button()

    # def players_dashboard_print_click_on_download_button(self):
    #     BasePage.wait_for_element_to_be_clickable(self, locator=self.players_file_print_button_xpath)
    #     return self.click_on_the_element(self.players_file_print_button_xpath)

    # def initiate_print_players_dashboard_file(self):
    #     """User downloading player's csv file from player's dashboard"""
    #     file_print = PlayersPage(self.driver)
    #     file_print.players_file_print_button_xpath()
