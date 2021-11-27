from coinonepy import CoinOne
import pprint

with open("account.txt") as f:
    lines = f.readlines()

access = lines[0].strip()
secret = lines[1].strip()

coinone = CoinOne(access, secret)
order = coinone.buy_limit_order('klay', 1500, 50)
print(order)
