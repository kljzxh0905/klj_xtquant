
#coding:utf-8

def connect(path, session):
    from xtquant import xttrader

    trader = xttrader.XtQuantTrader(path, session)
    trader.start()

    connect_result = trader.connect()
    return trader if connect_result == 0 else None


def try_connect_range():
    # 随机 session_id 的待尝试列表
    # 100以内的id保留
    ids = [i for i in range(100, 200)]

    import random
    random.shuffle(ids)

    # 要连接到的对接路径
    path = r'userdata_mini'

    # 遍历id列表尝试连接
    for session_id in ids:
        print(f'尝试id:{session_id}')
        trader = connect(path, session_id)

        if trader:
            print('连接成功')
            return trader
        else:
            print('连接失败，继续尝试下一个id')
            continue

    # 所有id都尝试后仍失败，放弃连接
    raise Exception('XtQuantTrader 连接失败,请重试')


try:
    trader = try_connect_range()
except Exception as e:
    import traceback
    print(e, traceback.format_exc())


import time
while True:
    print('.', end = '')
    time.sleep(2)




