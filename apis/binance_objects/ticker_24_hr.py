from .utils import convert_millis_to_seconds


def get_ticker_24_hr_from_json(json):
    return Ticker24Hr(json["symbol"], json["priceChange"], json["priceChangePercent"],
                      json["weightedAvgPrice"], json["prevClosePrice"], json["lastPrice"],
                      json["lastQty"], json["bidPrice"], json["askPrice"],
                      json["openPrice"], json["highPrice"], json["lowPrice"],
                      json["volume"], json["quoteVolume"],
                      convert_millis_to_seconds(json["openTime"]),
                      convert_millis_to_seconds(json["closeTime"]),
                      json["firstId"], json["lastId"], json["count"])

def get_ticker_list_24_hr_from_json(json):
    return [get_ticker_24_hr_from_json(t_json) for t_json in json]


class Ticker24Hr:

    def __init__(self, symbol, price_change, price_change_percent,
                 weighted_avg_price, prev_close_price, last_price,
                 last_qty, bid_price, ask_price, open_price, high_price,
                 low_price, volume, quote_volume, open_time, close_time,
                 first_id, last_id, count):
        self.symbol = symbol
        self.price_change = price_change
        self.price_change_percent = price_change_percent
        self.weighted_avg_price = weighted_avg_price
        self.prev_close_price = prev_close_price
        self.last_price = last_price
        self.last_qty = last_qty
        self.bid_price = bid_price
        self.ask_price = ask_price
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.volume = volume
        self.quote_volume = quote_volume
        self.open_time = open_time
        self.close_time = close_time
        self.first_id = first_id
        self.last_id = last_id
