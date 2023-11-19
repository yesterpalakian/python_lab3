"""
Создать программный файл F1 в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
Скопировать в файл F2 только те строки из F1, которые начинаются с буквы «А».
Подсчитать количество слов в F2.
"""

with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку: ")
        if not line:
            break
        f1.write(line + '\n')

with open('F1.txt', 'r') as f1:
    with open('F2.txt', 'w') as f2:
        for line in f1:
            if line.startswith('А'):
                f2.write(line)

with open('F2.txt', 'r') as f2:
    content = f2.read()
    word_count = len(content.split())

print(f"Количество слов в F2: {word_count}")

