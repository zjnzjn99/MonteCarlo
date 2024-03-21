from ipyparallel import Client
from MC_Option import MC_Option
from contracts import Arguments, AutoCallArgs, SnowballArgs
import numpy as np


class MC_Snowball(MC_Option):

    def __init__(self, args: SnowballArgs):
        super().__init__(args)
        self.sn_args = args
        # self.Obv_set = np.array([0])

    def generateObvSet(self):
        pricingDay = self.args.pricingDay
        knockOutDays = self.sn_args.knockOutObv
        knockInDays = self.sn_args.knockInObv
        # todo:敲出观察日和敲入观察日要消除包含估值日期当日及其之前的天
        knockInDays = set(self.TradeDayInterval(kiDay) for kiDay in knockInDays)
        knockOutDays = set(self.TradeDayInterval(koDay) for koDay in knockOutDays)
        # for knockInDay in knockInDays:
        #     self.obvSet = np.append(self.obvSet, self.TradeDayInterval(knockInDay))
        #
        self.obvSet = knockOutDays | knockOutDays | self.obvSet
    # def payoff(self, S, t):
    #     # if()
