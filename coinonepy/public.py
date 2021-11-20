import requests 


def get_current_price(ticker="btc", verbose=False):
    url = "https://api.coinone.co.kr/ticker/"
    params = {"currency": ticker}
    resp = requests.get(url, params=params)
    data = resp.json()
    cur_price = float(data['last'])
    if verbose:
        return data
    else:
        return cur_price


def get_orderbook(ticker):
    url = "https://api.coinone.co.kr/orderbook/"
    params = {"currency": ticker}
    resp = requests.get(url, params=params)
    data = resp.json()
    return data


if __name__ == "__main__":
    import pprint 

    btc_price = get_current_price("xrp")
    print(btc_price)

    btc_price = get_current_price("xrp", verbose=True)
    print(btc_price)

    order = get_orderbook("btc")
    pprint.pprint(order)
