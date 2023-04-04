import allure
import pytest

from sauce.pages.authorizationpage import AuthorizationPage
from sauce.pages.base_page import Base
from sauce.pages.cartpage import CartPage
from sauce.utilities.items_info import Items_info


@allure.suite("Смоук-тесты")
class Test_Smoke:
    base = Base()
    auth = AuthorizationPage()
    cart = CartPage()

    @pytest.mark.first
    @allure.title("Покупка товара от начала до конца")
    def test_do_order(self):
        self.auth.authentication()
        item_name_when_add = self.base.get_item_name_when_add("text")
        (self.base.click_add_to_cart_button()
         .click_cart_button())
        item_name_in_cart = self.base.get_item_name_in_cart()
        self.base.assert_equals(item_name_when_add, item_name_in_cart)
        """Шаги оформления заказа"""
        (self.cart.click_check_out_button()
         .input_first_name_placeholder("Dmtr")
         .input_last_name_placeholder("Kat")
         .input_postal_code_placeholder("123")
         .click_continue_button())
        """Подтверждение заказа"""
        item_name_in_cart_aprove = self.base.get_item_name_in_cart()
        self.base.assert_equals(item_name_in_cart, item_name_in_cart_aprove)
        (self.cart.click_finish_button()
         .get_thanks())

    @pytest.mark.run(order=1)
    @allure.title("Валидация на заполненность данных покупателя товара")
    def test_validate_not_empty_placeholders_in_checkout_info(self):
        self.auth.authentication()
        self.base.click_cart_button()
        (self.cart.click_check_out_button()
         .input_first_name_placeholder("")
         .input_last_name_placeholder("")
         .input_postal_code_placeholder("")
         .click_continue_button()
         .get_all_errors_placeholders()
         .get_note_error())

    @pytest.mark.run(order=2)
    @allure.title("Валидация, что имя товара и его описание сооветствует дефолтным значениям")
    def test_validate_items_with_their_descriptions(self):
        ii = Items_info()
        (self.auth.authentication()
         .assert_equals(self.base.validate_items(), ii.DICT_ITEMS))
