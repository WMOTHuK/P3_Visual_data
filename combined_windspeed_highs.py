from matplotlib import pyplot as plt

from year_weather import Year_Weather

sitka = Year_Weather('csv_data/sitka_weather_2014.csv')
death_valley = Year_Weather('csv_data/death_valley_2014.csv')
print(sitka.dates)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(sitka.dates, sitka.w_highs, c='red', alpha=0.5 )
plt.plot(death_valley.dates, death_valley.w_highs, c='blue', alpha=0.5 )


# Форматирование диаграммы.
plt.title("Daily high windspeeds, 2014", fontsize=24)
fig.autofmt_xdate()
plt.ylabel("Windspeed max (MPH) ", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()