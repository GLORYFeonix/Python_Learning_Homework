from tkinter import *
from PIL import Image, ImageTk
import random
import time

# 获得鼠标选中的位置（1-9）


def which(x, y):
    for i in po:
        if(x == int(i) % 3 and y == int(i)//3):
            return i


# 胜利判决事件（未完成胜利结果展示部分）
def win():
    win = 1  # 初始化win为1，若win一直为1则胜利
    for i in po:
        if int(i) != po[i][0]:  # 通过判断给win赋0
            win = 0
    if win == 1:
        # for i in range(1, 10):
        #     canvas.delete(i)
        # time.sleep(1)
        # w = ImageTk.PhotoImage(Image.open("GUI/png/win.jpg"))
        # id = canvas.create_image(450, 450, image=w)

        print("win!!!")
        # while(1):
        #     canvas.move(id, 1, 1)
        #     time.sleep(100)


# 交换两张图片的事件
def swap(a, b):
    # 移动两张图片
    canvas.moveto(po[a][1], int(b) % 3*300, int(b)//3*300)
    canvas.moveto(po[b][1], int(a) % 3*300, int(a)//3*300)
    # 更新字典
    temp = po[a]
    po[a] = po[b]
    po[b] = temp


# 鼠标移动事件
def move(event):
    # 更新鼠标位置信息
    global x, y, flag, a, b
    x = event.x
    y = event.y
    x = x//300
    y = y//300

    # 确认点击次数来确认是否已经选中一项，若没有则赋给a
    if flag == 0:
        flag = 1
        a = which(x, y)
        return
    # 若有则赋给b
    if flag == 1:
        flag = 0
        b = which(x, y)
        swap(a, b)
        win()   # 执行胜利判决事件
        return


flag = 0    # 通过flag的值来进行判定点击的次数，0为初始值，1为选中一个
a = 99  # 通过a，b来存储选中的目标，初始化为99以免占用
b = 99
root = Tk()
root.title("拼图游戏")
root.geometry("900x900")
canvas = Canvas(root, width=900, height=900)
canvas.pack()

List = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # 用来记录绘制的图片编号，其中1-9为初始的9张
# 九张图片的位置，以图片中心点为基准
lc = [[0, 0], [1, 0], [2, 0],
      [0, 1], [1, 1], [2, 1],
      [0, 2], [1, 2], [2, 2]]
# 绘制初始九张图
for i in range(0, 9):
    load = Image.open("Jigsaw puzzle/png/%s.jpg" % List[i])   # 打开图片
    exec('var{}= ImageTk.PhotoImage(load)'.format(i))  # 批量创建变量名，备用
    exec('List[i]=[var{},i]'.format(i))  # 将变量名存入数组

random.shuffle(List)  # 打乱图片顺序
po = {}  # 构建字典po来存储图片位置信息以及它的应该在的位置以及id key:position in all, 0:index, 1:id
for i in range(0, 9):
    id = canvas.create_image(i % 3*300+150, i//3*300 +
                             150, image=List[i][0])  # 生成图片
    List[i].append(id)  # 给数组加上一维，存储id
    exec('po[\'{}\']=List[i][1:3]'.format(i))   # 存入字典po
canvas.bind("<Button-1>", move)  # 点击左键，发生事件
root.mainloop()
