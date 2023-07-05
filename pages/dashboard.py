from pages.base_page import BasePage


class Dashboard(BasePage):
    shortcuts_add_player_button_xpath = "//child::div[contains(@class,'MuiGrid-root MuiGrid-item')][2]//button"
    scouts_panel_dev_team_contact_link_xpath = "//a[contains(@class, 'MuiButtonBase-root MuiButton-root')]"
    activity_last_created_player_link_xpath = "//child::div[contains(@class,'MuiGrid-root MuiGrid-item')][3]//a[1]/button"
    activity_last_updated_player_link_xpath = "//child::div//a[2]/button"
    activity_last_created_match_link_xpath = "//child::div//a[3]/button"
    activity_last_updated_match_link_xpath = "//child::div//a[4]/button"
    activity_last_updated_report_link_xpath = "//child::div//a[5]/button"
    menu_players_link_xpath = "//child::ul[1]/div[2]"
    menu_language_xpath = "//child::ul[2]/div[1]"
    menu_sign_out = "//child::ul[2]/div[2]"
