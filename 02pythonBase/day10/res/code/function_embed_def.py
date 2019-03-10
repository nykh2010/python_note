# function_embed_def.py

# 
def fn_outter():
    print("fn_outter被调用!")
    def fn_inner():
        print("fn_inner被调用")

    fn_inner()
    fn_inner()

    print("fn_outter调用结束")
    return fn_inner

f = fn_outter()  # 打印结果是什么？

f()  # 不能调用


