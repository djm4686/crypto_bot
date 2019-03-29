__author__ = 'dmadden'
from .base_api import Base
from utils import get_current_time
from .binance_objects.kline import Kline


class Binance(Base):

    CODE_418 = 418 # Rate limit
    CODE_429 = 429 # IP Ban

    GET_TIME_ENDPOINT = "/api/v1/time" # GET
    GET_EXCHANGE_INFO_ENDPOINT = "/api/v1/exchangeInfo" # GET
    GET_DEPTH_ENDPOINT = "/api/v1/depth" # GET
    GET_RECENT_TRADES_ENDPOINT = "/api/v1/trades" # GET
    GET_AGGREGATE_TRADES_ENDPOINT = "/api/v1/aggTrades" # GET
    GET_KLINES_ENDPOINT = "/api/v1/klines" # GET
    GET_AVG_PRICE_ENDPOINT = "/api/v3/avgPrice" # GET
    GET_24_PRICE_ENDPOINT = "/api/v1/ticker/24hr" # GET
    GET_PRICE_ENDPOINT = "/api/v3/ticker/price" # GET
    GET_ORDER_BOOK_ENDPOINT = "/api/v3/ticker/bookTicker" # GET
    GET_ORDER_INFO_ENDPOINT = "/api/v3/order" # GET (HMAC SHA256)
    GET_OPEN_ORDERS_ENDPOINT = "/api/v3/openOrders" # GET (HMAC SHA256)
    GET_ALL_ORDERS_ENDPOINT = "/api/v3/allOrders" # GET (HMAC SHA256)
    GET_ACCOUNT_INFO_ENDPOINT = "/api/v3/account" # GET (HMAC SHA256)
    GET_ACCOUNT_TRADES_ENDPOINT = "/api/v3/myTrades" # GET (HMAC SHA256)

    POST_NEW_TRADE_ENDPOINT = "/api/v3/order" # POST (HMAC SHA256)
    POST_TEST_NEW_TRADE_ENDPOINT = "/api/v3/order/test" # POST (HMAC SHA256)

    DELETE_TRADE_ENDPOINT = "/api/v3/order" # DELETE (HMAC SHA256)



    # Returns false if the bot should stop requests

    def check_code(self, error_code):
        if error_code in [self.CODE_418, self.CODE_429]:
            return False
        return True

    def test_connectivity(self):
        return self.do_get(self.build_url(self.GET_TIME_ENDPOINT), self.check_code)

    def build_url(self, endpoint):
        return self.api_endpoint + endpoint

    def initialize(self):
        self.read_config("binance")
        response = self.test_connectivity()
        if "serverTime" not in response:
            raise Exception("Difficulty connecting to Binance API.")
        else:
            print("Connected to Binance API.")

    def get_exchange_info(self):
        return self.do_get(self.build_url(self.GET_EXCHANGE_INFO_ENDPOINT), self.check_code)

    def get_depth(self, symbol, limit=100):
        parameters = self.craft_parameters(symbol=symbol, limit=limit)
        return self.do_get(self.build_url(self.GET_DEPTH_ENDPOINT), self.check_code, parameters)

    # Max limit 1000
    def get_recent_trades(self, symbol, limit=500):
        parameters = self.craft_parameters(symbol=symbol, limit=limit)
        return self.do_get(self.build_url(self.GET_RECENT_TRADES_ENDPOINT), self.check_code, parameters)

    def get_aggregate_trades(self, symbol, from_id=None, start_time=None, end_time=None, limit=500):
        parameters = self.craft_parameters(symbol=symbol,
                                           fromId=from_id,
                                           startTime=start_time,
                                           endTime=end_time,
                                           limit=limit)
        return self.do_get(self.build_url(self.GET_AGGREGATE_TRADES_ENDPOINT), self.check_code, parameters)

    def get_klines(self, symbol, interval, start_time=None, end_time=None, limit=500):
        parameters = self.craft_parameters(symbol=symbol,
                                           interval=interval,
                                           startTime=start_time,
                                           endTime=end_time,
                                           limit=limit)
        return [Kline(line) for line in self.do_get(self.build_url(self.GET_KLINES_ENDPOINT), self.check_code, parameters)]

    def get_average_price(self, symbol):
        parameters = self.craft_parameters(symbol=symbol)
        return self.do_get(self.build_url(self.GET_AVG_PRICE_ENDPOINT), self.check_code, parameters)

    def get_24_hr_price_change(self, symbol):
        parameters = self.craft_parameters(symbol=symbol)
        return self.do_get(self.build_url(self.GET_24_PRICE_ENDPOINT), self.check_code, parameters)

    def get_price(self, symbol):
        parameters = self.craft_parameters(symbol=symbol)
        return self.do_get(self.build_url(self.GET_PRICE_ENDPOINT), self.check_code, parameters)

    def get_order_book(self, symbol):
        parameters = self.craft_parameters(symbol=symbol)
        return self.do_get(self.build_url(self.GET_ORDER_BOOK_ENDPOINT), self.check_code, parameters)

    def post_trade(self, symbol, side, type, quantity, time_in_force=None, price=None, new_client_order_id=None,
                   stop_price=None, iceberg_qty=None, new_order_resp_type=None, recv_window=None, test=False):
        timestamp = get_current_time()
        parameters = self.craft_parameters(symbol=symbol, side=side, type=type, timeInForce=time_in_force,
                                           quantity=quantity, price=price, newClientOrderId=new_client_order_id,
                                           stopPrice=stop_price, icebergQty=iceberg_qty,
                                           newOrderRespType=new_order_resp_type, recvWindow=recv_window,
                                           timestamp=timestamp)
        assert quantity > 0
        if type == "LIMIT":
            assert None not in [time_in_force, price]
        elif type == "STOP_LOSS" or type == "TAKE_PROFIT":
            assert stop_price is not None
        elif type == "STOP_LOSS_LIMIT" or type == "TAKE_PROFIT_LIMIT":
            assert None not in [stop_price, time_in_force, price]
        elif type == "LIMIT_MAKER":
            assert price is not None
        endpoint = self.POST_NEW_TRADE_ENDPOINT
        if test:
            endpoint = self.POST_TEST_NEW_TRADE_ENDPOINT
        return self.do_post(self.build_url(endpoint), self.check_code, parameters)

    def get_order_data(self, symbol, order_id=None, orig_client_order_id=None, recv_window=None):
        timestamp = get_current_time()
        parameters = self.craft_parameters(symbol=symbol, orderId=order_id, origClientOrderId=orig_client_order_id,
                                           recvWindow=recv_window, timestamp=timestamp)
        assert order_id is not None or orig_client_order_id is not None
        return self.do_post(self.build_url(self.GET_ORDER_INFO_ENDPOINT), self.check_code, parameters)

    def cancel_order(self, symbol, order_id=None, orig_client_order_id=None, recv_window=None):
        timestamp = get_current_time()
        parameters = self.craft_parameters(symbol=symbol, orderId=order_id, origClientOrderId=orig_client_order_id,
                                           recvWindow=recv_window, timestamp=timestamp)
        assert order_id is not None or orig_client_order_id is not None
        return self.do_delete(self.build_url(self.DELETE_TRADE_ENDPOINT), self.check_code, parameters)

    def get_open_orders(self, symbol, recv_window=None):
        timestamp = get_current_time()
        parameters = self.craft_parameters(symbol=symbol, recvWindow=recv_window, timestamp=timestamp)
        return self.do_get(self.build_url(self.GET_OPEN_ORDERS_ENDPOINT), self.check_code, parameters)

    def get_all_orders(self, symbol, order_id=None, start_time=None, end_time=None, limit=500, recv_window=None):
        timestamp = get_current_time()
        parameters = self.craft_parameters(symbol=symbol, orderId=order_id, startTime=start_time, endTime=end_time,
                                           limit=limit, recvWindow=recv_window, timestamp=timestamp)
        return self.do_get(self.build_url(self.GET_ALL_ORDERS_ENDPOINT), self.check_code, parameters)

    def get_account_info(self, recv_window=None):
        timestamp = get_current_time()
        parameters = self.craft_parameters(recvWindow=recv_window, timestamp=timestamp)
        return self.do_get(self.build_url(self.GET_ACCOUNT_INFO_ENDPOINT), self.check_code, parameters)

    def get_account_trades(self, symbol, start_time, end_time, from_id, limit, recv_window):
        timestamp = get_current_time()
        parameters = self.craft_parameters(symbol=symbol, startTime=start_time, endTime=end_time,
                                          fromId=from_id, limit=limit, recvWindow=recv_window,
                                          timestamp=timestamp)
        return self.do_get(self.build_url(self.GET_ACCOUNT_TRADES_ENDPOINT), self.check_code, parameters)

