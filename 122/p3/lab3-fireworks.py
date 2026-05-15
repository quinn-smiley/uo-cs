# CS 122 Fall 2025 Lab 3
# Author: Your Name
# Credit: (List any sources of help, or write 'None')
# Description: Fireworks program using loops and conditionals

import turtle     # Turtle graphics module
import random     # Support generating random numbers

# Get access to and setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Fireworks Show")

# Get access to drawing capabilities
t = turtle.Turtle()
t.speed(0)           # fastest drawing
t.hideturtle()       # hide the turtle arrow

# Add test code to draw a white line on the black background
#t.color("white")
#t.forward(100)
#t.color("white")
#for i in range(36):
    #t.forward(70)
    #t.backward(70)
    #t.right(10)

# Function to draw a single firework
def draw_burst (turt, x, y, size, color):
    """
    Draw a radial 'burst' using Turtle

    Parameters:
       turt: turtle.Turtle instance to draw with
       size: length of each burst line
       color: turtle color name
    """
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color(color)
    for i in range(36):       # 36 lines make a circle
        turt.forward(size)
        turt.backward(size)
        turt.right(10)        # 360 / 36 = 10 degrees

# Draw a firework burst
#draw_burst(t, 50, "white")
#draw_burst(t, 50, "red")
#draw_burst(t, 70, "blue")

def draw_star(turt, x, y, size, color):
    """
    Draw a 5-point path that looks like a star.
    """
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color(color)
    for i in range(5):
        turt.forward(size)
        turt.right(144)

# Draw a star
#draw_star(t, 80, "gold")

canvas = screen.getcanvas()

def get_random_x(canvas, size):
    width = canvas.winfo_width()
    return random.randint(-width//2 + size, width//2 - size)

def get_random_y(canvas, size):
    height = canvas.winfo_height()
    return random.randint(-height//2 + size, height//2 - size)

# x = get_random_x(canvas, 50)
# y = get_random_y(canvas, 50)
# draw_burst(t, x, y, 50, "white")
# x = get_random_x(canvas, 70)
# y = get_random_y(canvas, 70)
# draw_burst(t, x, y, 70, "red")
# x = get_random_x(canvas, 90)
# y = get_random_y(canvas, 90)
# draw_burst(t, x, y, 90, "blue")
# x = get_random_x(canvas, 120)
# y = get_random_y(canvas, 120)
# draw_star(t, x, y, 120, "gold")


def random_fireworks(t): 
     random_seq_f = random.randrange(1, 16)
     random_seq_s = random.randrange(1, 11)
     for num in range(random_seq_f):
         color = random.choice(["white", "red", "blue", "green", "yellow", "purple", "orange"])
         size = random.randrange(1, 151)
         draw_burst(t, get_random_x(canvas, size), get_random_y(canvas, size), size, color)
     for num in range(random_seq_s):
         color = random.choice(["white", "red", "blue", "green", "yellow", "purple", "orange"])
         size = random.randrange(1, 151)
         draw_star(t, get_random_x(canvas, size), get_random_y(canvas, size), size, color)

random_fireworks(t)
# Wait for the user to do something, 
# or simply close the Python graphical window
screen.mainloop()