import allure
from IsmagilovaRe_13_12.pages.main_page import MainPage




@allure.feature('Корзина')
@allure.story('Добавление товара в корзину')
@allure.severity(allure.severity_level.NORMAL)
def test_add_item_to_cart(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.select_category()

    with allure.step("Добавляем товар в корзину"):
        main_page.add_item_to_cart()

    with allure.step("Проверяем, что корзина не пуста"):
        assert not main_page.is_cart_empty(), "Корзина не должна быть пуста после добавления товара"




@allure.feature('Корзина')
@allure.story('Удаление товара из корзины')
@allure.severity(allure.severity_level.MINOR)
def test_remove_item_from_cart(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.select_category()
    main_page.add_item_to_cart()
    main_page.open_cart()

    with allure.step("Удаляем товар из корзины"):
        main_page.remove_item_from_cart()

    with allure.step("Проверяем, что корзина пуста после удаления товара"):
        assert main_page.is_cart_empty(), "Корзина должна быть пуста после удаления товара"
