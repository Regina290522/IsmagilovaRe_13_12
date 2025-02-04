import allure
import requests

token = 'CID=1d457592316fd7abfb7765aadf017d3c; site_countryID=247; site_country_name=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F; _ga=GA1.1.1530799814.1737711614; _userGUID=0:m6akmmhq:0aaNDmcp3ha3QNYHl00O4V_xnlxwQJ8b; _userGUID=0:m6akmmhq:0aaNDmcp3ha3QNYHl00O4V_xnlxwQJ8b; _ym_uid=1737711615575158310; _ym_d=1737711615; PHPSESSID=linkk6glgi9vbhvj1qpcpbbvd1; _dvs=0:m6gs22u4:dboC_SP_vNkKUPaX01tajv6GrfH960Sc; _ym_isad=2; _ym_visorc=w; DIGI_CARTID=6810997929; dSesn=95dcd329-43b6-7c17-2e01-934a2d99e8a1; digi_uc=|v:173809:3823|s:173800:2814!173809:3823; _ga_2JB65Y3D22=GS1.1.1738086888.6.1.1738090739.0.0.0'
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


@allure.title("Проверка запроса добавление товара в корзину")
@allure.description("Проверка отправки post запроса для добавления товара в корзину")
@allure.severity("Critical")
def test_post_product():
    url = 'https://altaivita.ru/engine/cart/add_products_to_cart_from_preview.php'
    response = requests.post(url, headers=headers)

    assert response.status_code == 200


@allure.title("Проверка запроса удаления товара из корзины")
@allure.description("Проверка отправки post запроса для удаления товара из корзины")
@allure.severity("Critical")
def test_post_product_clear():
    url = 'https://altaivita.ru/engine/cart/delete_products_from_cart_preview.php'
    response = requests.post(url, headers=headers)

    assert response.status_code == 200

