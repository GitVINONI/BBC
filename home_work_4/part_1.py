import pandas as pd
import numpy as np

# Открытие датасета
file = pd.read_csv("home_work_4/tested.csv")

# Сумма пропущенных значений
print(file.isnull().sum())

# Типы данных
print(file.dtypes)

# Вывод первых n строк
n = int(input("Сколько вывести строк: "))
print(file.head(n))

# Вывести базовую статистику по стоимости
print(file["Fare"].describe())

# Количество заголовков и строк в общем
print(f"Колличество строк: {file.shape[0]}\nКолличество столбцов: {file.shape[1]}")



# Работа с возрастом (Создание нового датасета где все возраста будут заполнены)
file.fillna({"Age":file["Age"].median()}, inplace=True)
file.to_csv("home_work_4/new_1.csv", index=False)

new_file = pd.read_csv("home_work_4/new_1.csv")
print(new_file["Age"].isnull().sum())


# Удаление 20 строк с пропусками (Создание нового датасета)
print(file.isnull().sum())
rows = file[file.isnull().any(axis=1)].head(20)
file.drop(rows.index, inplace=True)
file.to_csv("home_work_4/new_2.csv", index=False)
new_file = pd.read_csv("home_work_4/new_2.csv")
print(new_file.isnull().sum())