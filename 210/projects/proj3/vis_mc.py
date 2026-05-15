import math
import random
import turtle

drawing_t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Darts")

drawing_t.speed(0)
drawing_t.hideturtle() 
drawing_t.pencolor('white')

def screen():
    wn.setworldcoordinates(-2, -2, 2, 2)

    drawing_t.up()
    drawing_t.goto(-1.2, 0)
    drawing_t.down()
    drawing_t.goto(1.2, 0)

    drawing_t.up()
    drawing_t.goto(0, -1.2)
    drawing_t.down()
    drawing_t.goto(0, 1.2)

    drawing_t.up()
    drawing_t.goto(0, -1)
    drawing_t.setheading(0)
    drawing_t.pencolor('gray')
    drawing_t.down()
    drawing_t.circle(1)
    drawing_t.pencolor('white')
    drawing_t.up()

def mc_vis(num_darts: int) -> float:
    screen()
    in_circle = 0

    drawing_t.up()

    for _ in range(num_darts):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        d = math.sqrt((x**2) + (y**2))

        drawing_t.goto(x, y)

        if d <= 1: 
            in_circle = in_circle + 1
            drawing_t.color("blue")
        else: 
            drawing_t.color("red")
        
        drawing_t.dot()
    
    pi = in_circle / num_darts * 4
    wn.exitonclick()

    return pi


mc_vis(5)