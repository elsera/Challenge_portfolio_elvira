from pages.base_page import BasePage

class AddMatchForm(BasePage):
    form_header_xpath = "//*[contains(@class,'MuiCardHeader')]/span"
    team_field_xpath = "//input[@name='myTeam']"
    team_score_xpath = "//input[@name='myTeamScore']"
    date_calendar_xpath = "//input[@name='date']"
    t_shirt_color_field_xpath = "//input[@name='tshirt']"
    web_match_field_xpath = "//input[@name='webMatch']"
    rating_field_xpath = "//input[@name='rating']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    enemy_team_score_xpath = "//input[@name='enemyTeamScore']"
    timeplayed_field_xpath = "//input[@name='timePlayed']"
    general_field_xpath ="//input[@name='general']"
    match_at_home_radiobutton_xpath = "//label[1]//input"
    match_out_home_radiobutton_xpath = "//label[2]//input"
    league_field_xpath = "//input[@name='league']"
    number_field_xpath = "//input[@name='number']"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//*[text()='Clear']/parent::button"
    main_page_panel_button_xpath = "//ul[1]/div[1]"
    players_panel_button_xpath = "//ul[1]/div[2]"
    match_player_name_panel_button_xpath = "//ul[2]/div[1]"
    matches_panel_button_xpath = "//ul[2]/div[2]"
    reports_player_panel_button_xpath = "//ul[2]/div[3]"
    language_panel_button_xpath = "//ul[3]/div[1]"
    sign_out_panek_button_xpath = "//ul[3]/div[2]"

    pass
