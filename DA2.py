import pandas as pd

# Загрузка данных
df = pd.read_csv(r'C:\PY\DATA\hw_AZ01.csv')

# Группировка по городу и расчет средней зарплаты
result = df.groupby('City')['Salary'].mean().round(2)

print("Средняя зарплата по городам:")
print(result)