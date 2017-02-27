from SimpleTrader import SimpleTrader
from RandomTrader import RandomTrader
from HODLTrader import HODLTrader
from Trader5 import Trader5
import json
import numpy

def test_algorithm(trader, starting_dollars):
    f_btc = open('pricesBitcoin.json', 'r')
    prices = json.loads(f_btc.read())['bpi']
    f_btc.close()

    f_eth = open('pricesEthereum.json', 'r')
    prices_eth = json.loads(f_eth.read())["data"]
    f_eth.close()

    # Bitcoin prices, since 2013
    # prices_arr = [(date, prices[date]) for date in sorted(prices) if int(date.split('-')[0]) >= 2013]

    # Ethereum prices, since August 2015
    prices_arr = [(x["time"], x["usd"]) for x in prices_eth][:1000]

    current_dollars = starting_dollars
    current_btc = 0
    trader = trader(current_dollars)
    for i, (date, price) in enumerate(prices_arr):
        operation = trader.nextDay(current_dollars, current_btc, date, price)
        if (operation[0] == 'BUY' and operation[1]*price <= current_dollars):
            current_dollars -= operation[1]*price
            current_btc += operation[1]
        elif (operation[0] == 'SELL' and current_btc > operation[1]):
            current_dollars += operation[1]*price
            current_btc -= operation[1]
    return (current_dollars, current_btc, current_dollars + current_btc * prices_arr[-1][1])

def main():
    simple_res = test_algorithm(SimpleTrader, 10000)

    print('Simple Trader:')
    print('Left with', simple_res[0], 'dollars')
    print('and', simple_res[1], 'BTC')
    print('total dollar value:', simple_res[2])

    results_random = []
    for n in range(100):
        results_random.append(test_algorithm(RandomTrader, 10000))

    print('')
    print('Random Trader:')
    print('Left with', numpy.mean([x[0] for x in results_random]), 'dollars')
    print('and', numpy.mean([x[1] for x in results_random]), 'BTC')
    print('total dollar value:', numpy.mean([x[2] for x in results_random]))

    HODL_res = test_algorithm(HODLTrader, 10000)
    print('')
    print('HODL Trader:')
    print('Left with', HODL_res[0], 'dollars')
    print('and', HODL_res[1], 'BTC')
    print('total dollar value:', HODL_res[2])

    Trader5_res = test_algorithm(Trader5, 10000)
    print('')
    print('Trader5:')
    print('Left with', Trader5_res[0], 'dollars')
    print('and', Trader5_res[1], 'BTC')
    print('total dollar value:', Trader5_res[2])

if __name__ == '__main__':
    main()
