# multi_task.py

# 思考两个任务函数能否同时执行
def task1():
    print(1)
    print(2)
    print(3)
    print(4)

def task2():
    print("A")
    print("B")
    print("C")
    print("D")

# 希望执行结果是: 1A2B3C4D
task1()
task2()