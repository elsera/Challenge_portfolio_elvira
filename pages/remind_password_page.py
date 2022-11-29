from pages.base_page import BasePage


class RemindPasswordPage(BasePage):
    title_page_xpath = "//h5"
    email_field_xpath = "//input[@name='email']"
    back_to_sign_in_hyperlink = "//a"
    language_dropdown_xpath = "//div[2]/div"
    language_dropdown_list_xpath = "//div[3]/ul"
    send_button_xpath = "//button[@type='submit']"
    expected_title = "Remind password"
    remind_pwd_page_url = "https://scouts-test.futbolkolektyw.pl/en/remind"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.title_page_xpath)
        assert self.get_page_title() == self.expected_title

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def click_on_back_to_sign_in(self):
        self.click_on_the_element(self.back_to_sign_in_hyperlink)

    def language_dropdown_option(self, language):
        self.click_dropdown_menu(self.language_dropdown_xpath,
                                 self.language_dropdown_list_xpath, language)

    def click_on_the_send_button(self):
        self.click_on_the_element(self.send_button_xpath)

