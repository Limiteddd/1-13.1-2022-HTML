import turtle
adam = turtle.Turtle()
adam.speed(10)
def draw_square(turtle, size):
    for i in range(4):
        adam.forward(size)
        adam.left(90)
        adam.speed(10)

if __name__ == "__main__":
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    adam = turtle.Turtle()
    adam.color("blue")
    adam.pensize(3)
    boxes = 20

    for _ in range(boxes):
        draw_square(adam, 200)
        adam.left(360 / boxes)

    wn.mainloop()