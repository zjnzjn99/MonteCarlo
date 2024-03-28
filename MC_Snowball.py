from ipyparallel import Client

import contracts
from MC_AutoCall import MC_AutoCall
from contracts import SnowballArgs
import numpy as np


class MC_Snowball(MC_AutoCall):

    def __init__(self, args: SnowballArgs):
        super().__init__(args)
        self.notionalInterestCountedRate = 1.
        self.knockInTimes = 0.
        self.knockOutTimes = 0.
        self.sn_args = args
        # self.isKnockOut = False

    def generateObvSet(self):
        pricingDay = self.args.pricingDay
        knockOutDays = self.sn_args.knockOutObv
        knockInDays = self.sn_args.knockInObv
        # todo:敲出观察日和敲入观察日要消除包含估值日期当日及其之前的天 需要处理
        knockInDays = set(self.TradeDayInterval(kiDay) for kiDay in knockInDays)
        knockOutDays = set(self.TradeDayInterval(koDay) for koDay in knockOutDays)
        # for knockInDay in knockInDays:
        #     self.obvSet = np.append(self.obvSet, self.TradeDayInterval(knockInDay))
        #
        self.obvSet = knockOutDays | knockInDays | {0}
        self.obvSet = np.array(list(self.obvSet))
        return self.obvSet

    def payoffKnockIn(self, S):
        # todo: 在数据处理的时候记得初始化self.notionalInterestCountedRate
        return self.sn_args.notionalRate + self.notionalInterestCountedRate * self.sn_args.backPremium[-1] - min(
            1 - self.sn_args.guaranteedRate,
            max(self.sn_args.strike - S, 0) * self.sn_args.kiPartRate)

    def payoff(self, S):
        isKnockIn = self.sn_args.isKnockIn
        self.notionalInterestCountedRate = self.sn_args.isAdvancePaymentAllCounted if 1. else self.sn_args.notionalRate
        if S >= self.sn_args.knockOutBarrier[-1]:
            payoff = self.sn_args.notionalRate + self.notionalInterestCountedRate * self.sn_args.backPremium[-1] + \
                     self.sn_args.knockOutCoupon[-1]
        elif isKnockIn or S <= self.sn_args.knockOutBarrier[-1]:
            # self.sn_args.contractStatus = contracts.ContractStatus.KnockIn
            payoff = self.payoffKnockIn(S)
        else:
            payoff = self.sn_args.notionalRate + self.notionalInterestCountedRate * self.sn_args.backPremium[-1] \
                     + self.sn_args.rebate
        return payoff

    def payoffKnockOut(self, S, t):
        """

        :param S: spot
        :param t: ObvSet中的index，最小值为0，最大值为长度-1
        :return:0 or knock-out coupon
        """
        idx = self.RightBound(self.sn_args.knockOutObv, 0, len(self.sn_args.knockOutObv) - 1, t)
        notionalInterestCountedRate = self.sn_args.isAdvancePaymentAllCounted if 1. else self.sn_args.notionalRate
        if self.sn_args.knockOutObv[idx] != t:
            # not a knock-out observation date
            return 0.
        elif S >= self.sn_args.knockOutBarrier[idx]:
            # set contracts status
            self.sn_args.contractStatus = contracts.ContractStatus.KnockOut
            return self.sn_args.notionalRate + notionalInterestCountedRate * self.sn_args.backPremium[idx] + \
                self.sn_args.knockOutCoupon[idx]
        else:
            # return 0
            return 0.

    def KnockOutFilter(self, S: np.array([])):
        """

        :param S: Simulated Paths
        :return: Filtered Simulated paths without knock-out
        """
        for t in self.sn_args.knockOutObv:
            knockOutStatus = np.where(S[t] >= self.sn_args.knockOutBarrier[t], 1, 0)
            condition = np.array([map(self.filter_condition, knockOutStatus)])
            self.knockOutTimes += knockOutStatus.sum()
            couponStatus = self.sn_args.knockOutCoupon[t] * np.exp(-self.args.rf * t)
            self.presentValue += couponStatus * self.knockOutTimes / self.sn_args.pathNum
            S = S[:, condition]
        return S

    def KnockInFilter(self, S: np.array([])):
        """

        :param S: Simulated Paths
        :return: Filtered Simulated Paths without knock-in
        """
        for t in self.sn_args.knockInObv:
            knockInStatus = np.where(S[t] <= self.sn_args.knockInBarrier[t], 1, 0)
            condition = np.array([map(self.filter_condition, knockInStatus)])
            self.knockInTimes += knockInStatus.sum()
            S = S[:, condition]
            payoff_KnockIn = np.array([map(self.payoffKnockIn, S)])
            Pv_KnockIn = payoff_KnockIn * np.exp(-self.args.rf * self.sn_args.knockInObv[-1])
            self.presentValue += Pv_KnockIn.sum() / self.sn_args.pathNum

        return S

    def Pv(self):
        # initialize Pv
        Pv = 0.
        if len(self.obvSet) == 1:
            return self.payoff(self.autoCall_args.spot)
        simulatedS = self.simulatePath()
        # knock-out filter
        filtered_S = self.KnockOutFilter(simulatedS)
        # knock-in filter
        filtered_S = self.KnockInFilter(filtered_S)
        # calculate !knock-out and !knock-in


    @staticmethod
    def filter_condition(status):
        if status:
            return False
        else:
            return True
