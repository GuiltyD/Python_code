class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def torrow(self):
        self.day += 1
    def __str__(self):
        return '{year}/{month}/{day}'.format(year = self.year,month = self.month,day = self.day)

new_day = Date(2018,12,31)
new_day.torrow()
print(new_day)
        
        
