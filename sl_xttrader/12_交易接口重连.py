
#本文用一个均线策略演示交易连接断开时怎么处理交易接口重连
# 策略本身不严谨，不能作为实盘策略或者参考策略，本策略仅是演示重连用法
import time
from xtquant.xttrader import XtQuantTrader, XtQuantTraderCallback
from xtquant.xttype import StockAccount
from xtquant import xtconstant
from xtquant import xtdata


class MyXtQuantTraderCallback(XtQuantTraderCallback):
    # 更多说明见 http://dict.thinktrader.net/nativeApi/xttrader.html?id=I3DJ97#%E5%A7%94%E6%89%98xtorder
    def on_disconnected(self):
        """
        连接断开
        :return:
        """
        print("connection lost, 交易接口断开，即将重连")
        global xt_trader
        xt_trader = None
    
    def on_stock_order(self, order):
        print(f'委托回报: 股票代码:{order.stock_code} 账号:{order.account_id}, 订单编号:{order.order_id} 柜台合同编号:{order.order_sysid} \
            委托状态:{order.order_status} 成交数量:{order.order_status} 委托数量:{order.order_volume} 已成数量：{order.traded_volume}')
        
    def on_stock_trade(self, trade):
        print(f'成交回报: 股票代码:{trade.stock_code} 账号:{trade.account_id}, 订单编号:{trade.order_id} 柜台合同编号:{trade.order_sysid} \
            成交编号:{trade.traded_id} 成交数量:{trade.traded_volume} 委托数量:{trade.direction} ')

    def on_order_error(self, order_error):
        print(f"报单失败： 订单编号：{order_error.order_id} 下单失败具体信息:{order_error.error_msg} 委托备注:{order_error.order_remark}")

    def on_cancel_error(self, cancel_error):
        print(f"撤单失败: 订单编号：{cancel_error.order_id} 失败具体信息:{cancel_error.error_msg} 市场：{cancel_error.market}")

    def on_order_stock_async_response(self, response):
        print(f"异步下单的请求序号:{response.seq}, 订单编号：{response.order_id} ")

    def on_account_status(self, status):
        print(f"账号状态发生变化， 账号:{status.account_id} 最新状态：{status.status}")

def create_trader(xt_acc,path, session_id):
    trader = XtQuantTrader(path, session_id,callback=MyXtQuantTraderCallback())
    trader.start()
    connect_result = trader.connect()
    trader.subscribe(xt_acc)
    return trader if connect_result == 0 else None


def try_connect(xt_acc,path):
    session_id_range = [i for i in range(100, 120)]

    import random
    random.shuffle(session_id_range)

    # 遍历尝试session_id列表尝试连接
    for session_id in session_id_range:
        trader = create_trader(xt_acc,path, session_id)
        if trader:
            print('连接成功，session_id:{}', session_id)
            return trader
        else:
            print('连接失败，session_id:{}，继续尝试下一个id', session_id)
            continue

    print('所有id都尝试后仍失败，放弃连接')
    return None


def get_xttrader(xt_acc,path):
    global xt_trader
    if xt_trader is None:
        xt_trader = try_connect(xt_acc,path)
    return xt_trader


if __name__ == "__main__":

    # 注意实际连接XtQuantTrader时不要写类似while True 这种无限循环的尝试，因为每次连接都会用session_id创建一个对接文件，这样就会占满硬盘导致电脑运行异常
    # 要控制session_id在有限的范围内尝试，这里提供10个session_id供重连尝试
    # 当所有session_id都尝试后，程序会抛出异常。实际使用过程中当session_id用完时，可以增加邮件等通知方式提醒人工处理 

    #指定客户端所在路径
    path = 'E:\qmt\\userdata_mini'
    xt_trader = None
    xt_acc = StockAccount('2000204')
    xt_trader = get_xttrader(xt_acc,path)
    if not xt_trader:
        raise Exception('交易接口连接失败')
    print('交易接口连接成功， 策略开始')

    stock = '513050.SH'
    xtdata.subscribe_quote(stock, '5m','','',count=-1)
    time.sleep(1)
    order_record = []
    while '093000'<=time.strftime('%H%M%S')<'150000':
        time.sleep(3)
        xt_trader = get_xttrader(xt_acc,path)
        
        price = xtdata.get_market_data_ex(['close'],[stock],period='5m',)[stock]
        #计算均线
        ma5 = price['close'].rolling(5).mean()
        ma10 = price['close'].rolling(10).mean()

        if ma5.iloc[-1]>ma5.iloc[-10]:
            t = price.index[-1]
            order_flag = (t, '买')
            if order_flag not in order_record: #防止重复下单
                print(f'发起买入 {stock}  k线时间:{t}')
                
                # 用最新价买100股
                xt_trader.order_stock_async(xt_acc, stock, xtconstant.STOCK_BUY,100,xtconstant.LATEST_PRICE,0)
                order_record.append(order_flag)
        elif ma5.iloc[-1]<ma5[-10]:
            t = price.index[-1]
            order_flag = (t, '卖')
            if order_flag not in order_record: #防止重复下单
                print(f'发起卖出 {stock} k线时间:{t}')
                # 用最新价买100股
                xt_trader.order_stock_async(xt_acc, stock, xtconstant.STOCK_SELL,100,xtconstant.LATEST_PRICE,0)
                
                order_record.append(order_flag)


