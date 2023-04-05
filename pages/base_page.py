import random
import re
import time
import allure

from sauce.driver_init import Driver


class Base(Driver):
    # VARIABLES
    URL = "https://www.saucedemo.com/"
    RAN_RAN = random.randint(0, 6)
    RANDOM_RANDINT = RAN_RAN

    # LOCATORS
    ADD_TO_CART = "//button[text()='Add to cart']"
    BURGER_MENU = "//button[@id='react-burger-menu-btn']"
    CART_BUTTON = "//a[@class='shopping_cart_link']"
    ITEM_NAME = "//div[@class='inventory_item_name']"
    ITEM_NAME_IN_CARD = "//div[@class='inventory_details_name large_size']"
    ITEM_PRICES = "//div[@class='inventory_item_price']"
    ITEM_DESCRIPTIONS = "//div[@class='inventory_item_desc']"
    LOGOUT = "//a[@id='logout_sidebar_link']"
    REMOVE_BUTTON = "//button[text()='Remove']"

    def add_to_cart_button(self):
        return "(//div[@class='inventory_item_name']/ancestor::div[@class='inventory_item_description']/\
        descendant::button[text()='Add to cart'])[" + str(self.RANDOM_RANDINT) + "]"

    def item_name_when_add(self):
        return ("(//div[@class='inventory_item_name']/ancestor::div[@class='inventory_item_description']/"
                "descendant::button[text()='Add to cart'])[" + str(
            self.RANDOM_RANDINT) + "]/ancestor::div[@class='inventory_item_description']"
                                   "//div[@class='inventory_item_name']")

    # GETTERS

    """Для выбора случайной кнопки 'Add to cart' на странице"""

    def get_add_to_cart_button(self):
        return self.wait_element_clickable(self.add_to_cart_button())

    """Для выбора единственной кнопки 'Add to cart' на странице"""

    def get_add_to_cart_button_2(self):
        return self.wait_element_clickable(self.ADD_TO_CART)

    def get_all_items_names(self):
        with allure.step("Парсинг всех названий товаров на странице"):
            return [e.text for e in self.wait_elements_visible(self.ITEM_NAME)]

    def get_all_prices(self):
        with allure.step("Парсинг всех цен товаров на странице"):
            prices = [e.text for e in self.wait_elements_visible(self.ITEM_PRICES)] #class list
            prices_str = "".join(prices) # class str
            no_dollar = re.split("\\$", prices_str)
            no_dollar.pop(0)
            x = " ".join(no_dollar)
            nums = [float(n) for n in x.split()]
            return nums

    def get_all_descriptions(self):
        with allure.step("Парсинг всех описаний товаров на странице"):
            return [e.text for e in self.wait_elements_visible(self.ITEM_DESCRIPTIONS)]

    def get_burger_menu(self):
        return self.wait_element_clickable(self.BURGER_MENU)

    def get_cart_button(self):
        with allure.step("Нажать "):
            return self.wait_element_clickable(self.CART_BUTTON)

    def get_item_name_when_add(self, driver_action):
        time.sleep(1)
        try:
            if driver_action == "click":
                with allure.step("Нажать на элемент"):
                    return self.wait_element_clickable(self.item_name_when_add()).click()
            elif driver_action == "text":
                with allure.step("Парсинг текста элемента"):
                    return self.wait_element_visible(self.item_name_when_add()).text
        except:
            self.driver.refresh()
            time.sleep(1)
            self.get_item_name_when_add(driver_action)

    def get_item_name_in_card(self):
        with allure.step("Парсинг текста (название товара) внутри карточки этого товара"):
            return self.wait_element_visible(self.ITEM_NAME_IN_CARD).text

    def get_item_name_in_cart(self):
        with allure.step("Парсинг текста (название товара) добавленного товара в корзину"):
            return self.wait_element_clickable(self.ITEM_NAME).text

    def get_logout_button(self):
        return self.wait_element_clickable(self.LOGOUT)

    def get_remove_from_cart_button(self):
        with allure.step("Нажать на кнопку 'Remove' из корзины"):
            return self.wait_element_clickable(self.REMOVE_BUTTON)

    # ACTIONS

    """Для клика по случайной кнопке 'Add to cart' на странице"""
    @Driver.chain
    def click_add_to_cart_button(self):
        with allure.step("Нажать на кнопку добавления товара (Add to cart) среди множества таких кнопок"):
            return self.get_add_to_cart_button().click()

    """Для клика по единственной кнопке 'Add to cart' на странице"""
    @Driver.chain
    def click_add_to_cart_button_2(self):
        with allure.step("Нажать на единственный кнопку добавления товара на странице (Add to cart)"):
            return self.get_add_to_cart_button_2().click()

    @Driver.chain
    def click_remove_from_cart_button(self):
        with allure.step("Нажать на кнопку 'Remove'"):
            return self.get_remove_from_cart_button().click()

    @Driver.chain
    def click_cart_button(self):
        with allure.step("Нажать на корзину"):
            return self.get_cart_button().click()

    def click_burger_menu(self):
        return self.get_burger_menu().click()

    def click_logout_button(self):
        return self.get_logout_button().click()

    # METHODS

    @Driver.chain
    def assert_equals(self, x, y):
        with allure.step("Сравнить результат парсинга (равенство)"):
            assert x == y

    @Driver.chain
    def assert_not_equals(self, x, y):
        with allure.step("Сравнить результат парсинга (неравенство)"):
            assert x != y

    def validate_items(self):
        with allure.step(""):
            names = self.get_all_items_names()
            # prices = self.get_all_prices()
            descriptions = self.get_all_descriptions()
            nd = dict(zip(names, descriptions))
            return nd
