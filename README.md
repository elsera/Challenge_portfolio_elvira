# Framework_test
## Task 1: software configuration.
### Subtask 1: Why did I choose to participate in the Dare IT Challenge?
Hello. My name is Elvira. And first of all, I take part in this project because I really like to learn something new for myself and test my abilities. 
I also like to find bugs and their causes in applications. 
I like to solve complex tasks and work in a team, this is a plus of this challenge for me, since it is easier to solve something complex collectively. 
Teamwork motivates me. My goal is to gain and use skills in using tools for automated testing, as well as communication with like-minded people.

I wish myself and everyone involved in this challenge good luck :smiley:. And thanks to all the mentors.

## Task 2: selectors.

Here are the selectors for each of the elements on the login page that I have found:

<kbd><img width="350" alt="login_page" src="https://github.com/elsera/images/blob/main/login_page.png?raw=true"></kbd>

* **scouts_panel_element_xpath**
``` 
//*[@id="__next"]/form/div/div[1]/h5

//*[text()="Scouts Panel"]

//child::div/h5
```

* **login_field_xpath**
``` 
//*[@id="login"]

//input[@name="login"]

//*[contains(@name, "login")]
```

* **password_field_xpath**
```
//*[@id="password"] 

//*[contains(@name, "password")]

//child::div/input[@type="password"]
```

* **empty_fields_reminder_xpath**

<kbd><img width="350" alt="empty_fields_message" src="https://github.com/elsera/images/blob/main/empty_fields_message.png?raw=true"></kbd>

```
//child::div/span

//*[text()="Please provide your username or your e-mail."]

//*[contains(text(),"provide your username")]
```

* **invalid_login_data_massage_xpath**

<kbd><img width="350" alt="invalid_login_data_massage" src="https://github.com/elsera/images/blob/main/invalid_password_message.png?raw=true"></kbd>

```
//child::div/span

//*[text()="Identifier or password invalid."]

//*[contains(text(),"password invalid")]
```

* **remind_password_hyperlink_xpath**
```
//div/div[1]/a

//*[text()="Remind password" or text()="Przypomnij hasło"]

//child::div/a
```

* **language_option_button_xpath**
```
//*[contains(@class,"MuiSelect-nativeInput")]

//child::div//following::input[3]

//input[@value="en" or @value="pl"]
```

* **signin_button_xpath**
```
//button[@type="submit"]

//child::div/button

//*[text()="Zaloguj" or text()="Sign in"]//ancestor::button
```
