import os
import unittest
from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboardSideMenu(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.login_page = LoginPage(self.driver)

    # Test side menu players button and verify players table is opening
    def test_players_button(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.title_of_page()
        self.login_page.log_in('user07@getnada.com', 'Test-1234')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_players_button()
        dashboard_page.visibility_of_element_located(dashboard_page.players_table_xpath)
        assert dashboard_page.get_page_title() != dashboard_page.expected_title
        self.driver.save_screenshot("./screenshots/dashboard_players_table.png")
        Image.open("./screenshots/dashboard_players_table.png").show()

    # Test change language option from dashboard page.
    def test_change_language(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.title_of_page()
        self.login_page.log_in('user07@getnada.com', 'Test-1234')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        self.driver.save_screenshot("./screenshots/dashboard_language.png")
        Image.open("./screenshots/dashboard_language.png").show()
        dashboard_page.change_language()
        self.driver.save_screenshot("./screenshots/dashboard_language_changed.png")
        Image.open("./screenshots/dashboard_language_changed.png").show()


    @classmethod
    def tearDown(self):
        self.driver.quit()


