import allure
import pytest

from sauce.pages.authorizationpage import AuthorizationPage
from sauce.pages.base_page import Base
from sauce.pages.mainpage import MainPage


@allure.suite("Тесты на фильтрацию (сортировку) страницы")
class Test_Filters:
    base = Base()
    auth = AuthorizationPage()
    mp = MainPage()

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("option", ["az", "za"])
    @allure.title("Фильтрация товаров по возрастающему и убывающему (по имени)")
    def test_filter_az_za(self, option):
        self.auth.authentication()
        default_sorting_names = self.mp.get_all_items_names()
        (self.mp.click_filter_button()
         .click_option_filter_button(option))
        after_sorting_names = self.mp.get_all_items_names()
        try:
            self.mp.assert_equals(default_sorting_names, after_sorting_names)
        except:
            after_sorting_names.reverse()
            self.mp.assert_equals(default_sorting_names, after_sorting_names)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("option", ["lohi", "hilo"])
    @allure.title("Фильтрация товаров по возрастающему и убывающему (по цене)")
    def test_filter_prices(self, option):
        self.auth.authentication()
        default_sorting_prices = self.mp.get_all_prices()
        (self.mp.click_filter_button()
         .click_option_filter_button(option))
        after_sorting_prices = self.mp.get_all_prices()
        try:
            self.mp.assert_not_equals(default_sorting_prices, after_sorting_prices)
            default_sorting_prices.sort()
            self.mp.assert_equals(default_sorting_prices, after_sorting_prices)
        except:
            default_sorting_prices.reverse()
            self.mp.assert_equals(default_sorting_prices, after_sorting_prices)
