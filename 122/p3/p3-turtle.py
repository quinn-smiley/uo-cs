# CS 122 Fall 2025 Project 3
# Author: Quinn Smiley
# Credit: None
# Description: Provide your own description

import turtle

# Get access to and setup the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Fireworks Show")

# Get access to drawing capabilities
t = turtle.Turtle()
t.speed(0)           # fastest drawing
t.hideturtle()       # hide the turtle arrow

def draw_line(t, x, y, angle, length):
    t.pu()
    t.setx(x)
    t.sety(y)
    t.seth(angle)
    t.pd()
    t.fd(length)
    t.pu()

#draw_line(t, 50, 50, 0, 50)
#draw_line(t, -50, -50, 135, 75)
#draw_line(t, 100, -100, 270, 100)

"""The function takes an x value, y value, angle, and length to draw a line.

   The function first uses the t.pu() method to amke sure turtle starts the function without drawing anything yet. Then, it uses the t.setx() and t.sety() methods to indicate the point in which the line will start from. Then it uses the seth() method to show what angle the line will be at - only then can it have the t.pd() method start the drawing in turtle. Then, it uses the t.fd() method to indicate how long the line will be - therefore how long the pen should be down for. Then, it ends the line with an additional t.pu().

Args:
   t (Turtle): Drawing Turtle
   x (int/float): starting x location
   y (int/float): starting y location
   angle (int/float): angle at which the line will be at
   length (int/float): how long the line will be.


   Returns:
      None
"""

def draw_radial_lines(t, x, y, length, num_lines):
    angle_init = 360 / num_lines
    for line in range(num_lines):
        angle = line * angle_init
        draw_line(t, x, y, angle, length)
    
#draw_radial_lines(t, -50, -50, 10, 4)
#draw_radial_lines(t, -50, 50, 20, 8)
#draw_radial_lines(t, 50, -50, 40, 16)
#draw_radial_lines(t, 50, 50, 80, 20)

"""This function takes an x value, y value, length, and the number of lines to create radial lines. 

   The function first uses the variable angle_init to change how the parameter angle (required for the draw_line() function) will be used in this new function. Then, the function uses a loop to repeat the draw_line function in a radiating shape. 

   Args:
   t (Turtle): Drawing Turtle
   x (int/float): starting x location
   y (int/float): starting y location
   length (int/float): how long the line will be.
   num_lines (int/float): number of lines in radiation

   Returns:
      None
"""

def draw_radials_in_quadrants(t, length, num_lines):
    draw_radial_lines(t, 100, 100, length, num_lines)
    draw_radial_lines(t, -100, 100, length, num_lines)
    draw_radial_lines(t, -100, -100, length, num_lines)
    draw_radial_lines(t, 100, -100, length, num_lines) 

#draw_radials_in_quadrants(t, 25, 3)
#draw_radials_in_quadrants(t, 50, 9)

"""This function uses length and number of lines to repeat radial lines in each quadrant. 

   The function calls draw_radial_lines() four times - once for each quadrant. I chose to use 100 as the x and y just because it is a good amount of space to show between radiations. 

Args:
   t (Turtle): Drawing Turtle
   length (int/float): length of the line that radiates
   num_lines (int/float): the number of times the line radiates

   Returns:
      None
"""

#turtle.done()