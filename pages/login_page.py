 from pages.base_page import BasePage


 class LoginPage(BasePage):
     login_field_xpath = "//*[@id='login']"
     password_field_xpath = "//*[@id='password']"
     sign_in_button_xpath = "//button[@type='submit']"
     remind_password_hyperlink_xpath = "//*[text()='Remind password' or text()='Przypomnij hasło']"
     language_option_xpath = "//input[@class='MuiSelect-nativeInput']/parent::div"
     scouts_panel_xpath = "//*[text()='Scouts Panel']"
     invalid_login_data_massage_xpath = "//*[contains(text(),'password invalid')]"
     empty_fields_reminder_xpath = "//*[contains(text(),'provide your username')]"

     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)
