import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'csv_data/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)

    # Headers
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Highest values
    dates, highs = [],[]
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d').date()
        print(date)
        dates.append(date.strftime('%Y-%m-%d')) 
        high = int(row[1])
        highs.append(high)
    print(dates)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# Форматирование диаграммы.
plt.title("Daily high temperatures, July 2014", fontsize=24)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()