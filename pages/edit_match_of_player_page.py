import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.matches_list_of_player_page import MatchesListOfPlayer


class EditMatch(BasePage):

    edit_match_upper_heading_text = "//form/div[1]//span"
    actions_edit_button_xpath = "//tr[1]/td[9]//button"

    required_my_team_input_xpath = "//input[@name='myTeam']"
    required_my_team_label_xpath = "//form/div[2]//div[1]/div/label"
    required_my_team_label_en = "My team\u2009*"
    required_my_team_label_pl = "Drużyna zawodnika\u2009*"
    required_my_team_warning_xpath = "//div[2]//div[1]/div/p"

    required_enemy_team_input_xpath = "//input[@name='enemyTeam']"
    required_enemy_team_label_xpath = "//form/div[2]//div[2]/div/label"
    required_enemy_team_label_en = "Enemy team\u2009*"
    required_enemy_team_label_pl = "Drużyna przeciwna\u2009*"
    required_enemy_team_warning_xpath = "//div[2]//div[2]/div/p"

    required_my_team_score_input_xpath = "//input[@name='myTeamScore']"
    required_my_team_score_label_xpath = "//form/div[2]//div[3]/div/label"
    required_my_team_score_label_en = "My team score\u2009*"
    required_my_team_score_label_pl = "Zdobyte gole\u2009*"
    required_my_team_score_warning_xpath = "//div[2]//div[3]//p"

    required_enemy_team_score_input_xpath = "//input[@name='enemyTeamScore']"
    required_enemy_team_score_label_xpath = "//form/div[2]//div[4]/div/label"
    required_enemy_team_score_label_en = "Enemy team score\u2009*"
    required_enemy_team_score_label_pl = "Stracone gole\u2009*"
    required_enemy_team_score_warning_xpath = "//div[2]//div[4]//p"

    required_date_input_xpath = "//input[@name='date']"
    required_date_label_xpath = "//form/div[2]//div[5]/div/label"
    required_date_label_en = "Date\u2009*"
    required_date_label_pl = "Data\u2009*"
    required_date_warning_xpath = "//div[2]//div[5]//p"

    required_in_or_out_input_xpath = "//input[@name='matchAtHome']"
    home_match_label_text_xpath = "//fieldset//label[1]/span[2]"
    home_match_label_en = "Match at home"
    home_match_label_pl = "Mecz domowy"
    out_match_label_text_xpath = "//fieldset/div/label[2]/span[2]"
    out_match_label_en = "Match out home"
    out_match_label_pl = "Mecz wyjazdowy"

    submit_button_xpath = "//form/div[3]/button[1]"
    submit_button_text_xpath = "//form/div[3]/button[1]/span"
    submit_button_en = "SUBMIT"
    submit_button_pl = "SUBMIT"

    clear_button_xpath = "//form/div[3]/button[2]"
    clear_button_text_xpath = "//form/div[3]/button[2]/span[1]"
    clear_button_en = "CLEAR"
    clear_button_pl = "CLEAR"

    optional_tshirt_col_xpath = "//input[@name='tshirt']"
    optional_tshirt_col_label_xpath = "//div[2]//div[7]//label"
    optional_tshirt_col_label_en = "T-shirt color"
    optional_tshirt_col_label_pl = "Kolor koszulki"

    optional_league_xpath = "//input[@name='league']"
    optional_league_label_xpath = "//div[2]//div[8]//label"
    optional_league_label_en = "League"
    optional_league_label_pl = "Liga"

    optional_time_played_xpath = "//input[@name='timePlayed']"
    optional_time_played_label_xpath = "//div[2]//div[9]//label"
    optional_time_played_label_en = "Time played"
    optional_time_played_label_pl = "Czas gry"

    optional_number_played_xpath = "//input[@name='number']"
    optional_number_played_label_xpath = "//div[2]//div[10]//label"
    optional_number_played_label_en = "Number"
    optional_number_played_label_pl = "Numer"

    optional_web_match_xpath = "//input[@name='webMatch']"
    optional_web_match_label_xpath = "//div[2]//div[11]//label"
    optional_web_match_label_en = "Web match"
    optional_web_match_label_pl = "Web match"

    optional_general_xpath = "//input[@name='general']"
    optional_general_label_xpath = "//div[2]//div[12]//label"
    optional_general_label_en = "General"
    optional_general_label_pl = "General"

    optional_rating_xpath = "//input[@name='rating']"
    optional_rating_label_xpath = "//div[2]//div[13]//label"
    optional_rating_label_en = "Rating"
    optional_rating_label_pl = "Recenzja"

    events_list_heading_xpath = "//div[3]//div/div/span"
    events_list_heading_label_xpath = "//div[3]//div/div/span"
    events_list_heading_label_en = "Events list"
    events_list_heading_label_pl = "Lista zdarzeń"

    events_list_type_xpath = "//tr/th[1]"
    events_list_type_label_xpath = "//tr/th[1]"
    events_list_type_label_en = "Type"
    events_list_type_label_pl = "Typ"

    events_list_time_xpath = "//tr/th[2]"
    events_list_time_label_xpath = "//tr/th[2]"
    events_list_time_label_en = "Time"
    events_list_time_label_pl = "Czas"

    events_list_positive_xpath = "//tr/th[3]"
    events_list_positive_label_xpath = "//tr/th[3]"
    events_list_positive_label_en = "Positive"
    events_list_positive_label_pl = "Udany"

    events_list_metadata_xpath = "//tr/th[4]"
    events_list_metadata_label_xpath = "//tr/th[4]"
    events_list_metadata_label_en = "Meta data"
    events_list_metadata_label_pl = "Meta dane"

    events_list_comment_xpath = "//tr/th[5]"
    events_list_comment_label_xpath = "//tr/th[5]"
    events_list_comment_label_en = "Comment"
    events_list_comment_label_pl = "Komentarz"

    def click_on_edit_match_button(self):
        """Method supporting edit_match_first_row_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.actions_edit_button_xpath)
        return self.click_on_the_element(self.actions_edit_button_xpath)

    def edit_match_first_row_button_click(self):
        """User click on edit match function[button] of match available in first row"""
        first_match_edit = EditMatch(self.driver)
        first_match_edit.click_on_edit_match_button()

    def path_to_edit_first_match_of_player(self):
        """User path to edit match available in first row of list"""
        MatchesListOfPlayer.path_to_matches_of_player(self)
        EditMatch.edit_match_first_row_button_click(self)

    def create_translation_dictionary(self):
        """Creates a translation dictionary"""
        time.sleep(2)
        menu_main_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[1]/div[1]/div[2]/span").text
        extended_menu_language_xpath = self.driver.find_element(By.XPATH, "//div[1]//ul[3]/div[1]/div[2]/span").text
        menu_logout_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[2]").text
        menu_extend_matches_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[2]/div[2]/span").text
        menu_extend_reports_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[3]/div[2]/span").text
        required_my_team_label_xpath = self.driver.find_element(By.XPATH, "//form/div[2]//div[1]/div/label").text
        required_enemy_team_label_xpath = self.driver.find_element(By.XPATH, "//form/div[2]//div[2]/div/label").text
        required_my_team_score_label_xpath = self.driver.find_element(By.XPATH, "//form/div[2]//div[3]/div/label").text
        required_enemy_team_score_label_xpath = self.driver.find_element(By.XPATH, "//form/div[2]//div[4]/div/label").text
        required_date_label_xpath = self.driver.find_element(By.XPATH, "//form/div[2]//div[5]/div/label").text
        home_match_label_text_xpath = self.driver.find_element(By.XPATH, "//fieldset//label[1]/span[2]").text
        out_match_label_text_xpath = self.driver.find_element(By.XPATH, "//fieldset/div/label[2]/span[2]").text
        submit_button_text_xpath = self.driver.find_element(By.XPATH, "//form/div[3]/button[1]/span").text
        clear_button_text_xpath = self.driver.find_element(By.XPATH, "//form/div[3]/button[2]/span[1]").text
        optional_tshirt_col_label_xpath = self.driver.find_element(By.XPATH, "//div[2]//div[7]//label").text
        optional_league_label_xpath = self.driver.find_element(By.XPATH, "//div[2]//div[8]//label").text
        optional_time_played_label_xpath = self.driver.find_element(By.XPATH, "//div[2]//div[9]//label").text
        optional_number_played_label_xpath = self.driver.find_element(By.XPATH, "//div[2]//div[10]//label").text
        optional_web_match_label_xpath = self.driver.find_element(By.XPATH, "//div[2]//div[11]//label").text
        optional_general_label_xpath = self.driver.find_element(By.XPATH, "//div[2]//div[12]//label").text
        optional_rating_label_xpath = self.driver.find_element(By.XPATH, "//div[2]//div[13]//label").text
        events_list_heading_label_xpath = self.driver.find_element(By.XPATH, "//div[3]//div/div/span").text
        events_list_type_label_xpath = self.driver.find_element(By.XPATH, "//tr/th[1]").text
        events_list_time_label_xpath = self.driver.find_element(By.XPATH, "//tr/th[2]").text
        events_list_positive_label_xpath = self.driver.find_element(By.XPATH, "//tr/th[3]").text
        events_list_metadata_label_xpath = self.driver.find_element(By.XPATH, "//tr/th[4]").text
        events_list_comment_label_xpath = self.driver.find_element(By.XPATH, "//tr/th[5]").text


        """Xpath for language detection - it will search for language tab and show 'Polski' option if webpage is 
        translated to English or 'English' option if webpage is translated to Polish"""
        global language_detect_xpath
        language_detect_xpath = self.driver.find_element(By.XPATH, "//span[contains(text(), 'English') or contains(text(), 'Polski')]").text

        global language_page_version_pl
        language_page_version_pl = {
            menu_main_name_text_xpath: Dashboard.menu_main_name_page_pl,
            extended_menu_language_xpath: Dashboard.menu_language_name_en,
            menu_logout_xpath: Dashboard.menu_logout_name_pl,
            menu_extend_matches_name_text_xpath: Dashboard.menu_extend_matches_name_pl,
            menu_extend_reports_name_text_xpath: Dashboard.menu_extend_reports_name_pl,
            required_my_team_label_xpath: EditMatch.required_my_team_label_pl,
            required_enemy_team_label_xpath: EditMatch.required_enemy_team_label_pl,
            required_my_team_score_label_xpath: EditMatch.required_my_team_score_label_pl,
            required_enemy_team_score_label_xpath: EditMatch.required_enemy_team_score_label_pl,
            required_date_label_xpath: EditMatch.required_date_label_pl,
            home_match_label_text_xpath: EditMatch.home_match_label_pl,
            out_match_label_text_xpath: EditMatch.out_match_label_pl,
            submit_button_text_xpath: EditMatch.submit_button_pl,
            clear_button_text_xpath: EditMatch.clear_button_pl,
            optional_tshirt_col_label_xpath: EditMatch.optional_tshirt_col_label_pl,
            optional_league_label_xpath: EditMatch.optional_league_label_pl,
            optional_time_played_label_xpath: EditMatch.optional_time_played_label_pl,
            optional_number_played_label_xpath: EditMatch.optional_number_played_label_pl,
            optional_web_match_label_xpath: EditMatch.optional_web_match_label_pl,
            optional_general_label_xpath: EditMatch.optional_general_label_pl,
            optional_rating_label_xpath: EditMatch.optional_rating_label_pl,
            events_list_heading_label_xpath: EditMatch.events_list_heading_label_pl,
            events_list_type_label_xpath: EditMatch.events_list_type_label_pl,
            events_list_time_label_xpath: EditMatch.events_list_time_label_pl,
            events_list_positive_label_xpath: EditMatch.events_list_positive_label_pl,
            events_list_metadata_label_xpath: EditMatch.events_list_metadata_label_pl,
            events_list_comment_label_xpath: EditMatch.events_list_comment_label_pl

            }

        global language_page_version_en
        language_page_version_en = {
            menu_main_name_text_xpath: Dashboard.menu_main_name_page_en,
            extended_menu_language_xpath: Dashboard.menu_language_name_pl,
            menu_logout_xpath: Dashboard.menu_logout_name_en,
            menu_extend_matches_name_text_xpath: Dashboard.menu_extend_matches_name_en,
            menu_extend_reports_name_text_xpath: Dashboard.menu_extend_reports_name_en,
            required_my_team_label_xpath: EditMatch.required_my_team_label_en,
            required_enemy_team_label_xpath: EditMatch.required_enemy_team_label_en,
            required_my_team_score_label_xpath: EditMatch.required_my_team_score_label_en,
            required_enemy_team_score_label_xpath: EditMatch.required_enemy_team_score_label_en,
            required_date_label_xpath: EditMatch.required_date_label_en,
            home_match_label_text_xpath: EditMatch.home_match_label_en,
            out_match_label_text_xpath: EditMatch.out_match_label_en,
            submit_button_text_xpath: EditMatch.submit_button_en,
            clear_button_text_xpath: EditMatch.clear_button_en,
            optional_tshirt_col_label_xpath: EditMatch.optional_tshirt_col_label_en,
            optional_league_label_xpath: EditMatch.optional_league_label_en,
            optional_time_played_label_xpath: EditMatch.optional_time_played_label_en,
            optional_number_played_label_xpath: EditMatch.optional_number_played_label_en,
            optional_web_match_label_xpath: EditMatch.optional_web_match_label_en,
            optional_general_label_xpath: EditMatch.optional_general_label_en,
            optional_rating_label_xpath: EditMatch.optional_rating_label_en,
            events_list_heading_label_xpath: EditMatch.events_list_heading_label_en,
            events_list_type_label_xpath: EditMatch.events_list_type_label_en,
            events_list_time_label_xpath: EditMatch.events_list_time_label_en,
            events_list_positive_label_xpath: EditMatch.events_list_positive_label_en,
            events_list_metadata_label_xpath: EditMatch.events_list_metadata_label_en,
            events_list_comment_label_xpath: EditMatch.events_list_comment_label_en
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
