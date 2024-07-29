import turtle
def setup():
    """ Provide the config for the screen """
    turtle.title('Multiple Squares Animation')
    turtle.setup(400, 400, 300, 300)
    turtle.pencolor('red')
    turtle.fillcolor('yellow')
    turtle.hideturtle()
def draw_square(size, flag):
    """ Draw a square in the current direction """
    def help():
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
    if flag:
        turtle.begin_fill()
        help()
        turtle.end_fill()
    else: help()
setup()

flag = 1

for _ in range(0, 12):
    flag = 1 - flag
    draw_square(50, flag)
    # Rotate the starting direction
    turtle.right(120)
# Add this so that the window will close when clicked on
turtle.exitonclick()
