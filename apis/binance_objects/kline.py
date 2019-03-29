__author__ = 'dmadden'
from datetime import datetime
from .utils import convert_millis_to_seconds


class Kline:

    def __init__(self, data):
        self.open_time = int(convert_millis_to_seconds(int(data[0])))
        self.open = data[1]
        self.high = data[2]
        self.low = data[3]
        self.close = data[4]
        self.volume = data[5]
        self.close_time = int(convert_millis_to_seconds(int(data[6])))
        self.quote_asset_volume = data[7]
        self.number_of_trades = data[8]
        self.taker_buy_base_asset_volume = data[9]
        self.taker_buy_quote_asset_volume = data[10]

    def __repr__(self):
        breaker = "==============================\n"
        open_time = "Open Time: {}\n".format(datetime.utcfromtimestamp(self.open_time).strftime('%Y-%m-%d %H:%M:%S'))
        open = "Open Price: {}\n".format(self.open)
        high = "High Price: {}\n".format(self.high)
        low = "Low Price: {}\n".format(self.low)
        close = "Closing Price: {}\n".format(self.close)
        volume = "Trade Volume: {}\n".format(self.volume)
        close_time = "Closing Time: {}\n".format(datetime.utcfromtimestamp(self.close_time).strftime('%Y-%m-%d %H:%M:%S'))
        quote_as = "Quote Asset Volume: {}\n".format(self.quote_asset_volume)
        num_trades = "Number of Trades: {}\n".format(self.number_of_trades)
        taker_buy_base = "Taker Buy Base Asset Volume: {}\n".format(self.taker_buy_base_asset_volume)
        taker_buy_quote = "Taker Buy Quote Asset Volume: {}\n".format(self.taker_buy_quote_asset_volume)
        return breaker + open_time + open + high + low + close + volume + close_time + \
               quote_as + num_trades + taker_buy_base + taker_buy_quote

    def __str__(self):
        return self.__repr__()
