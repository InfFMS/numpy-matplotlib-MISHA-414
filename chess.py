# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.

import matplotlib.pyplot as plt
import numpy as np
from numpy.matrixlib.defmatrix import matrix
desk=[]
for i in range(8):
    if i%2==0:
        desk.append([1 if i%2==0 else 0 for i in range(8)])
    else:
        desk.append([0 if i%2==0 else 1 for i in range(8)])
# Здесь находиться ферзь
x=int(input())-1
y=int(input())-1

fig, ax = plt.subplots()
circle = plt.Circle((x, y), 0.2, color="red")
ax.add_patch(circle)
# Красим диагонали
up_x, up_y=x+1, y+1
while up_x!=8 and up_y!=8:
    circle = plt.Circle((up_x, up_y), 0.1, color="pink")
    ax.add_patch(circle)
    up_x+=1
    up_y+=1
down_x, down_y=x-1, y-1
while down_x!= -1 and down_y!= -1:
    circle = plt.Circle((down_x, down_y), 0.1, color="pink")
    ax.add_patch(circle)
    down_x-=1
    down_y-=1
left_x, left_y=x-1, y+1
while left_x!= -1 and left_y!=8:
    circle = plt.Circle((left_x, left_y), 0.1, color="pink")
    ax.add_patch(circle)
    left_x-=1
    left_y+=1
right_x, right_y=x+1, y-1
while right_x!=8 and right_y!= -1:
    circle = plt.Circle((right_x, right_y), 0.1, color="pink")
    ax.add_patch(circle)
    right_x+=1
    right_y-=1
# Вертикаль и горизонталь





plt.imshow(desk, cmap='gray')
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8])
# Добавление цветовой шкалы
plt.colorbar()
plt.title("Тепловая карта")
plt.show()




