import requests

TRANSACT_FEE_TAKER_BTC = 0.0025
TRANSACT_FEE_TAKER_LTC = 0.003
TRANSACT_FEE_TAKER_ETH = 0.003


def get_gdax_api(relativeURL):
    return requests.get("https://api.gdax.com" + relativeURL)

def get_gdax_ticker(ticker):
    return get_gdax_api("/products/{}/ticker".format(ticker))

def get_gdax_json_value_float(response, key):
    res = response.json()[key]
    return float(res)