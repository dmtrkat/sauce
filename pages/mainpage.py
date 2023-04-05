import allure
import pytest

from sauce.driver_init import Driver
from sauce.pages.base_page import Base


class MainPage(Base):

    # LOCATORS

    FILTER_BUTTON = "//select"
    FILTER_AZ = "//option[@value='az']"
    FILTER_ZA = "//option[@value='za']"
    FILTER_LOHI = "//option[@value='lohi']"
    FILTER_HILO = "//option[@value='hilo']"
    INVENTORY_LIST_ON_MAIN_PAGE = "//div[@class='inventory_list']"

    # GETTERS

    def get_filter_button(self):
        return self.wait_element_clickable(self.FILTER_BUTTON)

    def get_filter(self, option):
        if option == "az":
            return self.wait_element_clickable(self.FILTER_AZ)
        if option == "za":
            return self.wait_element_clickable(self.FILTER_ZA)
        if option == "lohi":
            return self.wait_element_clickable(self.FILTER_LOHI)
        if option == "hilo":
            return self.wait_element_clickable(self.FILTER_HILO)

    # ACTIONS

    @Driver.chain
    def click_filter_button(self):
        with allure.step("Нажать на кнопку Фильтров"):
            return self.get_filter_button().click()

    @Driver.chain
    def click_option_filter_button(self, option):
        with allure.step("Выбрать опцию сортировки Фильтров"):
            return self.get_filter(option).click()
