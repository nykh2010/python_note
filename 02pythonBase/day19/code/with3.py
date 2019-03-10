# with3.py


class A:
    def __enter__(self):
        print('已进入with语句')
        # 通常做申请次源的工作,如打开文件等
        return self
    def __exit__(self, e_type, e_val, e_tb):
        '''
          e_type 用于绑定异常类型
          e_val 用于绑定异常对象
          e_tb 用于绑定追踪对象
        '''
        # 通常做释源的工作,如关闭文件等
        print("已离开with语句")
        # 如果调用__exit__时没有出现异常,则
        # e_type,e_val, e_tb 绑定 None
        print(e_type, e_val, e_tb)

# a = A()
with A() as a:
    print("with 语句内部的语句正在执行") 
    3 / 0

print("程序退出")

