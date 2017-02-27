import random

class Trader5:
    def __init__(self, startingDollars):
        self.startingDollars = startingDollars
        self.prevPrice = 0
        self.bought = False
        self.changeParam = 0.001
        self.sellParam = 0.01
        self.buyParam = 0.06

    # Sells when price increases more than 1 percent in a day
    # Buys a lot when price goes down more than 1 percent in a day
    def nextDay(self, currentDollars, currentBtc, date, btcPrice):
        if not self.bought:
            self.bought = True
            self.prevPrice = btcPrice
            return ('BUY', (currentDollars / 2) / btcPrice)

        increasePercent = (btcPrice / self.prevPrice) - 1
        self.prevPrice = btcPrice
        if increasePercent > self.changeParam:
            return ('SELL', currentBtc * self.sellParam)
        elif increasePercent < -1 * self.changeParam:
            return ('BUY', (currentDollars * self.buyParam) / btcPrice)
        return ('SELL', 0)
