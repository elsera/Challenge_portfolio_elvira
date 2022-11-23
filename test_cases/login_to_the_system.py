import os
import unittest
from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
import subprocess
subprocess.run("pytest --html=report.html --self-contained-html", shell=True)


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        #self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.login_page = LoginPage(self.driver)

    # Comparing expected title text with observed value from web element
    def test_compare_title_text(self):
        self.login_page.assert_element_text(self.login_page.scouts_panel_xpath,
                                            self.login_page.expected_title_text)

    # Log in to the system with valid user data.TC01
    def test_log_in_to_the_system(self):
        # check if the title of the opened page is correct
        self.login_page.title_of_page()
        self.login_page.log_in('user07@getnada.com', 'Test-1234')
        self.driver.save_screenshot("./screenshots/login_page_valid_data.png")
        Image.open("./screenshots/login_page_valid_data.png").show()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        self.driver.save_screenshot("./screenshots/login_go_to_dashboard.png")
        Image.open("./screenshots/login_go_to_dashboard.png").show()

    # Test log in to the system with invalid user credentials. TC02
    def test_log_in_with_invalid_data(self):
        self.login_page.log_in('abcd@abcd.com', '123456789abcd')
        self.login_page.visibility_of_element_located(self.login_page.invalid_login_data_message_xpath)
        self.login_page.assert_element_text(self.login_page.invalid_login_data_message_xpath,
                                            self.login_page.invalid_login_data_message)
        self.driver.save_screenshot("./screenshots/login_page_invalid_data.png")
        Image.open("./screenshots/login_page_invalid_data.png").show()

    # Test log in to the system with empty data. TC03
    def test_log_in_with_empty_data(self):
        self.login_page.log_in('', '')
        self.login_page.presence_of_element_located(self.login_page.empty_fields_reminder_xpath)
        self.login_page.assert_element_text(self.login_page.empty_fields_reminder_xpath,
                                            self.login_page.empty_fields_reminder)
        self.driver.save_screenshot("./screenshots/login_page_empty_data.png")
        Image.open("./screenshots/login_page_empty_data.png").show()

    # Test language dropdown menu. TC04
    def test_language_dropdown_menu(self):
        self.login_page.language_dropdown_option('Polski')
        self.driver.save_screenshot("./screenshots/login_page_language_option.png")
        Image.open("./screenshots/login_page_language_option.png").show()


    @classmethod
    def tearDown(self):
        self.driver.quit()
