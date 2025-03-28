# Створіть словник, де ключі - це назви продуктів, а значення - їх кількість на складі.
# Напишіть функцію, яка приймає назву продукту та кількість, і оновлює словник відповідно до додавання або видалення продуктів.
# Додатково: створіть список продуктів, в яких кількість менше ніж 5.

# Приймає назву продукту та кількість, і оновлює словник відповідно до додавання або видалення продуктів.
def update_inventory(product, quantity):
    if product in inventory:
         inventory[product] += quantity
         if inventory[product] < 0:
             inventory[product] = 0
    else:
        inventory[product] = quantity

# Словник продуктів
inventory = {'Oranges': 50, 'Grapefruit': 2, 'Kiwi': 100, 'Pomelo': 4}
print("Initial Dictionary", inventory)
# Використання функції для оновлення запасів
update_inventory('Lemon', 12)
print("Updated Dictionary:", inventory)
# Видалення продукту (встановлення кількості на 0)
update_inventory('Kiwi', -100)
print("Updated Dictionary:", inventory)

#  Список продуктів, в яких кількість менше ніж 5
list_low_quantity = []
for product, quantity in inventory.items():
    print("key:", product)
    print("value", quantity)
    if quantity < 5:
        list_low_quantity.append(product)
print("Products with low_quantity < 5:", list_low_quantity)