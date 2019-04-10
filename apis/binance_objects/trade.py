

def get_trade_from_json(json):
    return Trade(json["id"], json["price"], json["qty"], json["time"], json["isBuyerMaker"], json["isBestMatch"])


class Trade:

    def __init__(self, id, price, qty, time, is_buyer_maker, is_best_match):
        self.id = id
        self.price = price
        self.qty = qty
        self.time = time
        self.is_buyer_maker = is_buyer_maker
        self.is_best_match = is_best_match
