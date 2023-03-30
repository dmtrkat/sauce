import pytest
from sauce.pages.authorizationpage import AuthorizationPage
from sauce.pages.base_page import Base
from sauce.pages.cartpage import CartPage


class TestFunctionality:
    base = Base()
    auth = AuthorizationPage()
    cartp = CartPage()

    @pytest.mark.run(order=5)
    def test_continue_shopping_button(self):
        self.auth.authentication()
        x = self.base.get_all_items_names()
        (self.cartp.click_add_to_cart_button_2()
         .click_cart_button()
         .click_continue_shopping_button()
         .click_remove_from_cart_button())
        y = self.base.get_all_items_names()
        self.cartp.assert_equals(x, y)

    """Проблема локатора в строке с переменной 'y'"""
    # @pytest.mark.run(order=6)
    # def test_add_to_cart_from_itemcard(self):
    #     self.auth.authentication()
    #     self.base.get_item_name_when_add("click")
    #     x = self.base.get_item_name_in_card()
    #     self.base.click_add_to_cart_button_2()
    #     self.base.click_cart_button()
    #     y = self.base.get_item_name_when_add("text")
    #     self.cartp.click_remove_from_cart_button()
    #     assert x == y

    @pytest.mark.run(order=7)
    def test_remove_from_itemcard(self):
        self.auth.authentication()
        self.base.get_item_name_when_add("click")
        (self.base.click_add_to_cart_button_2()
         .click_remove_from_cart_button()
         .wait_element_visible(self.base.ADD_TO_CART))

    @pytest.mark.run(order=8)
    def test_back_to_products_button(self):
        self.auth.authentication()
        x = self.base.get_all_items_names()
        self.base.get_item_name_when_add("click")
        self.base.wait_element_clickable("//button[@id='back-to-products']").click()
        y = self.base.get_all_items_names()
        self.base.assert_equals(x, y)
#