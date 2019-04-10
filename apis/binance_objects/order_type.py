from enum import Enum

class OrderType(Enum):

    LIMIT = 1
    PARTIALLY_FILLED = 2
    FILLED = 3
    CANCELLED = 4
    PENDING_CANCEL = 5
    REJECTED = 6
    EXPIRED = 7