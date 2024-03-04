from checkException import checkException as ch
from Enums import ContractStatus


class Arguments(object):
    def __init__(self, pricingDay, spot, notional, refs, rf, q, vol, holidays, expiryDate, pathNum, oneYear):
        self.pricingDay = pricingDay
        self.spot = spot
        self.notional = notional
        self.refs = refs
        self.rf = rf
        self.q = q
        self.vol = vol
        self.oneYear = 365
        self.holidays = holidays
        self.expiryDate = expiryDate
        self.pathNum = pathNum
        self.oneYear = oneYear

    def validCheck(self):
        # ch.checkNon_negativeNumbers(self.pricingDay)
        ch.checkIsSorted(self.holidays)
        ch.checkTradeDay(self.pricingDay, self.holidays)
        ch.checkPricingDay(self.pricingDay, self.expiryDate)


class AutoCallArgs(Arguments):
    def __init__(self, pricingDay, spot, notional, refs, rf, q, vol, holidays, expiryDate, isKnockIn, notionalRate,
                 knockOutObv, knockInObv, knockOutBarrier, knockInBarrier, knockOutCoupon, strike, guaranteedRate,
                 backPremium):
        super().__init__(pricingDay, spot, notional, refs, rf, q, vol, holidays, expiryDate)
        self.isKnockIn = isKnockIn
        self.notionalRate = notionalRate
        self.knockOutObv = knockOutObv
        self.knockInObv = knockInObv
        self.knockOutBarrier = knockOutBarrier
        self.knockInBarrier = knockInBarrier
        self.knockOutCoupon = knockOutCoupon
        self.strike = strike
        self.guaranteedRate = guaranteedRate
        self.backPremium = backPremium
        self.contractStatus = self.isKnockIn if ContractStatus.KnockIn else ContractStatus.Normal


class SnowballArgs(AutoCallArgs):
    def __init__(self, pricingDay, spot, notional, refs, rf, q, vol, holidays, expiryDate,
                 isKnockIn, notionalRate, knockOutObv, knockInObv, knockOutBarrier, knockInBarrier, knockOutCoupon,
                 strike, guaranteedRate, backPremium, rebate, kiPartRate):
        super().__init__(pricingDay, spot, notional, refs, rf, q, vol, holidays, expiryDate, isKnockIn, notionalRate,
                         knockOutObv, knockInObv, knockOutBarrier, knockInBarrier, knockOutCoupon, strike,
                         guaranteedRate, backPremium)
        self.rebate = rebate
        self.kiPartRate = kiPartRate
