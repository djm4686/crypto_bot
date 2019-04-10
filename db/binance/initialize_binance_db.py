from apis.binance import Binance
from db.binance.binance_models import Base, Pair, Trade
from db.db_methods import get_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_


def fill_pairs_table():
    engine = get_engine("binance")
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    b = Binance()
    b.initialize()
    e_info = b.get_exchange_info()
    pairs = []
    for symbol in e_info.symbols:
        base = symbol.base_asset
        other = symbol.quote_asset
        pair = Pair(base=base, other=other)
        pairs.append(pair)
    session.add_all(pairs)
    session.commit()

def fill_trades_table_from_date(timestamp=1554076800000, base_sym="ETH", quote_sym="BTC", end_time=1554575285458): # apr 1 2019 00:00:00
    symbol = base_sym + quote_sym
    engine = get_engine("binance")
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    b = Binance()
    b.initialize()
    trades = b.get_aggregate_trades(symbol, start_time=1554091200000, end_time=1554094800000)
    while trades[-1].timestamp < end_time:
        trades += b.get_aggregate_trades(symbol, start_time=trades[-1].timestamp, end_time=trades[-1].timestamp + 3600000)
        print("getting another...")
    for chunk in chunk_trades(trades):
        t_objs = []
        for t in chunk:
            t_object = Trade(trade_id=t.first_trade_id,
                             pair=session.query(Pair).filter(
                                 and_(Pair.base == base_sym, Pair.other == quote_sym)).one().id,
                             price=t.price,
                             time=t.timestamp)
            t_objs.append(t_object)
        print("Committing to db...")
        session.add_all(t_objs)
        session.commit()
        print("Done.")

def chunk_trades(trades):
    chunk_num = 1
    while len(trades) > 0:
        print(len(trades))
        ret = []
        print("Chunk {}".format(chunk_num))
        for _ in range(1000):
            try:
                ret.append(trades.pop())
            except IndexError:
                print("Done chunking")
                yield ret
                break
        yield ret
        chunk_num += 1



if __name__ == "__main__":
    fill_pairs_table()
    fill_trades_table_from_date()