# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import random
import matplotlib.pyplot as plt
lst=[random.randint(1, 6) for i in range(1001)]
lst_count=[lst.count(1), lst.count(2), lst.count(3), lst.count(4), lst.count(5), lst.count(6)]
plt.bar([i for i in range(1, 7)], lst_count, color='purple')
for i in range(1, 7):
    plt.text(i, lst_count[i-1], lst_count[i-1]/1000)
plt.title("Столбчатая диаграмма")
plt.show()
# Ищем максимальное количество подряд выпавших одинаковых значений
max_len=0
line=1
for i in range(1000):
    if lst[i]==lst[i+1]:
        line+=1
    else:
        if line>max_len:
            max_len=line
        line=1
print(max_len)
