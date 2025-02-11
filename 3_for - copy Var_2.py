"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
sold_phone = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


sum_all_sold_phones = 0


for one_phone in sold_phone:
    sum_sold_phone = sum(one_phone['items_sold'])
    avg_sold_every_phone = round(sum_sold_phone / len(one_phone['items_sold']), 1)
    print(f'Сумарное количество продаж {one_phone["product"]}: {sum_sold_phone}')
    print(f'Среднее количество продаж {one_phone["product"]}: {avg_sold_every_phone}')
    sum_all_sold_phones += sum_sold_phone


avg_sum_all_sold_phones = round(sum_all_sold_phones / len(sold_phone), 1)


print(f'Суммарное количество продаж всех товаров: {sum_all_sold_phones}')
print(f'Среднее количество продаж всех товаров: {avg_sum_all_sold_phones}')