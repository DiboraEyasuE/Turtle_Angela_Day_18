from turtle  import Turtle
from turtle import Screen
from turtle import colormode
import random as rd

turtle = Turtle()
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("white")


turtleColor = colormode(255)
tim = Turtle()
color_list = [(198, 167, 27), (220, 232, 238), (241, 225, 231), (225, 214, 102), (156, 64, 117), (151, 87, 47), (109, 180, 207), (13, 107, 164), (198, 173, 110), (212, 72, 123), (239, 212, 4), (21, 133, 62), (189, 144, 182), (61, 41, 35), (154, 174, 160), (174, 25, 46), (7, 90, 50), (149, 32, 26), (17, 63, 141), (222, 57, 42), (220, 176, 171), (142, 206, 214), (59, 158, 69), (10, 69, 40), (44, 158, 205), (65, 67, 52), (168, 208, 192), (15, 54, 91)]

tim.speed("fastest")
tim.setheading(225)
tim.up()
tim.hideturtle()
tim.fd(300)
tim.setheading(0)

num_dots = 100
for dot_count in range (1,num_dots+1):
        tim.dot(20,rd.choice(color_list))
        tim.fd(50)
        if dot_count%10 == 0:
                tim.setheading(90)
                tim.fd(50)
                tim.setheading(180)
                tim.fd(500)
                tim.setheading(0)


screen.exitonclick()