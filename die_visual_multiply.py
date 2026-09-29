import pygal

from die import Die

# Создание кубика D6.
die = Die()
# Моделирование серии бросков с сохранением результатов в списке.
results = []
numb_rolls = 1000
for roll_num in range(numb_rolls):
    result = die.roll() * die.roll()
    results.append(result)

possible_results = die.num_sides ** 2 + 1

print(die.num_sides)
print(possible_results)

# Анализ результатов.
frequencies = []
for value in range(1, possible_results):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
hist = pygal.Bar()


hist.title = f"Results of rolling two D6 {numb_rolls} times and multiply them."
hist.x_labels = range(1, possible_results)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

