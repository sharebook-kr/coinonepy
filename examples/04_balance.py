from coinonepy import CoinOne
import pprint

with open("account.txt") as f:
    lines = f.readlines()

access = lines[0].strip()
secret = lines[1].strip()

coinone = CoinOne(access, secret)
balance = coinone.get_balance()
#pprint.pprint(balance)
krw = balance['krw']
pprint.pprint(krw)

