import random
import time
from selenium.webdriver.common.by import By
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
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    leg_dropdown_list_xpath = "//*[@id='menu-leg']//li"
    district_xpath = "//*[@id='mui-component-select-district']"
    menu_district_xpath = "//*[@id='menu-district']//li"
    weblaczy_field_xpath = "//input[@name='webLaczy']"
    minut90_field_xpath = "//input[@name='web90']"
    facebook_field_xpath = "//input[@name='webFB']"
    add_language_button_xpath = "//button[@aria-label='Add language']"
    languages_field_xpath = "//input[contains(@name,'languages')]"
    add_link_to_youtube_button_xpath = "//button[@aria-label='Add link to Youtube']"
    youtube_link_field_xpath = "//input[contains(@name,'webYT')]"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//button[contains(@class,'containedSecondary')]"
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    page_logo_xpath = "//*[text()='Scouts Panel']"
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

    def click_on_the_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)

    def leg_dropdown(self, leg):
        self.click_dropdown_menu(self.leg_dropdown_xpath,
                                 self.leg_dropdown_list_xpath, leg)

    def district_random_option(self):
        self.click_on_the_element(self.district_xpath)
        time.sleep(3)
        self.presence_of_all_elements_located(self.menu_district_xpath)
        items = self.driver.find_elements(By.TAG_NAME, 'li')
        amount = len(items)
        self.click_on_the_element(self.menu_district_xpath+'['+str(random.randint(0, amount))+']')

    def district_dropdown(self, district):
        self.click_dropdown_menu(self.district_xpath, self.menu_district_xpath, district)

    def add_language(self, language):
        self.click_on_the_element(self.add_language_button_xpath)
        self.field_send_keys(self.languages_field_xpath, language)

    def add_link_to_youtube(self, youtube_link):
        self.click_on_the_element(self.add_link_to_youtube_button_xpath)
        self.field_send_keys(self.youtube_link_field_xpath, youtube_link)

    def add_a_player(self, email, name, surname, phone, weight, height,
                    age, club, level, main_position, second_position, achievements,
                    weblaczy, minut90, facebook, district, leg, language, youtube_link):
        self.type_in_email(email)
        self.type_in_name(name)
        self.type_in_surname(surname)
        self.type_in_phone(phone)
        self.type_in_weight(weight)
        self.type_in_height(height)
        self.type_in_age(age)
        self.type_in_club(club)
        self.type_in_level(level)
        self.type_in_main_position(main_position)
        self.type_in_second_position(second_position)
        self.type_in_achievements(achievements)
        self.type_in_weblaczy(weblaczy)
        self.type_in_minut90(minut90)
        self.type_in_facebook(facebook)
        self.district_dropdown(district)
        self.leg_dropdown(leg)
        self.add_language(language)
        self.add_link_to_youtube(youtube_link)
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_submit_button()
        time.sleep(2)

    def clear_player_form(self, name, surname, age, main_position):
        self.type_in_name(name)
        self.type_in_surname(surname)
        self.type_in_age(age)
        self.type_in_main_position(main_position)
        self.wait_for_element_to_be_clickable(self.clear_button_xpath)
        self.click_on_the_clear_button()
        fields = self.driver.find_elements(By.TAG_NAME, 'input')
        for field in fields:
            if len(field.get_attribute('value')) == 0:
                assert True
            else:
                print(field.get_attribute('value'))
                break



    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.page_logo_xpath)
        assert self.get_page_title() == self.expected_title





