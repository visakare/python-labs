# Створіть словник в якому зберігаються ім'я користувача (login), зашифрований пароль та повне ПІБ користувача.
# Для хешування пароля використовуйте функцію hashlib.md5().
# Зробіть функцію перевірки введеного паролю користувача; пароль користувач вводить з консолі, зчитування за допомогою методу input().

import hashlib

# Перевірка введеного паролю користувача
def verify_password(login, entered_password, users_data):
    if login in users_data:
        stored_hashed_password = users_data[login]['hashed_password']
        hashed_entered_password = hashlib.md5(entered_password.encode()).hexdigest()
        return hashed_entered_password == stored_hashed_password


# Словник користувачів
users = {
    'pavlo_mel': {
        'hashed_password': hashlib.md5('esTF76$!y'.encode()).hexdigest(),
        'full_name': 'Melnyk Pavlo Yakovych'
    },
    'rom_vov': {
        'hashed_password': hashlib.md5('QU^N85@ei_*'.encode()).hexdigest(),
        'full_name': 'Vovk Roman Antonovych'
    }
}
# print(users)

if __name__ == '__main__':
    login_input = input("Enter your login: ")
    password_input = input("Enter your password: ")

    if verify_password(login_input, password_input, users):
        print("Password is correct.")
        print(f"Welcome, {users[login_input]['full_name']}!")
    else:
        print("Incorrect login or password.")