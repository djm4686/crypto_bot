__author__ = 'dmadden'
from apis.binance import Binance
from pprint import pprint


def main():
    b = Binance()
    b.initialize()
    print(b.get_exchange_info())

if __name__ == "__main__":
    main()