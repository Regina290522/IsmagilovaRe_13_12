import allure
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://altaivita.ru/")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    with allure.step("Добавление книги на кириллице"):
        def rus_add(self, term):
            self._driver.find_element(By.CLASS_NAME, "header-add__input").send_keys(term)
            self._driver.find_element(By.CLASS_NAME, "header-add__button").click()
            txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
            return txt

    with allure.step("Пустая корзина"):
        def empty_basket(self, term):
            self._driver.find_element(By.CLASS_NAME, "header-basket__input").send_keys(term)
            self._driver.find_element(By.CLASS_NAME, "header-basket__button").click()

