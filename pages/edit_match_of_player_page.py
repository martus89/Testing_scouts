from pages.base_page import BasePage


class EditMatch(BasePage):

    edit_match_upper_heading_text = "//form/div[1]//span"

    required_my_team_input_xpath = "//input[@name='myTeam']"
    required_my_team_label_xpath = "//form/div[2]//div[1]/div/label/text()"
    required_my_team_label_en = "My team"
    required_my_team_label_pl = "Drużyna zawodnika"
    required_my_team_warning_xpath = "//div[2]//div[1]/div/p"

    required_enemy_team_input_xpath = "//input[@name='enemyTeam']"
    required_enemy_team_label_xpath = "//form/div[2]//div[2]/div/label/text()"
    required_enemy_team_label_en = "Enemy team"
    required_enemy_team_label_pl = "Drużyna przeciwna"
    required_enemy_team_warning_xpath = "//div[2]//div[2]/div/p"

    required_my_team_score_input_xpath = "//input[@name='myTeamScore']"
    required_my_team_score_label_xpath = "//form/div[2]//div[3]/div/label/text()"
    required_my_team_score_label_en = "My team score"
    required_my_team_score_label_pl = "Zdobyte gole"
    required_my_team_score_warning_xpath = "//div[2]//div[3]//p"

    required_enemy_team_score_input_xpath = "//input[@name='enemyTeamScore']"
    required_enemy_team_score_label_xpath = "//form/div[2]//div[4]/div/label/text()"
    required_enemy_team_score_label_en = "Enemy team score"
    required_enemy_team_score_label_pl = "Stracone gole"
    required_enemy_team_score_warning_xpath = "//div[2]//div[4]//p"

    required_date_input_xpath = "//input[@name='date']"
    required_date_label_xpath = "//form/div[2]//div[5]/div/label/text()"
    required_date_label_en = "Date"
    required_date_label_pl = "Data"
    required_date_warning_xpath = "//div[2]//div[5]//p"

    required_in_or_out_input_xpath = "//input[@name='matchAtHome']"
    home_match_label_text_xpath = "//fieldset//label[1]/span[2]/text()"
    home_match_label_en = "Match at home"
    home_match_label_pl = "Mecz domowy"
    out_match_label_text_xpath = "//fieldset/div/label[2]/span[2]/text()"
    out_match_label_en = "Match out home"
    out_match_label_pl = "Mecz wyjazdowy"

    submit_button_xpath = "//form/div[3]/button[1]"
    submit_button_text_xpath = "//form/div[3]/button[1]/span/text()"
    submit_button_en = "Submit"
    submit_button_pl = "Submit"

    clear_button_xpath = "//form/div[3]/button[2]"
    clear_button_text_xpath = "//form/div[3]/button[2]/span[1]/text()"
    clear_button_en = "Clear"
    clear_button_pl = "Clear"

    optional_tshirt_col_xpath = "//input[@name='tshirt']"
    optional_tshirt_col_label_xpath = "//div[2]//div[7]//label/text()"
    optional_tshirt_col_label_en = "T-shirt color"
    optional_tshirt_col_label_pl = "Kolor koszulki"

    optional_league_xpath = "//input[@name='league']"
    optional_league_label_xpath = "//div[2]//div[8]//label/text()"
    optional_league_label_en = "League"
    optional_league_label_pl = "Liga"

    optional_time_played_xpath = "//input[@name='timePlayed']"
    optional_time_played_label_xpath = "//div[2]//div[9]//label/text()"
    optional_time_played_label_en = "Time played"
    optional_time_played_label_pl = "Czas gry"

    optional_number_played_xpath = "//input[@name='number']"
    optional_number_played_label_xpath = "//div[2]//div[10]//label/text()"
    optional_number_played_label_en = "Number"
    optional_number_played_label_pl = "Numer"

    optional_web_match_xpath = "//input[@name='webMatch']"
    optional_web_match_label_xpath = "//div[2]//div[11]//label/text()"
    optional_web_match_label_en = "Web match"
    optional_web_match_label_pl = "Web match"

    optional_general_xpath = "//input[@name='general']"
    optional_general_label_xpath = "//div[2]//div[12]//label/text()"
    optional_general_label_en = "General"
    optional_general_label_pl = "General"

    optional_rating_xpath = "//input[@name='rating']"
    optional_rating_label_xpath = "//div[2]//div[13]//label/text()"
    optional_rating_label_en = "Rating"
    optional_rating_label_pl = "Recenzja"

    events_list_heading_xpath = "//div[3]//div/div/span"
    events_list_heading_label_xpath = "//div[3]//div/div/span/text()"
    events_list_heading_label_en = "Events list"
    events_list_heading_label_pl = "Lista zdarzeń"

    events_list_type_xpath = "//tr/th[1]"
    events_list_type_label_xpath = "//tr/th[1]/text()"
    events_list_type_label_en = "Type"
    events_list_type_label_pl = "Typ"

    events_list_time_xpath = "//tr/th[2]"
    events_list_time_label_xpath = "//tr/th[2]/text()"
    events_list_time_label_en = "Time"
    events_list_time_label_pl = "Czas"

    events_list_positive_xpath = "//tr/th[3]"
    events_list_positive_label_xpath = "//tr/th[3]/text()"
    events_list_positive_label_en = "Positive"
    events_list_positive_label_pl = "Udany"

    events_list_metadata_xpath = "//tr/th[4]"
    events_list_metadata_label_xpath = "//tr/th[4]/text()/text()"
    events_list_metadata_label_en = "Meta data"
    events_list_metadata_label_pl = "Meta dane"

    events_list_comment_xpath = "//tr/th[5]"
    events_list_comment_label_xpath = "//tr/th[5]/text()"
    events_list_comment_label_en = "Comment"
    events_list_comment_label_pl = "Komentarz"



