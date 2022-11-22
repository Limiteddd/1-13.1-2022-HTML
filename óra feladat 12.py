import turtle
adam = turtle.Turtle()
ablak = turtle.Screen()
ablak.bgcolor('#90EE90')
adam=turtle.Pen()
adam.shape('turtle')
adam.color('blue')
adam.stamp()
move=30
for i in range(12):
    adam.penup()
    adam.forward(50)
    adam.pendown()
    adam.forward(25)
    adam.penup()
    adam.forward(15)
    adam.stamp()
    adam.home()
    adam.right(move)
    move = move + 30
    
