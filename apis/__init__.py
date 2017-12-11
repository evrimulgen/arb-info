from apis.bittrex_apis import *
from apis.coinbase_apis import *
from apis.poloniex_apis import *


def calc_perc(price_1, price_2):
    return ((price_1 / price_2) -1) * 100