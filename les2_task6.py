'''

6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:

[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ
— характеристика товара, например название, а значение — список значений-характеристик,
например список названий товаров.

Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}

'''
some_list = []
number_of_product = 0
some_dict = {}

while True:
    product = input('Enter name of product:\n>>>')
    price = input('Enter price of product:\n>>>')

    if price.isdigit():
        price = int(price)
    else:
        print('You shoud enter an integer')

    quantity = input('Enter quantity of product:\n>>>')
    if quantity.isdigit():
        quantity = int(quantity)
    else:
        print('You shoud enter an integer')

    unit = input('Enter unit of product:\n>>>')

    some_dict.update({'product': product, 'price': price, 'quantity': quantity, 'unit': unit})
    number_of_product += 1
    some_list.append((number_of_product, some_dict.copy()))

    next_product = input('Do you wnat enter the next one product? enter Y or N\n>>>')
    next_product = next_product.lower()

    if next_product == 'y':
        continue
    elif next_product == 'n':
        break
    else:
        print('You shoud make a choice.')

if len(some_list):
    product = []
    price = []
    quantity = []
    unit = set()
    for el in some_list:
        product.append(el[1].get('product'))
        price.append(el[1].get('price'))
        quantity.append(el[1].get('quantity'))
        unit.add(el[1].get('unit'))
    statistic = {
        'product': product,
        'price': price,
        'quantity': quantity,
        'unit': unit
    }
else:
    print('You didn\'t enter any product.')

print(f'Let see the statistic of products that you have entered before:\n{statistic}')

