# 1、假如你现在25周岁,每年365天,
# 计算你过了多少个星期天

# sundays = 25 * 365 // 7

# print("我一共过了",sundays,"个星期天")
# print("我一共过了%d个星期天" % sundays)



# 1、定义两个变量,name的值为 关羽, gongji 的值为
# 666,在终端输出：关羽的攻击力为666
# name = "关羽"
# gongji = 666
# print("%s的攻击力为%d" % (name,gongji))

# 2、定义3个变量,name,gongsi,salary,在终端输出：
#     ...入职..公司,薪资为...元！
# name = "小昭"
# gongsi = "光明顶"
# salary = 10000
# print("%s入职%s公司，薪资为%d元" % 
#      (name,gongsi,salary))

# 3、定义两个变量,computer,you,值分别为：石头 剪刀,在终端输出：
#     电脑出拳：石头 你的出拳：剪刀 你输了！

# computer = "石头"
# you = "剪刀"
# print("电脑出拳：%s 你的出拳：%s 你输了！" % 
#      (computer,you))

# 2、一个圆的半径为3cm,计算圆的周长和面积分别是多少？
#     半径为3cm的圆的周长为：？厘米
#     半径为3cm的圆的面积为：？平方厘米
r = 3
zc = 2 * 3.14 * r
mj = 3.14 * (r ** 2)
print("半径为3cm的圆的周长为:%s厘米" % zc)
print("半径为3cm的圆的面积为:%s平方厘米" % mj)

# 3、从凌晨0:0:0计时,到现在过了63320秒,请问现在是几时 几分 几秒
#     提示：// % 
h = 63320 // 3600 # 小时
m = 63320 % 3600 // 60 # 分钟
s = 63320 % 3600 % 60 # 秒
print("现在是%s时%s分%s秒" % (h,m,s))















