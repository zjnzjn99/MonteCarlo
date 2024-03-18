from ipyparallel import Client
from MC_Option import MC_Option
from contracts import Arguments, AutoCallArgs, SnowballArgs
import numpy as np


class MC_Snowball(MC_Option):

    def __init__(self, args: SnowballArgs):
        super().__init__(args)
        self.sn_args = args

    def getObvSet(self):
        pricingDay = self.args.pricingDay
        knockOutDays = self.sn_args.knockOutObv
        knockInDays = self.sn_args.knockInObv
