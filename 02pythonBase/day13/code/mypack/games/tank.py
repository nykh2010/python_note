# mypack/games/tank.py

def play():
    print("正在玩坦克大战 ....")

def gameover():
    print("坦克大战游戏结束")
    # 绝对导入menu模块的内的show_menu
    from mypack.menu import show_menu
    show_menu()
    # 相对导入(使用. 位置)show_menu
    from ..menu import show_menu
    show_menu()
    # 相对导入 当前模块所在文件夹下的contra模块内的play
    # from .contra import play
    from ..games.contra import play
    from ...mypack.games.contra import play # 错误
    play()  # 正在玩魂斗罗....


print("坦克大战 模块被导入")
