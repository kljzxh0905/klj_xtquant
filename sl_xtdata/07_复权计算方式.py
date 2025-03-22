#coding:utf-8

import numpy as np
import pandas as pd

from xtquant import xtdata

#def gen_divid_ratio(quote_datas, divid_datas):
#    drl = []
#    for qi in range(len(quote_datas)):
#        q = quote_datas.iloc[qi]
#        dr = 1.0
#        for di in range(len(divid_datas)):
#            d = divid_datas.iloc[di]
#            if d.name <= q.name:
#                dr *= d['dr']
#        drl.append(dr)
#    return pd.DataFrame(drl, index = quote_datas.index, columns = quote_datas.columns)

def gen_divid_ratio(quote_datas, divid_datas):
    drl = []
    dr = 1.0
    qi = 0
    qdl = len(quote_datas)
    di = 0
    ddl = len(divid_datas)
    while qi < qdl and di < ddl:
        qd = quote_datas.iloc[qi]
        dd = divid_datas.iloc[di]
        if qd.name >= dd.name:
            dr *= dd['dr']
            di += 1
        if qd.name <= dd.name:
            drl.append(dr)
            qi += 1
    while qi < qdl:
        drl.append(dr)
        qi += 1
    return pd.DataFrame(drl, index = quote_datas.index, columns = quote_datas.columns)

def process_forward_ratio(quote_datas, divid_datas):
    drl = gen_divid_ratio(quote_datas, divid_datas)
    drlf = drl / drl.iloc[-1]
    result = (quote_datas * drlf).apply(lambda x: round(x, 2))
    return result

def process_backward_ratio(quote_datas, divid_datas):
    drl = gen_divid_ratio(quote_datas, divid_datas)
    result = (quote_datas * drl).apply(lambda x: round(x, 2))
    return result

def process_forward(quote_datas1, divid_datas):
    quote_datas = quote_datas1.copy()
    def calc_front(v, d):
        return round(
            (v - d['interest'] + d['allotPrice'] * d['allotNum'])
            / (1 + d['allotNum'] + d['stockBonus'] + d['stockGift'])
            , 2
        )
    for qi in range(len(quote_datas)):
        q = quote_datas.iloc[qi]
        for di in range(len(divid_datas)):
            d = divid_datas.iloc[di]
            if d.name <= q.name:
                continue
            q.iloc[0] = calc_front(q.iloc[0], d)
    return quote_datas

def process_backward(quote_datas1, divid_datas):
    quote_datas = quote_datas1.copy()
    def calc_front(v, d):
        return round(
            (v * (1 + d['stockGift'] + d['stockBonus'] + d['allotNum'])
            + d['interest'] - d['allotNum'] * d['allotPrice'])
            , 2
        )
    for qi in range(len(quote_datas)):
        q = quote_datas.iloc[qi]
        for di in range(len(divid_datas)):
            d = divid_datas.iloc[di]
            if d.name > q.name:
                continue
            q.iloc[0] = calc_front(q.iloc[0], d)
    return quote_datas


#--------------------------------

s = '002594.SZ'

#xtdata.download_history_data(s, '1d', '20100101', '')

dd = xtdata.get_divid_factors(s)
print(dd)

#复权计算用于处理价格字段
field_list = ['open', 'high', 'low', 'close']
datas_ori = xtdata.get_market_data(field_list, [s], '1d', dividend_type = 'none')['close'].T
#print(datas_ori)

#等比前复权
datas_forward_ratio = process_forward_ratio(datas_ori, dd)
print('datas_forward_ratio', datas_forward_ratio)

#等比后复权
datas_backward_ratio = process_backward_ratio(datas_ori, dd)
print('datas_backward_ratio', datas_backward_ratio)

#前复权
datas_forward = process_forward(datas_ori, dd)
print('datas_forward', datas_forward)

#后复权
datas_backward = process_backward(datas_ori, dd)
print('datas_backward', datas_backward)



