import requests

POLO_TRANSACT_FEE_TAKER = 0.0025
POLO_WITHDRAWAL_FEE_BTC = 0.001
POLO_WITHDRAWAL_FEE_ETH_BTC = 0.001
POLO_WITHDRAWAL_FEE_LTC_BTC = 0.001


def get_polo_api(relativeURL):
    return requests.get("https://poloniex.com" + relativeURL)

def get_polo_tickers():
    return get_polo_api("/public?command=returnTicker")

def get_polo_json_value_float(response, ticker, ticker_value_key):
    res = response.json()[ticker][ticker_value_key]
    return float(res)