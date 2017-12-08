import requests
from time import sleep

TRANSACTFEE_BTC = 0.0025
TRANSACTFEE_LTC = 0.003
TRANSACTFEE_ETH = 0.003

EXAMPLE_ARB_BTC = 1


def get_gdax_api(relativeURL):
    return requests.get("https://api.gdax.com" + relativeURL)

def get_gdax_ticker(ticker):
    return get_gdax_api("/products/{}/ticker".format(ticker))

def get_json_value(response, key):
    res = response.json()[key]
    return float(res)
    

ltcusd_price = get_json_value(get_gdax_ticker("ltc-usd"), "price")
ltceur_price = get_json_value(get_gdax_ticker("ltc-eur"), "price")
ltcbtc_price = get_json_value(get_gdax_ticker("ltc-btc"), "price")
ethusd_price = get_json_value(get_gdax_ticker("eth-usd"), "price")
etheur_price = get_json_value(get_gdax_ticker("eth-eur"), "price")
ethbtc_price = get_json_value(get_gdax_ticker("eth-btc"), "price")
sleep(1)
btcusd_price = get_json_value(get_gdax_ticker("btc-usd"), "price")
btceur_price = get_json_value(get_gdax_ticker("btc-eur"), "price") 


print "==="
print "Ticker:"
print "BTC/USD: {} usd".format(btcusd_price)
print "BTC/EUR: {} eu".format(btceur_price)
print "LTC/USD: {} usd".format(ltcusd_price)
print "LTC/EUR: {} eu".format(ltceur_price)
print "LTC/BTC: {} btc".format(ltcbtc_price)
print "ETH/USD: {} usd".format(ethusd_price)
print "ETH/EUR: {} eu".format(etheur_price)
print "ETH/BTC: {} btc".format(ethbtc_price)

ltcusd_btcfirst_arb = (((EXAMPLE_ARB_BTC / ltcbtc_price) * ltcusd_price) / btcusd_price) - (TRANSACTFEE_BTC + (TRANSACTFEE_LTC *2))
ltcusd_usdfirst_arb = (((EXAMPLE_ARB_BTC * btcusd_price) / ltcusd_price) * ltcbtc_price) - (TRANSACTFEE_BTC + (TRANSACTFEE_LTC *2))
ltceur_btcfirst_arb = (((EXAMPLE_ARB_BTC / ltcbtc_price) * ltceur_price) / btceur_price) - (TRANSACTFEE_BTC + (TRANSACTFEE_LTC *2))
ltceur_eurfirst_arb = (((EXAMPLE_ARB_BTC * btceur_price) / ltceur_price) * ltcbtc_price) - (TRANSACTFEE_BTC + (TRANSACTFEE_LTC *2))
print "==="
print "LTC:"
print "USD native: {} usd".format(ltcusd_price)
print "USD btc-first: {} usd [{} btc arbed: {}, arb profit: {} btc/{} usd]".format(ltcbtc_price * btcusd_price, EXAMPLE_ARB_BTC, ltcusd_btcfirst_arb, ltcusd_btcfirst_arb - EXAMPLE_ARB_BTC, (ltcusd_btcfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "USD usd-first: {} usd [{} btc arbed: {}, arb profit: {} btc/{} usd]".format(ltcbtc_price * btcusd_price, EXAMPLE_ARB_BTC, ltcusd_usdfirst_arb, ltcusd_usdfirst_arb - EXAMPLE_ARB_BTC, (ltcusd_usdfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "EUR btc-first: {} usd [{} btc arbed: {}, arb profit: {} btc/{} usd]".format(ltceur_price / btceur_price * btcusd_price, EXAMPLE_ARB_BTC, ltceur_btcfirst_arb, ltceur_btcfirst_arb- EXAMPLE_ARB_BTC, (ltceur_btcfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "EUR eur-first: {} usd [{} btc arbed: {}, arb profit: {} btc/{} usd]".format(ltceur_price / btceur_price * btcusd_price, EXAMPLE_ARB_BTC, ltceur_eurfirst_arb, ltceur_eurfirst_arb- EXAMPLE_ARB_BTC, (ltceur_eurfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)

ethusd_btcfirst_arb = (((EXAMPLE_ARB_BTC / ethbtc_price) * ethusd_price) / btcusd_price) - (TRANSACTFEE_BTC + (TRANSACTFEE_ETH *2))
ethusd_usdfirst_arb = (((EXAMPLE_ARB_BTC * btcusd_price) / ethusd_price) * ethbtc_price) - (TRANSACTFEE_BTC + (TRANSACTFEE_ETH *2))
etheur_btcfirst_arb = (((EXAMPLE_ARB_BTC / ethbtc_price) * etheur_price) / btceur_price) - (TRANSACTFEE_BTC + (TRANSACTFEE_ETH *2))
etheur_eurfirst_arb = (((EXAMPLE_ARB_BTC * btceur_price) / etheur_price) * ethbtc_price) - (TRANSACTFEE_BTC + (TRANSACTFEE_ETH *2))
print "==="
print "ETH:"
print "USD native: {} usd".format(ethusd_price)
print "USD btc-first: {} usd [{} btc arbed: {}, profit: {} btc/{} usd]".format(ethbtc_price * btcusd_price, EXAMPLE_ARB_BTC, ethusd_btcfirst_arb, ethusd_btcfirst_arb - EXAMPLE_ARB_BTC, (ethusd_btcfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "USD usd-first: {} usd [{} btc arbed: {}, profit: {} btc/{} usd]".format(ethbtc_price * btcusd_price, EXAMPLE_ARB_BTC, ethusd_usdfirst_arb, ethusd_usdfirst_arb - EXAMPLE_ARB_BTC, (ethusd_usdfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "EUR btc-first: {} usd [{} btc arbed: {}, profit: {} btc/{} usd]".format((etheur_price / btceur_price) * btcusd_price, EXAMPLE_ARB_BTC, etheur_btcfirst_arb, etheur_btcfirst_arb - EXAMPLE_ARB_BTC, (etheur_btcfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "EUR eur-first: {} usd [{} btc arbed: {}, profit: {} btc/{} usd]".format((etheur_price / btceur_price) * btcusd_price, EXAMPLE_ARB_BTC, etheur_eurfirst_arb, etheur_eurfirst_arb - EXAMPLE_ARB_BTC, (etheur_eurfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
