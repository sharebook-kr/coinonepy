# coinonepy
python wrapper for coinone 

# Public API

## 티커 조회 

```
import coinonepy

tickers = coinonepy.get_tickers()
print(len(tickers))
```


## 현재가 조회

```
import coinonepy

xrp_price = coinonepy.get_current_price("xrp")
print(xrp_price)
```

## 호가 조회

```
import coinonepy 
import pprint

orderbook = coinonepy.get_orderbook('btc')
ask = orderbook['ask']
bid = orderbook['bid']

pprint.pprint(ask)
```

# Private API

## 잔고 조회 

```
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
```

## 매수

```
from coinonepy import CoinOne
import pprint

with open("account.txt") as f:
    lines = f.readlines()

access = lines[0].strip()
secret = lines[1].strip()

coinone = CoinOne(access, secret)
order = coinone.buy_limit_order('klay', 1500, 50)
print(order)

```

## 매도 

```
```

## 주문 취소

```
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
```
