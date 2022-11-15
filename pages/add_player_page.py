from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    player_email_field_xpath = "//input[@name='email']"
    player_name_field_xpath = "//input[@name='name']"
    player_surname_field_xpath = "//input[@name='surname']"
    player_phone_field_xpath = "//input[@name='phone']"
    player_weight_field_xpath = "//input[@name='weight']"
    player_height_field_xpath = "//input[@name='height']"
    player_age_field_xpath = "//input[@name='age']"
    player_club_field_xpath = "//input[@name='club']"
    player_level_field_xpath = "//input[@name='level']"
    player_main_position_field_xpath = "//input[@name='mainPosition']"
    player_second_position_field_xpath = "//input[@name='secondPosition']"
    player_achievements_field_xpath = "//input[@name='achievements']"
    weblaczy_field_xpath = "//input[@name='webLaczy']"
    minut90_field_xpath = "//input[@name='web90']"
    facebook_field_xpath = "//input[@name='webFB']"
    submit_button_xpath = "//button[@type='submit']"
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    expected_title = 'Add player'

    def type_in_email(self, email):
        self.field_send_keys(self.player_email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.player_name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.player_surname_field_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.player_phone_field_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.player_weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.player_height_field_xpath, height)

    def type_in_age(self, age):
        self.field_send_keys(self.player_age_field_xpath, age)

    def type_in_club(self, club):
        self.field_send_keys(self.player_club_field_xpath, club)

    def type_in_level(self, level):
        self.field_send_keys(self.player_level_field_xpath, level)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.player_main_position_field_xpath, main_position)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.player_second_position_field_xpath, second_position)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.player_achievements_field_xpath, achievements)

    def type_in_weblaczy(self, weblaczy):
        self.field_send_keys(self.weblaczy_field_xpath, weblaczy)

    def type_in_minut90(self, minut90):
        self.field_send_keys(self.minut90_field_xpath, minut90)

    def type_in_facebook(self, facebook):
        self.field_send_keys(self.facebook_field_xpath, facebook)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title




