from .exchange_symbol import get_exchange_symbol_from_json
from .rate_limit import get_rate_limit_from_json

def get_exchange_info_from_json(json):
    return ExchangeInfo(json["timezone"],
                        [get_rate_limit_from_json(rl_json) for rl_json in json["rateLimits"]],
                        json["exchangeFilters"], # TODO make exchangefilter object
                        [get_exchange_symbol_from_json(es_json) for es_json in json["symbols"]])


class ExchangeInfo:

    def __init__(self, timezone, rate_limits, exchange_filters, symbols):
        self.timezone = timezone
        self.rate_limits = rate_limits
        self.exchange_filters = exchange_filters
        self.symbols = symbols

    def __repr__(self):
        return "{'timezone': {}}"