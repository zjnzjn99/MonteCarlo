from ipyparallel import Client

import contracts
from MC_Option import MC_Option
from contracts import AutoCallArgs
import numpy as np


class MC_AutoCall(MC_Option):
    def __init__(self, args: AutoCallArgs):
        super().__init__(args)
        self.autoCall_args = args
        self.presentValue = 0.

    def payoffKnockIn(self, S):
        pass

    def payoff(self, S):
        pass

    def payoffKnockOut(self, S, t):
        pass

    def KnockOutFilter(self, S):
        pass

    def KnockInFilter(self, S):
        pass

    def Pv(self):
        # initialize Pv
        Pv = 0.
        if len(self.obvSet) == 1:
            return self.payoff(self.autoCall_args.spot)
        simulatedS = self.simulatePath()
        # knock-out filter
        # filtered_S = self.KnockOutFilter(simulatedS)
