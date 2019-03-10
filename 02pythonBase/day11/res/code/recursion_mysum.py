# recursion_mysum.py


# 此函数用来求1 + 2 + 3 + 4 + .....+ n 的 和
# 100 + (99 + (98 + (97 + .... + (2 + 1))))

def mysum(n):
    if n == 1:
        return 1
    return n + mysum(n - 1)


s = mysum(100)
print(s)
