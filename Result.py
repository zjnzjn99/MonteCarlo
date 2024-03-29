class Result(object):
    def __init__(self):
        self.date = 0.
        self.spot = 0.
        self.price = 0.
        self.delta = 0.
        self.gamma = 0.
        self.theta = 0.
        self.rho = 0.
        self.vega = 0.

    def __str__(self):
        res = {'date': self.date, 'spot': self.spot, 'price': self.price, 'delta': self.delta, 'gamma': self.gamma,
               'theta': self.theta, 'rho': self.rho, 'vega': self.vega}
        return f'{res}'

    def __add__(self, other):
        self.price += other.price
        self.delta += other.delta
        self.gamma += other.gamma
        self.theta += other.theta
        self.rho += other.rho
        self.vega += other.vega

    def __sub__(self, other):
        self.price -= other.price
        self.delta -= other.delta
        self.gamma -= other.gamma
        self.theta -= other.theta
        self.rho -= other.rho
        self.vega -= other.vega

    def __mul__(self, other):
        self.price *= other
        self.delta *= other
        self.gamma *= other
        self.theta *= other
        self.rho *= other
        self.vega *= other

