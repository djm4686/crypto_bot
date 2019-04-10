__author__ = 'dmadden'
import time


def get_current_time():
    return int(time.time())

def get_timestamp_millis():
    return int(time.time()*1000)