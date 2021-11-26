import requests 


def get_tickers():
    url = "https://api.coinone.co.kr/ticker/"
    params = {"currency": "all"}
    resp = requests.get(url, params=params)
    data = resp.json()
    reserved_keys = ['result', 'errorCode', 'timestamp']
    tickers = [k for k in data.keys() if k not in reserved_keys]
    return tickers


def get_current_price(ticker="btc"):
    url = "https://api.coinone.co.kr/ticker/"
    params = {"currency": ticker}
    resp = requests.get(url, params=params)
    data = resp.json()
    return data


def get_orderbook(ticker):
    url = "https://api.coinone.co.kr/orderbook/"
    params = {"currency": ticker}
    resp = requests.get(url, params=params)
    data = resp.json()
    return data


if __name__ == "__main__":
    import pprint 
    #tickers = get_tickers()
    #print(tickers)

    btc_price = get_current_price("xrp")
    pprint.pprint(btc_price)

    #btc_price = get_current_price("all")
    #print(btc_price)

    #order = get_orderbook("btc")
    #pprint.pprint(order)
