import turtle
turtle.setup(400, 500)
wn = turtle.Screen()
wn.bgcolor('lightGreen')
ter = turtle.Turtle()

def draw_housing():
    ter.pensize(3)
    ter.color('black', 'darkGrey')
    ter.begin_fill()
    ter.forward(80)
    ter.left(90)
    ter.forward(200)
    ter.circle(40, 180)
    ter.forward(200)
    ter.left(90)
    ter.end_fill()
draw_housing()

ter.penup()
ter.forward(40)
ter.left(90)
ter.forward(50)
ter.shape('circle')
ter.shapesize(3)
ter.fillcolor('green')

sn = 0
def asm():
    global sn
    if sn == 0:
        wn.ontimer(asm, 2000)
        ter.forward(70)
        ter.fillcolor('orange')
        sn = 1
    elif sn == 1:
        wn.ontimer(asm, 3000)
        ter.forward(70)
        ter.fillcolor('green')
        sn = 2
    else:
        wn.ontimer(asm, 5000)
        ter.back(140)
        ter.fillcolor('red')
        sn = 0

asm()
wn.listen()
wn.mainloop()
