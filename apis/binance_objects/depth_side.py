
def get_side_from_json(json):
    return DepthSide(json[0], json[1])

class DepthSide:
    def __init__(self, price, qty):
        self.price = price
        self.qty = qty