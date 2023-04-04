import allure

from sauce.driver_init import Driver
from sauce.pages.base_page import Base


class MainPage(Base):

    # LOCATORS

    filter_button = "//select"
    filter_az = "//option[@value='az']"
    filter_za = "//option[@value='za']"
    filter_lohi = "//option[@value='lohi']"
    filter_hilo = "//option[@value='hilo']"
    inventory_list_on_main_page = "//div[@class='inventory_list']"

    # GETTERS

    def get_filter_az(self):
        return self.wait_element_clickable(self.filter_az)

    def get_filter_button(self):
        return self.wait_element_clickable(self.filter_button)

    def get_filter_hilo(self):
        return self.wait_element_clickable(self.filter_hilo)

    def get_filter_lohi(self):
        return self.wait_element_clickable(self.filter_lohi)

    def get_filter_za(self):
        return self.wait_element_clickable(self.filter_za)

    # ACTIONS

    @Driver.chain
    def click_filter_button(self):
        with allure.step("Нажать на кнопку Фильтров"):
            return self.get_filter_button().click()

    @Driver.chain
    def click_option_filter_button(self, option):
        with allure.step("Выбрать опцию сортировки Фильтров"):
            if option == "az":
                return self.get_filter_az().click()
            elif option == "za":
                return self.get_filter_za().click()
            elif option == "lohi":
                return self.get_filter_lohi().click()
            else:
                return self.get_filter_hilo().click()
