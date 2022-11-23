from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    remind_password_hyperlink_xpath = "//child::div/a"
    language_dropdown_xpath = "//*[@aria-haspopup='listbox']"
    language_dropdown_list_xpath = "//*[@role='listbox']"
    language_button_pl_text = "Polski"
    language_button_en_text = "English"
    scouts_panel_xpath = "//*[text()='Scouts Panel']"
    invalid_login_data_message_xpath = "//*[contains(text(),'password invalid')]"
    invalid_login_data_message = "Identifier or password invalid."
    empty_fields_reminder_xpath = "//*[contains(text(),'provide your username')]"
    empty_fields_reminder = "Please provide your username or your e-mail."
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login'
    expected_title = "Scouts panel - sign in"
    expected_title_text = "Scouts Panel"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_signin_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def log_in(self, email, password):
        self.type_in_email(email)
        self.type_in_password(password)
        self.click_on_the_signin_button()

    def title_of_page(self):
        assert self.get_page_title() == self.expected_title

    def language_dropdown_option(self, language):
        self.click_dropdown_menu(self.language_dropdown_xpath,
                                 self.language_dropdown_list_xpath, language)




