import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_panel_button_xpath = "//div[@role='presentation']/ul[1]/div[1]"
    players_panel_button_xpath = "//div[@role='presentation']/ul[1]/div[2]"
    language_panel_button_xpath = "//div[@role='presentation']/ul[2]/div[1]"
    sign_out_panel_button_xpath = "//div[@role='presentation']/ul[2]/div[2]"
    add_player_hyperlink_xpath = "(//a[1]/button)[1]"
    logo_platform_image_xpath = "//div[@title='Logo Scouts Panel']"
    dev_team_contact_button = "//span[text()='Dev team contact']/parent::a"
    last_created_player_hyperlink_xpath = "//*[contains(@class,'MuiCardContent')]//h6[1]//following::a[1]"
    last_updated_player_hyperlink_xpath = "//*[contains(@class,'MuiCardContent')]//h6[2]//following::a[1]"
    last_created_match_hyperlink_xpath = "//*[contains(@class,'MuiCardContent')]//h6[3]//following::a[1]"
    last_updated_report_hyperlink_xpath = "//*[contains(@class,'MuiCardContent')]//h6[4]//following::a[1]"
    players_count_xpath = "(//*[contains(@class, 'MuiGrid-root')]//b)[1]"
    reports_count_xpath = "(//*[contains(@class, 'MuiGrid-root')]//b)[2]"
    matches_count_xpath = "(//*[contains(@class, 'MuiGrid-root')]//b)[3]"
    events_count_xpath = "(//*[contains(@class, 'MuiGrid-root')]//b)[4]"

    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.logo_platform_image_xpath)
        assert self.get_page_title() == self.expected_title

    def click_on_the_add_player_link(self):
        self.click_on_the_element(self.add_player_hyperlink_xpath)


