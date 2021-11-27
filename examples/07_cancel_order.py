from coinonepy import CoinOne
import pprint

with open("account.txt") as f:
    lines = f.readlines()

access = lines[0].strip()
secret = lines[1].strip()

coinone = CoinOne(access, secret)
ret = coinone.cancel_order(
    'klay', 
    '855854fb-1e4e-11e9-9ec7-00e04c3600d7',
    1500, 
    50, 
    0)
print(ret)