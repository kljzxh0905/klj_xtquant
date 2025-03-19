
from xtquant import xtdata # 导入xtdata模块
import time # 导入time模块
# .startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
all_stock_code = ['600000', '000004', '600006', '300007', '600008', '688009', '300010', '002211', '003212', '600015']
stock_code = '600'
for code in all_stock_code:
    if code.startswith(stock_code):
        print(code)

# f"{}" 用于格式化字符串
price_list = [1.5126, 2.309, 3.547, 4.711233, 5.60999]
for price in price_list:
    print(f"{price:.2f}")

# {}.format() 用于格式化字符串
for price in price_list:
    print("{:.2f}".format(price))

# for i in code_list:
# i 是一个字符串，code_list 是一个列表，所以 i 会遍历 code_list 中的每一个元素

'''
C:\\Users\ttyrc33>netstat -ano | findstr :58609
  TCP    127.0.0.1:58609        0.0.0.0:0              LISTENING       21460

C:\\Users\ttyrc33>taskkill /PID 21460 /F
成功: 已终止 PID 为 21460 的进程。
'''
'''
# 检查当前状态
git status

# 添加所有更改的文件
git add .

# 提交更改
git commit -m "Initial commit"

# 添加远程仓库（如果还没有添加）
git remote add origin https://github.com/yourusername/yourrepository.git

# 推送到远程仓库
git push -u origin main'
'''
