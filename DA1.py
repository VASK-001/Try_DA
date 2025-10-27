#  1: Импорт библиотек
import pandas as pd
import os

#  2: Загрузка данных из CSV файла
try:
    # Запишем путь к файлу
    file_path = r'C:\PY\DATA\World-happiness-report-2024.csv'

    # Читаем CSV файл в DataFrame
    df = pd.read_csv(file_path, encoding='utf-8')

    # Альтернатива если возникнут проблемы с кодировкой:
    # df = pd.read_csv(file_path, encoding='latin-1')

    print("✅ Файл загружен")
    print(f"Размер данных: {df.shape[0]} строк и {df.shape[1]} столбцов\n")

except FileNotFoundError:
    print("❌ Ошибка: Файл не найден! Проверьте путь:")
    print(r"C:\PY\DATA\World-happiness-report-2024.csv")
    print("\nСодержимое папки DATA:")
    try:
        print(os.listdir(r'C:\PY\DATA'))
    except:
        print("Папка DATA не найдена")
except Exception as e:
    print(f"❌ Произошла ошибка: {e}")

#  3: Выводим первые 5 строк данных
print("=" * 50)
print("ПЕРВЫЕ 5 СТРОК ДАННЫХ:")
print("=" * 50)
print(df.head())

# Шаг 4: Выводим инфо о данных
print("\n" + "=" * 50)
print("ИНФОРМАЦИЯ О ДАННЫХ (df.info()):")
print("=" * 50)
print(df.info())

# Шаг 5: Выводим стат описание
print("\n" + "=" * 50)
print("СТАТИСТИЧЕСКОЕ ОПИСАНИЕ (df.describe()):")
print("=" * 50)
print(df.describe())

# Доп: выводим названия столбцов
print("\n" + "=" * 50)
print("НАЗВАНИЯ СТОЛБЦОВ:")
print("=" * 50)
print(df.columns.tolist())

# Доп: проверка на пропущенные значения
print("\n" + "=" * 50)
print("ПРОПУЩЕННЫЕ ЗНАЧЕНИЯ:")
print("=" * 50)
print(df.isnull().sum())