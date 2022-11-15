from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    remind_password_hyperlink_xpath = "//child::div/a"
    language_option_xpath = "//input[@class='MuiSelect-nativeInput']"
    scouts_panel_xpath = "//*[text()='Scouts Panel']"
    invalid_login_data_massage_xpath = "//*[contains(text(),'password invalid')]"
    empty_fields_reminder_xpath = "//*[contains(text(),'provide your username')]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login'
    expected_title = 'Scouts panel - sign in'
    expected_text = 'Scouts Panel'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_signin_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    # Comparing expected text with observed value from web element
    def compare_title_text(self, driver):
        self.assert_element_text(driver, self.scouts_panel_xpath, self.expected_text)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

