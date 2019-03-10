# star_tuple_args.py


# 此示例示意星号元组形参的用法
def func(*args):
    print("实参个数是:", len(args))
    print("args =", args)


func(1, 2, 3)
func(1, 2, 3, 4, 'AAA', 'BBB', 3.14)
