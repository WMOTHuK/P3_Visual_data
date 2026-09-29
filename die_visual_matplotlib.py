from die import Die
import matplotlib.pyplot as plt

# Создание кубика D6.
die = Die()
# Моделирование серии бросков с сохранением результатов в списке.
results = []
numb_rolls = 100
for roll_num in range(numb_rolls):
    result = die.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
input_values = [1, 2, 3, 4, 5, 6]
plt.bar(input_values, frequencies, linewidth=5)

# Назначение заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', labelsize=14)
plt.show()