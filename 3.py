"""
Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести его на экран.
"""

with open('subjects.txt', 'r') as file:
    subjects = {}

    for line in file:
        parts = line.split(':')
        subject = parts[0]
        lessons = parts[1].split()

        all_lessons = 0

        for lesson in lessons:
            count, lesson_type = lesson[:-1].split('(')
            count = int(count)

            all_lessons += count

        subjects[subject] = all_lessons

print("Словарь, содержащий название предмета и общее количество занятий по нему:")
print(subjects)
