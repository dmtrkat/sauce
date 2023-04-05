import allure

from sauce.driver_init import Driver
from sauce.pages.base_page import Base
from sauce.utilities.auth_data import Auth_data


class AuthorizationPage(Base):

    auth = Auth_data()

    # LOCATORS
    LOGIN_BUTTON = "//input[@id='login-button']"
    PASSWORDS_PLACEHOLDER = "//input[@id='password']"
    USERNAME_PLACEHOLDER = "//input[@id='user-name']"

    # GETTERS

    def get_login_button(self):
        return self.wait_element_clickable(self.LOGIN_BUTTON)

    def get_password(self):
        return self.wait_element_clickable(self.PASSWORDS_PLACEHOLDER)

    def get_username(self):
        return self.wait_element_clickable(self.USERNAME_PLACEHOLDER)

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
