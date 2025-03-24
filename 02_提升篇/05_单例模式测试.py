class MusicPlayer4:
    # 创建类属性 记录第一个被创建对象的引用地址的
    isinstance = None

    # 创建类属性 记录是否执行过初始化动作
    init_flag = False

    # 重写new方法 分配空间
    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.isinstance is None:
            # 2. 调用父类方法分配空间
            cls.isinstance = super().__new__(cls)

        # 3. 返回类属性中记录的对象引用
        return cls.isinstance
    

player4_1 = MusicPlayer4()
print(player4_1)
player4_2 = MusicPlayer4()
print(player4_2)