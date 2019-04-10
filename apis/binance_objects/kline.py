__author__ = 'dmadden'
from datetime import datetime
from .utils import convert_millis_to_seconds

def get_kline_from_json(json):
    return Kline(convert_millis_to_seconds(json[0]),
                 json[1],
                 json[2],
                 json[3],
                 json[4],
                 json[5],
                 convert_millis_to_seconds(json[6]),
                 json[7],
                 json[8],
                 json[9],
                 json[10])

def get_klines_from_json(json):
    return [Kline(k_json) for k_json in json]


class Kline:

    def __init__(self, open_time, open, high, low, close, volume,
                 close_time, quote_asset_volume, number_of_trades,
                 taker_buy_base_asset_volume, taker_buy_quote_asset_volume):
        self.open_time = open_time
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.close_time = close_time
        self.quote_asset_volume = quote_asset_volume
        self.number_of_trades = number_of_trades
        self.taker_buy_base_asset_volume = taker_buy_base_asset_volume
        self.taker_buy_quote_asset_volume = taker_buy_quote_asset_volume

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
