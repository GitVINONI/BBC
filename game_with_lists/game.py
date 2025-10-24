import random

class Player:
    # Класс игрока
    def __init__(self, heart, max_len_inventory):
        # инциализация игрока (сердечки, инвентарь, длина и нвенторя и координаты)
        self.heart = heart
        self.inventory = []
        self.mli = max_len_inventory
        self.x = 0
        self.y = 0
    
    def show_inventory(self):
        # Отрисовка иннвентаря с учетом его длины
        out = self.inventory + ["пусто"] * (self.mli - len(self.inventory))
        print(out)

    def get_item(self, item):
        # Подбор предмета/ добавление предмета в инвентарь
        if len(self.inventory) < self.mli:
            self.inventory.append(item)
        else:
            print("Инвентарь переполнен!")

    def drop_item(self, num_of_item):
        # Функция для того чтобы выкинуть предмет из инвентаря по номеру ячейки (начиная с единицы)
        if len(self.inventory) < num_of_item:
            print("У тебя в этом слоте и так ничего нет")
        else:
            self.inventory.pop(num_of_item - 1)

    def show_map_player(self, n, m):
        # отрисовка карты, которую видит игрок, без указания комнат
        for y in range(n):
            for x in range(m):
                if x == self.x and y == self.y:
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            print()
    
    def go(self, napr):
        # Перемещение игрока на 1 в указанном направлении
        if napr == "up":
            if self.y - 1 > 0:
                self.y -= 1
            else:
                print("Никакого out of bounds!")
        elif napr == "left":
            if self.x - 1 > 0:
                self.x -= 1
            else:
                print("Никакого out of bounds!")
        elif napr == "down":
            if self.y + 1 < n:
                self.y += 1
            else:
                print("Никакого out of bounds!")
        elif napr == "right":
            if self.x + 1 < m:
                self.x += 1
            else:
                print("Никакого out of bounds!")
        else:
            print("такого направления не существует")


def map_generation(n, m):
    # Генерация карты

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


# Ввод размеров карты и ее генерация
n, m = map(int, input("Введи размеры карты: ").split(" "))
# desk = map_generation(n, m)

# Инициализация игрока

player = Player(10, 5)

# player.show_inventory()
# player.get_item("Палка")
# player.show_inventory()
# player.get_item("Меч")
# player.get_item("Кинжал")
# player.get_item("Посох")
# player.get_item("голова дракона")
# player.get_item("Ключ")
# player.show_inventory()
# player.drop_item(5)
# player.drop_item(1)
# player.drop_item(2)
# player.get_item("Ключ")
# player.show_inventory()

# player.show_map_player(n, m)
# player.go("up")
# player.go("left")
# player.go("down")
# player.go("down")
# player.go("down")
# player.go("right")
# player.go("right")
# player.go("right")
# player.show_map_player(n, m)