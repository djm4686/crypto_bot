from enum import Enum


INTERVALS = {
    "SECOND": 1,
    "MINUTE": 2,
    "DAY": 3
}

def get_rate_limit_from_json(json):
    return RateLimit(json["rateLimitType"],
                     get_rate_limit_interval(json["interval"]),
                     json["intervalNum"],
                     json["limit"])

def get_rate_limit_interval(string):
    return RateLimitInterval(INTERVALS[string])


class RateLimitInterval(Enum):

    SECOND = 1
    MINUTE = 2
    DAY = 3


class RateLimit:

    def __init__(self, rate_limit_type, interval, interval_num, limit):
        self.rate_limit_type = rate_limit_type
        self.interval = interval
        self.interval_num = interval_num
        self.limit = limit