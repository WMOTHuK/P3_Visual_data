import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной.

# Построение случайного блуждания и нанесение точек на диаграмму.
rw = RandomWalk(5000000,1,-1)
rw.fill_walk()

point_numbers = list(range(rw.num_points))
# Назначение размера области просмотра.
plt.figure(figsize=(10, 6))

plt.plot(rw.x_values, rw.y_values, linewidth=1)

# Выделение первой и последней точек.
plt.scatter(0, 0, c='green', edgecolors='none', s=200)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
s=200)

# Удаление осей.
plt.axis('off')



plt.show()


