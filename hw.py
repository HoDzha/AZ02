import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Имена учеников
students = [f"Студент {i+1}" for i in range(10)]
# Предметы
subjects = ["Математика", "Русский", "История", "Философия", "ОБЖД"]
# Генерация случайных оценок от 1 до 100 для каждого ученика по каждому предмету
grades = np.random.randint(2, 6, size=(10, 5))
# Создание DataFrame
df = pd.DataFrame(data=grades, index=students, columns=subjects)
# Вывод таблицы
print(df.head())

#print(df.describe())
# Можно было бы оставить .describe(), но ..
for subject in subjects:
    print('Средняя оценка по предмету ', subject, ': ', df[subject].mean())
    print('Медиана оценки по предмету ', subject, ': ', df[subject].median())
    print('Стандартное отклонение оценки по предмету ', subject, ': ', df[subject].std())
    print()

# Вычисление межквартильного размаха
print('Межквартильный размах по предмету Математика:')
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print('Q1_math: ', Q1_math, ' Q3_math: ', Q3_math, ' IQR_math: ', IQR_math)

