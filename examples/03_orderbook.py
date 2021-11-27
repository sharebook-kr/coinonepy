import coinonepy 
import pprint

orderbook = coinonepy.get_orderbook('btc')
ask = orderbook['ask']
bid = orderbook['bid']

pprint.pprint(ask)