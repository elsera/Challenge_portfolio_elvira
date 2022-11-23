import os
import time
import unittest
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.add_player_page import AddPlayerPage
from pages.dashboard_page import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayerPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    # Test choose random district from a range of districts
    def test_random_district_option(self):
        login_page = LoginPage(self.driver)
        login_page.log_in('user07@getnada.com', 'Test-1234')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_link()
        add_player_page = AddPlayerPage(self.driver)
        add_player_page.district_random_option()
        time.sleep(3)

    # Test select a specific district. TC05
    def test_district_dropdown(self):
        login_page = LoginPage(self.driver)
        login_page.log_in('user07@getnada.com', 'Test-1234')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_link()
        add_player_page = AddPlayerPage(self.driver)
        add_player_page.district_dropdown('Lublin')
        self.driver.save_screenshot("./screenshots/add_player_page_district_selected.png")
        Image.open("./screenshots/add_player_page_district_selected.png").show()

    # Test leg dropdown menu
    def test_leg_dropdown(self):
        login_page = LoginPage(self.driver)
        login_page.log_in('user07@getnada.com', 'Test-1234')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_link()
        add_player_page = AddPlayerPage(self.driver)
        add_player_page.leg_dropdown('Left leg')

    # Test add language functionality
    def test_add_language(self):
        login_page = LoginPage(self.driver)
        login_page.log_in('user07@getnada.com', 'Test-1234')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_link()
        add_player_page = AddPlayerPage(self.driver)
        add_player_page.add_language('German')

    # Test add youtube_link functionality
    def test_add_youtube_link_button(self):
        login_page = LoginPage(self.driver)
        login_page.log_in('user07@getnada.com', 'Test-1234')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_link()
        add_player_page = AddPlayerPage(self.driver)
        add_player_page.add_link_to_youtube('https://www.youtube.com/@FazzerHD')

    # Filling Add Player form and add a player. TC06
    def test_add_a_player(self):
        # login into the system
        login_page = LoginPage(self.driver)
        login_page.log_in('user07@getnada.com', 'Test-1234')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_link()
        add_player_page = AddPlayerPage(self.driver)
        # checking page title
        add_player_page.title_of_page()
        # test player creating
        add_player_page.add_a_player('sheva@gmail.com', 'Petro', 'Shevchenko', '12348448888',
                                    '76', '186', '04.07.1985', 'Dynamo', 'High', 'Goalkeeper',
                                    'Defender', 'Many', 'aaa',  '90', 'sheva', 'Opole', 'Right leg',
                                    'German', 'https://www.youtube.com/@footballplayer')
        self.driver.save_screenshot("./screenshots/new_player_created.png")
        Image.open("./screenshots/new_player_created.png").show()

    # Test clear Add Player form. TC07
    def test_clear_add_player_form(self):
        login_page = LoginPage(self.driver)
        login_page.log_in('user07@getnada.com', 'Test-1234')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_link()
        add_player_page = AddPlayerPage(self.driver)
        add_player_page.clear_player_form('Harry', 'Potter', '23071998', 'goalkeeper')
        self.driver.save_screenshot("./screenshots/add_player_form_cleared.png")
        Image.open("./screenshots/add_player_form_cleared.png").show()


    @classmethod
    def tearDown(self):
        self.driver.quit()
