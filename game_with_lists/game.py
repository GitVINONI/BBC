import random

class Player:
    # Класс игрока
    def __init__(self, heart, max_len_inventory, desk, player_desk):
        # инциализация игрока (сердечки, инвентарь, длина и инвенторя и координаты)
        self.heart = heart
        self.inventory = []
        self.mli = max_len_inventory
        self.x = 0
        self.y = 0
        self.desk = desk
        self.p_d = player_desk
        self.p_d[0][0] = "P"

    
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
            return "0"
        else:
            item = self.inventory[num_of_item - 1]
            self.inventory.pop(num_of_item - 1)
            return item

    def use_item(self, use):
        # Функция возвращает предмет из ячейки инвентаря
        if (use - 1) >= len(self.inventory):
            return 0
        return self.inventory[use - 1]

    def show_map_player(self):
        # отрисовка карты, которую видит игрок, без указания комнат
        for y in range(len(self.p_d)):
            for x in range(len(self.p_d[y])):
                print(f"{self.p_d[y][x]}", end=" ")
            print()
    
    def go(self, napr):
        # Перемещение игрока на 1 в указанном направлении
        if napr == "u":
            if self.y - 1 >= 0:
                if(self.desk[self.y][self.x] == "старт"): self.p_d[self.y][self.x] = "S"
                elif(self.desk[self.y][self.x] == "пусто"): self.p_d[self.y][self.x] = "E"
                elif(self.desk[self.y][self.x] == "сундук"): self.p_d[self.y][self.x] = "C"
                elif(self.desk[self.y][self.x] == "ключ"): self.p_d[self.y][self.x] = "K"
                elif(self.desk[self.y][self.x] == "ловушка"): self.p_d[self.y][self.x] = "T"
                elif(self.desk[self.y][self.x] == "портал"): self.p_d[self.y][self.x] = "O"
                elif(self.desk[self.y][self.x] == "монстр"): self.p_d[self.y][self.x] = "M"
                self.y -= 1
                self.p_d[self.y][self.x] = "P"
            else:
                print("Никакого out of bounds!")
        elif napr == "l":
            if self.x - 1 >= 0:
                if(self.desk[self.y][self.x] == "старт"): self.p_d[self.y][self.x] = "S"
                elif(self.desk[self.y][self.x] == "пусто"): self.p_d[self.y][self.x] = "E"
                elif(self.desk[self.y][self.x] == "сундук"): self.p_d[self.y][self.x] = "C"
                elif(self.desk[self.y][self.x] == "ключ"): self.p_d[self.y][self.x] = "K"
                elif(self.desk[self.y][self.x] == "ловушка"): self.p_d[self.y][self.x] = "T"
                elif(self.desk[self.y][self.x] == "портал"): self.p_d[self.y][self.x] = "O"
                elif(self.desk[self.y][self.x] == "монстр"): self.p_d[self.y][self.x] = "M"
                self.x -= 1
                self.p_d[self.y][self.x] = "P"
            else:
                print("Никакого out of bounds!")
        elif napr == "d":
            if self.y + 1 < n:
                if(self.desk[self.y][self.x] == "старт"): self.p_d[self.y][self.x] = "S"
                elif(self.desk[self.y][self.x] == "пусто"): self.p_d[self.y][self.x] = "E"
                elif(self.desk[self.y][self.x] == "сундук"): self.p_d[self.y][self.x] = "C"
                elif(self.desk[self.y][self.x] == "ключ"): self.p_d[self.y][self.x] = "K"
                elif(self.desk[self.y][self.x] == "ловушка"): self.p_d[self.y][self.x] = "T"
                elif(self.desk[self.y][self.x] == "портал"): self.p_d[self.y][self.x] = "O"
                elif(self.desk[self.y][self.x] == "монстр"): self.p_d[self.y][self.x] = "M"
                self.y += 1
                self.p_d[self.y][self.x] = "P"
            else:
                print("Никакого out of bounds!")

        elif napr == "r":
            if self.x + 1 < m:
                if(self.desk[self.y][self.x] == "старт"): self.p_d[self.y][self.x] = "S"
                elif(self.desk[self.y][self.x] == "пусто"): self.p_d[self.y][self.x] = "E"
                elif(self.desk[self.y][self.x] == "сундук"): self.p_d[self.y][self.x] = "C"
                elif(self.desk[self.y][self.x] == "ключ"): self.p_d[self.y][self.x] = "K"
                elif(self.desk[self.y][self.x] == "ловушка"): self.p_d[self.y][self.x] = "T"
                elif(self.desk[self.y][self.x] == "портал"): self.p_d[self.y][self.x] = "O"
                elif(self.desk[self.y][self.x] == "монстр"): self.p_d[self.y][self.x] = "M"
                self.x += 1
                self.p_d[self.y][self.x] = "P"
            else:
                print("Никакого out of bounds!")
        else:
            print("Такого направления не существует.")
    

def chest():
        loot = ["Хил", "Молоток", "Меч", "Чебурек"]
        item = loot[random.randint(0, 3)]
        print(f"Ты нашел сундук и из него выпал {item}, если ты его не подберешь, то он исчезнет!")
        return item


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
    player_desk = [["*"] * m for i in range(n)]

    return desk, player_desk

# Ввод размеров карты и ее генерация
n, m = map(int, input("Введи размеры карты: ").split(" "))
desk = map_generation(n, m)[0]
player_desk = map_generation(n, m)[1]

# Инициализация игрока
health = int(input("Введите количество своих жизней: "))
inventory = int(input("Введите размер инвентаря: "))
player = Player(health, inventory, desk, player_desk)

print("""

Добро пожаловать!
      
Ты попал в жадное подземелье!
      
Как только ты выйдешь из комнаты все предметы в ней исчезнут! (Кроме комнаты с ключом, он наоборот появляется каждый раз когдв ты заходишь в комнату)
      
В подземелье ты можешь найти 4 предмета:
      Молоток - ты можешь попробовать отбиться ей от монстра, но вряд ли уйдешь целым
      Меч - он поможет тебе мгновенно одолеть 1 чудовище
      Хил - если ты его выпьешь, то восстановишь 10 хп
      Чебурек - если ты его съешь, то восстановишь 20 хп 

Будь осторожен, удачи!
      
Обозначения пройденых комнат:
      S - старт
      E - пусто
      C - сундук
      K - ключ от портала
      T - ловушка
      O - портал (открывается только с ключом)
      M - комната монстра

Двигаться:
      u - вверх 
      d - вниз
      r - вправо
      l - влево

Выкинуть предмет: drop номер ячейки из которой выкинуть предмет
      Например "drop 1" без кавычек, эта команда выкинет 1 предмет из инвентаря.

Подобрать предмет: take
      
Использовать предмет: use номер ячейки, предмет из которой нужно использовать.
      Аналогично drop
      
""")
item = ""
item_in_room = 0
was_in = []
flag_win = 0
while (player.heart > 0):
    if item_in_room: print(f"В комнате лежит {item}")
    player.show_map_player()
    print(f"HP: {player.heart}")
    player.show_inventory()
    command = input("Действие: ")
    print()
    if command in "lrud":
        player.go(command)
        item_in_room = 0
        if player.desk[player.y][player.x] == "пусто":
            print("Ты вошел в пустую комнату")
        if player.desk[player.y][player.x] == "ловушка":
            print("Ты наткнулся на ловушку и получил 3 урона")
            player.heart -= 3
        if player.desk[player.y][player.x] == "сундук":
            if (player.x, player.y) not in was_in:
                item = chest()
                item_in_room = 1
                was_in.append((player.x, player.y))
            else:
                print("Ты видишь пустой сундук")
        if player.desk[player.y][player.x] == "ключ":
            print("Ты видишь перед собой тот самый долгожданый ключ")
            item = "Ключ"
            item_in_room = 1
        
        if player.desk[player.y][player.x] == "портал":
            print("Ты видишь перед собой портал.")
            if "Ключ" in player.inventory:
                print("Ключ сам по себе влетает в портал и ты оказываешься на свободе!")
                flag_win = 1
                break
            else:
                print("Приходи, когда найдешь ключ.")
        
        

        if player.desk[player.y][player.x] == "монстр":
            if (player.x, player.y) not in was_in:
                print("Ты наткнулся на страшного монстра")
                print("Используй что нибудь!")
                use = int(input("Укажи номер ячейки, которой хочешь воспользоваться: "))
                do = player.use_item(use)
                if do == 0:
                    print("К сожалению ты ничем не воспользовался.")
                    if player.heart - 10 < 0:
                        print("Ты пал в бою с монстром")
                        player.heart = 0
                        break
                    else:
                        print("После пары ударов по тебе монстр устал и погиб от истощения.")
                        print("Ты получил 10 урона")
                        player.heart -= 10
                if do == "Молоток":
                    if player.heart - 5 < 0:
                        print("Молоток не смог тебя защитить")
                        player.heart = 0
                        break
                    print("Ты попытался отбиться от монстра палкой и что-то даже получилось, но получилось скверно.")
                    print("Молоток сломана")
                    print("Ты получил 5 урона")
                    player.drop_item(use)
                    player.heart -= 5
                if do == "Меч":
                    print("Ты смог одолеть монстра.")
                    print("Меч сломан")
                    player.drop_item(use)
                
                if do == "Хил" or do == "Чебурек":
                    print("Ты не успел восстанновиться и потерял восстанавливающий предмет, когда напал монстр.")
                    if player.heart - 10 < 0:
                        print("Ты пал в бою с монстром")
                        player.heart = 0
                        break
                    else:
                        print("После пары ударов по тебе монстр устал и погиб от истощения.")
                        print("Ты получил 10 урона")
                        player.heart -= 10
                    player.drop_item(use)
                
                if do == "Ключ":
                    print("Ключ тебе ничем не поможет")
                    if player.heart - 10 < 0:
                        print("Ты пал в бою с монстром")
                        player.heart = 0
                        break
                    else:
                        print("После пары ударов по тебе монстр устал и погиб от истощения.")
                        print("Ты получил 10 урона")
                        player.heart -= 10
                
                was_in.append((player.x, player.y))
            else:
                print("Монстр в этой пещере уже повержен")
    elif "drop" in command:
        suckses = player.drop_item(int(command.split(" ")[1]))
        if suckses != "0":
            item_in_room = 1
            item = suckses
    elif command == "take":
        if item_in_room:
            if item == "": print("Здесь ничего нет")
            else: player.get_item(item)
            item_in_room = 0
        else: print("Комната пуста")
    elif "use" in command:
        using = int(command.split(" ")[1])
        if using - 1 >= len(player.inventory):
            print("В этой ячейке ничего нет")
        elif player.inventory[using - 1] == "Чебурек":
            print("Ты восстановил 10 хп")
            player.heart += 10
            player.drop_item(using)
        elif player.inventory[using - 1] == "Хил":
            print("Ты восстановил 5 хп")
            player.heart += 5
            player.drop_item(using)
        else:
            print("Ты ничего не можешь сделать со своим оружием сейчас")
    else:
        print("Неизвестная команда")
if flag_win == 1:
    print("ПОБЕДА!!!!!")
else:
    print("ПОРАЖЕНИЕ!")