
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
        if not self._fract_price:
            # If none string, exit early. Nothing to process
            return None

        if self._fract_price.count("/") > 1:
            return None

        accepted_chars = ["/"]
        value = ""

        for s in self._fract_price:
            try:
                num = int(s)
                value += str(num)
            except:
                if s in accepted_chars:
                    value += s
                    continue
                return None
        return value
