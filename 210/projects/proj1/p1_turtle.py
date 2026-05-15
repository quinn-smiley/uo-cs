# CIS 210 Project 1 – Turtle
# Author: Quinn Smiley
# Credits: Google & 122 Projects
# Drawing a duck in turtle. 

import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Duck")

t = turtle.Turtle()
t.speed(0)
t.hideturtle() 

t.pencolor('white')

t.penup()
t.goto(-215, 222)
t.pendown()

def head(my_turtle, side): 
    my_turtle.pencolor('yellow')
    for i in range(4):
        my_turtle.forward(side)
        my_turtle.right(45)
        my_turtle.forward(50)
        my_turtle.right(45)


def beak(my_turtle):
    my_turtle.pencolor('orange')
    my_turtle.penup()
    my_turtle.goto(-325, 100)
    my_turtle.pendown()
    for i in range(2):
        my_turtle.forward(75)
        my_turtle.right(90)
        my_turtle.forward(40)
        my_turtle.right(90)
    my_turtle.right(90)
    my_turtle.penup()
    my_turtle.forward(60)
    my_turtle.right(-90)
    my_turtle.forward(25)
    my_turtle.pendown()
    for i in range(2):
        my_turtle.forward(50)
        my_turtle.left(90)
        my_turtle.forward(20)
        my_turtle.left(90)


def eye(my_turtle):
    my_turtle.pencolor('white')
    my_turtle.penup()
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(60)
    my_turtle.pendown()
    for i in range(2):
        my_turtle.forward(50)
        my_turtle.right(90)
        my_turtle.forward(40)
        my_turtle.right(90)
    my_turtle.pencolor('blue')
    my_turtle.right(90)
    my_turtle.forward(25)
    for i in range(3):
        my_turtle.left(90)
        my_turtle.forward(25)

def body(my_turtle):
    my_turtle.pencolor('yellow')
    my_turtle.penup()
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(20)
    my_turtle.pendown()
    my_turtle.right(90)
    my_turtle.forward(150)
    my_turtle.left(35)
    my_turtle.forward(90)
    my_turtle.left(55)
    my_turtle.forward(300)
    my_turtle.left(45)
    my_turtle.forward(100)
    my_turtle.left(25)
    my_turtle.forward(100)
    my_turtle.left(20)
    my_turtle.forward(150)
    my_turtle.left(90)
    my_turtle.forward(3)
    my_turtle.left(40)
    my_turtle.forward(50)
    my_turtle.right(10)
    my_turtle.forward(50)
    my_turtle.right(25)
    my_turtle.forward(50)
    my_turtle.right(5)
    my_turtle.forward(180)

def duck():
    head(t, 150)
    beak(t)
    eye(t)
    body(t)

duck()

turtle.getscreen().getcanvas().postscript(file='duck.ps')

turtle.done()