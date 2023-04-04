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

    """Набор тестов на фильтр предметов на главной странице"""

    @pytest.mark.run(order=3)
    @allure.title("Фильтрация товаров по возрастающему и убывающему (по имени)")
    def test_filter_az_za(self):
        self.auth.authentication()
        """Парсинг предметов и их сравнение"""
        default_az_sorting = self.mp.get_all_items_names()
        (self.mp.click_filter_button()
         .click_option_filter_button("az"))
        choose_az_sorting = self.mp.get_all_items_names()
        (self.mp.assert_equals(default_az_sorting, choose_az_sorting)
         .click_filter_button()
         .click_option_filter_button("za"))
        choose_za_sorting = self.mp.get_all_items_names()
        self.mp.assert_not_equals(choose_az_sorting, choose_za_sorting)
        choose_za_sorting.reverse()
        self.mp.assert_equals(choose_az_sorting, choose_za_sorting)

    @pytest.mark.run(order=4)
    @allure.title("Фильтрация товаров по возрастающему и убывающему (по цене)")
    def test_filter_prices(self):
        self.auth.authentication()
        """Парсинг предметов и их сравнение"""
        prices = self.mp.get_all_prices()
        self.mp.click_filter_button()
        self.mp.click_option_filter_button("lohi")
        choose_lohi_sorting = self.mp.get_all_prices()
        (self.mp.assert_not_equals(prices, choose_lohi_sorting)
         .click_filter_button()
         .click_option_filter_button("hilo"))
        choose_hilo_sorting = self.mp.get_all_prices()
        self.mp.assert_not_equals(choose_lohi_sorting, choose_hilo_sorting)
        choose_hilo_sorting.reverse()
        self.mp.assert_equals(choose_lohi_sorting, choose_hilo_sorting)
