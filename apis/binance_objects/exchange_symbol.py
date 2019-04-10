
def get_exchange_symbol_from_json(json):
    return ExchangeSymbol(json["symbol"],
                          json["status"],
                          json["baseAsset"],
                          json["baseAssetPrecision"],
                          json["quoteAsset"],
                          json["quotePrecision"],
                          json["orderTypes"],
                          json["icebergAllowed"],
                          json["filters"])


class ExchangeSymbol:

    def __init__(self, symbol, status, base_asset, base_asset_precision, quote_asset, quote_precision, order_types, iceberg_allowed, filters):
        self.symbol = symbol
        self.status = status
        self.base_asset = base_asset
        self.base_asset_precision = base_asset_precision
        self.quote_asset = quote_asset
        self.quote_precisions = quote_precision
        self.order_types = order_types
        self.iceberg_allowed = iceberg_allowed
        self.filters = filters