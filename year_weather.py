import csv
from datetime import datetime


class Year_Weather:
    """Класс, данные погоды за один год"""
    
    def __init__(self, filename):
        """Пока храним только даты и минимальные и максимальные значения"""
        self.filename = filename
        self.dates, self.highs, self.lows, self.errors = [],[],[],[]
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
                except ValueError:
                    self.errors.append((row[0], 'missing data'))
                else:
                    self.highs.append(high)
                    self.dates.append(date) 
                    self.lows.append(low)