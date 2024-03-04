from enum import Enum


class ExerciseType(Enum):
    European = 1
    American = 2


class OptionType(Enum):
    Call = 1
    Put = 2


class BarrierType(Enum):
    UpIn = 1
    DownIn = 2
    UpOut = 3
    DownOut = 4


class ContractStatus(Enum):
    Normal = 1
    KnockIn = 2
    KnockOut = 3

