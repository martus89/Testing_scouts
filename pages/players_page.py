import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard


class PlayersPage(BasePage):

    table_name_xpath = "//th[1]//span[1]/div/div[1]/text()"
    table_name_en = "Name"
    table_name_pl = "Imię"

    table_surname_xpath = "//th[2]//span[1]/div/div[1]/text()"
    table_surname_en = "Surname"
    table_surname_pl = "Nazwisko"

    table_age_xpath = "//th[3]//span[1]/div/div[1]/text()"
    table_age_en = "Age"
    table_age_pl = "Wiek"

    table_main_position_xpath = "//th[4]//span[1]/div/div[1]/text()"
    table_main_position_en = "Main position"
    table_main_position_pl = "Pozycja"

    table_club_xpath = "//th[5]//span[1]/div/div[1]/text()"
    table_club_en = "Club"
    table_club_pl = "Klub"

    table_rating_xpath = "//th[6]//span[1]/div/div[1]/text()"
    table_rating_en = "Rating"
    table_rating_pl = "Recenzja"

    table_matches_xpath = "//th[7]/div/text()"
    table_matches_en = "Matches"
    table_matches_pl = "Mecze"

    table_reports_xpath = "//th[8]/div/text()"
    table_reports_en = "Reports"
    table_reports_pl = "Raporty"

    players_file_download_button_xpath = "//button[contains(@data-testid,'Download CSV')]"
    players_edit_first_player_from_table_xpath = "//td[1]"
    players_page_url_en = "https://scouts-test.futbolkolektyw.pl/en/players"
    players_page_url_pl = "https://scouts-test.futbolkolektyw.pl/pl/players"

    def players_dashboard_download_click_on_download_button(self):
        """Method supporting initiate_download_players_dashboard_file(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.players_file_download_button_xpath)
        return self.click_on_the_element(self.players_file_download_button_xpath)

    def initiate_download_players_dashboard_file(self):
        """User downloading player's csv file from player's dashboard"""
        file_download = PlayersPage(self.driver)
        file_download.players_dashboard_download_click_on_download_button()

    def edit_first_player_from_table_xpath_button(self):
        """Method supporting initiate_download_players_dashboard_file(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.players_edit_first_player_from_table_xpath)
        return self.click_on_the_element(self.players_edit_first_player_from_table_xpath)

    def edit_first_player_from_table_xpath_click(self):
        """Editing first player from player's list click"""
        edit_player = PlayersPage(self.driver)
        edit_player.edit_first_player_from_table_xpath_button()

    def create_translation_dictionary(self):
        """Creates a translation dictionary"""
        time.sleep(2)
        table_name_xpath = self.driver.find_element(By.XPATH, "//th[1]//span[1]/div/div[1]").text
        table_surname_xpath = self.driver.find_element(By.XPATH, "//th[2]//span[1]/div/div[1]").text
        table_age_xpath = self.driver.find_element(By.XPATH, "//th[3]//span[1]/div/div[1]").text
        table_main_position_xpath = self.driver.find_element(By.XPATH, "//th[4]//span[1]/div/div[1]").text
        table_club_xpath = self.driver.find_element(By.XPATH, "//th[5]//span[1]/div/div[1]").text
        table_rating_xpath = self.driver.find_element(By.XPATH, "//th[6]//span[1]/div/div[1]").text
        table_matches_xpath = self.driver.find_element(By.XPATH, "//th[7]/div").text
        table_reports_xpath = self.driver.find_element(By.XPATH, "//th[8]/div").text
        menu_main_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[1]/div[1]/div[2]/span").text
        menu_language_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[1]").text
        menu_logout_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[2]").text
        menu_player_button_xpath = self.driver.find_element(By.XPATH,"//ul[1]/div[2]").text

        """Xpath for language detection - it will search for language tab and show 'Polski' option if webpage is 
        translated to English or 'English' option if webpage is translated to Polish"""
        global language_detect_xpath
        language_detect_xpath = self.driver.find_element(By.XPATH, "//span[contains(text(), 'English') or contains(text(), 'Polski')]").text

        global language_page_version_pl
        language_page_version_pl = {
            table_name_xpath: PlayersPage.table_name_pl, table_surname_xpath: PlayersPage.table_surname_pl,
            table_age_xpath: PlayersPage.table_age_pl, table_main_position_xpath: PlayersPage.table_main_position_pl,
            table_club_xpath: PlayersPage.table_club_pl, table_rating_xpath: PlayersPage.table_rating_pl,
            table_matches_xpath: PlayersPage.table_matches_pl, table_reports_xpath: PlayersPage.table_reports_pl,
            menu_main_name_text_xpath: Dashboard.menu_main_name_page_pl, menu_language_xpath: Dashboard.menu_language_name_en,
            menu_logout_xpath: Dashboard.menu_logout_name_pl,
            menu_player_button_xpath: Dashboard.menu_players_name_pl,
        }

        global language_page_version_en
        language_page_version_en = {
            table_name_xpath: PlayersPage.table_name_en, table_surname_xpath: PlayersPage.table_surname_en,
            table_age_xpath: PlayersPage.table_age_en, table_main_position_xpath: PlayersPage.table_main_position_en,
            table_club_xpath: PlayersPage.table_club_en, table_rating_xpath: PlayersPage.table_rating_en,
            table_matches_xpath: PlayersPage.table_matches_en, table_reports_xpath: PlayersPage.table_reports_en,
            menu_main_name_text_xpath: Dashboard.menu_main_name_page_en, menu_language_xpath: Dashboard.menu_language_name_pl,
            menu_logout_xpath: Dashboard.menu_logout_name_en, menu_player_button_xpath: Dashboard.menu_players_name_en,
        }

    def webpage_dictionary_language_check(self):
        """Based on language chosen by user, checks if page elements display correct language"""
        time.sleep(2)
        language_options = ["Polski", "English"]
        page_dictionary = {}

        for index, language_name in enumerate(language_options):
            if language_name == language_detect_xpath:
                print(f"Current language chosen is {language_options[index-1]} and can be changed to {language_detect_xpath}")
            else:
                continue

        if language_detect_xpath == "Polski":
            page_dictionary = language_page_version_en
            print("Page dictionary is in English")
        elif language_detect_xpath == "English":
            page_dictionary = language_page_version_pl
            print("Page dictionary is in Polish")
        else:
            print("Language not detected - check your webpage")

        for field_name in page_dictionary:
            assert field_name == page_dictionary[field_name]
        print("Dictionary checked - everything seems in order")
