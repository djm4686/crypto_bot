

def get_price_from_json(json):
    return Price(json["symbol"], json["price"])

def get_price_list_from_json(json):
    return [get_price_from_json(p_json) for p_json in json]


class Price:

    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
