import requests

BITTREX_TRANSACT_FEE_TAKER = 0.0025
BITTREX_WITHDRAWAL_FEE_BTC = 0.001
BITTREX_WITHDRAWAL_FEE_ETH_BTC = 0.001
BITTREX_WITHDRAWAL_FEE_LTC_BTC = 0.001


def get_bittrex_api(relativeURL):
    return requests.get("https://bittrex.com/api" + relativeURL)

def get_bittrex_tickers():
    return get_bittrex_api("/v1.1/public/getmarketsummaries")

def get_bittrex_json_value_float(response, ticker, ticker_value_key):
    results = response.json()["result"]
    for item in results:
        if item["MarketName"] == ticker:
            return item[ticker_value_key]
    return None