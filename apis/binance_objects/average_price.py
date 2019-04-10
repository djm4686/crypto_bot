

def get_avg_price_from_json(json):
    return AveragePrice(json["mins"], json["price"])


class AveragePrice:

    def __init__(self, mins, price):
        self.mins = mins
        self.price = price