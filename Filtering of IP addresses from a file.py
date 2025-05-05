# Напишіть функцію filter_ips(input_file_path, output_file_path, allowed_ips), яка аналізує IP-адреси з лог-файла http-сервера:
# 1. Читає IP-адреси з кожного рядка файлу input_file_path.
# 2. Перевіряє, чи кожна прочитана IP-адреса присутня у списку дозволених IP-адрес allowed_ips. Попередньо необхідно задати список (масив) дозволених IP-адрес allowed_ips.
# 3. Рахує скільки разів зустрічаються дозволені адреси у лог файлі.
# 4. Записує результат аналізу лог-файлу до файлу output_file_path, у вигляді <IP адерса> - <кількість входженнь>.
# 5. Обробити можливі винятки, такі як відсутність вхідного файлу (FileNotFoundError) або помилки запису до вихідного файлу (IOError), виводячи інформативні повідомлення.

# Функція filter_ips аналізує лог-файл з IP-адресами та зберігає лише дозволені IP-адреси з підрахунком входжень
def filter_ips(input_file_path, output_file_path, allowed_ips):
    # Словник для підрахунку входжень IP-адрес
    ip_counts = {}
    try:
        # Читання лог-файлу
        with open(input_file_path, 'r') as infile:
            # Читання кожного рядка у файлі
            for line in infile:
                # Розбиття рядка на частини (IP — перший елемент)
                split_result = line.split()
                # Отримання IP-адреси
                ipaddress = split_result[0]
                # Перевірка, чи IP-адреса знаходиться у списку дозволених
                if ipaddress in allowed_ips:
                    if ipaddress in ip_counts:
                        ip_counts[ipaddress] += 1
                    else:
                        ip_counts[ipaddress] = 1
        print(ip_counts)
        # Запис результатів у вихідний файл
        with open(output_file_path, 'w') as outfile:
            for ip, count in ip_counts.items():
                # Форматований запис: <IP> - <кількість входжень>
                outfile.write(f"{ip} - {count}\n")
    # Обробка помилки, якщо файл не знайдено
    except FileNotFoundError:
        print(f"Error: file '{input_file_path}' not found.")
    # Обробка помилки, якщо виникла проблема із записом у файл
    except IOError:
        print(f"Error: failed to write file '{output_file_path}'.")

allowed_ips = ["212.33.34.196", "59.90.241.113", "94.79.44.40"]
filter_ips("apache_logs.txt", "filtered_ips.txt", allowed_ips)