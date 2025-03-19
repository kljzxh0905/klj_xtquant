# 以卖出为例

import pandas as pd
import numpy as np
from xtquant import xtdata

to_do_trade_list = ["000016.SZ"]
tick = xtdata.get_full_tick(to_do_trade_list)


# 取买一价为对手价，若买一价为0，说明已经跌停，则取最新价
for i in tick:
    fix_price = tick[i]["bidPrice"][0] if tick[i]["bidPrice"][0] != 0 else tick[i]["lastPrice"]
    print(fix_price)
