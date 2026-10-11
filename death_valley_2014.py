import csv
from datetime import datetime

import matplotlib.dates as mdates
from matplotlib import pyplot as plt
from pyparsing import alphas

filename = 'csv_data/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)

    # Headers
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Highest values
    dates, highs, lows = [],[],[]
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d').date()
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            highs.append(high)
            dates.append(date) 
            lows.append(low)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5 )
plt.plot(dates, lows, c='blue', alpha=0.5 )
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Форматирование диаграммы.


plt.title("Daily high and lows temperatures, 2014", fontsize=24)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()