import os
import unittest
from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.remind_password_page import RemindPasswordPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestRemindPassword(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    # Test sending email in remind password page
    def test_send_email(self):
        login_page = LoginPage(self.driver)
        login_page.get_page_title()
        login_page.click_on_remind_pwd_hyperlink()
        remind_pwd_page = RemindPasswordPage(self.driver)
        remind_pwd_page.get_page_title()
        remind_pwd_page.type_in_email('Test@abc.com')
        remind_pwd_page.visibility_of_element_located(remind_pwd_page.send_button_xpath)
        remind_pwd_page.click_on_the_send_button()
        self.driver.save_screenshot("./screenshots/remind_pwd_email_send.png")
        Image.open("./screenshots/remind_pwd_email_send.png").show()

    # Test back to sign in form page remind password page
    def test_back_to_sign_in(self):
        login_page = LoginPage(self.driver)
        login_page.get_page_title()
        login_page.click_on_remind_pwd_hyperlink()
        remind_pwd_page = RemindPasswordPage(self.driver)
        remind_pwd_page.get_page_title()
        self.driver.save_screenshot("./screenshots/remind_pwd_page.png")
        remind_pwd_page.click_on_back_to_sign_in()
        self.driver.save_screenshot("./screenshots/back_to_login_page.png")
        Image.open("./screenshots/remind_pwd_page.png").show()
        Image.open("./screenshots/back_to_login_page.png").show()

    # Test change language of remind password page
    def test_language_dropdown_menu(self):
        login_page = LoginPage(self.driver)
        login_page.get_page_title()
        login_page.click_on_remind_pwd_hyperlink()
        remind_pwd_page = RemindPasswordPage(self.driver)
        remind_pwd_page.get_page_title()
        self.driver.save_screenshot("./screenshots/remind_pwd_language.png")
        remind_pwd_page.language_dropdown_option('Polski')
        self.driver.save_screenshot("./screenshots/remind_pwd_language_changed.png")
        Image.open("./screenshots/remind_pwd_language.png").show()
        Image.open("./screenshots/remind_pwd_language_changed.png").show()


    @classmethod
    def tearDown(self):
        self.driver.quit()
