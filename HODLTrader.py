class HODLTrader:
    def __init__(self, starting_dollars):
        self.starting_dollars = starting_dollars
        self.HODLd = False

    def nextDay(self, current_dollars, current_btc, date, btc_price):
        if not self.HODLd:
            self.HODLd = True
            return ('BUY', self.starting_dollars/btc_price)
        return ('SELL', 0)
