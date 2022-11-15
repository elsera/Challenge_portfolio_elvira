import os
import time
import unittest

from selenium import webdriver
from test_cases.login_to_the_system import TestLoginPage
from pages.add_player_page import AddPlayerPage
from pages.dashboard_page import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayerPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):
        self.user_login = TestLoginPage.test_log_in_to_the_system(self)  # login into the system
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_link()
        add_player_page = AddPlayerPage(self.driver)
        add_player_page.title_of_page() # checking page title
        add_player_page.type_in_email('sheva@gmail.com')
        add_player_page.type_in_surname('Shevchenko')
        add_player_page.type_in_name('Petro')
        add_player_page.type_in_level('High')
        add_player_page.type_in_age('04071985')
        add_player_page.type_in_phone('12348448888')
        add_player_page.type_in_achievements('many')
        add_player_page.type_in_club('Dynamo')
        add_player_page.type_in_height('186')
        add_player_page.type_in_weight('76')
        add_player_page.type_in_main_position('Goalkeeper')
        add_player_page.type_in_second_position('Defender')
        add_player_page.type_in_minut90('90')
        add_player_page.type_in_weblaczy('aaa')
        add_player_page.type_in_facebook('https://www.facebook.com/sheva/')
        add_player_page.click_on_the_submit_button()  # player creating
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
