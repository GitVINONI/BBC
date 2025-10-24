import random

def map_generation(n, m):
    desk = []
    # Типы комнат, ключ должен встречаться только 1 раз и портал должен быть только 1
    rooms = ["пусто", "сундук", "монстр", "ловушка", "ключ", "портал"]

    n, m = n, m

    # Генерация карты
    for y in range(n):
        adder = [0] * m
        for x in range(m):
            if x == 0 and y == 0:
                adder[0] = "старт"
                continue
            room = rooms[random.randint(0, 3)]
            adder[x] = room
        desk.append(adder)
    
    # Добавление ключа и портала
    if m >= n:
        x_key = random.randint(0, m - 1)
        x_portal = random.randint(0, m - 1)
        y_key = random.randint(1, n - 1)
        y_portal = random.randint(1, n - 1)
    else:
        x_key = random.randint(1, m - 1)
        x_portal = random.randint(1, m - 1)
        y_key = random.randint(0, n - 1)
        y_portal = random.randint(0, n - 1)
        
    
    if x_key == x_portal and y_key == y_portal:
        y_portal = 0
        x_portal = 1

    desk[y_key][x_key] = "ключ"
    desk[y_portal][x_portal] = "портал"

    return desk

# Ввод размеров карты
n, m = map(int, input("Введи размеры карты: ").split(" "))

desk = map_generation(n, m)
print(desk)