import csv
from datetime import datetime


class Year_Weather:
    """Класс, данные погоды за один год"""
    
    def __init__(self, filename):
        """Пока храним только даты и минимальные и максимальные значения"""
        self.filename = filename

        #dates
        self.dates = []

        #Temperature
        self.highs, self.lows = [],[]

        #Humidity
        self.h_highs, self.h_lows = [],[]

        #Errors
        self.errors = []

        self.fill_data()

    def fill_data(self):
        """"Импортируем данные из файла"""
        with open(self.filename) as f:
            reader = csv.reader(f)
            # values
            for row in reader:
                try:
                    date = datetime.strptime(row[0], '%Y-%m-%d').date() 
                    high = int(row[1])
                    low = int(row[3])
                    h_high = int(row[7])
                    h_low = int(row[9])    
                except ValueError:
                    self.errors.append((row[0], 'missing data'))
                else:
                    self.highs.append(high)
                    self.dates.append(date) 
                    self.lows.append(low)
                    self.h_highs.append(h_high)
                    self.h_lows.append(h_low)