
import pygal

from random_walk import RandomWalk

# Построение случайного блуждания и нанесение точек на диаграмму.
rw = RandomWalk(15000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))
# Назначение размера области просмотра.
xy_chart = pygal.XY(
    stroke=False, 
    show_x_labels=False, 
    show_y_labels=False,
    dots_size=2
)
xy_chart.title = 'Пример точечного графика'

rwalk = list(zip(rw.x_values, rw.y_values))

xy_chart.add('randomwalk', rwalk)


xy_chart.render_to_file('scatter.svg')