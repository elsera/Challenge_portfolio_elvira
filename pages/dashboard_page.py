from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Dashboard(BasePage):
    side_menu_main_page_button_xpath = "//ul[1]/div[1]"
    side_menu_players_button_xpath = "//ul[1]/div[2]"
    side_menu_language_button_xpath = "//ul[2]/div[1]"
    side_menu_sign_out_button_xpath = "//ul[2]/div[2]"
    players_table_xpath = "//*[@role='grid']"
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

    def click_on_sign_out_button(self):
        self.click_on_the_element(self.side_menu_sign_out_button_xpath)

    def click_on_language_button(self):
        self.click_on_the_element(self.side_menu_language_button_xpath)

    def change_language(self):
        previous_language = self.driver.find_element(By.XPATH, self.side_menu_language_button_xpath).text
        self.click_on_language_button()
        current_language = self.driver.find_element(By.XPATH, self.side_menu_language_button_xpath).text
        assert previous_language != current_language

    def click_on_players_button(self):
        self.click_on_the_element(self.side_menu_players_button_xpath)

    def click_on_main_page_button(self):
        self.click_on_the_element(self.side_menu_main_page_button_xpath)


