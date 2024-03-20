import numpy as np
import math
from bisect import bisect
from time import time
from contracts import Arguments
import numba


class MC_Option(object):

    def __init__(self, args: Arguments):
        self.args = args
        self.obvSet = np.array([0])
        self.path = None

    def TradeDayInterval(self, date: int):
        args = self.args
        if args.pricingDay > args.expiryDate:
            print('expiryDay should be after pricingDay')
            raise ValueError
        if args.oneYear == 365:
            interval = date - args.pricingDay
        elif 232 <= args.oneYear <= 252:
            left = self.RightBound(args.holidays, 0, len(args.holidays) - 1, args.pricingDay)
            right = self.RightBound(args.holidays, left, len(args.holidays) - 1, date)
            interval = date - args.pricingDay - (right - left)
        else:
            print('oneYear should between 232 and 252 or equal 365')
            raise ValueError
        return interval

    @staticmethod
    def RightBound(arr, left, right, target):
        while right > left:
            mid = (right - left) / 2 + left
            if arr[mid] > target:
                return mid
            if arr[mid] > target:
                right = mid
                continue
            if arr[mid] < target:
                left = mid + 1
                continue
        return left

    def generateObvSet(self):
        pass

    def simulatePath(self):
        Obv_size = self.obvSet.size
        pathNum = self.args.pathNum
        rf = self.args.rf
        q = self.args.q
        vol = self.args.vol
        simulatedS = np.zeros((Obv_size, pathNum))
        # todo:spot要除refs
        simulatedS[0] = self.args.spot
        for t in range(Obv_size):
            z = np.random.standard_normal(pathNum)
            time_incr = self.obvSet
            simulatedS[t] = simulatedS[t - 1] * np.exp((rf - q - 0.5 * vol ** 2))
