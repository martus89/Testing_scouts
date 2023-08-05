from pages.base_page import BasePage


class EditMatch(BasePage):

    edit_match_url = "https://scouts-test.futbolkolektyw.pl/en/players/6026b48956c79737b3f3c624/matches/635e8b50f7933858f18c2203/edit"
    edit_match_upper_heading_text = "//form/div[1]//span"

    required_my_team_input_xpath = ""
    required_my_team_label_xpath = ""
    required_my_team_label_en = ""
    required_my_team_label_pl = ""
    required_my_team_warning_xpath = "//div[2]//div[1]/div/p"

    required_enemy_team_input_xpath = ""
    required_enemy_team_label_xpath = ""
    required_enemy_team_label_en = ""
    required_enemy_team_label_pl = ""
    required_enemy_team_warning_xpath = "//div[2]//div[2]/div/p"

    required_my_team_score_input_xpath = ""
    required_my_team_score_label_xpath = ""
    required_my_team_score_label_en = ""
    required_my_team_score_label_pl = ""
    required_my_team_score_warning_xpath = "//div[2]//div[3]//p"

    required_enemy_team_score_input_xpath = ""
    required_enemy_team_score_label_xpath = ""
    required_enemy_team_score_label_en = ""
    required_enemy_team_score_label_pl = ""
    required_enemy_team_score_warning_xpath = "//div[2]//div[4]//p"

    required_date_input_xpath = ""
    required_date_label_xpath = ""
    required_date_label_en = ""
    required_date_label_pl = ""
    required_date_warning_xpath = "//div[2]//div[5]//p"

    required_in_or_out_input_xpath = ""
    required_in_or_out_label_xpath = ""
    required_in_or_out_label_en = ""
    required_in_or_out_label_pl = ""
    required_in_or_out_warning_xpath = ""

    submit_button_xpath = ""
    submit_button_text_xpath = ""
    submit_button_en = ""
    submit_button_pl = ""

    clear_button_xpath = ""
    clear_button_text_xpath = ""
    clear_button_en = ""
    clear_button_pl = ""

    optional_tshirt_col_xpath = ""
    optional_tshirt_col_label_xpath = ""
    optional_tshirt_col_label_en = ""
    optional_tshirt_col_label_pl = ""

    optional_league_xpath = ""
    optional_league_label_xpath = ""
    optional_league_label_en = ""
    optional_league_label_pl = ""

    optional_time_played_xpath = ""
    optional_time_played_label_xpath = ""
    optional_time_played_label_en = ""
    optional_time_played_label_pl = ""

    optional_number_played_xpath = ""
    optional_number_played_label_xpath = ""
    optional_number_played_label_en = ""
    optional_number_played_label_pl = ""

    optional_web_match_xpath = ""
    optional_web_match_label_xpath = ""
    optional_web_match_label_en = ""
    optional_web_match_label_pl = ""

    optional_general_xpath = ""
    optional_general_label_xpath = ""
    optional_general_label_en = ""
    optional_general_label_pl = ""

    optional_rating_xpath = ""
    optional_rating_label_xpath = ""
    optional_rating_label_en = ""
    optional_rating_label_pl = ""

    events_list_heading_xpath = ""
    events_list_heading_label_xpath = ""
    events_list_heading_label_en = ""
    events_list_heading_label_pl = ""

    events_list_type_xpath = ""
    events_list_type_label_xpath = ""
    events_list_type_label_en = ""
    events_list_type_label_pl = ""

    events_list_time_xpath = ""
    events_list_time_label_xpath = ""
    events_list_time_label_en = ""
    events_list_time_label_pl = ""

    events_list_positive_xpath = ""
    events_list_positiv_label_xpath = ""
    events_list_positiv_label_en = ""
    events_list_positiv_label_pl = ""

    events_list_metadata_xpath = ""
    events_list_metadata_label_xpath = ""
    events_list_metadata_label_en = ""
    events_list_metadata_label_pl = ""

    events_list_comment_xpath = ""
    events_list_comment_label_xpath = ""
    events_list_comment_label_en = ""
    events_list_comment_label_pl = ""
