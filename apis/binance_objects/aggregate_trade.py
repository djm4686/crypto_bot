

def get_aggregate_trade_from_json(json):
    return AggregateTrade(json["a"],
                          json["p"],
                          json["q"],
                          json["f"],
                          json["l"],
                          json["T"],
                          json["m"],
                          json["M"])

def get_aggregate_trade_list_from_json(json):
    return [get_aggregate_trade_from_json(a_json) for a_json in json]


class AggregateTrade:

    def __init__(self, agg_trade_id, price, qty, first_trade_id,
                 last_trade_id, timestamp, is_buyer_maker, is_best_price_match):
        self.agg_trade_id = agg_trade_id
        self.price = price
        self.qty = qty
        self.first_trade_id = first_trade_id
        self.last_trade_id = last_trade_id
        self.timestamp = timestamp
        self.is_buyer_maker = is_buyer_maker
        self.is_best_price_match = is_best_price_match
