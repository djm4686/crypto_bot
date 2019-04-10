from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, BigInteger
from apis.binance import Binance
from db.db_methods import get_engine


Base = declarative_base()

class Pair(Base):

    __tablename__ = "pairs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    base = Column(String, nullable=False)
    other = Column(String, nullable=False)

    def __repr__(self):
        return "<Pair('{}|{}')>".format(self.base, self.other)

    def to_string(self):
        return str.upper("{}{}".format(self.base, self.other))




class Trade(Base):

    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trade_id = Column(Integer, nullable=False)
    pair = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    time = Column(BigInteger, nullable=False)

    def __repr__(self):
        return "<Trade(trade_id='{}', pair='{}', price='{}', time='{}')>".format(self.trade_id, self.pair,
                                                                                 self.price, self.time)
