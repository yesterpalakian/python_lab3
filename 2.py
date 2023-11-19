"""
Создать текстовый файл (не программно).
Построчно записать названия цветов и их стоимость (не менее 10 строк).
Вывести на экран все цветы, стоимость которых меньше 5 рублей,
от 5 до 10 рублей и выше 10 рублей.
Вывести на экран названия цветов, с минимальной стоимостью.
"""

with open('flowers.txt', 'r') as file:
    less_than_5 = []
    from_5_to_10 = []
    more_than_10 = []
    all_flowers = []

    for line in file:
        flower, cost = line.split()
        cost = float(cost)

        all_flowers.append((flower, cost))
        if cost < 5:
            less_than_5.append((flower, cost))
        elif 5 <= cost <= 10:
            from_5_to_10.append((flower, cost))
        else:
            more_than_10.append((flower, cost))

print("Цветы, стоимость которых меньше 5 рублей:")
for flower, cost in less_than_5:
    print(f"{flower}: {cost} рублей")

print("\nЦветы, стоимость которых от 5 до 10 рублей:")
for flower, cost in from_5_to_10:
    print(f"{flower}: {cost} рублей")

print("\nЦветы с стоимостью выше 10 рублей:")
for flower, cost in more_than_10:
    print(f"{flower}: {cost} рублей")

min_cost = min(all_flowers, key=lambda x: x[1])
print(f"\nЦветы с минимальной стоимостью: {min_cost[0]}")
