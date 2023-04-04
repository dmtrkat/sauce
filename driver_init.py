import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver:

    driver = webdriver.Chrome(executable_path="C:\\chromedriver")

    def __init__(self):
        self.driver = self.driver
        self.driver.maximize_window()

    def __call__(self, *args, **kwargs):
        pass

    """Декоратор на чейнинг методов"""
    def chain(func):
        def method(*args, **kwargs):
            func(*args, **kwargs)
            return args[0]
        return method

    def wait_element_clickable(self, xpath):
        with allure.step("Ожидание кликабельности на странице"):
            return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def wait_element_visible(self, xpath):
        with allure.step("Ожидание видимости элемента на странице"):
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def wait_elements_visible(self, xpath):
        with allure.step("Ожидание видимости элементов на странице"):
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))

    def tear_down(self):
        self.driver.close()
        self.driver.quit()
