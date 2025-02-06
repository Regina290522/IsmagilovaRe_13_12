Инструкция по работе с коллекцией Postman
Доступ в Postman:
логин: reginafaizova579@gmail.com
пароль: Ramina290522

1. Коллекция нацелена провести смоук-тест основного функционала  “Аттестация в Postman” на интернет-магазин https://altaivita.ru/ :
добавление товара;
изменение количества товара (увеличение)
удаление товара
Составлены позитивные и негативные тесты.

2. Запросы в коллекции                                                  |
ID: 1
Шаги: Добавление товара
Метод API: Request URL: https://altaivita.ru/engine/cart/add_products_to_cart_from_preview.php                                      Request Method: POST
           Request Method: POST
           Request Body (Payload): {
product_id=934&this_listId=search_list&LANG_key=ru&S_wh=1&S_CID=1d457592316fd7abfb7765aadf017d3c&S_cur_code=rub&S_koef=1&quantity=1&S_hint_code=&S_customerID=
}
Ожидаемый результат: Status Code: 200 ОК
                     Response Body:
{
"status":"ok",
"btn_text":"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u043e",
"alert_text":"",
"new_quantity":1,
"total_bonus_discount":"0",
"sum_quantity":"3",
"products_amount":6398,
"cur_icon":"\u20bd",
"lang_unit":"\u0448\u0442.",
"total_cart_hint":0,
"total_cart_hint_icon":null
}

ID: 2
Шаги: Изменение количества товара (увеличение)
Метод API: Request URL: https://altaivita.ru/engine/cart/action_with_basket_on_cart_page.php
           Request Method: POST
           Request Body (Payload): {
itemID=770952&quantity=2&action=update_quantity&LANG_key=ru&S_wh=1&S_CID=1d457592316fd7abfb7765aadf017d3c&S_cur_code=rub&S_koef=1&S_hint_code=&S_customerID=
}
Ожидаемый результат: Status Code: 200 ОК
                     Response Body:
{
"status":"ok",
"btn_text":"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u043e",
"alert_text":"",
"total_bonus_discount":"0",
"sum_quantity":"2",
"products_amount":400,
"cur_icon":"\u20bd","lang_unit":"\u0448\u0442.",
"total_cart_hint":0,
"total_cart_hint_icon":null,
"total_quantity_items":"2",
"total_cost_items":400,
"discount_by_itemID":0,
"text_discount_quantity":"\u0441\u043a\u0438\u0434\u043a\u0430 \u0437\u0430 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e"
}

ID: 3
Шаги: Удаление товара
Метод API: Request URL: https://altaivita.ru/engine/cart/delete_products_from_cart_preview.php
           Request Method: POST
           Request Body (Payload): {
product_id=7099&LANG_key=ru&S_wh=1&S_CID=1d457592316fd7abfb7765aadf017d3c&S_cur_code=rub&S_koef=1&S_hint_code=&S_customerID=
}
Ожидаемый результат: Status Code: 200 ОК
                     Response Body:
{
"quantity_to_delete":"2",
"price_to_delete":"3099",
"type_items":"product",
"status":"ok",
"alert_text":"",
"total_bonus_discount":"0",
"sum_quantity":"2",
"products_amount":400,
"cur_icon":"\u20bd",
"lang_unit":"\u0448\u0442.",
"total_cart_hint":0,
"total_cart_hint_icon":null
}

3. Переменные и скрипты
В коллекции используются переменные:
CID=1d457592316fd7abfb7765aadf017d3c
idProd: ID товара, который вы хотите добавить, изменить или удалить.

В коллекции используются скрипты для проверки ответа,например:
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});


pm.test("Ответ должен быть 1 при увеличении товара", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.eql(1);
});

4. Авторизация
Для выполнения запросов не требуется авторизация, но необходимо передавать куки в заголовках, например:
Cookie: CID=1d457592316fd7abfb7765aadf017d3c; site_countryID=247; site_country_name=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F; _ga=GA1.1.1530799814.1737711614; _userGUID=0:m6akmmhq:0aaNDmcp3ha3QNYHl00O4V_xnlxwQJ8b; _userGUID=0:m6akmmhq:0aaNDmcp3ha3QNYHl00O4V_xnlxwQJ8b; _ym_uid=1737711615575158310; _ym_d=1737711615; PHPSESSID=8s8lfn68ee503qmlmqe63b8a41; dSesn=fffc0f5b-5c58-2011-642a-2fcfdef955b5; _dvs=0:m6kmvdtx:aOwhx6k87_DDZiARTDRVYadxm1NGAbSP; _ym_isad=2; _ym_visorc=w; digi_uc=|v:173809:3823|s:173832:3823:2814; DIGI_CARTID=40654545131; _ga_2JB65Y3D22=GS1.1.1738320043.8.1.1738321173.0.0.0

5. Создание коллекции в Postman: необходимо зайти в интернет-магазин https://altaivita.ru/, через вкладку DevTools, выбираем вкладку Network, далее находим наш запрос в колонке Name, и во вкладке Headers, находим в разделе Request Headers наш Cookie и это значение применяем в Cookie, далее мы добавляем в коллекцию в Postman, для успешного прохождения тестов. Или вторым способом импортируйте коллекцию в Postman.
Нажмите на кнопку "Import" и выберите файл коллекции, добавьте переменные,
проверить отработку переменных на правильность и запустите тесты.
Далее выберите нужный запрос и нажмите кнопку "Send".
Проверьте ответ на соответствие ожидаемым результатам.

6. Выводы
В результате работы с помощью Postman коллекции были проанализированы запросы интернет-магазина https://altaivita.ru/ с помощью метода POST и по всем тест-кейсам статус 200, даже в случае негативных.
