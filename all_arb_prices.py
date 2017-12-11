from apis import *
from time import sleep


EXAMPLE_ARB_BTC = 1


# Get GDAX Prices
gdax_ltcusd_resp = get_gdax_ticker("ltc-usd")
gdax_ltceur_resp = get_gdax_ticker("ltc-eur")
gdax_ltcbtc_resp = get_gdax_ticker("ltc-btc")
gdax_ethusd_resp = get_gdax_ticker("eth-usd")
gdax_etheur_resp = get_gdax_ticker("eth-eur")
gdax_ethbtc_resp = get_gdax_ticker("eth-btc")
sleep(1)
gdax_btcusd_resp = get_gdax_ticker("btc-usd")
gdax_btceur_resp = get_gdax_ticker("btc-eur")

# Get Poloniex Prices
bittrex_tickers = get_bittrex_tickers()

# Get Poloniex Prices
polo_tickers = get_polo_tickers()


# Extract GDAX Prices
gdax_ltcusd_price = get_gdax_json_value_float(gdax_ltcusd_resp, "price")
gdax_ltcusd_bid = get_gdax_json_value_float(gdax_ltcusd_resp, "bid")
gdax_ltceur_price = get_gdax_json_value_float(gdax_ltceur_resp, "price")
gdax_ltceur_bid = get_gdax_json_value_float(gdax_ltceur_resp, "bid")
gdax_ltcbtc_price = get_gdax_json_value_float(gdax_ltcbtc_resp, "price")
gdax_ltcbtc_bid = get_gdax_json_value_float(gdax_ltcbtc_resp, "bid")
gdax_ethusd_price = get_gdax_json_value_float(gdax_ethusd_resp, "price")
gdax_ethusd_bid = get_gdax_json_value_float(gdax_ethusd_resp, "bid")
gdax_etheur_price = get_gdax_json_value_float(gdax_etheur_resp, "price")
gdax_etheur_bid = get_gdax_json_value_float(gdax_etheur_resp, "bid")
gdax_ethbtc_price = get_gdax_json_value_float(gdax_ethbtc_resp, "price")
gdax_ethbtc_bid = get_gdax_json_value_float(gdax_ethbtc_resp, "bid")
gdax_btcusd_price = get_gdax_json_value_float(gdax_btcusd_resp, "price")
gdax_btcusd_bid = get_gdax_json_value_float(gdax_btcusd_resp, "bid")
gdax_btcusd_ask = get_gdax_json_value_float(gdax_btcusd_resp, "ask")
gdax_btceur_price = get_gdax_json_value_float(gdax_btceur_resp, "price")
gdax_btceur_bid = get_gdax_json_value_float(gdax_btceur_resp, "bid")

# Extract Bittrex Prices
bittrex_usdtbtc_price = get_bittrex_json_value_float(bittrex_tickers, "USDT-BTC", "Last")
bittrex_usdtbtc_bid = get_bittrex_json_value_float(bittrex_tickers, "USDT-BTC", "Bid")
bittrex_usdtltc_price = get_bittrex_json_value_float(bittrex_tickers, "USDT-LTC", "Last")
bittrex_usdtltc_bid = get_bittrex_json_value_float(bittrex_tickers, "USDT-LTC", "Bid")
bittrex_usdteth_price = get_bittrex_json_value_float(bittrex_tickers, "USDT-ETH", "Last")
bittrex_usdteth_bid = get_bittrex_json_value_float(bittrex_tickers, "USDT-ETH", "Bid")
bittrex_btcltc_price = get_bittrex_json_value_float(bittrex_tickers, "BTC-LTC", "Last")
bittrex_btcltc_bid = get_bittrex_json_value_float(bittrex_tickers, "BTC-LTC", "Bid")
bittrex_btceth_price = get_bittrex_json_value_float(bittrex_tickers, "BTC-ETH", "Last")
bittrex_btceth_bid = get_bittrex_json_value_float(bittrex_tickers, "BTC-ETH", "Bid")
                                            
# Extract Poloniex Prices
polo_usdtbtc_price = get_polo_json_value_float(polo_tickers, "USDT_BTC", "last")
polo_usdtbtc_bid = get_polo_json_value_float(polo_tickers, "USDT_BTC", "highestBid")
polo_usdtltc_price = get_polo_json_value_float(polo_tickers, "USDT_LTC", "last")
polo_usdtltc_bid = get_polo_json_value_float(polo_tickers, "USDT_LTC", "highestBid")
polo_usdteth_price = get_polo_json_value_float(polo_tickers, "USDT_ETH", "last")
polo_usdteth_bid = get_polo_json_value_float(polo_tickers, "USDT_ETH", "highestBid")
polo_btcltc_price = get_polo_json_value_float(polo_tickers, "BTC_LTC", "last")
polo_btcltc_bid = get_polo_json_value_float(polo_tickers, "BTC_LTC", "highestBid")
polo_btceth_price = get_polo_json_value_float(polo_tickers, "BTC_ETH", "last")
polo_btceth_bid = get_polo_json_value_float(polo_tickers, "BTC_ETH", "highestBid")


print "==="
print "Tickers:"
print "-"
print "BTC/USD:"
print "  GDAX - {} usd, highest bid: {} usd".format(gdax_btcusd_price, gdax_btcusd_bid)
print "  BTRX - {} usd, highest bid: {} usd, [last: {}%, bid: {}% diff vs GDAX]".format(bittrex_usdtbtc_price, bittrex_usdtbtc_bid, calc_perc(gdax_btcusd_price, bittrex_usdtbtc_price), calc_perc(gdax_btcusd_bid, bittrex_usdtbtc_bid))
print "  POLO - {} usd, highest bid: {} usd, [last: {}%, bid: {}% diff vs GDAX]".format(polo_usdtbtc_price, polo_usdtbtc_bid, calc_perc(gdax_btcusd_price, polo_usdtbtc_price), calc_perc(gdax_btcusd_bid, polo_usdtbtc_bid))
print "LTC/USD:"
print "  GDAX - {} usd, highest bid: {} usd".format(gdax_ltcusd_price, gdax_ltcusd_bid)
print "  BTRX - {} usd, highest bid: {} usd, [last: {}%, bid: {}% diff vs GDAX]".format(bittrex_usdtltc_price, bittrex_usdtltc_bid, calc_perc(gdax_ltcusd_price, bittrex_usdtltc_price), calc_perc(gdax_ltcusd_bid, bittrex_usdtltc_bid))
print "  POLO - {} usd, highest bid: {} usd, [last: {}%, bid: {}% diff vs GDAX]".format(polo_usdtltc_price, polo_usdtltc_bid, calc_perc(gdax_ltcusd_price, polo_usdtltc_price), calc_perc(gdax_ltcusd_bid, polo_usdtltc_bid))
print "LTC/BTC:"
print "  GDAX - {} btc, highest bid: {} btc".format(gdax_ltcbtc_price, gdax_ltcbtc_bid)
print "  BTRX - {} btc, highest bid: {} btc, [last: {}%, bid: {}% diff vs GDAX]".format(bittrex_btcltc_price, bittrex_btcltc_bid, calc_perc(gdax_ltcbtc_price, bittrex_btcltc_price), calc_perc(gdax_ltcbtc_bid, bittrex_btcltc_bid))
print "  POLO - {} btc, highest bid: {} btc, [last: {}%, bid: {}% diff vs GDAX]".format(polo_btcltc_price, polo_btcltc_bid, calc_perc(gdax_ltcbtc_price, polo_btcltc_price), calc_perc(gdax_ltcbtc_bid, polo_btcltc_bid))
print "ETH/USD:"
print "  GDAX - {} usd, highest bid: {} usd".format(gdax_ethusd_price, gdax_ethusd_bid)
print "  BTRX - {} usd, highest bid: {} usd, [last: {}%, bid: {}% diff vs GDAX]".format(bittrex_usdteth_price, bittrex_usdteth_bid, calc_perc(gdax_ethusd_price, bittrex_usdteth_price), calc_perc(gdax_ethusd_bid, bittrex_usdteth_bid))
print "  POLO - {} usd, highest bid: {} usd, [last: {}%, bid: {}% diff vs GDAX]".format(polo_usdteth_price, polo_usdteth_bid, calc_perc(gdax_ethusd_price, polo_usdteth_price), calc_perc(gdax_ethusd_bid, polo_usdteth_bid))
print "ETH/BTC:"
print "  GDAX - {} btc, highest bid: {} btc".format(gdax_ethbtc_price, gdax_ethbtc_bid)
print "  BTRX - {} btc, highest bid: {} btc, [last: {}%, bid: {}% diff vs GDAX]".format(bittrex_btceth_price, bittrex_btceth_bid, calc_perc(gdax_ethbtc_price, bittrex_btceth_price), calc_perc(gdax_ethbtc_bid, bittrex_btceth_bid))
print "  POLO - {} btc, highest bid: {} btc, [last: {}%, bid: {}% diff vs GDAX]".format(polo_btceth_price, polo_btceth_bid, calc_perc(gdax_ethbtc_price, polo_btceth_price), calc_perc(gdax_ethbtc_bid, polo_btceth_bid))
print "==="


#GDAX BTC/ETH to BITTREX ETH/BTC
gdax_btceth_bittrex_ethbtc_route_arb = (EXAMPLE_ARB_BTC / gdax_ethbtc_bid) * bittrex_btceth_bid
gdax_btceth_bittrex_ethbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_ETH + BITTREX_TRANSACT_FEE_TAKER) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btceth_bittrex_ethbtc_route_result = gdax_btceth_bittrex_ethbtc_route_arb - gdax_btceth_bittrex_ethbtc_route_fees
#GDAX BTC/ETH to POLO ETH/BTC 
gdax_btceth_polo_ethbtc_route_arb = (EXAMPLE_ARB_BTC / gdax_ethbtc_bid) * polo_btceth_bid
gdax_btceth_polo_ethbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_ETH + POLO_TRANSACT_FEE_TAKER) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btceth_polo_ethbtc_route_result = gdax_btceth_polo_ethbtc_route_arb - gdax_btceth_polo_ethbtc_route_fees
#GDAX BTC/ETH to BITTREX LTC/BTC
gdax_btcltc_bittrex_ltcbtc_route_arb = (EXAMPLE_ARB_BTC / gdax_ltcbtc_bid) * bittrex_btcltc_bid
gdax_btcltc_bittrex_ltcbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_LTC + BITTREX_TRANSACT_FEE_TAKER) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btcltc_bittrex_ltcbtc_route_result = gdax_btcltc_bittrex_ltcbtc_route_arb - gdax_btcltc_bittrex_ltcbtc_route_fees
#GDAX BTC/LTC to POLO LTC/BTC 
gdax_btcltc_polo_ltcbtc_route_arb = (EXAMPLE_ARB_BTC / gdax_ltcbtc_bid) * polo_btcltc_bid
gdax_btcltc_polo_ltcbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_LTC + POLO_TRANSACT_FEE_TAKER) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btcltc_polo_ltcbtc_route_result = gdax_btcltc_polo_ltcbtc_route_arb - gdax_btcltc_polo_ltcbtc_route_fees

print "==="
print "ARB Routes:"
print "-"
print "GDAX BTC Pairs:"
print "  GDAX BTC/ETH to BITTREX ETH/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btceth_bittrex_ethbtc_route_result, gdax_btceth_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceth_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/ETH to POLO ETH/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btceth_polo_ethbtc_route_result, gdax_btceth_polo_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceth_polo_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/LTC to BITTREX ETH/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btcltc_bittrex_ltcbtc_route_result, gdax_btcltc_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcltc_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/LTC to POLO ETH/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btcltc_polo_ltcbtc_route_result, gdax_btcltc_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcltc_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)


#GDAX BTC/USD -> ETH/USD to BITTREX ETH/BTC 
gdax_btcusd_ethusd_bittrex_ethbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btcusd_bid) / gdax_ethusd_bid) * bittrex_btceth_bid
gdax_btcusd_ethusd_bittrex_ethbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_ETH + BITTREX_TRANSACT_FEE_TAKER) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btcusd_ethusd_bittrex_ethbtc_route_result = gdax_btcusd_ethusd_bittrex_ethbtc_route_arb - gdax_btcusd_ethusd_bittrex_ethbtc_route_fees
#GDAX BTC/USD -> ETH/USD to POLO ETH/BTC 
gdax_btcusd_ethusd_polo_ethbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btcusd_bid) / gdax_ethusd_bid) * polo_btceth_bid
gdax_btcusd_ethusd_polo_ethbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_ETH + POLO_TRANSACT_FEE_TAKER) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btcusd_ethusd_polo_ethbtc_route_result = gdax_btcusd_ethusd_polo_ethbtc_route_arb - gdax_btcusd_ethusd_polo_ethbtc_route_fees
#GDAX BTC/USD -> LTC/USD to BITTREX LTC/BTC
gdax_btcusd_ltcusd_bittrex_ltcbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btcusd_bid) / gdax_ltcusd_bid) * bittrex_btcltc_bid
gdax_btcusd_ltcusd_bittrex_ltcbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_LTC + BITTREX_TRANSACT_FEE_TAKER) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btcusd_ltcusd_bittrex_ltcbtc_route_result = gdax_btcusd_ltcusd_bittrex_ltcbtc_route_arb - gdax_btcusd_ltcusd_bittrex_ltcbtc_route_fees
#GDAX BTC/USD -> LTC/USD to POLO LTC/BTC
gdax_btcusd_ltcusd_polo_ltcbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btcusd_bid) / gdax_ltcusd_bid) * polo_btcltc_bid
gdax_btcusd_ltcusd_polo_ltcbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_LTC + POLO_TRANSACT_FEE_TAKER) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btcusd_ltcusd_polo_ltcbtc_route_result = gdax_btcusd_ltcusd_polo_ltcbtc_route_arb - gdax_btcusd_ltcusd_polo_ltcbtc_route_fees

print "GDAX USD Pairs:"
print "  GDAX BTC/USD -> ETH/USD to BITTREX ETH/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btcusd_ethusd_bittrex_ethbtc_route_result, gdax_btcusd_ethusd_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcusd_ethusd_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/USD -> ETH/USD to POLO ETH/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btcusd_ethusd_polo_ethbtc_route_result, gdax_btcusd_ethusd_polo_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcusd_ethusd_polo_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/USD -> LTC/USD to BITTREX LTC/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btcusd_ltcusd_bittrex_ltcbtc_route_result, gdax_btcusd_ltcusd_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcusd_ltcusd_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/USD -> LTC/USD to POLO LTC/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btcusd_ltcusd_polo_ltcbtc_route_result, gdax_btcusd_ltcusd_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcusd_ltcusd_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)


#GDAX BTC/EUR -> ETH/EUR to BITTREX ETH/BTC 
gdax_btceur_etheur_bittrex_ethbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btceur_bid) / gdax_etheur_bid) * bittrex_btceth_bid
gdax_btceur_etheur_bittrex_ethbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_ETH + BITTREX_TRANSACT_FEE_TAKER) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btceur_etheur_bittrex_ethbtc_route_result = gdax_btceur_etheur_bittrex_ethbtc_route_arb - gdax_btceur_etheur_bittrex_ethbtc_route_fees
#GDAX BTC/EUR -> ETH/EUR to POLO ETH/BTC 
gdax_btceur_etheur_polo_ethbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btceur_bid) / gdax_etheur_bid) * polo_btceth_bid
gdax_btceur_etheur_polo_ethbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_ETH + POLO_TRANSACT_FEE_TAKER) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btceur_etheur_polo_ethbtc_route_result = gdax_btceur_etheur_polo_ethbtc_route_arb - gdax_btceur_etheur_polo_ethbtc_route_fees
#GDAX BTC/EUR -> LTC/EUR to BITTREX LTC/BTC
gdax_btceur_ltceur_bittrex_ltcbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btceur_bid) / gdax_ltceur_bid) * bittrex_btcltc_bid
gdax_btceur_ltceur_bittrex_ltcbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_LTC + BITTREX_TRANSACT_FEE_TAKER) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btceur_ltceur_bittrex_ltcbtc_route_result = gdax_btceur_ltceur_bittrex_ltcbtc_route_arb - gdax_btceur_ltceur_bittrex_ltcbtc_route_fees
#GDAX BTC/EUR -> LTC/EUR to POLO LTC/BTC
gdax_btceur_ltceur_polo_ltcbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btceur_bid) / gdax_ltceur_bid) * polo_btcltc_bid
gdax_btceur_ltceur_polo_ltcbtc_route_fees = (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_LTC + POLO_TRANSACT_FEE_TAKER) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btceur_ltceur_polo_ltcbtc_route_result = gdax_btceur_ltceur_polo_ltcbtc_route_arb - gdax_btceur_ltceur_polo_ltcbtc_route_fees

print "GDAX EUR Pairs:"
print "  GDAX BTC/EUR -> ETH/EUR to BITTREX ETH/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btceur_etheur_bittrex_ethbtc_route_result, gdax_btceur_etheur_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceur_etheur_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btceur_bid)
print "  GDAX BTC/EUR -> ETH/EUR to POLO ETH/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btceur_etheur_polo_ethbtc_route_result, gdax_btceur_etheur_polo_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceur_etheur_polo_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btceur_bid)
print "  GDAX BTC/EUR -> LTC/EUR to BITTREX LTC/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btceur_ltceur_bittrex_ltcbtc_route_result, gdax_btceur_ltceur_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceur_ltceur_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btceur_bid)
print "  GDAX BTC/EUR -> LTC/EUR to POLO LTC/BTC - [{} btc arbed: {}, profit: {} btc/{} usd]".format(EXAMPLE_ARB_BTC, gdax_btceur_ltceur_polo_ltcbtc_route_result, gdax_btceur_ltceur_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceur_ltceur_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btceur_bid)
print "==="
