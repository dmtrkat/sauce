import allure

from sauce.driver_init import Driver
from sauce.pages.base_page import Base


class CartPage(Base):

    # LOCATORS
    CHECKOUT_BUTTON = "//button[@id='checkout']"
    CONTINUE_BUTTON = "//input[@id='continue']"
    CONTINUE_SHOPPING_BUTTON = "//button[@id='continue-shopping']"
    FIRST_NAME_PLACEHOLDER = "//input[@id='first-name']"
    FINISH_BUTTON = "//button[@id='finish']"
    INPUT_ERROR_FNAME = "//input[@class='input_error form_input error' and @placeholder='First Name']"
    INPUT_ERROR_LNAME = "//input[@class='input_error form_input error' and @placeholder='Last Name']"
    INPUT_ERROR_PCODE = "//input[@class='input_error form_input error' and @placeholder='Zip/Postal Code']"
    LAST_NAME_PLACEHOLDER = "//input[@id='last-name']"
    NOTE_ERROR = "//h3[text()='Error: First Name is required']"
    POSTAL_CODE_PLACEHOLDER = "//input[@id='postal-code']"
    THANK_YOU_FOR_ORDER = "//h2[text()='Thank you for your order!']"

    # GETTERS

    @Driver.chain
    def get_all_errors_placeholders(self):
        with allure.step("Парсинг ошибок (предупреждений) на обязательные поля"):
            return self.INPUT_ERROR_FNAME, self.INPUT_ERROR_LNAME, self.INPUT_ERROR_PCODE

    def get_check_out_button(self):
        return self.wait_element_clickable(self.CHECKOUT_BUTTON)

    def get_continue_button(self):
        return self.wait_element_clickable(self.CONTINUE_BUTTON)

    def get_continue_shopping_button(self):
        return self.wait_element_clickable(self.CONTINUE_SHOPPING_BUTTON)

    def get_first_name_placeholder(self):
        return self.wait_element_clickable(self.FIRST_NAME_PLACEHOLDER)

    def get_finish_button(self):
        return self.wait_element_clickable(self.FINISH_BUTTON)

    def get_last_name_placeholder(self):
        return self.wait_element_clickable(self.LAST_NAME_PLACEHOLDER)

    @Driver.chain
    def get_note_error(self):
        with allure.step("Плашка уведомления на обязательные поля ФЛК"):
            return self.wait_element_visible(self.NOTE_ERROR)

    def get_postal_code_placeholder(self):
        return self.wait_element_clickable(self.POSTAL_CODE_PLACEHOLDER)

    @Driver.chain
    def get_thanks(self):
        with allure.step("Подтверждение, что заказ удался"):
            return self.wait_element_visible(self.THANK_YOU_FOR_ORDER)

    # ACTIONS

    @Driver.chain
    def click_check_out_button(self):
        with allure.step("Нажать кнопку Check out"):
            return self.get_check_out_button().click()

    @Driver.chain
    def click_continue_button(self):
        return self.get_continue_button().click()

    @Driver.chain
    def click_continue_shopping_button(self):
        with allure.step("Нажать на кнопку 'Continue Shopping'"):
            return self.get_continue_shopping_button().click()

    @Driver.chain
    def click_finish_button(self):
        with allure.step("Нажать на кнопку 'Finish'"):
            return self.get_finish_button().click()

    @Driver.chain
    def input_first_name_placeholder(self, fname):
        with allure.step("Ввод имени покупателя"):
            return self.get_first_name_placeholder().send_keys(fname)

    @Driver.chain
    def input_last_name_placeholder(self, lname):
        with allure.step("Ввод фамилии покупателя"):
            return self.get_last_name_placeholder().send_keys(lname)

    @Driver.chain
    def input_postal_code_placeholder(self, pcode):
        with allure.step("Ввод индекса покупателя"):
            return self.get_postal_code_placeholder().send_keys(pcode)
