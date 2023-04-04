import allure

from sauce.driver_init import Driver
from sauce.pages.base_page import Base
from sauce.utilities.auth_data import Auth_data


class AuthorizationPage(Base):

    auth = Auth_data()

    # LOCATORS
    login_button = "//input[@id='login-button']"
    passwords_placeholder = "//input[@id='password']"
    username_placeholder = "//input[@id='user-name']"

    # GETTERS

    def get_login_button(self):
        return self.wait_element_clickable(self.login_button)

    def get_password(self):
        return self.wait_element_clickable(self.passwords_placeholder)

    def get_username(self):
        return self.wait_element_clickable(self.username_placeholder)

    # ACTIONS

    def login_click(self):
        self.get_login_button().click()

    def input_password(self, password_index):
        self.get_password().send_keys(self.auth.PASSWORDS[password_index])

    def input_username(self, name_index):
        self.get_username().send_keys(self.auth.USERNAMES[name_index])


    # METHODS

    @Driver.chain
    def authentication(self):
        with allure.step("Авторизация на сайте"):
            self.driver.get(self.URL)
            self.driver.delete_all_cookies()
            self.input_username(0)
            self.input_password(0)
            self.login_click()
