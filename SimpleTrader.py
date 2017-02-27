import random

class SimpleTrader:
    def __init__(self, starting_dollars):
        self.starting_dollars = starting_dollars

    def nextDay(self, current_dollars, current_btc, date, btc_price):
        return ('BUY', 3.0 / btc_price)
