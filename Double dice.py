import pygal
from die import Die
die_sides = 3
# Создание двух кубиков D6.
die_1 = Die(die_sides)
die_2 = Die(die_sides)
die_3 = Die(die_sides)
# Моделирование серии бросков с сохранением результатов в списке.
num_rolls = 1000000
results = []
for roll_num in range(num_rolls):
    result = die_1.roll() * die_2.roll() * die_3.roll()
    results.append(result)
# Анализ результатов.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides * die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# Визуализация результатов.
hist = pygal.Bar()
hist.title = f"Results of rolling three D{die_sides} dice {num_rolls} times."
hist.x_labels = list(range(3,max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add(f'D{die_sides} + D{die_sides} + D{die_sides}', frequencies)
hist.render_to_file('dice_visual.svg')