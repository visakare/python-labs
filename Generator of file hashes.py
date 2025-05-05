# Створіть функцію generate_file_hashes(file_paths), яка приймає список шляхів до файлів. Для кожного файлу у списку функція повинна:
# 1. Відкрити файл у бінарному режимі для читання.
# 2. Обчислити хеш SHA-256 вмісту файлу.
# 3. Зберегти результати у словнику, де ключем є шлях до файлу, а значенням - його SHA-256 хеш (у шістнадцятковому форматі).
# 4. Обробити можливі винятки, такі як відсутність файлу (FileNotFoundError) або помилки читання файлу (IOError), виводячи відповідне повідомлення.
# 5. Повернути словник з хешами файлів.
# Для обчислення хешів скористайтеся бібліотекою hashlib.

import hashlib
# Функція для обчислення SHA-256 хешів для списку файлів
def generate_file_hashes(file_paths):
    # Ініціалізація словника для збереження хешів
    hashes_dict = {}
    for path in file_paths:
        try:
            # Відкриття файлу у бінарному режимі читання
            with open(path, 'rb') as file:
                # Зчитування вмісту файлу
                file_content = file.read()
                # Обчислення SHA-256 хеш вмісту
                sha256_hash = hashlib.sha256(file_content)
                # Отримання хешу у шістнадцятковому форматі
                hash_hex = sha256_hash.hexdigest()
                # Збереження результату у словнику
                hashes_dict[path] = hash_hex
        # Обробка помилки, якщо файл не знайдено
        except FileNotFoundError:
            print(f"Error: file '{path}' not found.")
        # Обробка загальних помилок при читанні файлу
        except IOError:
            print(f"Error while reading file '{path}'.")
    # Повернення словника з результатами
    return hashes_dict

# Функція для обчислення хешу файлу "apache_logs.txt"
results = generate_file_hashes(["apache_logs.txt"])
print(results)


