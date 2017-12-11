from apis import *
from time import sleep


EXAMPLE_ARB_BTC = 1

# Get Poloniex Prices
polo_tickers = get_polo_tickers()

# Extract Poloniex Prices
usdtbtc_last = get_polo_json_value_float(polo_tickers, "USDT_BTC", "last")
usdtbtc_bid = get_polo_json_value_float(polo_tickers, "USDT_BTC", "highestBid")
usdtltc_last = get_polo_json_value_float(polo_tickers, "USDT_LTC", "last")
usdtltc_bid = get_polo_json_value_float(polo_tickers, "USDT_LTC", "highestBid")
usdteth_last = get_polo_json_value_float(polo_tickers, "USDT_ETH", "last")
usdteth_bid = get_polo_json_value_float(polo_tickers, "USDT_ETH", "highestBid")
btcltc_last = get_polo_json_value_float(polo_tickers, "BTC_LTC", "last")
btcltc_bid = get_polo_json_value_float(polo_tickers, "BTC_LTC", "highestBid")
btceth_last = get_polo_json_value_float(polo_tickers, "BTC_ETH", "last")
btceth_bid = get_polo_json_value_float(polo_tickers, "BTC_ETH", "highestBid")


print "==="
print "Poloniex Tickers:"
print "BTC/USD: {} usd, highest bid: {} usd".format(usdtbtc_last, usdtbtc_bid)
print "LTC/USD: {} usd, highest bid: {} usd".format(usdtltc_last, usdtltc_bid)
print "LTC/BTC: {} btc, highest bid: {} btc".format(btcltc_last, btcltc_bid)
print "ETH/USD: {} usd, highest bid: {} usd".format(usdteth_last, usdteth_bid)
print "ETH/BTC: {} btc, highest bid: {} btc".format(btceth_last, btceth_bid)