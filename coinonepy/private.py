import requests
import time
import json
import base64
import hashlib 
import hmac
import pprint


class CoinOne:
    def __init__(self, access_token, secret_key):
        self.access_token = access_token 
        self.secret_key = secret_key

    def generate_payload(self, **param):
        param['access_token'] = self.access_token
        param['nonce'] = int(time.time() * 1000) 
        json_param = json.dumps(param) 
        self.payload = base64.b64encode(json_param.encode('utf-8'))

    def generate_signature(self):
        self.signature = hmac.new(
            self.secret_key.upper().encode('utf-8'), 
            self.payload,
            hashlib.sha512).hexdigest()

    def request_post(self, url, **kwargs):
        self.generate_payload(**kwargs)
        self.generate_signature()
        headers = {
            'Content-Type': 'application/json',
            'X-COINONE-PAYLOAD': self.payload,
            'X-COINONE-SIGNATURE': self.signature
        }
        resp = requests.post(url=url, headers=headers)
        return resp.json()

    def get_balance(self):
        url = "https://api.coinone.co.kr/v2/account/balance/"
        data = self.request_post(url=url)
        return data

    def get_user_info(self):
        url = "https://api.coinone.co.kr/v2/account/user_info/"
        data = self.request_post(url=url)
        return data

    def buy_limit_order(self, ticker, price, quantity, is_post_only=False):
        url = "https://api.coinone.co.kr/v2/order/limit_buy/"
        param = {
            'price': price, 
            'qty': quantity, 
            'currency': ticker, 
            'is_post_only': is_post_only
        }
        data = self.request_post(url=url, **param)
        return data        

    def sell_limit_order(self, ticker, price, quantity, is_post_only=False):
        url = "https://api.coinone.co.kr/v2/order/limit_sell/"
        param = {
            'price': price, 
            'qty': quantity, 
            'currency': ticker, 
            'is_post_only': is_post_only
        }
        data = self.request_post(url=url, **param)
        return data        

    def cancel_order(self, ticker, order_id, price, quantity, is_ask):
        url = "https://api.coinone.co.kr/v2/order/cancel/"
        param = {
            'order_id': order_id,
            'price': price, 
            'qty': quantity, 
            'is_ask': is_ask,
            'currency': ticker 
        }
        data = self.request_post(url=url, **param) 
        return data        


if __name__ == "__main__":
    with open("account.txt") as f:
        lines = f.readlines()

    access_token = lines[0].strip()
    secret_key = lines[1].strip()
    coinone = CoinOne(access_token, secret_key)

    balance = coinone.get_balance()
    pprint.pprint(balance)

    #user_info = coinone.get_user_info()
    #pprint.pprint(user_info)