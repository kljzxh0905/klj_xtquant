from xtquant import xtdata
import time
import threading

# 设定一个标的列表
code_list = ["000001.SZ"]
# 设定获取数据的周期
period = "1d"

print("hello world")

# 下载标的行情数据
if 1:
    try:
        for i in code_list:
            xtdata.download_history_data(i, period=period, incrementally=True)  # 增量下载行情数据（开高低收,等等）到本地
        xtdata.download_financial_data(code_list)  # 下载财务数据到本地
        xtdata.download_sector_data()  # 下载板块数据到本地
    except Exception as e:
        print(f"数据下载过程中出现错误: {e}")
print("=" * 20)
# 读取本地历史行情数据
try:
    history_data = xtdata.get_market_data_ex([], code_list, period=period, count=-1)
    print(history_data)
    print("=" * 20)
except Exception as e:
    print(f"读取本地历史行情数据过程中出现错误: {e}")

# 如果需要盘中的实时行情，需要向服务器进行订阅后才能获取
# 订阅后，get_market_data函数于get_market_data_ex函数将会自动拼接本地历史行情与服务器实时行情

# 向服务器订阅数据
try:
    for i in code_list:
        xtdata.subscribe_quote(i, period=period, count=-1)  # 设置count = -1来取到当天所有实时行情
except Exception as e:
    print(f"订阅数据过程中出现错误: {e}")

# 等待订阅完成
time.sleep(1)

# 获取订阅后的行情
try:
    kline_data = xtdata.get_market_data_ex([], code_list, period=period)
    print(kline_data)
except Exception as e:
    print(f"获取订阅后的行情数据过程中出现错误: {e}")

# 获取订阅后的行情，并以固定间隔进行刷新,预期会循环打印10次
try:
    for i in range(10):
        kline_data = xtdata.get_market_data_ex([], code_list, period=period)
        print(kline_data)
        time.sleep(3)  # 三秒后再次获取行情
except Exception as e:
    print(f"获取订阅后的行情数据过程中出现错误: {e}")

# 如果不想用固定间隔触发，可以以用订阅后的回调来执行
# 这种模式下当订阅的callback回调函数将会异步的执行，每当订阅的标的tick发生变化更新，callback回调函数就会被调用一次
# 本地已有的数据不会触发callback

# 定义的回调函数
def f(data):
    try:
        code_list = list(data.keys())  # 获取到本次触发的标的代码
        kline_in_callabck = xtdata.get_market_data_ex([], code_list, period=period)  # 在回调中获取klines数据
        print(kline_in_callabck)
    except Exception as e:
        print(f"回调函数执行过程中出现错误: {e}")

try:
    for i in code_list:
        xtdata.subscribe_quote(i, period=period, count=-1, callback=f)  # 订阅时设定回调函数
except Exception as e:
    print(f"订阅数据过程中出现错误: {e}")

# 使用回调时，必须要同时使用xtdata.run()来阻塞程序，否则程序运行到最后一行就直接结束退出了。

print("开始运行xtdata.run()")

def run_xtdata():
    try:
        xtdata.run()
    except Exception as e:
        print(f"运行xtdata.run()过程中出现错误: {e}")

# 创建并启动一个线程来运行xtdata.run()

t = threading.Thread(target=run_xtdata)
t.start()

# 主线程继续执行其他代码
print("goodbye world")
# 等待子线程结束
t.join()
print("子线程已结束")