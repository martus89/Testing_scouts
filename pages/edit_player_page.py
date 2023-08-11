from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class EditPlayer(BasePage):

    edit_player_url_en = "https://scouts-test.futbolkolektyw.pl/en/players/6026b48956c79737b3f3c624/edit"
    edit_player_url_pl = "https://scouts-test.futbolkolektyw.pl/pl/players/6026b48956c79737b3f3c624/edit"
    edit_player_menu_player_name_xpath = "//ul[2]/div[1]/div[2]/span"
    edit_player_upper_title_span_text_xpath = "//div[2]/*/div[1]/*/span"
    edit_player_player_added_popup_container = "//*[@id='__next']/div[2]/div"

    test_edit_player_form_name_input = " "
    test_add_player_form_surname_input = " "
    test_add_player_form_age_input = "15102024"
    test_add_player_form_main_position_input = " "

    add_player_form_title_xpath = ""
    add_player_form_title_en = "Add player"
    add_player_form_title_pl = "Dodaj gracza"

    add_player_form_name_field_xpath = "//input[@name='name']"
    add_player_form_name_xpath = ""
    add_player_form_name_en = "Imię"
    add_player_form_name_pl = "Name"

    add_player_form_surname_xpath = "//input[@name='surname']"
    add_player_form_surname_text_xpath = ""
    add_player_form_surname_name_en = "Surname"
    add_player_form_surname_name_pl = "Nazwisko"

    add_player_form_age_xpath = "//input[@name='age']"
    add_player_form_age_text_xpath = ""
    add_player_form_age_name_en = "Age"
    add_player_form_age_name_pl = "Data urodzenia"

    add_player_form_main_position_xpath = "//input[@name='mainPosition']"
    add_player_form_main_position_text_xpath = ""
    add_player_form_main_position_name_en = "Główna pozycja"
    add_player_form_main_position_name_pl = "Main position"

    add_player_submit_button_xpath = "//form/*/button[1]"
    add_player_submit_button_text_xpath = ""
    add_player_submit_button_name_en = "Submit"
    add_player_submit_button_name_pl = "Submit"

    add_player_clear_button_xpath = ""
    add_player_clear_button_text_xpath = ""
    add_player_clear_button_name_en = "Clear"
    add_player_clear_button_name_pl = "Clear"

    add_player_add_language_button_xpath = ""
    add_player_language_delete_button_xpath = ""
    add_player_add_language_button_text_xpath = ""
    add_player_add_language_button_en = "Add language"
    add_player_add_language_button_pl = "Dodaj język"
    add_player_add_language_extra_field_en = "Languages"
    add_player_add_language_extra_field_pl = "Języki"

    add_player_yt_link_button_xpath = ""
    add_player_yt_link_delete_button_xpath = ""
    add_player_yt_link_button_text_xpath = ""
    add_player_yt_link_button_en = "Add link to Youtube"
    add_player_yt_link_button_pl = "Dodaj link z Youtube"
    add_player_yt_link_extra_field_en = "YouTube"
    add_player_yt_link_extra_field_pl = "Link do YouTube"

    form_optional_email_xpath = ""
    form_optional_email_en = "E-mail"
    form_optional_email_pl = ""

    form_optional_phone_xpath = ""
    form_optional_phone_en = "Phone"
    form_optional_phone_pl = ""

    form_optional_weight_xpath = ""
    form_optional_weight_en = "Weight"
    form_optional_weight_pl = ""

    form_optional_height_xpath = ""
    form_optional_height_en = "Height (cm)"
    form_optional_height_pl = ""

    form_optional_leg_xpath = ""
    form_optional_leg_en = "Leg"
    form_optional_leg_pl = "Dominująca noga"

    form_optional_club_xpath = ""
    form_optional_club_en = "Club"
    form_optional_club_pl = "Klub"

    form_optional_level_xpath = ""
    form_optional_level_en = "Level"
    form_optional_level_pl = "Poziom rozgrywek"

    form_optional_2pos_xpath = ""
    form_optional_2pos_en = "Second position"
    form_optional_2pos_pl = "Pozycja alternatywna"

    form_optional_district_xpath = ""
    form_optional_district_en = "District"
    form_optional_district_pl = "Województwo"

    form_optional_achvm_xpath = ""
    form_optional_achvm_en = "Achievements"
    form_optional_achvm_pl = "Osiągnięcia"

    form_optional_lnp_xpath = ""
    form_optional_lnp_en = "Łączy nas piłka"
    form_optional_lnp_pl = "Łączy nas piłka"

    form_optional_90m_xpath = ""
    form_optional_90m_en = "90 minut"
    form_optional_90m_pl = "90 minut"

    form_optional_fb_xpath = ""
    form_optional_fb_en = "Facebook"
    form_optional_fb_pl = "Profil facebook"

    def edit_player_url_for_check(self):
        driver = self.driver
        current_url = driver.current_url
        current_url_slice = current_url.split("/")[5]
        print(current_url_slice)
        return current_url_slice

    def wait_for_alert_turnaround(self, locator_type=By.XPATH):
        """Waiting until alert from current XPath disappears"""
        wait = WebDriverWait(self.driver, timeout=60)
        element_present = wait.until_not(ec.visibility_of_element_located((locator_type, EditPlayer.edit_player_player_added_popup_container)))
