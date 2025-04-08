# Напишіть функцію, яка приймає рядок як вхідні дані та повертає словник, де ключі - це унікальні слова в рядку, а значення - кількість їх появ.
# Створіть та виведіть на екран список, де зберігаються слова, що зустрічаються більше 3 разів.


# Напишіть функцію, яка приймає рядок як вхідні дані та повертає словник, де ключі - це унікальні слова в рядку, а значення - кількість їх появ.
def count_words(text):
    words = text.split() # Перетворюємо рядок на список слів, розділяючи його за пробілами
    word_count = {}
    for word in words:
        word = word.lower() # Перетворюємо слово в нижній регістр для коректного порівняння
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

text = "Apricot Cherry Coconut Lime Cherry Lime Plum cherry lime apricot Cherry Coconut Lime"
word_count = count_words(text)

print(text)
print("\nWord count dictionary:", word_count)

# Cписок слів, які зустрічаються більше 3 разів
list_frequent_words =[]
for word in word_count:
    print("key:", word)
    print("value", word_count[word])
    if word_count[word] > 3:
        list_frequent_words.append(word)

print("\nList of words occurring more than 3 times:", list_frequent_words)

