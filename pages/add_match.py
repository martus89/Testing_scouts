from pages.base_page import BasePage


class AddMatch(BasePage):
    form_my_team_input_xpath = "//child::div/input[@name='myTeam']"
    form_enemy_team_score_input_xpath = "//child::div/input[@name='enemyTeamScore']"
    form_tshirt_color_input_xpath = "//child::div/input[@name='tshirt']"
    form_date_input_xpath = "//child::div/input[@name='date']"
    form_time_played_input_xpath = "//child::div/input[@name='timePlayed']"
    form_submit_button_xpath = "//button[@type='submit']"
    form_clear_button_xpath = "//child::div/button[2]"
    menu_players_button_xpath = "//child::ul[1]/div[2]"
    menu_reports_button_xpath = "//child::ul[2]/div[3]"
    menu_sign_out_button_xpath = "//child::ul[3]/div[2]"
