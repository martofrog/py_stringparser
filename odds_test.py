import unittest
from odds import Odds


class OddsTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_fract_odds(self):
        odds = Odds("1/2")
        self.assertEquals(odds.get_fract_odds(), "1/2")
