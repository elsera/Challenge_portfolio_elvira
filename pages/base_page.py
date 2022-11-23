import time
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        time.sleep(2)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        self.wait_for_element_to_be_clickable(selector)
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self):
        return self.driver.title

    def assert_element_text(self, xpath, expected_text):
        """Comparing expected text with observed value from web element
            :param xpath: xpath to element with text to be observed
            :param expected_text: text what we expecting to be found
            :return: None
        """
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text

    def visibility_of_element_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        time.sleep(3)

    def presence_of_element_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        time.sleep(3)

    def presence_of_all_elements_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))

    def click_dropdown_menu(self, selector1, selector2, value):
        # identify the dropdown element
        self.click_on_the_element(selector1)
        self.visibility_of_element_located(selector2)
        # open dropdown element
        self.click_on_the_element(selector2)
        options = self.driver.find_elements(By.TAG_NAME, 'li')
        for option in options:
            if option.text == value:
                print(option.text)
                option.click()
                time.sleep(3)
                break



