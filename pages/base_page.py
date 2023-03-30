import random
import time

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
                "descendant::button[text()='Add to cart'])[" + str(self.RANDOM_RANDINT) + "]/ancestor::div[@class='inventory_item_description']"
                "//div[@class='inventory_item_name']")
    # GETTERS

    """Для выбора случайной кнопки 'Add to cart' на странице"""
    def get_add_to_cart_button(self):
        return self.wait_element_clickable(self.add_to_cart_button())

    """Для выбора единственной кнопки 'Add to cart' на странице"""
    def get_add_to_cart_button_2(self):
        return self.wait_element_clickable(self.ADD_TO_CART)

    def get_all_items_names(self):
        return [e.text for e in self.wait_elements_visible(self.ITEM_NAME)]

    def get_all_prices(self):
        return [e.text for e in self.wait_elements_visible(self.ITEM_PRICES)]

    def get_all_descriptions(self):
        return [e.text for e in self.wait_elements_visible(self.ITEM_DESCRIPTIONS)]

    def get_burger_menu(self):
        return self.wait_element_clickable(self.BURGER_MENU)

    def get_cart_button(self):
        return self.wait_element_clickable(self.CART_BUTTON)

    def get_item_name_when_add(self, driver_action):
        time.sleep(1)
        if driver_action == "click":
            return self.wait_element_clickable(self.item_name_when_add()).click()
        elif driver_action == "text":
            return self.wait_element_visible(self.item_name_when_add()).text

    def get_item_name_in_card(self):
        return self.wait_element_visible(self.ITEM_NAME_IN_CARD).text

    def get_item_name_in_cart(self):
        return self.wait_element_clickable(self.ITEM_NAME).text

    def get_logout_button(self):
        return self.wait_element_clickable(self.LOGOUT)

    def get_remove_from_cart_button(self):
        return self.wait_element_clickable(self.REMOVE_BUTTON)

    # ACTIONS

    """Для клика по случайной кнопке 'Add to cart' на странице"""
    @Driver.chain
    def click_add_to_cart_button(self):
        return self.get_add_to_cart_button().click()

    """Для клика по единственной кнопке 'Add to cart' на странице"""
    @Driver.chain
    def click_add_to_cart_button_2(self):
        return self.get_add_to_cart_button_2().click()

    @Driver.chain
    def click_remove_from_cart_button(self):
        return self.get_remove_from_cart_button().click()

    @Driver.chain
    def click_cart_button(self):
        return self.get_cart_button().click()

    def click_burger_menu(self):
        return self.get_burger_menu().click()

    def click_logout_button(self):
        return self.get_logout_button().click()

    # METHODS

    @Driver.chain
    def assert_equals(self, x, y):
        assert x == y

    @Driver.chain
    def assert_not_equals(self, x, y):
        assert x != y

    def validate_items(self):
        names = self.get_all_items_names()
        # prices = self.get_all_prices()
        descriptions = self.get_all_descriptions()
        nd = dict(zip(names, descriptions))
        return nd
