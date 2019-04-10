from .depth_side import DepthSide, get_side_from_json


def get_depth_from_json(json):
    return Depth(json["lastUpdateId"],
                 DepthSide(get_side_from_json(json["bids"])),
                 DepthSide(get_side_from_json(json["asks"])))

class Depth:

    def __init__(self, last_update_id, bids, asks):
        self.last_update_id = last_update_id
        self.bids = bids
        self.asks = asks