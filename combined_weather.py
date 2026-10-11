from matplotlib import pyplot as plt

from year_weather import Year_Weather

sitka = Year_Weather('csv_data/sitka_weather_2014.csv')
death_valley = Year_Weather('csv_data/death_valley_2014.csv')
print(sitka.dates)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(sitka.dates, sitka.highs, c='red', alpha=0.5 )
plt.plot(sitka.dates, sitka.lows, c='blue', alpha=0.5 )
plt.fill_between(sitka.dates, sitka.highs, sitka.lows, facecolor='blue', alpha=0.1)


plt.plot(death_valley.dates, death_valley.highs, c='yellow', alpha=0.5 )
plt.plot(death_valley.dates, death_valley.lows, c='green', alpha=0.5 )
plt.fill_between(
    death_valley.dates, 
    death_valley.highs, 
    death_valley.lows, 
    facecolor='green', 
    alpha=0.1)


# Форматирование диаграммы.


plt.title("Daily high and lows temperatures, 2014", fontsize=24)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()