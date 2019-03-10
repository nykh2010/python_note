# function_embed_def.py

def fn_outter():
    def fn_inner():
        print("fn_inner被调用")

    return fn_inner

f = fn_outter()  # 打印结果是什么？
f()  # fn_inner被调用"

f2 = fn_outter()
f2() # fn_inner被调用


if f is f2:
    print("f和f2绑定是同一个函数")
else:
    print("f和f2绑定不是同一个函数")

print(id(f))
print(id(f2))