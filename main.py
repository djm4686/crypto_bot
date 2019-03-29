__author__ = 'dmadden'
from apis.binance import Binance
from pprint import pprint


def main():
    b = Binance()
    b.initialize()
    print(b.get_klines("ETHBTC", interval="1m", limit=10))

if __name__ == "__main__":
    main()