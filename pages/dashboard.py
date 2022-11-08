from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_panel_button_xpath = "//div[@role='presentation']/ul[1]/div[1]"
    players_panel_button_xpath = "//div[@role='presentation']/ul[1]/div[2]"
    language_select_panel_button_xpath = "//div[@role='presentation']/ul[2]/div[1]"
    sign_out_panel_button_xpath = "//div[@role='presentation']/ul[2]/div[2]"
    add_player_hyperlink_xpath = "//*[contains(@href,'/players/add')]/button"
    logo_platform_image_xpath = "//div[@title='Logo Scouts Panel']"
    dev_team_contact_button = "//span[text()='Dev team contact']/parent::a"
    last_created_player_hyperlink_xpath = "//h2[text()='Activity' or text()='Aktywnosć']/following-sibling::a[1]"
    last_updated_player_hyperlink_xpath = "//h2[text()='Activity' or text()='Aktywnosć']/following-sibling::a[2]"
    last_created_match_hyperlink_xpath = "//h2[text()='Activity' or text()='Aktywnosć']/following-sibling::a[3]"
    last_updated_report_hyperlink_xpath = "//h2[text()='Activity' or text()='Aktywnosć']/following-sibling::a[4]"
    players_count_xpath = "//*[text()= 'Players count' or text()='Ilość graczy']//following-sibling::div/b"
    reports_count_xpath = "//*[text()= 'Matches count' or text()= 'Ilość meczy']//following-sibling::div/b"
    matches_count_xpath = "//*[text()= 'Reports count' or text() = 'Ilość raportów']//following-sibling::div/b"
    events_count_xpath = "//*[text()= 'Events count' or text() = 'Ilość akcji']/following::div/b"
    pass
