import random

class RandomTrader:
    def __init__(self, starting_dollars):
        self.starting_dollars = starting_dollars
        self.buy_param = 0.2
        self.sell_param = 0.2

    def nextDay(self, currentDollars, current_btc, date, btc_price):
        op = 'BUY' if random.random() > 0.5 else 'SELL'
        amount_btc = 0
        if op == 'BUY':
            amount_dollars = random.random()*self.starting_dollars*self.buy_param
            amount_btc = amount_dollars/btc_price
        if op == 'SELL':
            amount_btc = random.random()*current_btc*self.sell_param
        return (op, amount_btc)
