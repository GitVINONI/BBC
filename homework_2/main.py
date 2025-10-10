# Первый уровень
def level_1():
    stroka = str(input("Введи строку: "))
    method = str(input("Введи метод(up, low, cap): "))

    if method == "up":
        print(stroka.upper())
    elif method == "low": 
        print(stroka.lower())
    elif method == "cap":
        print(stroka.capitalize())
    else: print("ERROR")
    
    return 0

# Второй уровень
def level_2():
    stroka = str(input("Введи строку: "))
    method = str(input("Введи метод(find, replace, count): "))

    if method == "find":
        fi = str(input("Что вы хотите найти: "))
        print(stroka.find(fi))
    elif method == "replace": 
        chto = str(input("Что вы хотите поменять: "))
        na_chto = str(input("На что вы хотите поменять: "))
        num = int(input("Сколько раз вы хотите это поменять (-1 если хотите заменить все): "))
        print(stroka.replace(chto, na_chto, num))
    elif method == "count":
        chto = str(input("Что вы хотите посчитать: "))
        print(f"Колличество: {stroka.count(chto)} \nЭлемент: {chto}")
    else: print("ERROR")
    
    return 0

# Третий уровень
def level_3():
    stroka = str(input("Введи строку: "))

    a = list(stroka.split(","))
    print(f"Разбиение по запятой: {a}")

    b = str(" ".join(a))
    print(f"Соединение с пробелом: {b}")
    return 0

# Четвертый уровень
def level_4():
    stroka = str(input("Введи строку: "))

    if stroka.isdigit():
        print("Ты ввел только цифры")
    elif stroka.isalpha():
        print("Ты ввел только буквы")
    else: 
        print("Ты ввел ничем не примечательную строку")
    return 0

# Пятый уровень
def level_5():
    # stroka = str(input("Введи строку: "))
    stroka = "    pYThON;IS;AwesoME"
    stroka = stroka.strip()
    a = list(stroka.split(";"))
    a[0] = a[0].capitalize()
    a[1] = a[1].lower()
    a[2] = a[2].lower()
    stroka = " ".join(a)
    print(stroka)
    return 0    

# выбор уровня
level = int(input("Выбери уровень: "))

if level == 1:
    level_1()
elif level == 2:
    level_2()
elif level == 3:
    level_3()
elif level == 4:
    level_4()
elif level == 5:
    level_5()