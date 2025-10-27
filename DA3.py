import pandas as pd
import numpy as np

# 1. Создаем DataFrame с данными
data = {
    'Имя': ['Вася', 'Петя', 'Боря', 'Саша', 'Маша', 'Даша', 'Витя', 'Катя', 'Света', 'Федя'],
    'Геометрия': [5, 4, 3, 5, 4, 3, 5, 4, 5, 3],
    'Алгебра': [4, 3, 5, 4, 3, 4, 5, 3, 4, 5],
    'Физика': [3, 5, 4, 3, 5, 4, 3, 5, 4, 3],
    'Химия': [5, 4, 5, 4, 5, 3, 2, 5, 4, 5],
    'История': [4, 3, 4, 5, 4, 5, 3, 4, 5, 4]
}

df = pd.DataFrame(data)  # читаем ДФ в ~ df
print("1. DataFrame создан:")

# 2. Выводим первые строки ДФ
print("\n2. Первые 5 строк DataFrame:")
print(df.head())

# 3. Вычисляем среднюю оценку по каждому предмету
print("\n3. Средние оценки по предметам:")
mean_grades = df.mean(numeric_only=True)
print(mean_grades)

# 4. Вычисляем медианную оценку по каждому предмету
print("\n4. Медианные оценки по предметам:")
median_grades = df.median(numeric_only=True)
print(median_grades)

# 5. Вычисляем Q1 и Q3 для оценок по алгебре
Q1_alg = df['Алгебра'].quantile(0.25)
Q3_alg = df['Алгебра'].quantile(0.75)
print(f"\n5. Для алгебры:")
print(f"Q1 (25-%-ль): {Q1_alg}")
print(f"Q3 (75-%-ль): {Q3_alg}")

# 6. Рассчитываем IQR (Interquartile Range)
IQR_alg = Q3_alg - Q1_alg
print(f"Межквартильный интервал МКИ/IQR для алгебры: {IQR_alg}")

# 7. Вычисляем стандартное отклонение std/СКО
print("\n7. Стандартное отклонение - СКО - по предметам:")
std_grades = df.std(numeric_only=True)
print(std_grades)

# Доп: выводим осн статистику
print("\nБонус)): Осн статистические пок-ли по всем предметам:")
print(df.describe().round(3))