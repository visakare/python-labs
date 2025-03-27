# Створіть список словників, де кожен словник представляє продаж з ключами: "продукт", "кількість", "ціна".
# Напишіть функцію, яка обчислює загальний дохід для кожного продукту та повертає словник, де ключі - це назви продуктів, а значення - загальний дохід.
# Створіть список продуктів, що принесли дохід більший ніж 1000.


# Обчислення загального доходу для кожного продукту та повернення словника, де наявні продукти та їхній загальний дохід
def calculate_total_revenue(sales):
    total_revenue = {}
    for sale in sales:
        product = sale['product']
        quantity = sale['quantity']
        price = sale['price']
        revenue = quantity * price
        if product in total_revenue:
            total_revenue[product] += revenue
        else:
            total_revenue[product] = revenue
    return total_revenue


# Список словників, що представляють продажі
sales = [
    {'product': 'Oranges', 'quantity': 20, 'price': 54},
    {'product': 'Grapefruit', 'quantity': 5, 'price': 80},
    {'product': 'Kiwi', 'quantity': 102, 'price': 128},
    {'product': 'Oranges', 'quantity': 4, 'price': 54},
    {'product': 'Pomelo', 'quantity': 2, 'price': 70},
    {'product': 'Grapefruit', 'quantity': 3, 'price': 80},
]
print(sales)

total_revenue = calculate_total_revenue(sales)
print("Total revenue:", total_revenue)

#  Список продуктів, що принесли дохід більший ніж 1000.
list_for_products = []
for product in total_revenue:
    print("key:", product)
    print("value", total_revenue[product])
    if total_revenue[product] > 1000:
        list_for_products.append(product)


print("Products with revenue > 1000:", list_for_products)