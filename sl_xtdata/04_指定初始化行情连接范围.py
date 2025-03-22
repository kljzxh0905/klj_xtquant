if 1:
    from xtquant import xtdatacenter as xtdc

    ## 设置数据目录
    xtdc.set_data_home_dir('data')

    ## 设置token
    token = "你的token"
    xtdc.set_token(token)

    ## 限定行情站点的优选范围
    opt_list = [
        '115.231.218.73:55310',
        '115.231.218.79:55310',
        '42.228.16.210:55300',
        '42.228.16.211:55300',
        '36.99.48.20:55300',
        '36.99.48.21:55300',
    ]
    xtdc.set_allow_optmize_address(opt_list)

    ## 开启指定市场的K线全推
    xtdc.set_kline_mirror_markets(['SH', 'SZ', 'BJ'])

    ## 设置要初始化的市场列表
    init_markets = [
        'SH', 'SZ', 'BJ',
        #'DF', 'GF', 'IF', 'SF', 'ZF', 'INE',
        #'SHO', 'SZO',
    ]
    xtdc.set_init_markets(init_markets)

    ## 初始化xtdc模块
    xtdc.init(start_local_service = False)

    ## 监听端口 (58620, 58650)
    #xtdc.listen(port = 58620)
    listen_port = xtdc.listen(port = 58620)
    print('监听端口:', listen_port)

    #import code; code.interact(local = locals())


import xtquant.xtdata as xtdata

xtdata.connect(port = listen_port)



import code; code.interact(local = locals())




