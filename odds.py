
class Odds:

    _num = 0.0

    _den = 0.0

    _fract_price = None

    def __init__(self, fract_price):
        self._fract_price = fract_price

    def get_decimal_odds(self):
        # returns decimal price as double roundDown((num/den)+1, 2)
        pass

    def get_fract_odds(self):
        # returns fractional odds as string
        pass
