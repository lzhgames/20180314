# -*- coding: utf-8 -*-
# __author__ = 'Lu'
# import turtle
# turtle.circle(10)
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(120)

import turtle
import time
from builtins import print

turtle.color("yellow")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.end_fill()
time.sleep(5)
pr