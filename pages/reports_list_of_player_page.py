import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.players_page import PlayersPage


# !!!!!FIXED WITH NEW FUNCTIONS!!!!

class ReportsListOfPlayer(BasePage):
    actions_edit_button_row_1xpath = "//tr[1]/td[8]//button"
    reports_button_extended_menu = "//div[1]//ul[2]/div[3]"
    edit_report_save_button = "//div[2]/div[1]/button"

    add_report_button_xpath = "//main/a/button"
    add_report_label_xpath = "//a//span[1]"
    add_report_text_en = "ADD REPORT"
    add_report_text_pl = "DODAJ RAPORT"

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
    date_text_en = "Date"
    date_text_pl = "Data"

    last_mod_text_xpath = "//th[6]"
    last_mod_text_en = "Last modified"
    last_mod_text_pl = "Ostatnia modyfikacja"

    author_text_xpath = "//th[7]"
    author_text_en = "Author"
    author_text_pl = "Autor"

    actions_text_xpath = "//th[8]"
    actions_text_en = "Actions"
    actions_text_pl = "Akcje"

    extended_menu_language_xpath = "//div[1]//ul[3]/div[1]/div[2]/span"

    def click_on_reports_extended_menu_button(self):
        """Method supporting dashboard_menu_main_page_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.reports_button_extended_menu)
        return self.click_on_the_element(self.reports_button_extended_menu)

    def reports_extended_menu_button_click(self):
        """User click on reports button from extended menu"""
        reports_extended = ReportsListOfPlayer(self.driver)
        reports_extended.click_on_reports_extended_menu_button()

    def click_on_edit_first_row_button(self):
        """Method supporting reports_first_row_edit_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.actions_edit_button_row_1xpath)
        return self.click_on_the_element(self.actions_edit_button_row_1xpath)

    def reports_first_row_edit_button_click(self):
        """User click on edit report from first row"""
        report_edit = ReportsListOfPlayer(self.driver)
        report_edit.click_on_edit_first_row_button()

    def path_to_reports_of_player(self):
        Dashboard.dashboard_menu_players_button_click(self)
        PlayersPage.edit_first_player_from_table_xpath_click(self)
        ReportsListOfPlayer.reports_extended_menu_button_click(self)

    # !!!!!FIXED WITH NEW FUNCTIONS!!!!
    def create_translation_dictionary(self):
        """Creates a translation dictionary"""
        time.sleep(2)
        add_report_label_xpath = self.driver.find_element(By.XPATH, "//div[1]/main/a//span[1]").text
        my_team_label_text_xpath = self.driver.find_element(By.XPATH, "//th[1]").text
        my_team_score_label_text_xpath = self.driver.find_element(By.XPATH, "//th[2]").text
        enemy_team_score_label_text_xpath = self.driver.find_element(By.XPATH, "//th[3]").text
        enemy_team_label_text_xpath = self.driver.find_element(By.XPATH, "//th[4]").text
        date_label_text_xpath = self.driver.find_element(By.XPATH, "//th[5]").text
        last_mod_text_xpath = self.driver.find_element(By.XPATH, "//th[6]").text
        author_text_xpath = self.driver.find_element(By.XPATH, "//th[7]").text
        actions_text_xpath = self.driver.find_element(By.XPATH, "//th[8]").text
        menu_main_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[1]/div[1]/div[2]/span").text
        extended_menu_language_xpath = self.driver.find_element(By.XPATH, "//div[1]//ul[3]/div[1]/div[2]/span").text
        menu_logout_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[2]").text
        menu_player_button_xpath = self.driver.find_element(By.XPATH,"//ul[1]/div[2]").text
        menu_extend_matches_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[2]/div[2]/span").text
        menu_extend_reports_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[3]/div[2]/span").text


        """Xpath for language detection - it will search for language tab and show 'Polski' option if webpage is 
        translated to English or 'English' option if webpage is translated to Polish"""
        global language_detect_xpath
        language_detect_xpath = self.driver.find_element(By.XPATH, "//span[contains(text(), 'English') or contains(text(), 'Polski')]").text

        global language_page_version_pl
        language_page_version_pl = {
            menu_main_name_text_xpath: Dashboard.menu_main_name_page_pl, extended_menu_language_xpath: Dashboard.menu_language_name_en,
            menu_logout_xpath: Dashboard.menu_logout_name_pl,
            add_report_label_xpath: ReportsListOfPlayer.add_report_text_pl, my_team_label_text_xpath: ReportsListOfPlayer.my_team_text_pl,
            my_team_score_label_text_xpath: ReportsListOfPlayer.my_team_score_text_pl,
            enemy_team_score_label_text_xpath: ReportsListOfPlayer.enemy_team_score_text_pl, enemy_team_label_text_xpath: ReportsListOfPlayer.enemy_team_text_pl,
            date_label_text_xpath: ReportsListOfPlayer.date_text_pl, last_mod_text_xpath: ReportsListOfPlayer.last_mod_text_pl,
            author_text_xpath: ReportsListOfPlayer.author_text_pl, actions_text_xpath: ReportsListOfPlayer.actions_text_pl,
            menu_player_button_xpath: Dashboard.menu_players_name_pl, menu_extend_matches_name_text_xpath: Dashboard.menu_extend_matches_name_pl,
            menu_extend_reports_name_text_xpath: Dashboard.menu_extend_reports_name_pl
        }

        global language_page_version_en
        language_page_version_en = {
            menu_main_name_text_xpath: Dashboard.menu_main_name_page_en, extended_menu_language_xpath: Dashboard.menu_language_name_pl,
            menu_logout_xpath: Dashboard.menu_logout_name_en, menu_player_button_xpath: Dashboard.menu_players_name_en,
            add_report_label_xpath: ReportsListOfPlayer.add_report_text_en, my_team_label_text_xpath: ReportsListOfPlayer.my_team_text_en,
            my_team_score_label_text_xpath: ReportsListOfPlayer.my_team_score_text_en, enemy_team_score_label_text_xpath: ReportsListOfPlayer.enemy_team_score_text_en,
            enemy_team_label_text_xpath: ReportsListOfPlayer.enemy_team_text_en, date_label_text_xpath: ReportsListOfPlayer.date_text_en,
            last_mod_text_xpath: ReportsListOfPlayer.last_mod_text_en, author_text_xpath: ReportsListOfPlayer.author_text_en,
            actions_text_xpath: ReportsListOfPlayer.actions_text_en,
            menu_extend_matches_name_text_xpath: Dashboard.menu_extend_matches_name_en,
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
