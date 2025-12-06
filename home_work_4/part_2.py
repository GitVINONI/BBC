import pandas as pd
import numpy as np

# Открытие датасета
file = pd.read_csv("home_work_4/tested.csv")

age = file["Age"].values
survived = file["Survived"].values
sex = file["Sex"].values

is_male = sex == "male"
is_female = sex == "female"

# Процент выживших
male_sr = np.mean(survived[is_male])
female_sr = np.mean(survived[is_female])
print(male_sr, female_sr)

# Для среднего возраста заполним пропуски медианой 
file.fillna({"Age":file["Age"].median()}, inplace=True)

# Средний возраст М и Ж
male_age = np.mean(age[is_male])
female_age = np.mean(age[is_female])
print(male_age, female_age)

# Средний возраст В и П
is_alive = survived == 1
is_die = survived == 0

female_alive_age = np.mean(age[is_female & is_alive])
# female_die_age = np.mean(age[is_female & is_die]) # Все женщины выжили
print(female_alive_age)

# male_alive_age = np.mean(age[is_male & is_alive]) # Все мужчины мертвы
male_die_age = np.mean(age[is_male & is_die])
print(male_die_age)



pclass = file["Pclass"].values

# Группа 1
group_a = (age > 30) & (sex == "male") & (pclass == 1)
people_group_a = file[group_a]
print(people_group_a)

# Группа 2
group_b = ((age < 18) | (sex == "female")) & (survived == 1)
people_group_b = file[group_b]
print(people_group_b)


# Группировка по классу билета и стоимости
group = file.groupby(["Pclass", "Sex"])
print(group.agg({"Age":"mean", "Survived":"mean", "Fare": "mean"}))