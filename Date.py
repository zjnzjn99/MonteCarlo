from datetime import datetime


class Date(object):
    def __init__(self, year, month, day):
        self.isLeap = False
        self.excel_date = None
        self.date = datetime(year, month, day)
        self.year = year
        self.month = month
        self.day = day
        self.transform_date_to_excel()

    def transform_date_to_excel(self):
        excel_base_date = datetime(1899, 12, 30)
        delta = self.date - excel_base_date
        # excel_serial_date = delta.days + delta.seconds / (24 * 60 * 60)
        excel_serial_date = delta.days
        self.excel_date = excel_serial_date

    def isLeapYear(self):
        if (self.year % 100 != 0 and self.year % 4 == 0) or (self.year % 100 == 0 and self.year % 400 == 0):
            isLeap = True
            return isLeap

    __monthAndDay = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31,
                     '11': 30, '12': 31}

    __monthAndDayLeap = {'1': 31, '2': 29, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31,
                         '11': 30, '12': 31}

    def transform_date(self):
        date = str(self.date)
        length = len(date)
        if length != 8:
            raise SyntaxError
        else:
            date = int(date)
        year = int(date / 10000)
        month = int((date - 10000 * year) / 100)
        day = date - 100 * int(date / 100)
        if year < 1900:
            raise ValueError
        if month < 0 or month > 12:
            raise ValueError
        isLeap = self.isLeapYear()
        if isLeap and day > self.__monthAndDayLeap.get(str(month)):
            raise ValueError
        elif not isLeap and day > self.__monthAndDay.get(str(month)):
            raise ValueError
        self.date = datetime(year, month, day)
