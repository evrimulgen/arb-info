from apis import *
from time import sleep


EXAMPLE_ARB_BTC = 1


# Get GDAX Prices
gdax_ltcusd_resp = get_gdax_ticker("ltc-usd")
gdax_ltceur_resp = get_gdax_ticker("ltc-eur")
gdax_ltcbtc_resp = get_gdax_ticker("ltc-btc")
sleep(0.6)
gdax_ethusd_resp = get_gdax_ticker("eth-usd")
gdax_etheur_resp = get_gdax_ticker("eth-eur")
gdax_ethbtc_resp = get_gdax_ticker("eth-btc")
sleep(0.6)
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
bittrex_ethltc_price = get_bittrex_json_value_float(bittrex_tickers, "ETH-LTC", "Last")
bittrex_ethltc_bid = get_bittrex_json_value_float(bittrex_tickers, "ETH-LTC", "Bid")
                                            
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
print "  GDAX - {:.2f} usd, highest bid: {:.2f} usd".format(gdax_btcusd_price, gdax_btcusd_bid)
print "  BTRX - {:.2f} usd, highest bid: {:.2f} usd   - [last: {:.5f}%, bid: {:.5f}% diff vs GDAX]".format(bittrex_usdtbtc_price, bittrex_usdtbtc_bid, calc_perc(gdax_btcusd_price, bittrex_usdtbtc_price), calc_perc(gdax_btcusd_bid, bittrex_usdtbtc_bid))
print "  POLO - {:.2f} usd, highest bid: {:.2f} usd   - [last: {:.5f}%, bid: {:.5f}% diff vs GDAX]".format(polo_usdtbtc_price, polo_usdtbtc_bid, calc_perc(gdax_btcusd_price, polo_usdtbtc_price), calc_perc(gdax_btcusd_bid, polo_usdtbtc_bid))
print "LTC/USD:"
print "  GDAX - {:.2f} usd, highest bid: {:.2f} usd".format(gdax_ltcusd_price, gdax_ltcusd_bid)
print "  BTRX - {:.2f} usd, highest bid: {:.2f} usd       - [last: {:.5f}%, bid: {:.5f}% diff vs GDAX]".format(bittrex_usdtltc_price, bittrex_usdtltc_bid, calc_perc(gdax_ltcusd_price, bittrex_usdtltc_price), calc_perc(gdax_ltcusd_bid, bittrex_usdtltc_bid))
print "  POLO - {:.2f} usd, highest bid: {:.2f} usd       - [last: {:.5f}%, bid: {:.5f}% diff vs GDAX]".format(polo_usdtltc_price, polo_usdtltc_bid, calc_perc(gdax_ltcusd_price, polo_usdtltc_price), calc_perc(gdax_ltcusd_bid, polo_usdtltc_bid))
print "LTC/BTC:"
print "  GDAX - {:.5f} btc, highest bid: {:.5f} btc".format(gdax_ltcbtc_price, gdax_ltcbtc_bid)
print "  BTRX - {:.5f} btc, highest bid: {:.5f} btc     - [last: {:.5f}%, bid: {:.5f}% diff vs GDAX]".format(bittrex_btcltc_price, bittrex_btcltc_bid, calc_perc(gdax_ltcbtc_price, bittrex_btcltc_price), calc_perc(gdax_ltcbtc_bid, bittrex_btcltc_bid))
print "  POLO - {:.5f} btc, highest bid: {:.5f} btc     - [last: {:.5f}%, bid: {:.5f}% diff vs GDAX]".format(polo_btcltc_price, polo_btcltc_bid, calc_perc(gdax_ltcbtc_price, polo_btcltc_price), calc_perc(gdax_ltcbtc_bid, polo_btcltc_bid))
print "ETH/USD:"
print "  GDAX - {:.2f} usd, highest bid: {:.2f} usd".format(gdax_ethusd_price, gdax_ethusd_bid)
print "  BTRX - {:.2f} usd, highest bid: {:.2f} usd       - [last: {:.5f}%, bid: {:.5f}% diff vs GDAX]".format(bittrex_usdteth_price, bittrex_usdteth_bid, calc_perc(gdax_ethusd_price, bittrex_usdteth_price), calc_perc(gdax_ethusd_bid, bittrex_usdteth_bid))
print "  POLO - {:.2f} usd, highest bid: {:.2f} usd       - [last: {:.5f}%, bid: {:.5f}% diff vs GDAX]".format(polo_usdteth_price, polo_usdteth_bid, calc_perc(gdax_ethusd_price, polo_usdteth_price), calc_perc(gdax_ethusd_bid, polo_usdteth_bid))
print "ETH/BTC:"
print "  GDAX - {:.5f} btc, highest bid: {:.5f} btc".format(gdax_ethbtc_price, gdax_ethbtc_bid)
print "  BTRX - {:.5f} btc, highest bid: {:.5f} btc     - [last: {:.5f}%, bid: {:.5f}% diff vs GDAX]".format(bittrex_btceth_price, bittrex_btceth_bid, calc_perc(gdax_ethbtc_price, bittrex_btceth_price), calc_perc(gdax_ethbtc_bid, bittrex_btceth_bid))
print "  POLO - {:.5f} btc, highest bid: {:.5f} btc     - [last: {:.5f}%, bid: {:.5f}% diff vs GDAX]".format(polo_btceth_price, polo_btceth_bid, calc_perc(gdax_ethbtc_price, polo_btceth_price), calc_perc(gdax_ethbtc_bid, polo_btceth_bid))
print "==="                                                   


#GDAX BTC/LTC to BITTREX LTC/BTC
gdax_btcltc_bittrex_ltcbtc_route_arb = (EXAMPLE_ARB_BTC / bittrex_btcltc_bid) * gdax_ltcbtc_bid
gdax_btcltc_bittrex_ltcbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_LTC + BITTREX_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btcltc_bittrex_ltcbtc_route_result = gdax_btcltc_bittrex_ltcbtc_route_arb - gdax_btcltc_bittrex_ltcbtc_route_fees
#GDAX BTC/LTC to POLO LTC/BTC 
gdax_btcltc_polo_ltcbtc_route_arb = (EXAMPLE_ARB_BTC / polo_btcltc_bid) * gdax_ltcbtc_bid
gdax_btcltc_polo_ltcbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_LTC + POLO_TRANSACT_FEE_TAKER)) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btcltc_polo_ltcbtc_route_result = gdax_btcltc_polo_ltcbtc_route_arb - gdax_btcltc_polo_ltcbtc_route_fees

print "==="
print "ARB Routes:"
print "-"
print "GDAX LTC Native Pairs:"
print "  GDAX LTC/BTC --BTC--> BITTREX BTC/LTC            - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btcltc_bittrex_ltcbtc_route_result, gdax_btcltc_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcltc_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX LTC/BTC --BTC--> POLO BTC/LTC               - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btcltc_polo_ltcbtc_route_result, gdax_btcltc_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcltc_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)


#GDAX BTC/ETH to BITTREX ETH/BTC
gdax_btceth_bittrex_ethbtc_route_arb = (EXAMPLE_ARB_BTC / bittrex_btceth_bid) * gdax_ethbtc_bid
gdax_btceth_bittrex_ethbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_ETH + BITTREX_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btceth_bittrex_ethbtc_route_result = gdax_btceth_bittrex_ethbtc_route_arb - gdax_btceth_bittrex_ethbtc_route_fees
#GDAX BTC/ETH to POLO ETH/BTC 
gdax_btceth_polo_ethbtc_route_arb = (EXAMPLE_ARB_BTC / polo_btceth_bid) * gdax_ethbtc_bid
gdax_btceth_polo_ethbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_ETH + POLO_TRANSACT_FEE_TAKER)) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btceth_polo_ethbtc_route_result = gdax_btceth_polo_ethbtc_route_arb - gdax_btceth_polo_ethbtc_route_fees

print "GDAX ETH Native Pairs:"
print "  GDAX ETH/BTC --BTC--> BITTREX BTC/ETH            - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btceth_bittrex_ethbtc_route_result, gdax_btceth_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceth_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX ETH/BTC --BTC--> POLO BTC/ETH               - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btceth_polo_ethbtc_route_result, gdax_btceth_polo_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceth_polo_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)


#GDAX LTC/BTC -> BTC/ETH --ETH--> BITTREX ETH/LTC
gdax_ltcbtc_ethltc_bittrex_ethltc_route_arb = ((((EXAMPLE_ARB_BTC / polo_btcltc_bid) * gdax_ltcbtc_bid) / gdax_ethbtc_bid) / bittrex_ethltc_bid) * polo_btcltc_bid
gdax_ltcbtc_ethltc_bittrex_ethltc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_LTC + COINBASE_TRANSACT_FEE_TAKER_ETH + BITTREX_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_LTC_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_ltcbtc_ethltc_bittrex_ethltc_route_result = gdax_ltcbtc_ethltc_bittrex_ethltc_route_arb - gdax_ltcbtc_ethltc_bittrex_ethltc_route_fees
#GDAX ETH/BTC -> BTC/LTC --LTC--> BITTREX ETH/LTC
gdax_ltcbtc_ethltc_polo_ethltc_route_arb = ((((EXAMPLE_ARB_BTC / polo_btceth_bid) * gdax_ethbtc_bid) / gdax_ltcbtc_bid) * bittrex_ethltc_bid) * polo_btceth_bid
gdax_ltcbtc_ethltc_polo_ethltc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_ETH + COINBASE_TRANSACT_FEE_TAKER_LTC + POLO_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_ETH_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_ltcbtc_ethltc_polo_ethltc_route_result = gdax_ltcbtc_ethltc_polo_ethltc_route_arb - gdax_ltcbtc_ethltc_polo_ethltc_route_fees

print "GDAX LTC-BTC and ETH-BTC Pairs:"
print "  GDAX LTC/BTC -> BTC/ETH --ETH--> BITTREX ETH/LTC - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_ltcbtc_ethltc_bittrex_ethltc_route_result, gdax_ltcbtc_ethltc_bittrex_ethltc_route_result - EXAMPLE_ARB_BTC, (gdax_ltcbtc_ethltc_bittrex_ethltc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX ETH/BTC -> BTC/LTC --LTC--> BITTREX ETH/LTC - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_ltcbtc_ethltc_polo_ethltc_route_result, gdax_ltcbtc_ethltc_polo_ethltc_route_result - EXAMPLE_ARB_BTC, (gdax_ltcbtc_ethltc_polo_ethltc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)


#GDAX LTC/USD -> USD/ETH --ETH--> BITTREX ETH/LTC
gdax_ltcusd_usdeth_bittrex_ethltc_route_arb = ((((EXAMPLE_ARB_BTC / gdax_ltcbtc_bid) * gdax_ltcusd_bid) / gdax_ethusd_bid) / bittrex_ethltc_bid) * gdax_ltcbtc_bid
gdax_ltcusd_usdeth_bittrex_ethltc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_LTC + COINBASE_TRANSACT_FEE_TAKER_ETH + BITTREX_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_LTC_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_ltcusd_usdeth_bittrex_ethltc_route_result = gdax_ltcusd_usdeth_bittrex_ethltc_route_arb - gdax_ltcusd_usdeth_bittrex_ethltc_route_fees
#GDAX LTC/EUR -> EUR/ETH --LTC--> BITTREX ETH/LTC
gdax_ltceur_eureth_bittrex_ethltc_route_arb = ((((EXAMPLE_ARB_BTC / gdax_ltcbtc_bid) * gdax_ltceur_bid) / gdax_etheur_bid) / bittrex_ethltc_bid) * gdax_ltcbtc_bid
gdax_ltceur_eureth_bittrex_ethltc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_ETH + COINBASE_TRANSACT_FEE_TAKER_LTC + POLO_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_ETH_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_ltceur_eureth_bittrex_ethltc_route_result = gdax_ltceur_eureth_bittrex_ethltc_route_arb - gdax_ltceur_eureth_bittrex_ethltc_route_fees
#GDAX ETH/USD -> USD/LTC --LTC--> BITTREX LTC/ETH
gdax_ethusd_usdltc_bittrex_ethltc_route_arb = ((((EXAMPLE_ARB_BTC / gdax_ethbtc_bid) * gdax_ethusd_bid) / gdax_ltcusd_bid) * bittrex_ethltc_bid) * gdax_ethbtc_bid
gdax_ethusd_usdltc_bittrex_ethltc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_LTC + COINBASE_TRANSACT_FEE_TAKER_ETH + BITTREX_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_LTC_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_ethusd_usdltc_bittrex_ethltc_route_result = gdax_ethusd_usdltc_bittrex_ethltc_route_arb - gdax_ethusd_usdltc_bittrex_ethltc_route_fees
#GDAX ETH/EUR -> EUR/LTC --LTC--> BITTREX LTC/ETH
gdax_etheur_eurltc_bittrex_ethltc_route_arb = ((((EXAMPLE_ARB_BTC / gdax_ethbtc_bid) * gdax_etheur_bid) / gdax_ltceur_bid) * bittrex_ethltc_bid) * gdax_ethbtc_bid
gdax_etheur_eurltc_bittrex_ethltc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_ETH + COINBASE_TRANSACT_FEE_TAKER_LTC + POLO_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_ETH_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_etheur_eurltc_bittrex_ethltc_route_result = gdax_etheur_eurltc_bittrex_ethltc_route_arb - gdax_etheur_eurltc_bittrex_ethltc_route_fees

print "GDAX LTC-FIAT and ETH-FIAT Pairs:"
print "  GDAX LTC/USD -> USD/ETH --ETH--> BITTREX ETH/LTC - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_ltcusd_usdeth_bittrex_ethltc_route_result, gdax_ltcusd_usdeth_bittrex_ethltc_route_result - EXAMPLE_ARB_BTC, (gdax_ltcusd_usdeth_bittrex_ethltc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX LTC/EUR -> EUR/ETH --ETH--> BITTREX ETH/LTC - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_ltceur_eureth_bittrex_ethltc_route_result, gdax_ltceur_eureth_bittrex_ethltc_route_result - EXAMPLE_ARB_BTC, (gdax_ltceur_eureth_bittrex_ethltc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX ETH/USD -> USD/LTC --LTC--> BITTREX LTC/ETH - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_ethusd_usdltc_bittrex_ethltc_route_result, gdax_ethusd_usdltc_bittrex_ethltc_route_result - EXAMPLE_ARB_BTC, (gdax_ethusd_usdltc_bittrex_ethltc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX ETH/EUR -> EUR/LTC --LTC--> BITTREX LTC/ETH - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_etheur_eurltc_bittrex_ethltc_route_result, gdax_etheur_eurltc_bittrex_ethltc_route_result - EXAMPLE_ARB_BTC, (gdax_etheur_eurltc_bittrex_ethltc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)


#GDAX BTC/ETH to BITTREX ETH/BTC
gdax_btceth_bittrex_ethbtc_route_arb = (EXAMPLE_ARB_BTC / gdax_ethbtc_bid) * bittrex_btceth_bid
gdax_btceth_bittrex_ethbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_ETH + BITTREX_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btceth_bittrex_ethbtc_route_result = gdax_btceth_bittrex_ethbtc_route_arb - gdax_btceth_bittrex_ethbtc_route_fees
#GDAX BTC/ETH to POLO ETH/BTC 
gdax_btceth_polo_ethbtc_route_arb = (EXAMPLE_ARB_BTC / gdax_ethbtc_bid) * polo_btceth_bid
gdax_btceth_polo_ethbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_ETH + POLO_TRANSACT_FEE_TAKER)) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btceth_polo_ethbtc_route_result = gdax_btceth_polo_ethbtc_route_arb - gdax_btceth_polo_ethbtc_route_fees
#GDAX BTC/LTC to BITTREX LTC/BTC
gdax_btcltc_bittrex_ltcbtc_route_arb = (EXAMPLE_ARB_BTC / gdax_ltcbtc_bid) * bittrex_btcltc_bid
gdax_btcltc_bittrex_ltcbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_LTC + BITTREX_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btcltc_bittrex_ltcbtc_route_result = gdax_btcltc_bittrex_ltcbtc_route_arb - gdax_btcltc_bittrex_ltcbtc_route_fees
#GDAX BTC/LTC to POLO LTC/BTC 
gdax_btcltc_polo_ltcbtc_route_arb = (EXAMPLE_ARB_BTC / gdax_ltcbtc_bid) * polo_btcltc_bid
gdax_btcltc_polo_ltcbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_LTC + POLO_TRANSACT_FEE_TAKER)) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btcltc_polo_ltcbtc_route_result = gdax_btcltc_polo_ltcbtc_route_arb - gdax_btcltc_polo_ltcbtc_route_fees

print "GDAX BTC Native Pairs:"
print "  GDAX BTC/ETH --ETH--> BITTREX ETH/BTC            - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btceth_bittrex_ethbtc_route_result, gdax_btceth_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceth_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/ETH --ETH--> POLO ETH/BTC               - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btceth_polo_ethbtc_route_result, gdax_btceth_polo_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceth_polo_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/LTC --LTC--> BITTREX LTC/BTC            - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btcltc_bittrex_ltcbtc_route_result, gdax_btcltc_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcltc_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/LTC --LTC--> POLO LTC/BTC               - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btcltc_polo_ltcbtc_route_result, gdax_btcltc_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcltc_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)


#GDAX BTC/USD -> USD/ETH --ETH--> BITTREX ETH/BTC
gdax_btcusd_ethusd_bittrex_ethbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btcusd_bid) / gdax_ethusd_bid) * bittrex_btceth_bid
gdax_btcusd_ethusd_bittrex_ethbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_ETH + BITTREX_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btcusd_ethusd_bittrex_ethbtc_route_result = gdax_btcusd_ethusd_bittrex_ethbtc_route_arb - gdax_btcusd_ethusd_bittrex_ethbtc_route_fees
#GDAX BTC/USD -> USD/ETH --ETH--> POLO ETH/BTC
gdax_btcusd_ethusd_polo_ethbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btcusd_bid) / gdax_ethusd_bid) * polo_btceth_bid
gdax_btcusd_ethusd_polo_ethbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_ETH + POLO_TRANSACT_FEE_TAKER)) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btcusd_ethusd_polo_ethbtc_route_result = gdax_btcusd_ethusd_polo_ethbtc_route_arb - gdax_btcusd_ethusd_polo_ethbtc_route_fees
#GDAX BTC/USD -> USD/LTC --LTC--> BITTREX LTC/BTC
gdax_btcusd_ltcusd_bittrex_ltcbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btcusd_bid) / gdax_ltcusd_bid) * bittrex_btcltc_bid
gdax_btcusd_ltcusd_bittrex_ltcbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_LTC + BITTREX_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btcusd_ltcusd_bittrex_ltcbtc_route_result = gdax_btcusd_ltcusd_bittrex_ltcbtc_route_arb - gdax_btcusd_ltcusd_bittrex_ltcbtc_route_fees
#GDAX BTC/USD -> USD/LTC --LTC--> POLO LTC/BTC
gdax_btcusd_ltcusd_polo_ltcbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btcusd_bid) / gdax_ltcusd_bid) * polo_btcltc_bid
gdax_btcusd_ltcusd_polo_ltcbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_LTC + POLO_TRANSACT_FEE_TAKER)) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btcusd_ltcusd_polo_ltcbtc_route_result = gdax_btcusd_ltcusd_polo_ltcbtc_route_arb - gdax_btcusd_ltcusd_polo_ltcbtc_route_fees

print "GDAX BTC-USD Pairs:"
print "  GDAX BTC/USD -> USD/ETH --ETH--> BITTREX ETH/BTC - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btcusd_ethusd_bittrex_ethbtc_route_result, gdax_btcusd_ethusd_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcusd_ethusd_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/USD -> USD/ETH --ETH--> POLO ETH/BTC    - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btcusd_ethusd_polo_ethbtc_route_result, gdax_btcusd_ethusd_polo_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcusd_ethusd_polo_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/USD -> USD/LTC --LTC--> BITTREX LTC/BTC - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btcusd_ltcusd_bittrex_ltcbtc_route_result, gdax_btcusd_ltcusd_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcusd_ltcusd_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)
print "  GDAX BTC/USD -> USD/LTC --LTC--> POLO LTC/BTC    - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btcusd_ltcusd_polo_ltcbtc_route_result, gdax_btcusd_ltcusd_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btcusd_ltcusd_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btcusd_bid)


#GDAX BTC/EUR -> EUR/ETH --ETH--> BITTREX ETH/BTC
gdax_btceur_etheur_bittrex_ethbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btceur_bid) / gdax_etheur_bid) * bittrex_btceth_bid
gdax_btceur_etheur_bittrex_ethbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_ETH + BITTREX_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btceur_etheur_bittrex_ethbtc_route_result = gdax_btceur_etheur_bittrex_ethbtc_route_arb - gdax_btceur_etheur_bittrex_ethbtc_route_fees
#GDAX BTC/EUR -> EUR/ETH --ETH--> POLO ETH/BTC
gdax_btceur_etheur_polo_ethbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btceur_bid) / gdax_etheur_bid) * polo_btceth_bid
gdax_btceur_etheur_polo_ethbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_ETH + POLO_TRANSACT_FEE_TAKER)) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_ETH_BTC
gdax_btceur_etheur_polo_ethbtc_route_result = gdax_btceur_etheur_polo_ethbtc_route_arb - gdax_btceur_etheur_polo_ethbtc_route_fees
#GDAX BTC/EUR -> EUR/LTC --LTC--> BITTREX LTC/BTC
gdax_btceur_ltceur_bittrex_ltcbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btceur_bid) / gdax_ltceur_bid) * bittrex_btcltc_bid
gdax_btceur_ltceur_bittrex_ltcbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_LTC + BITTREX_TRANSACT_FEE_TAKER)) \
    + BITTREX_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btceur_ltceur_bittrex_ltcbtc_route_result = gdax_btceur_ltceur_bittrex_ltcbtc_route_arb - gdax_btceur_ltceur_bittrex_ltcbtc_route_fees
#GDAX BTC/EUR -> EUR/LTC --LTC--> POLO LTC/BTC
gdax_btceur_ltceur_polo_ltcbtc_route_arb = ((EXAMPLE_ARB_BTC * gdax_btceur_bid) / gdax_ltceur_bid) * polo_btcltc_bid
gdax_btceur_ltceur_polo_ltcbtc_route_fees = (EXAMPLE_ARB_BTC * (COINBASE_TRANSACT_FEE_TAKER_BTC + COINBASE_TRANSACT_FEE_TAKER_LTC + POLO_TRANSACT_FEE_TAKER)) \
    + POLO_WITHDRAWAL_FEE_BTC + COINBASE_WITHDRAWAL_FEE_LTC_BTC
gdax_btceur_ltceur_polo_ltcbtc_route_result = gdax_btceur_ltceur_polo_ltcbtc_route_arb - gdax_btceur_ltceur_polo_ltcbtc_route_fees

print "GDAX BTC-EUR Pairs:"
print "  GDAX BTC/EUR -> EUR/ETH --ETH--> BITTREX ETH/BTC - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btceur_etheur_bittrex_ethbtc_route_result, gdax_btceur_etheur_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceur_etheur_bittrex_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btceur_bid)
print "  GDAX BTC/EUR -> EUR/ETH --ETH--> POLO ETH/BTC    - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btceur_etheur_polo_ethbtc_route_result, gdax_btceur_etheur_polo_ethbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceur_etheur_polo_ethbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btceur_bid)
print "  GDAX BTC/EUR -> EUR/LTC --LTC--> BITTREX LTC/BTC - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btceur_ltceur_bittrex_ltcbtc_route_result, gdax_btceur_ltceur_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceur_ltceur_bittrex_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btceur_bid)
print "  GDAX BTC/EUR -> EUR/LTC --LTC--> POLO LTC/BTC    - [{} btc arbed: {:.5f}, profit: {:.5f} btc / {:.2f} usd]".format(EXAMPLE_ARB_BTC, gdax_btceur_ltceur_polo_ltcbtc_route_result, gdax_btceur_ltceur_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC, (gdax_btceur_ltceur_polo_ltcbtc_route_result - EXAMPLE_ARB_BTC) * gdax_btceur_bid)
print "==="
