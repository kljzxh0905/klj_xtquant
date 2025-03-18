
import time
from xtquant import xtdata

#用token方式连接，不需要账号密码
#其他连接方式，需要账号密码
info = {"ip": '115.231.218.73', "port": 55300, "username": '', "pwd": ''}

connect_success = 0
def func(d):
    ip = d.get('ip', '')
    port = d.get('port')
    status = d.get('status', 'disconnected')

    global connect_success
    if ip == info['ip'] and port == info['port']:
        if status == 'connected':
            connect_success = 1
        else:
            connect_success = 2

# 注册连接回调信息
xtdata.watch_quote_server_status(func)

# 行情连接
qs = xtdata.QuoteServer(info)
qs.connect()

# 获取当前数据连接站点
data_server_info = xtdata.get_quote_server_status()
# 显示当前数据连接站点
if 1:
    for k,v in data_server_info.items():
        print(f"data:{k}, connect info:{v.info}")


# 等待连接状态
while connect_success == 0:
    time.sleep(0.3)

if connect_success == 2:
    print("连接失败")

