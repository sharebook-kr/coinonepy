import coinonepy

btc = coinonepy.get_current_price("btc")
btc_last_price = float(btc['last'])
print(btc_last_price)