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
    

ltcusd_resp = get_gdax_ticker("ltc-usd")
ltceur_resp = get_gdax_ticker("ltc-eur")
ltcbtc_resp = get_gdax_ticker("ltc-btc")
ethusd_resp = get_gdax_ticker("eth-usd")
etheur_resp = get_gdax_ticker("eth-eur")
ethbtc_resp = get_gdax_ticker("eth-btc")
sleep(1)
btcusd_resp = get_gdax_ticker("btc-usd")
btceur_resp = get_gdax_ticker("btc-eur")


ltcusd_price = get_json_value(ltcusd_resp, "price")
ltcusd_bid = get_json_value(ltcusd_resp, "bid")
ltcusd_ask = get_json_value(ltcusd_resp, "ask")
ltceur_price = get_json_value(ltceur_resp, "price")
ltceur_bid = get_json_value(ltceur_resp, "bid")
ltceur_ask = get_json_value(ltceur_resp, "ask")
ltcbtc_price = get_json_value(ltcbtc_resp, "price")
ltcbtc_bid = get_json_value(ltcbtc_resp, "bid")
ltcbtc_ask = get_json_value(ltcbtc_resp, "ask")
ethusd_price = get_json_value(ethusd_resp, "price")
ethusd_bid = get_json_value(ethusd_resp, "bid")
ethusd_ask = get_json_value(ethusd_resp, "ask")
etheur_price = get_json_value(etheur_resp, "price")
etheur_bid = get_json_value(etheur_resp, "bid")
etheur_ask = get_json_value(etheur_resp, "ask")
ethbtc_price = get_json_value(ethbtc_resp, "price")
ethbtc_bid = get_json_value(ethbtc_resp, "bid")
ethbtc_ask = get_json_value(ethbtc_resp, "ask")
btcusd_price = get_json_value(btcusd_resp, "price")
btcusd_bid = get_json_value(btcusd_resp, "bid")
btcusd_ask = get_json_value(btcusd_resp, "ask")
btceur_price = get_json_value(btceur_resp, "price")
btceur_bid = get_json_value(btceur_resp, "bid")
btceur_ask = get_json_value(btceur_resp, "ask") 



print "==="
print "Ticker:"
print "BTC/USD: {} usd, highest bid: {} usd".format(btcusd_price, btcusd_bid)
print "BTC/EUR: {} eu, highest bid: {} eu".format(btceur_price, btceur_bid)
print "LTC/USD: {} usd, highest bid: {} usd".format(ltcusd_price, ltcusd_bid)
print "LTC/EUR: {} eu, highest bid: {} eu".format(ltceur_price, ltceur_bid)
print "LTC/BTC: {} btc, highest bid: {} btc".format(ltcbtc_price, ltcbtc_bid)
print "ETH/USD: {} usd, highest bid: {} usd".format(ethusd_price, ethusd_bid)
print "ETH/EUR: {} eu, , highest bid: {} eu".format(etheur_price, etheur_bid)
print "ETH/BTC: {} btc, highest bid: {} btc".format(ethbtc_price, ethbtc_bid)


ltc_fees = TRANSACTFEE_BTC + (TRANSACTFEE_LTC *2)
ltcusd_btcfirst_arb = (((EXAMPLE_ARB_BTC / ltcbtc_bid) * ltcusd_bid) / btcusd_bid) - ltc_fees
ltcusd_usdfirst_arb = (((EXAMPLE_ARB_BTC * btcusd_bid) / ltcusd_bid) * ltcbtc_bid) - ltc_fees
ltceur_btcfirst_arb = (((EXAMPLE_ARB_BTC / ltcbtc_bid) * ltceur_bid) / btceur_bid) - ltc_fees
ltceur_eurfirst_arb = (((EXAMPLE_ARB_BTC * btceur_bid) / ltceur_bid) * ltcbtc_bid) - ltc_fees
print "==="
print "LTC:"
print "USD native: {} usd [{} btc arb fees: {} btc/{} usd]".format(ltcusd_price, EXAMPLE_ARB_BTC, ltc_fees * EXAMPLE_ARB_BTC, ltc_fees * EXAMPLE_ARB_BTC * btcusd_price)
print "USD btc-first: {} usd [{} btc arbed: {}, arb profit: {} btc/{} usd]".format(ltcbtc_price * btcusd_price, EXAMPLE_ARB_BTC, ltcusd_btcfirst_arb, ltcusd_btcfirst_arb - EXAMPLE_ARB_BTC, (ltcusd_btcfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "USD usd-first: {} usd [{} btc arbed: {}, arb profit: {} btc/{} usd]".format(ltcbtc_price * btcusd_price, EXAMPLE_ARB_BTC, ltcusd_usdfirst_arb, ltcusd_usdfirst_arb - EXAMPLE_ARB_BTC, (ltcusd_usdfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "EUR btc-first: {} usd [{} btc arbed: {}, arb profit: {} btc/{} usd]".format(ltceur_price / btceur_price * btcusd_price, EXAMPLE_ARB_BTC, ltceur_btcfirst_arb, ltceur_btcfirst_arb- EXAMPLE_ARB_BTC, (ltceur_btcfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "EUR eur-first: {} usd [{} btc arbed: {}, arb profit: {} btc/{} usd]".format(ltceur_price / btceur_price * btcusd_price, EXAMPLE_ARB_BTC, ltceur_eurfirst_arb, ltceur_eurfirst_arb- EXAMPLE_ARB_BTC, (ltceur_eurfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)


eth_fees = TRANSACTFEE_BTC + (TRANSACTFEE_ETH *2)
ethusd_btcfirst_arb = (((EXAMPLE_ARB_BTC / ethbtc_bid) * ethusd_bid) / btcusd_bid) - eth_fees
ethusd_usdfirst_arb = (((EXAMPLE_ARB_BTC * btcusd_bid) / ethusd_bid) * ethbtc_bid) - eth_fees
etheur_btcfirst_arb = (((EXAMPLE_ARB_BTC / ethbtc_bid) * etheur_bid) / btceur_bid) - eth_fees
etheur_eurfirst_arb = (((EXAMPLE_ARB_BTC * btceur_bid) / etheur_bid) * ethbtc_bid) - eth_fees
print "==="
print "ETH:"
print "USD native: {} usd [{} btc arb fees: {} btc/{} usd]".format(ethusd_price, EXAMPLE_ARB_BTC, eth_fees * EXAMPLE_ARB_BTC, eth_fees * EXAMPLE_ARB_BTC * btcusd_price)
print "USD btc-first: {} usd [{} btc arbed: {}, profit: {} btc/{} usd]".format(ethbtc_price * btcusd_price, EXAMPLE_ARB_BTC, ethusd_btcfirst_arb, ethusd_btcfirst_arb - EXAMPLE_ARB_BTC, (ethusd_btcfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "USD usd-first: {} usd [{} btc arbed: {}, profit: {} btc/{} usd]".format(ethbtc_price * btcusd_price, EXAMPLE_ARB_BTC, ethusd_usdfirst_arb, ethusd_usdfirst_arb - EXAMPLE_ARB_BTC, (ethusd_usdfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "EUR btc-first: {} usd [{} btc arbed: {}, profit: {} btc/{} usd]".format((etheur_price / btceur_price) * btcusd_price, EXAMPLE_ARB_BTC, etheur_btcfirst_arb, etheur_btcfirst_arb - EXAMPLE_ARB_BTC, (etheur_btcfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
print "EUR eur-first: {} usd [{} btc arbed: {}, profit: {} btc/{} usd]".format((etheur_price / btceur_price) * btcusd_price, EXAMPLE_ARB_BTC, etheur_eurfirst_arb, etheur_eurfirst_arb - EXAMPLE_ARB_BTC, (etheur_eurfirst_arb - EXAMPLE_ARB_BTC) * btcusd_price)
