import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.players_page import PlayersPage


class MatchesListOfPlayer(BasePage):

    actions_edit_button_xpath = "//tr[1]/td[9]//button"
    actions_create_report_button_xpath = "//tr[1]/td[10]//button"
    actions_start_report_button_xpath = "//tr[1]/td[11]//button"

    add_match_button_xpath = "//main/a/button"
    add_match_label_xpath = "//a//span[1]"
    add_match_text_en = "ADD MATCH"
    add_match_text_pl = "DODAJ MECZ"

    my_team_label_text_xpath = "//th[1]"
    my_team_text_en = "My team"
    my_team_text_pl = "Drużyna zawodnika"

    my_team_score_label_text_xpath = "//th[2]"
    my_team_score_text_en = "My team score"
    my_team_score_text_pl = "Zdobyte gole"

    enemy_team_score_label_text_xpath = "//th[3]"
    enemy_team_score_text_en = "Enemy team score"
    enemy_team_score_text_pl = "Stracone gole"

    enemy_team_label_text_xpath = "//th[4]"
    enemy_team_text_en = "Enemy team"
    enemy_team_text_pl = "Drużyna przeciwna"

    date_label_text_xpath = "//th[5]"
    date_team_text_en = "Date"
    date_team_text_pl = "Data"

    time_played_text_xpath = "//th[6]"
    time_played_text_en = "Time played"
    time_played_text_pl = "Czas gry"

    rating_text_xpath = "//th[7]"
    rating_text_en = "Rating"
    rating_text_pl = "Recenzja"

    author_text_xpath = "//th[8]"
    author_text_en = "Author"
    author_text_pl = "Autor"

    actions_text_xpath = "//th[9]"
    actions_text_en = "Actions"
    actions_text_pl = "Akcje"

    def path_to_matches_of_player(self):
        """User's path to matches of player list"""

        Dashboard.dashboard_menu_players_button_click(self)
        PlayersPage.edit_first_player_from_table_xpath_click(self)
        Dashboard.extended_dashboard_matches_button_click(self)

    def create_translation_dictionary(self):
        """Creates a translation dictionary"""

        time.sleep(2)
        add_match_label_xpath = self.driver.find_element(By.XPATH, "//a//span[1]").text
        my_team_label_text_xpath = self.driver.find_element(By.XPATH, "//th[1]").text
        my_team_score_label_text_xpath = self.driver.find_element(By.XPATH, "//th[2]").text
        enemy_team_score_label_text_xpath = self.driver.find_element(By.XPATH, "//th[3]").text
        enemy_team_label_text_xpath = self.driver.find_element(By.XPATH, "//th[4]").text
        date_label_text_xpath = self.driver.find_element(By.XPATH, "//th[5]").text
        time_played_text_xpath = self.driver.find_element(By.XPATH, "//th[6]").text
        rating_text_xpath = self.driver.find_element(By.XPATH, "//th[7]").text
        author_text_xpath = self.driver.find_element(By.XPATH, "//th[8]").text
        actions_text_xpath = self.driver.find_element(By.XPATH, "//th[9]").text
        menu_main_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[1]/div[1]/div[2]/span").text
        extended_menu_language_xpath = self.driver.find_element(By.XPATH, "//div[1]//ul[3]/div[1]/div[2]/span").text
        menu_logout_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[2]").text
        menu_extend_matches_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[2]/div[2]/span").text
        menu_extend_reports_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[3]/div[2]/span").text

        """Xpath for language detection - it will search for language tab and show 'Polski' option if webpage is 
        translated to English or 'English' option if webpage is translated to Polish"""
        global language_detect_xpath
        language_detect_xpath = self.driver.find_element(By.XPATH, "//span[contains(text(), 'English') or contains(text(), 'Polski')]").text

        global language_page_version_pl
        language_page_version_pl = {
            add_match_label_xpath: MatchesListOfPlayer.add_match_text_pl, my_team_label_text_xpath: MatchesListOfPlayer.my_team_text_pl,
            my_team_score_label_text_xpath: MatchesListOfPlayer.my_team_score_text_pl,
            enemy_team_score_label_text_xpath: MatchesListOfPlayer.enemy_team_score_text_pl,
            enemy_team_label_text_xpath: MatchesListOfPlayer.enemy_team_text_pl,
            date_label_text_xpath: MatchesListOfPlayer.date_team_text_pl, time_played_text_xpath: MatchesListOfPlayer.time_played_text_pl,
            rating_text_xpath: MatchesListOfPlayer.rating_text_pl, author_text_xpath: MatchesListOfPlayer.author_text_pl,
            actions_text_xpath: MatchesListOfPlayer.actions_text_pl, menu_main_name_text_xpath: Dashboard.menu_main_name_page_pl, extended_menu_language_xpath: Dashboard.menu_language_name_en,
            menu_logout_xpath: Dashboard.menu_logout_name_pl, menu_extend_matches_name_text_xpath: Dashboard.menu_extend_matches_name_pl,
            menu_extend_reports_name_text_xpath: Dashboard.menu_extend_reports_name_pl
            }

        global language_page_version_en
        language_page_version_en = {
            add_match_label_xpath: MatchesListOfPlayer.add_match_text_en, my_team_label_text_xpath: MatchesListOfPlayer.my_team_text_en,
            my_team_score_label_text_xpath: MatchesListOfPlayer.my_team_score_text_en,
            enemy_team_score_label_text_xpath: MatchesListOfPlayer.enemy_team_score_text_en,
            enemy_team_label_text_xpath: MatchesListOfPlayer.enemy_team_text_en,
            date_label_text_xpath: MatchesListOfPlayer.date_team_text_en, time_played_text_xpath: MatchesListOfPlayer.time_played_text_en,
            rating_text_xpath: MatchesListOfPlayer.rating_text_en, author_text_xpath: MatchesListOfPlayer.author_text_en,
            actions_text_xpath: MatchesListOfPlayer.actions_text_en, menu_main_name_text_xpath: Dashboard.menu_main_name_page_en, extended_menu_language_xpath: Dashboard.menu_language_name_pl,
            menu_logout_xpath: Dashboard.menu_logout_name_en, menu_extend_matches_name_text_xpath: Dashboard.menu_extend_matches_name_en,
            menu_extend_reports_name_text_xpath: Dashboard.menu_extend_reports_name_en
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
