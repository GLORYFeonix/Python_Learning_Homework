import turtle


def drawanexample():
    # 初始化画布
    turtle.screensize(800, 1600)
    turtle.home()
    turtle.speed(7)
    # 画风车杆
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(5)
    turtle.right(90)
    turtle.goto(5, -500)
    turtle.right(90)
    turtle.forward(10)
    turtle.goto(-5, 0)
    turtle.goto(0, 0)
    turtle.end_fill()

    # 画风车的四分之一
    def drawapart(color):
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.forward(300)
        turtle.right(135)
        turtle.forward(212)
        turtle.right(45)
        turtle.forward(150)
        turtle.goto(0, 0)
        turtle.end_fill()
        return
    # 画风车
    turtle.pensize(5)
    drawapart("red")
    drawapart("green")
    turtle.right(90)
    drawapart("blue")
    drawapart("yellow")
    turtle.color("white", "white")
    turtle.begin_fill()
    # 随便画点
    turtle.penup()
    turtle.goto(30, 0)
    turtle.pendown()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.pencolor("gold")
    turtle.pensize(1)
    # 画个螺线
    for i in range(100):
        turtle.forward(0.1*i)
        turtle.right(20)
    turtle.mainloop()
    return


def w():
    turtle.forward(10)
    return


def a():
    turtle.left(30)
    return


def d():
    turtle.right(30)
    return


def drawbyyourself():
    sc = turtle.Screen()
    sc.setup(600, 600)
    # 用w向前ad左右
    turtle.onkey(w, 'w')
    turtle.onkey(a, 'a')
    turtle.onkey(d, 'd')

    turtle.listen()
    turtle.mainloop()
    return


# 选择所执行的函数
n = input("input '1' to draw by yourself, input '0' to draw by example: ")
if n == '1':
    drawbyyourself()
else:
    drawanexample()
