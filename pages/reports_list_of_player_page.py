from pages.base_page import BasePage

# XPATHS DONE!

class ReportsListOfPlayer(BasePage):
    all_reports_of_player_example_url_en = "https://scouts-test.futbolkolektyw.pl/en/players/6026b48956c79737b3f3c624/reports"
    all_reports_of_player_example_url_pl = "https://scouts-test.futbolkolektyw.pl/en/players/6026b48956c79737b3f3c624/reports"

    actions_edit_button_row_1xpath = "//tr[1]/td[8]//button"

    add_report_button_xpath = "//main/a/button"
    add_report_label_xpath = "//a//span[1]/text()"
    add_report_text_en = "Add report"
    add_report_text_pl = "Dodaj raport"

    my_team_label_text_xpath = "//th[1]/text()"
    my_team_text_en = "My team"
    my_team_text_pl = "Drużyna zawodnika"

    my_team_score_label_text_xpath = "//th[2]/text()"
    my_team_score_text_en = "My team score"
    my_team_score_text_pl = "Zdobyte gole"

    enemy_team_score_label_text_xpath = "//th[3]/text()"
    enemy_team_score_text_en = "Enemy team score"
    enemy_team_score_text_pl = "Stracone gole"

    enemy_team_label_text_xpath = "//th[4]/text()"
    enemy_team_text_en = "Enemy team"
    enemy_team_text_pl = "Drużyna przeciwna"

    date_label_text_xpath = "//th[5]/text()"
    date_team_text_en = "Date"
    date_team_text_pl = "Data"

    time_played_text_xpath = "//th[6]/text()"
    time_played_text_en = "Last modified"
    time_played_text_pl = "Ostatnia modyfikacja"

    rating_text_xpath = "//th[7]/text()"
    rating_text_en = "Author"
    rating_text_pl = "Autor"

    author_text_xpath = "//th[8]/text()"
    author_text_en = "Actions"
    author_text_pl = "Akcje"