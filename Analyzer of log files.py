# Напишіть функцію analyze_log_file(log_file_path), яка приймає шлях до файлу журналу http-сервера (текстового файлу). Функція повинна:
# 1. Прочитати кожний рядок файлу. Типовий лог-файл “apache_logs.txt” додається
# 2. Визначити кількість входжень унікальний кодів відповідей http-сервера (наприклад, 200, 404, 500 і т.д.).
# 3. Зберегти результати у словнику, де ключем є код відповіді, а значенням - кількість його входжень.
# 4. Обробити можливі винятки, такі як відсутність файлу (FileNotFoundError) або помилки читання файлу (IOError), виводячи інформативне повідомлення про помилку.
# 5. Повернути отриманий словник з результатами аналізу.

# Функція analyze_log_file приймає шлях до лог-файлу HTTP-сервера
def analyze_log_file(log_file_path):
    # Порожній словник для збереження кількості входжень кодів відповіді
    response_codes = {}
    try:
        # Відкриття файлу у режимі читання
        with open(log_file_path, 'r') as file:
            for line in file:
                # print(line)
                # Розбиття рядка на частини за пробілами
                parts = line.split()
                # Перевірка, чи у рядку достатньо елементів (щоб уникнути IndexError)
                if len(parts) > 8:
                    # Код відповіді зазвичай знаходиться на 9-й позиції (індекс 8)
                    status_code = parts[8]
                    # Перевірка, чи це число (наприклад, 200, 404)
                    if status_code.isdigit():
                        # Збільшення лічильнику цього коду у словнику
                        response_codes[status_code] = response_codes.get(status_code, 0) + 1
    # Обробка помилки, якщо файл не знайдено
    except FileNotFoundError:
        print(f"Error: file '{log_file_path}' not found.")
    # Обробка загальних помилок при читанні файлу
    except IOError:
        print(f"Error while reading file '{log_file_path}'.")
    # Повернення словника з результатами аналізу
    return response_codes

# Функція з назвою лог-файлу та збереження результату
results = analyze_log_file("apache_logs.txt")
print(results)








