Вариант 1 - «Полезные продукты»

Задание №1. Вывести все уникальные названия продуктов
SELECT DISTINCT product_name
FROM Products;

Задание №2. Вывести идентификатор, название и стоимость продуктов с содержанием клетчатки (fiber) более 5 граммов
SELECT p.product_id, p.product_name, p.price
FROM Products p
JOIN Nutritional_Information n ON p.product_id = n.product_id
WHERE n.fiber > 5;

Задание №3. Вывести название продукта с самым высоким содержанием белка (protein)
SELECT p.product_name
FROM Products p
JOIN Nutritional_Information n ON p.product_id = n.product_id
WHERE n.protein = (SELECT MAX(protein) FROM Nutritional_Information);

Задание №4. Подсчитать общую сумму калорий для продуктов каждой категории, но не учитывать продукты с нулевым содержанием жира (fat = 0). Вывести идентификатор категории, сумму калорий
SELECT c.category_id, SUM(p.calories) AS total_calories
FROM Products p
JOIN Categories c ON p.category_id = c.category_id
WHERE p.fat > 0
GROUP BY c.category_id;

Задание №5. Рассчитать среднюю цену товаров каждой категории. Вывести название категории, среднюю цену
SELECT c.category_name, AVG(p.price) AS average_price
FROM Products p
JOIN Categories c ON p.category_id = c.category_id
GROUP BY c.category_name;

