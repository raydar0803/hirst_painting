# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import colorgram
# colors = colorgram.extract('hirst.jpg', 30)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
spot = [(239, 234, 226), (220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222),
        (203, 134, 157), (180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52), (213, 87, 61),
        (197, 85, 112), (208, 223, 231), (229, 199, 114), (57, 166, 135), (141, 33, 42), (8, 104, 80), (47, 158, 182),
        (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157), (126, 38, 34), (156, 210, 197), (32, 57, 78),
        (70, 41, 37), (25, 65, 56), (74, 37, 47), (32, 62, 111), (236, 171, 157), (126, 38, 34), (156, 210, 197),
        (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47)]
tim.pencolor("black")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
tim.speed("fastest")
number = 100
for _ in range(1, number + 1):
    tim.dot(20, random.choice(spot))
    tim.forward(50)
    if _ % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
