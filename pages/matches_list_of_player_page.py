from pages.base_page import BasePage

class MatchesListOfPlayer(BasePage):

    all_matches_of_player_example_url_en = "https://scouts-test.futbolkolektyw.pl/en/players/6026d92156c79737b3f3c62a/matches"
    all_matches_of_player_example_url_pl = "https://scouts-test.futbolkolektyw.pl/pl/players/6026d92156c79737b3f3c62a/matches"

    actions_edit_button_xpath = "//tr[1]/td[9]//button"
    actions_create_report_button_xpath = "//tr[1]/td[10]//button"
    actions_start_report_button_xpath = "//tr[1]/td[11]//button"

    add_match_button_xpath = "//main/a/button"
    add_match_label_xpath = "//a//span[1]/text()"
    add_match_text_en = "Add match"
    add_match_text_pl = "Dodaj mecz"

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
    time_played_text_en = "Time played"
    time_played_text_pl = "Czas gry"

    rating_text_xpath = "//th[7]/text()"
    rating_text_en = "Rating"
    rating_text_pl = "Recenzja"

    author_text_xpath = "//th[8]/text()"
    author_text_en = "Author"
    author_text_pl = "Autor"

    actions_text_xpath = "//th[9]/text()"
    actions_text_en = "Actions"
    actions_text_pl = "Akcje"

