# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.

import random
import matplotlib.pyplot as plt
import requests
import json

temp=[random.randint(-10, 36) for i in range(365)]
average_temp=sum(temp)/365
higher_25=0
max_len = 0
line = 1
for i in range(365):
    if temp[i]>25:
        higher_25+=1

    if temp[i] < 0:
        line += 1
    else:
        if line > max_len:
            max_len = line
        line = 1
print('Подряд ниже 0:', max_len)
print('Выше 25:', higher_25)

plt.plot(temp, color='blue')
plt.title("Погода")
plt.show()
