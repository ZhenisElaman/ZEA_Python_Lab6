#!/usr/bin/env python3
# coding=utf-8

import turtle

def draw_circle(color, dir, radius, angle):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(dir)
    #turtle.goto(crX, crY)
    turtle.circle(radius, angle)
    turtle.end_fill()

draw_circle("#000000", 0, 50, 90)

#создаем круг поделенный на 2 цвета пополам
draw_circle("#ffffff", 0, 50, 180)
draw_circle("#000000",0, 50, 180)

#создание 2 дуг
draw_circle("#ffffff",0, 25, -180)
draw_circle("#000000",180, 25, 180)

# создание и расстановка кругов
turtle.goto(-32, 50)
draw_circle("#ffffff",0, 8, 360)
turtle.up()
turtle.goto(17, 50)
turtle.down()
draw_circle("#000000",0, 8, 360)
turtle.done()