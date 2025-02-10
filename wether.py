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

temp=[random.randint(-10, 36) for i in range(365)]
average_temp=sum(temp)/365
higher_25=0
max_len = 0
line = 1
hot=[]
cold=[]
for i in range(365):
    if temp[i]>25:
        higher_25+=1

    if temp[i] < 0:
        line += 1
        cold.append(i)
    else:
        hot.append(i)
        if line > max_len:
            max_len = line
        line = 1
print('Подряд ниже 0:', max_len)
print('Выше 25:', higher_25)

# Создание подграфиков
fig, axs = plt.subplots(1, 2, figsize=(10, 4))  # 1 ряд, 2 столбца

# График 1

axs[0].scatter(hot, [temp[i] for i in hot], color="red")
axs[0].scatter(cold, [temp[i] for i in cold], color="blue")
axs[0].plot([i for i in range(365)], temp, color='grey')
axs[0].set_title("Погода")
axs[0].set_ylabel("Температура")
axs[0].set_xlabel("День")



count_day=[0]*45
for i in temp:
    count_day[i-10]+=1

# График 2
axs[1].bar([i for i in range(-10, 35)], count_day, color="green")
axs[1].set_title("Распределение Погоды")
axs[1].set_ylabel("Кол-во дней")
axs[1].set_xlabel("Температура")

plt.show()

