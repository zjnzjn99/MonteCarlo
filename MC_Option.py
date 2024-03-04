import numpy as np
import math
from bisect import bisect
from time import time
from contracts import Arguments


class MC_Option(object):
    def __init__(self, object_name: Arguments):
        self.Arguments = Arguments

    # def simulatePath(self):
    #     simulatedS = np.zeros()
    @staticmethod
    def TradeDayInterval(holidays, pricingDay, expiryDay, oneYear):
        if oneYear == 365:
            interval = expiryDay - pricingDay
