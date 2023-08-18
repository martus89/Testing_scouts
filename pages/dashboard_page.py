import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Dashboard(BasePage):

    players_count_text_xpath = "//div[2]/div[1]/div/div[1]"
    players_count_text_en = "Players count"
    players_count_text_pl = "Ilość graczy"

    matches_count_text_xpath = "//div[2]/div[2]/div/div[1]"
    matches_count_text_en = "Matches count"
    matches_count_text_pl = "Ilość meczy"

    reports_count_text_xpath = "//div[2]/div[3]/div/div[1]"
    reports_count_text_en = "Reports count"
    reports_count_text_pl = "Ilość raportów"

    events_count_text_xpath = "//div[2]/div[4]/div/div[1]"
    events_count_text_en = "Events count"
    events_count_text_pl = "Ilość akcji"

    panel_name_en = "Scouts Panel"
    panel_name_pl = "Scouts Panel"
    panel_name_upper_blue = "//h6"
    panel_name_under_logo = "//div[2]/h2"

    under_logo_text_xpath = "//div[2]/p"
    under_logo_text_en = "Player, match and report management panel."
    under_logo_text_pl = "Panel zarządzania graczami, meczami i do tworzenia raportów."

    shortcuts_text_xpath = "//div[3]/div[2]//h2"
    shortcuts_text_en = "Shortcuts"
    shortcuts_text_pl = "Linki pomocnicze"

    add_player_button_xpath = "//div[2]//button"
    add_player_button_text_en = "ADD PLAYER"
    add_player_button_text_pl = "DODAJ GRACZA"

    activity_text_xpath = "//div[3]/div[3]//h2"
    activity_name_en = "Activity"
    activity_name_pl = "Aktywnosć"

    activity_last_created_player_text_xpath = "//div[3]//h6[1]"
    activity_last_created_player_name_en = "Last created player"
    activity_last_created_player_name_pl = "Ostatnio stworzony gracz"
    activity_last_created_player_link_xpath = "//div[3]/div[3]//a[1]/button"

    activity_last_updated_player_text_xpath = "//div[3]//h6[2]"
    activity_last_updated_player_name_en = "Last updated player"
    activity_last_updated_player_name_pl = "Ostatnio zaaktualizowany gracz"
    activity_last_updated_player_link_xpath = "//a[2]/button"

    activity_last_created_match_text_xpath = "//div[3]//h6[3]"
    activity_last_created_match_name_en = "Last created match"
    activity_last_created_match_name_pl = "Ostatnio stworzony mecz"
    activity_last_created_match_link_xpath = "//a[3]/button"

    activity_last_updated_match_text_xpath = "//div[3]//h6[4]"
    activity_last_updated_match_name_en = "Last updated match"
    activity_last_updated_match_name_pl = "Ostatnio zaaktualizowany mecz"
    activity_last_updated_match_link_xpath = "//a[4]/button"

    activity_last_updated_report_text_xpath = "//div[3]//h6[5]"
    activity_last_updated_report_name_en = "Last updated report"
    activity_last_updated_report_name_pl = "Ostatnio zaaktualizowany raport"
    activity_last_updated_report_link_xpath = "//a[5]/button"

    menu_main_page_redirect_url_en = "https://dareit.futbolkolektyw.pl/en"
    menu_main_page_redirect_url_pl = "https://dareit.futbolkolektyw.pl/pl"
    menu_main_page_xpath = "//ul[1]/div[1]"
    menu_main_name_page_en = "Main page"
    menu_main_name_page_pl = "Strona główna"
    menu_main_name_text_xpath = "//ul[1]/div[1]/div[2]/span"

    menu_players_page_redirect_url_en = "https://dareit.futbolkolektyw.pl/en/players"
    menu_players_page_redirect_url_pl = "https://dareit.futbolkolektyw.pl/pl/players"
    menu_players_name_text_xpath = "//ul[1]/div[2]/div[2]/span"
    menu_player_button_xpath = "//ul[1]/div[2]"
    menu_players_name_en = "Players"
    menu_players_name_pl = "Gracze"

    menu_language_xpath = "//ul[2]/div[1]"
    menu_language_name_en = "English"
    menu_language_name_pl = "Polski"

    menu_logout_page_redirect_url = "https://dareit.futbolkolektyw.pl/en/login"
    menu_logout_xpath = "//ul[2]/div[2]"
    menu_logout_name_en = "Sign out"
    menu_logout_name_pl = "Wyloguj"
    menu_logout_name_text_xpath = "//ul[2]/div[2]/div[2]/span"

    menu_extend_player_name_xpath = "//ul[2]/div[1]"

    menu_extend_matches_xpath = "//span[contains(text(), 'Matches') or contains(text(), 'Mecze')]"
    menu_extend_matches_name_en = "Matches"
    menu_extend_matches_name_pl = "Mecze"
    menu_extend_matches_name_text_xpath = "//ul[2]/div[2]/div[2]/span"

    menu_extend_reports_xpath = "//ul[2]/div[3]"
    menu_extend_reports_name_en = "Reports"
    menu_extend_reports_name_pl = "Raporty"
    menu_extend_reports_name_text_xpath = "//ul[2]/div[3]/div[2]/span"

    def click_on_menu_main_page_button(self):
        """Method supporting dashboard_menu_main_page_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.menu_main_page_xpath)
        return self.click_on_the_element(self.menu_main_page_xpath)

    def dashboard_menu_main_page_button_click(self):
        """User click on main page button from menu"""
        main_page = Dashboard(self.driver)
        main_page.click_on_menu_main_page_button()

    def click_on_dashboard_menu_players_button(self):
        """Method supporting dashboard_menu_players_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.menu_player_button_xpath)
        return self.click_on_the_element(self.menu_player_button_xpath)

    def dashboard_menu_players_button_click(self):
        """User click on players button from menu"""
        players_page = Dashboard(self.driver)
        players_page.click_on_dashboard_menu_players_button()

    def click_on_extended_dashboard_menu_players_name_button(self):
        """Method supporting extended_dashboard_menu_players_name_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.menu_extend_player_name_xpath)
        return self.click_on_the_element(self.menu_extend_player_name_xpath)

    def extended_dashboard_menu_players_name_button_click(self):
        """User click on player name from extended menu for player"""
        extended_players_name_page = Dashboard(self.driver)
        extended_players_name_page.click_on_extended_dashboard_menu_players_name_button()

    def click_on_extended_dashboard_menu_matches_button(self):
        """Method supporting extended_dashboard_matches_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.menu_extend_matches_xpath)
        return self.click_on_the_element(self.menu_extend_matches_xpath)

    def extended_dashboard_matches_button_click(self):
        """User click on matches from extended menu for player"""
        extended_matches_page = Dashboard(self.driver)
        extended_matches_page.click_on_extended_dashboard_menu_matches_button()

    def click_on_extended_dashboard_menu_reports_button(self):
        """Method supporting extended_dashboard_reports_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.menu_extend_reports_xpath)
        return self.click_on_the_element(self.menu_extend_reports_xpath)

    def extended_dashboard_reports_button_click(self):
        """User click on reports from extended menu for player"""
        extended_reports_page = Dashboard(self.driver)
        extended_reports_page.click_on_extended_dashboard_menu_reports_button()

    def click_on_language_change_button(self):
        """Method supporting dashboard_menu_language_change_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator="//div[div[span[contains(text(), 'English') or contains(text(), 'Polski')]]]")
        return self.click_on_the_element("//div[div[span[contains(text(), 'English') or contains(text(), 'Polski')]]]")

    def dashboard_menu_language_change_button_click(self):
        """User click on language change button from menu"""
        language_change = Dashboard(self.driver)
        language_change.click_on_language_change_button()

    def click_on_sign_out_button(self):
        """Method supporting dashboard_menu_sign_out_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.menu_logout_xpath)
        return self.click_on_the_element(self.menu_logout_xpath)

    def dashboard_menu_sign_out_button_click(self):
        """User click on sign out button from menu"""
        sign_out = Dashboard(self.driver)
        sign_out.click_on_sign_out_button()

    def click_on_add_player_button(self):
        """Method supporting dashboard_add_player_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.add_player_button_xpath)
        return self.click_on_the_element(self.add_player_button_xpath)

    def dashboard_add_player_button_click(self):
        """User click on last added player link"""
        add_player = Dashboard(self.driver)
        add_player.click_on_add_player_button()

    def click_on_last_created_player_button(self):
        """Method supporting dashboard_last_created_player_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.activity_last_created_player_link_xpath)
        return self.click_on_the_element(self.activity_last_created_player_link_xpath)

    def dashboard_last_created_player_button_click(self):
        """User click on last created player link"""
        last_created_player = Dashboard(self.driver)
        last_created_player.click_on_last_created_player_button()

    def click_on_last_updated_player_button(self):
        """Method supporting dashboard_last_updated_player_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.activity_last_updated_player_link_xpath)
        return self.click_on_the_element(self.activity_last_updated_player_link_xpath)

    def dashboard_last_updated_player_button_click(self):
        """User click on last updated player link"""
        last_updated_player = Dashboard(self.driver)
        last_updated_player.click_on_last_updated_player_button()

    def click_on_last_created_match_button(self):
        """Method supporting dashboard_activity_last_created_match_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.activity_last_created_match_link_xpath)
        return self.click_on_the_element(self.activity_last_created_match_link_xpath)

    def dashboard_activity_last_created_match_click(self):
        """User click on last created match link"""
        last_match_created = Dashboard(self.driver)
        last_match_created.click_on_last_created_match_button()

    def click_on_last_updated_match_button(self):
        """Method supporting dashboard_last_updated_match_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.activity_last_updated_match_link_xpath)
        return self.click_on_the_element(self.activity_last_updated_match_link_xpath)

    def dashboard_last_updated_match_button_click(self):
        """User click on last updated match link"""
        last_updated_match = Dashboard(self.driver)
        last_updated_match.click_on_last_updated_match_button()

    def click_on_last_updated_report_button(self):
        """Method supporting dashboard_last_updated_report_button_click"""
        BasePage.wait_for_element_to_be_clickable(self, locator=self.activity_last_updated_report_link_xpath)
        return self.click_on_the_element(self.activity_last_updated_report_link_xpath)

    def dashboard_last_updated_report_button_click(self):
        """User click on last updated report link"""
        last_updated_report = Dashboard(self.driver)
        last_updated_report.click_on_last_updated_report_button()

    def create_translation_dictionary(self):
        """Creates a translation dictionary"""
        time.sleep(2)
        players_count_text_xpath = self.driver.find_element(By.XPATH, "//div[2]/div[1]/div/div[1]").text
        matches_count_text_xpath = self.driver.find_element(By.XPATH, "//div[2]/div[2]/div/div[1]").text
        reports_count_text_xpath = self.driver.find_element(By.XPATH, "//div[2]/div[3]/div/div[1]").text
        events_count_text_xpath = self.driver.find_element(By.XPATH, "//div[2]/div[4]/div/div[1]").text
        panel_name_upper_blue = self.driver.find_element(By.XPATH, "//h6").text
        panel_name_under_logo = self.driver.find_element(By.XPATH, "//div[2]/h2").text
        under_logo_text_xpath = self.driver.find_element(By.XPATH, "//div[2]/p").text
        shortcuts_text_xpath = self.driver.find_element(By.XPATH, "//div[3]/div[2]//h2").text
        add_player_button_xpath = self.driver.find_element(By.XPATH, "//div[2]//button").text
        activity_text_xpath = self.driver.find_element(By.XPATH, "//div[3]/div[3]//h2").text
        activity_last_created_player_text_xpath = self.driver.find_element(By.XPATH, "//div[3]//h6[1]").text
        activity_last_updated_player_text_xpath = self.driver.find_element(By.XPATH, "//div[3]//h6[2]").text
        activity_last_created_match_text_xpath = self.driver.find_element(By.XPATH, "//div[3]//h6[3]").text
        activity_last_updated_match_text_xpath = self.driver.find_element(By.XPATH, "//div[3]//h6[4]").text
        activity_last_updated_report_text_xpath = self.driver.find_element(By.XPATH, "//div[3]//h6[5]").text
        menu_main_page_xpath = self.driver.find_element(By.XPATH, "//ul[1]/div[1]").text
        menu_players_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[1]/div[2]/div[2]/span").text
        menu_logout_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[2]").text

        """Xpath for language detection - it will search for language tab and show 'Polski' option if webpage is 
        translated to English or 'English' option if webpage is translated to Polish"""
        global language_detect_xpath
        language_detect_xpath = self.driver.find_element(By.XPATH, "//span[contains(text(), 'English') or contains(text(), 'Polski')]").text

        global language_page_version_pl
        language_page_version_pl = {
            players_count_text_xpath: Dashboard.players_count_text_pl, matches_count_text_xpath: Dashboard.matches_count_text_pl,
            reports_count_text_xpath: Dashboard.reports_count_text_pl, events_count_text_xpath: Dashboard.events_count_text_pl,
            panel_name_upper_blue: Dashboard.panel_name_pl, under_logo_text_xpath: Dashboard.under_logo_text_pl,
            shortcuts_text_xpath: Dashboard.shortcuts_text_pl, add_player_button_xpath: Dashboard.add_player_button_text_pl,
            activity_text_xpath: Dashboard.activity_name_pl, activity_last_created_player_text_xpath: Dashboard.activity_last_created_player_name_pl,
            activity_last_updated_player_text_xpath: Dashboard.activity_last_updated_player_name_pl, activity_last_created_match_text_xpath: Dashboard.activity_last_created_match_name_pl,
            activity_last_updated_match_text_xpath: Dashboard.activity_last_updated_match_name_pl, panel_name_under_logo: Dashboard.panel_name_pl,  activity_last_updated_report_text_xpath: Dashboard.activity_last_updated_report_name_pl,
            menu_main_page_xpath: Dashboard.menu_main_name_page_pl, menu_players_name_text_xpath: Dashboard.menu_players_name_pl,
            menu_logout_xpath: Dashboard.menu_logout_name_pl
        }

        global language_page_version_en
        language_page_version_en = {
            players_count_text_xpath: Dashboard.players_count_text_en, matches_count_text_xpath: Dashboard.matches_count_text_en,
            reports_count_text_xpath: Dashboard.reports_count_text_en, events_count_text_xpath: Dashboard.events_count_text_en,
            panel_name_upper_blue: Dashboard.panel_name_en, panel_name_under_logo: Dashboard.panel_name_en,
            under_logo_text_xpath: Dashboard.under_logo_text_en, shortcuts_text_xpath: Dashboard.shortcuts_text_en,
            add_player_button_xpath: Dashboard.add_player_button_text_en, activity_text_xpath: Dashboard.activity_name_en,
            activity_last_created_player_text_xpath: Dashboard.activity_last_created_player_name_en, activity_last_updated_player_text_xpath: Dashboard.activity_last_updated_player_name_en,
            activity_last_created_match_text_xpath: Dashboard.activity_last_created_match_name_en, activity_last_updated_match_text_xpath: Dashboard.activity_last_updated_match_name_en,
            activity_last_updated_report_text_xpath: Dashboard.activity_last_updated_report_name_en, menu_main_page_xpath: Dashboard.menu_main_name_page_en,
            menu_players_name_text_xpath: Dashboard.menu_players_name_en, menu_logout_xpath: Dashboard.menu_logout_name_en
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
