__author__ = 'dmadden'
from configparser import ConfigParser
import requests
from os.path import dirname, abspath

class RateLimitException(Exception):
    pass

class Base:

    def __init__(self):
        self.api_key = None
        self.api_secret = None
        self.api_endpoint = None
        self.rate_limit = False

    def read_config(self, api):
        c = ConfigParser()
        path = dirname(abspath(__file__)) + "/../" + "config.txt"
        c.read(path)
        self.api_key = c.get(api, "api_key")
        self.api_secret = c.get(api, "secret_key")
        self.api_endpoint = c.get(api, "endpoint")

    def craft_parameters(self, **kwargs):
        params = {}
        for key, val in kwargs.items():
            if val is not None:
                params[key] = val
        return params

    def perform_request(self, func, err_func):
        if self.rate_limit:
            raise RateLimitException
        try:
            response = func()
            cont = err_func(response.status_code)
            if not cont:
                print("You are being rate limited. No more requests.")
                self.rate_limit = True
            return response.json()
        except Exception as e:
            print(str(e))
            raise e

    def check_code(self, code):
        return True

    def do_get(self, endpoint, err_func, parameters=None):
        if parameters is None:
            parameters = {}
        return self.perform_request(lambda: requests.get(endpoint, parameters), err_func)

    def do_post(self, endpoint, err_func, parameters=None):
        if parameters is None:
            parameters = {}
        return self.perform_request(lambda: requests.post(endpoint, parameters), err_func)

    def do_delete(self, endpoint, err_func, parameters=None):
        if parameters is None:
            parameters = {}
        return self.perform_request(lambda: requests.delete(endpoint, params=parameters), err_func)
