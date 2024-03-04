import bisect


class checkException(object):

    @staticmethod
    def checkNon_negativeNumbers(number):
        if number < 0:
            raise ValueError

    @staticmethod
    def checkIsSorted(holiday):
        if sorted(holiday) != holiday:
            raise KeyError

    @staticmethod
    def checkTradeDay(day, holiday):
        idx = bisect.bisect(holiday, day) - 1
        if holiday[idx] == day:
            raise ValueError

    @staticmethod
    def checkPricingDay(day, expiryDate):
        if day - expiryDate > 0:
            raise ValueError
