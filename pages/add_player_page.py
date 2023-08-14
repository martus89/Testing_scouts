import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard


class AddPlayer(BasePage):

    test_add_player_form_name_input = " "
    test_add_player_form_surname_input = " "
    test_add_player_form_age_input = "15102024"
    test_add_player_form_main_position_input = " "

    add_player_form_title_label_xpath = "//form/div[1]//span"
    add_player_form_title_en = "Add player"
    add_player_form_title_pl = "Dodaj gracza"

    add_player_form_name_field_xpath = "//input[@name='name']"
    add_player_form_name_label_xpath = "//form/div[2]//div[2]//label"
    add_player_form_name_pl = "Imię\u2009*"
    add_player_form_name_en = "Name\u2009*"
    add_player_form_name_required_error_xpath = "//div[2]//div[2]/div/p"

    add_player_form_surname_xpath = "//input[@name='surname']"
    add_player_form_surname_label_xpath = "//form//div[3]//label"
    add_player_form_surname_name_en = "Surname\u2009*"
    add_player_form_surname_name_pl = "Nazwisko\u2009*"
    add_player_form_surname_required_error_xpath = "//div[2]//div[3]/div/p"

    add_player_form_age_xpath = "//input[@name='age']"
    add_player_form_age_label_xpath = "//form//div[7]//label"
    add_player_form_age_name_en = "Age\u2009*"
    add_player_form_age_name_pl = "Data urodzenia\u2009*"
    add_player_form_age_required_error_xpath = "//div[2]//div[7]/div/p"

    add_player_form_main_position_xpath = "//input[@name='mainPosition']"
    add_player_form_main_position_label_xpath = "//form//div[11]//label"
    add_player_form_main_position_name_pl = "Główna pozycja\u2009*"
    add_player_form_main_position_name_en = "Main position\u2009*"
    add_player_form_main_position_required_error_xpath = "//div[2]/div/div[11]//p"

    add_player_submit_button_xpath = "//form/*/button[1]"
    add_player_submit_button_label_xpath = "//button[@type='submit']/span"
    add_player_submit_button_name_en = "SUBMIT"
    add_player_submit_button_name_pl = "SUBMIT"

    add_player_clear_button_xpath = "//div[3]/button[2]"
    add_player_clear_button_label_xpath = "//div[3]/button[2]/span"
    add_player_clear_button_name_en = "CLEAR"
    add_player_clear_button_name_pl = "CLEAR"

    add_player_add_language_button_xpath = "//div[15]/button"
    add_player_language_delete_button_xpath = "//div[15]/div/button"
    add_player_add_language_button_label_xpath = "//div[15]/button/span"
    add_player_add_language_button_en = "ADD LANGUAGE"
    add_player_add_language_button_pl = "DODAJ JĘZYK"
    add_player_add_language_extra_field_en = "Languages"
    add_player_add_language_extra_field_pl = "Języki"

    add_player_yt_link_button_xpath = "//div[19]/button"
    add_player_yt_link_delete_button_xpath = "//div[19]/div/button"
    add_player_yt_link_button_label_xpath = "//div[19]/button/span"
    add_player_yt_link_button_en = "ADD LINK TO YOUTUBE"
    add_player_yt_link_button_pl = "DODAJ LINK Z YOUTUBE"
    add_player_yt_link_extra_field_en = "YouTube"
    add_player_yt_link_extra_field_pl = "Link do YouTube"

    form_optional_email_xpath = "//input[@name='email']"
    form_optional_email_label_xpath = "//div[2]/div/div[1]//div/label"
    form_optional_email_en = "E-mail"
    form_optional_email_pl = "E-mail"

    form_optional_phone_xpath = "//input[@name='phone']"
    form_optional_phone_label_xpath = "//div[4]//label"
    form_optional_phone_en = "Phone"
    form_optional_phone_pl = "Telefon"

    form_optional_weight_xpath = "//input[@name='weight']"
    form_optional_weight_label_xpath = "//div[5]//label"
    form_optional_weight_en = "Weight"
    form_optional_weight_pl = "Waga"

    form_optional_height_xpath = "//input[@name='height']"
    form_optional_height_label_xpath = "//div[6]//label"
    form_optional_height_en = "Height (cm)"
    form_optional_height_pl = "Wzrost (cm)"

    form_optional_leg_xpath = "//input[@name='leg']"
    form_optional_leg_label_xpath = "//div[8]//label"
    form_optional_leg_en = "Leg"
    form_optional_leg_pl = "Dominująca noga"

    form_optional_club_xpath = "//input[@name='club']"
    form_optional_club_label_xpath = "//div[9]//label"
    form_optional_club_en = "Club"
    form_optional_club_pl = "Klub"

    form_optional_level_xpath = "//input[@name='level']"
    form_optional_level_label_xpath = "//div[10]//label"
    form_optional_level_en = "Level"
    form_optional_level_pl = "Poziom rozgrywek"

    form_optional_2pos_xpath = "//input[@name='secondPosition']"
    form_optional_2pos_label_xpath = "//div[12]//label"
    form_optional_2pos_en = "Second position"
    form_optional_2pos_pl = "Pozycja alternatywa"

    form_optional_district_xpath = "//input[@name='district']"
    form_optional_district_label_xpath = "//div[13]//label"
    form_optional_district_en = "District"
    form_optional_district_pl = "Województwo"

    form_optional_achvm_xpath = "//input[@name='achievements']"
    form_optional_achvm_label_xpath = "//div[14]//label"
    form_optional_achvm_en = "Achievements"
    form_optional_achvm_pl = "Osiągnięcia"

    form_optional_lnp_xpath = "//input[@name='webLaczy']"
    form_optional_lnp_label_xpath = "//div[16]//label"
    form_optional_lnp_en = "Łączy nas piłka"
    form_optional_lnp_pl = "Łączy nas piłka"

    form_optional_90m_xpath = "//input[@name='web90']"
    form_optional_90m_label_xpath = "//div[17]//label"
    form_optional_90m_en = "90 minut"
    form_optional_90m_pl = "90 minut"

    form_optional_fb_xpath = "//input[@name='webFB']"
    form_optional_fb_label_xpath = "//div[18]//label"
    form_optional_fb_en = "Facebook"
    form_optional_fb_pl = "Profil facebook"

    def add_player_form_restricted_data_only_fill_up(self):
        """Adding only restricted data to add player form"""
        BasePage.wait_for_element_to_be_clickable(self, locator=AddPlayer.add_player_submit_button_xpath)
        name = self.driver.find_element(By.XPATH, AddPlayer.add_player_form_name_field_xpath)
        name.send_keys(AddPlayer.test_add_player_form_name_input)
        surname = self.driver.find_element(By.XPATH, AddPlayer.add_player_form_surname_xpath)
        surname.send_keys(AddPlayer.test_add_player_form_surname_input)
        age = self.driver.find_element(By.XPATH, AddPlayer.add_player_form_age_xpath)
        age.send_keys(AddPlayer.test_add_player_form_age_input)
        main_position = self.driver.find_element(By.XPATH, AddPlayer.add_player_form_main_position_xpath)
        main_position.send_keys(AddPlayer.test_add_player_form_main_position_input)

    def path_to_add_player(self):
        """User click on Add player button in dashboard"""
        Dashboard.dashboard_add_player_button_click(self)

    def click_on_submit_button(self):
        """Method function for add_player_form_submit_button_click(self)"""
        BasePage.wait_for_element_to_be_clickable(self, locator=AddPlayer.add_player_submit_button_xpath)
        return self.click_on_the_element(self.add_player_submit_button_xpath)

    def add_player_form_submit_button_click(self):
        """User click on form submit button in add player subpage"""
        submit_form = AddPlayer(self.driver)
        submit_form.click_on_submit_button()

    def create_translation_dictionary(self):
        """Creates a translation dictionary"""
        time.sleep(2)
        add_player_form_title_label_xpath = self.driver.find_element(By.XPATH, "//form/div[1]//span").text
        add_player_form_name_label_xpath = self.driver.find_element(By.XPATH, "//form/div[2]//div[2]/div/label").text
        add_player_form_surname_label_xpath = self.driver.find_element(By.XPATH, "//form/div[2]//div[3]/div/label").text
        add_player_form_age_label_xpath = self.driver.find_element(By.XPATH, "//form/div[2]//div[7]/div/label").text
        add_player_form_main_position_label_xpath = self.driver.find_element(By.XPATH, "//form/div[2]//div[11]/div/label").text
        add_player_submit_button_label_xpath = self.driver.find_element(By.XPATH, "//button[@type='submit']/span").text
        add_player_clear_button_label_xpath = self.driver.find_element(By.XPATH, "//div[3]/button[2]/span").text
        add_player_add_language_button_label_xpath = self.driver.find_element(By.XPATH, "//div[15]/button/span").text
        add_player_yt_link_button_label_xpath = self.driver.find_element(By.XPATH, "//div[19]/button/span").text
        form_optional_email_label_xpath = self.driver.find_element(By.XPATH, "//div[2]/div/div[1]//div/label").text
        form_optional_phone_label_xpath = self.driver.find_element(By.XPATH, "//div[4]//label").text
        form_optional_weight_label_xpath = self.driver.find_element(By.XPATH, "//div[5]//label").text
        form_optional_height_label_xpath = self.driver.find_element(By.XPATH, "//div[6]//label").text
        form_optional_leg_label_xpath = self.driver.find_element(By.XPATH, "//div[8]//label").text
        form_optional_club_label_xpath = self.driver.find_element(By.XPATH, "//div[9]//label").text
        form_optional_level_label_xpath = self.driver.find_element(By.XPATH, "//div[10]//label").text
        form_optional_2pos_label_xpath = self.driver.find_element(By.XPATH, "//div[12]//label").text
        form_optional_district_label_xpath = self.driver.find_element(By.XPATH, "//div[13]//label").text
        form_optional_achvm_label_xpath = self.driver.find_element(By.XPATH, "//div[14]//label").text
        form_optional_lnp_label_xpath = self.driver.find_element(By.XPATH, "//div[16]//label").text
        form_optional_90m_label_xpath = self.driver.find_element(By.XPATH, "//div[17]//label").text
        form_optional_fb_label_xpath = self.driver.find_element(By.XPATH, "//div[18]//label").text
        menu_main_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[1]/div[1]/div[2]/span").text
        menu_language_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[1]").text
        menu_logout_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[2]").text
        menu_player_button_xpath = self.driver.find_element(By.XPATH, "//ul[1]/div[2]").text


        """Xpath for language detection - it will search for language tab and show 'Polski' option if webpage is 
        translated to English or 'English' option if webpage is translated to Polish"""
        global language_detect_xpath
        language_detect_xpath = self.driver.find_element(By.XPATH, "//span[contains(text(), 'English') or contains(text(), 'Polski')]").text

        global language_page_version_pl
        language_page_version_pl = {
            add_player_form_title_label_xpath: AddPlayer.add_player_form_title_pl, add_player_form_name_label_xpath: AddPlayer.add_player_form_name_pl,
            add_player_form_surname_label_xpath: AddPlayer.add_player_form_surname_name_pl, add_player_form_age_label_xpath: AddPlayer.add_player_form_age_name_pl,
            add_player_form_main_position_label_xpath: AddPlayer.add_player_form_main_position_name_pl, add_player_submit_button_label_xpath: AddPlayer.add_player_submit_button_name_pl,
            add_player_clear_button_label_xpath: AddPlayer.add_player_clear_button_name_pl, add_player_add_language_button_label_xpath: AddPlayer.add_player_add_language_button_pl,
            add_player_yt_link_button_label_xpath: AddPlayer.add_player_yt_link_button_pl, form_optional_email_label_xpath: AddPlayer.form_optional_email_pl,
            form_optional_phone_label_xpath: AddPlayer.form_optional_phone_pl, form_optional_weight_label_xpath: AddPlayer.form_optional_weight_pl,
            form_optional_height_label_xpath: AddPlayer.form_optional_height_pl, form_optional_leg_label_xpath: AddPlayer.form_optional_leg_pl,
            form_optional_club_label_xpath: AddPlayer.form_optional_club_pl, form_optional_level_label_xpath: AddPlayer.form_optional_level_pl,
            form_optional_2pos_label_xpath: AddPlayer.form_optional_2pos_pl, form_optional_district_label_xpath: AddPlayer.form_optional_district_pl,
            form_optional_achvm_label_xpath: AddPlayer.form_optional_achvm_pl, form_optional_lnp_label_xpath: AddPlayer.form_optional_lnp_pl,
            form_optional_90m_label_xpath: AddPlayer.form_optional_90m_pl, form_optional_fb_label_xpath: AddPlayer.form_optional_fb_pl,
            menu_main_name_text_xpath: Dashboard.menu_main_name_page_pl, menu_language_xpath: Dashboard.menu_language_name_en,
            menu_logout_xpath: Dashboard.menu_logout_name_pl, menu_player_button_xpath: Dashboard.menu_players_name_pl
        }

        global language_page_version_en
        language_page_version_en = {
            add_player_form_title_label_xpath: AddPlayer.add_player_form_title_en, add_player_form_name_label_xpath: AddPlayer.add_player_form_name_en,
            add_player_form_surname_label_xpath: AddPlayer.add_player_form_surname_name_en, add_player_form_age_label_xpath: AddPlayer.add_player_form_age_name_en,
            add_player_form_main_position_label_xpath: AddPlayer.add_player_form_main_position_name_en, add_player_submit_button_label_xpath: AddPlayer.add_player_submit_button_name_en,
            add_player_clear_button_label_xpath: AddPlayer.add_player_clear_button_name_en, add_player_add_language_button_label_xpath: AddPlayer.add_player_add_language_button_en,
            add_player_yt_link_button_label_xpath: AddPlayer.add_player_yt_link_button_en, form_optional_email_label_xpath: AddPlayer.form_optional_email_en,
            form_optional_phone_label_xpath: AddPlayer.form_optional_phone_en, form_optional_weight_label_xpath: AddPlayer.form_optional_weight_en,
            form_optional_height_label_xpath: AddPlayer.form_optional_height_en, form_optional_leg_label_xpath: AddPlayer.form_optional_leg_en,
            form_optional_club_label_xpath: AddPlayer.form_optional_club_en, form_optional_level_label_xpath: AddPlayer.form_optional_level_en,
            form_optional_2pos_label_xpath: AddPlayer.form_optional_2pos_en, form_optional_district_label_xpath: AddPlayer.form_optional_district_en,
            form_optional_achvm_label_xpath: AddPlayer.form_optional_achvm_en, form_optional_lnp_label_xpath: AddPlayer.form_optional_lnp_en,
            form_optional_90m_label_xpath: AddPlayer.form_optional_90m_en, form_optional_fb_label_xpath: AddPlayer.form_optional_fb_en,
            menu_main_name_text_xpath: Dashboard.menu_main_name_page_en, menu_language_xpath: Dashboard.menu_language_name_pl,
            menu_logout_xpath: Dashboard.menu_logout_name_en, menu_player_button_xpath: Dashboard.menu_players_name_en
        }

        AddPlayer.check_for_language_extension(self)

    def check_for_language_extension(self):
        """"Function checks if left side dashboard menu extends itself and adds extra fields upon that extension"""

        my_current_url = BasePage.get_page_url(self)
        list_of_extend_vocab = ["matches", "reports", "edit"]

        for element in list_of_extend_vocab:
            if element not in my_current_url:
                pass
            else:
                menu_extend_matches_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[2]/div[2]/span").text
                menu_extend_reports_name_text_xpath = self.driver.find_element(By.XPATH, "//ul[2]/div[3]/div[2]/span").text

                global language_page_extended_version_en
                language_page_extended_version_en = {
                    menu_extend_matches_name_text_xpath: Dashboard.menu_extend_matches_name_en,
                    menu_extend_reports_name_text_xpath: Dashboard.menu_extend_reports_name_en}

                global language_page_extended_version_pl
                language_page_extended_version_pl = {
                    menu_extend_matches_name_text_xpath: Dashboard.menu_extend_matches_name_pl,
                    menu_extend_reports_name_text_xpath: Dashboard.menu_extend_reports_name_pl}

                language_page_version_pl.update(language_page_extended_version_pl)
                language_page_version_en.update(language_page_extended_version_en)

    def address_dictionary_translation_check(self):
        """Based on language chosen in dropdown by user, checks if page elements have correct language"""
        time.sleep(2)
        if language_detect_xpath == "Polski":
            page_dictionary = language_page_version_en
        elif language_detect_xpath == "English":
            page_dictionary = language_page_version_pl
        else:
            print("Language not detected - check your webpage")
        for field_name in page_dictionary:
            assert field_name == page_dictionary[field_name]
        print("Dictionary checked - everything seems in order")
