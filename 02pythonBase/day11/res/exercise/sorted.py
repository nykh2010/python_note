# 练习:
#   names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#   排序的依据是字符串的反序:
#            'moT'   'yrreJ'  'ekipS' 'ekyT'
#   结果:['Spike', 'Tyke', 'Tom', 'Jerry']


names = ['Tom', 'Jerry', 'Spike', 'Tyke']

def fkey(n):
    r = n[::-1]
    print("字符串", n, '的排序依据是:', r)
    return r

L = sorted(names, key=fkey)
print(L)

