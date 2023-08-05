from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.edit_player_page import EditPlayer


class AddPlayer(BasePage):
    add_player_page_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    test_add_player_form_name_input = " "
    test_add_player_form_surname_input = " "
    test_add_player_form_age_input = "15102024"
    test_add_player_form_main_position_input = " "

    add_player_form_title_label_xpath = "//form/div[1]//span/text()"
    add_player_form_title_en = "Add player"
    add_player_form_title_pl = "Dodaj gracza"

    add_player_form_name_field_xpath = "//input[@name='name']"
    add_player_form_name_label_xpath = "//form/div[2]//div[2]//label/text()"
    add_player_form_name_en = "Imię"
    add_player_form_name_pl = "Name"

    add_player_form_surname_xpath = "//input[@name='surname']"
    add_player_form_surname_label_xpath = "//form//div[3]//label/text()"
    add_player_form_surname_name_en = "Surname"
    add_player_form_surname_name_pl = "Nazwisko"

    add_player_form_age_xpath = "//input[@name='age']"
    add_player_form_age_label_xpath = "//form//div[7]//label/text()"
    add_player_form_age_name_en = "Age"
    add_player_form_age_name_pl = "Wiek"

    add_player_form_main_position_xpath = "//input[@name='mainPosition']"
    add_player_form_main_position_label_xpath = "//form//div[11]//label/text()"
    add_player_form_main_position_name_en = "Główna pozycja"
    add_player_form_main_position_name_pl = "Main position"

    add_player_submit_button_xpath = "//form/*/button[1]"
    add_player_submit_button_label_xpath = "//button[@type='submit']/span/text()"
    add_player_submit_button_name_en = "Submit"
    add_player_submit_button_name_pl = "Submit"

    add_player_clear_button_xpath = "//div[3]/button[2]"
    add_player_clear_button_label_xpath = "//div[3]/button[2]/span/text()"
    add_player_clear_button_name_en = "Clear"
    add_player_clear_button_name_pl = "Clear"

    add_player_add_language_button_xpath = "//div[15]/button"
    add_player_language_delete_button_xpath = "//div[15]/div/button"
    add_player_add_language_button_label_xpath = "//div[15]/button/span/text()"
    add_player_add_language_button_en = "Add language"
    add_player_add_language_button_pl = "Dodaj język"
    add_player_add_language_extra_field_en = "Languages"
    add_player_add_language_extra_field_pl = "Języki"

    add_player_yt_link_button_xpath = "//div[19]/button"
    add_player_yt_link_delete_button_xpath = "//div[19]/div/button"
    add_player_yt_link_button_label_xpath = "//div[19]/button/span/text()"
    add_player_yt_link_button_en = "Add link to Youtube"
    add_player_yt_link_button_pl = "Dodaj link z Youtube"
    add_player_yt_link_extra_field_en = "YouTube"
    add_player_yt_link_extra_field_pl = "Link do YouTube"

    form_optional_email_xpath = "//input[@name='email']"
    form_optional_email_label_xpath = "//div[2]/div/div[1]//div/label/text()"
    form_optional_email_en = "E-mail"
    form_optional_email_pl = "E-mail"

    form_optional_phone_xpath = "//input[@name='phone']"
    form_optional_phone_label_xpath = "//div[4]//label/text()"
    form_optional_phone_en = "Phone"
    form_optional_phone_pl = "Telefon"

    form_optional_weight_xpath = "//input[@name='weight']"
    form_optional_weight_label_xpath = "//div[5]//label/text()"
    form_optional_weight_en = "Weight"
    form_optional_weight_pl = "Waga"

    form_optional_height_xpath = "//input[@name='height']"
    form_optional_height_label_xpath = "//div[6]//label/text()"
    form_optional_height_en = "Height (cm)"
    form_optional_height_pl = "Wzrost (cm)"

    form_optional_leg_xpath = "//input[@name='leg']"
    form_optional_leg_label_xpath = "//div[8]//label/text()"
    form_optional_leg_en = "Leg"
    form_optional_leg_pl = "Dominująca noga"

    form_optional_club_xpath = "//input[@name='club']"
    form_optional_club_label_xpath = "//div[9]//label/text()"
    form_optional_club_en = "Club"
    form_optional_club_pl = "Klub"

    form_optional_level_xpath = "//input[@name='level']"
    form_optional_level_label_xpath = "//div[10]//label/text()"
    form_optional_level_en = "Level"
    form_optional_level_pl = "Poziom rozgrywek"

    form_optional_2pos_xpath = "//input[@name='secondPosition']"
    form_optional_2pos_label_xpath = "//div[12]//label/text()"
    form_optional_2pos_en = "Second position"
    form_optional_2pos_pl = "Pozycja alternatywna"

    form_optional_district_xpath = "//input[@name='district']"
    form_optional_district_label_xpath = "//div[13]//label/text()"
    form_optional_district_en = "District"
    form_optional_district_pl = "Województwo"

    form_optional_achvm_xpath = "//input[@name='achievements']"
    form_optional_achvm_label_xpath = "//div[14]//label/text()"
    form_optional_achvm_en = "Achievements"
    form_optional_achvm_pl = "Osiągnięcia"

    form_optional_lnp_xpath = "//input[@name='webLaczy']"
    form_optional_lnp_label_xpath = "//div[16]//label/text()"
    form_optional_lnp_en = "Łączy nas piłka"
    form_optional_lnp_pl = "Łączy nas piłka"

    form_optional_90m_xpath = "//input[@name='web90']"
    form_optional_90m_label_xpath = "//div[17]//label/text()"
    form_optional_90m_en = "90 minut"
    form_optional_90m_pl = "90 minut"

    form_optional_fb_xpath = "//input[@name='webFB']"
    form_optional_fb_label_xpath = "//div[18]//label/text()"
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
        AddPlayer.add_player_form_submit_button_click(self)
        BasePage.wait_for_element_to_be_clickable(self, locator=EditPlayer.edit_player_menu_player_name_xpath)

    def click_on_submit_button(self):
        BasePage.wait_for_element_to_be_clickable(self, locator=AddPlayer.add_player_submit_button_xpath)
        return self.click_on_the_element(self.add_player_submit_button_xpath)

    def path_to_add_player(self):
        Dashboard.dashboard_add_player_button_click(self)

    def add_player_form_submit_button_click(self):
        submit_form = AddPlayer(self.driver)
        submit_form.click_on_submit_button()

    def add_player_url_for_check(self):
        driver = self.driver
        current_url = driver.current_url
        return current_url