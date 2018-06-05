#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import turtle
import time
import sys

def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)

def draw_gibbet(step):
    if step == 1:
        # вертикальная линия
        draw_line(-160, -100, -160, 80)
    elif step == 2:
        # горизонтальная линия
        draw_line(-160, 80, -80, 80)
    elif step == 3:
        # ребро жесткости
        draw_line(-160, 40, -120, 80)
    elif step == 4:
        # веревка
        draw_line(-100, 80, -100, 40)
    elif step == 5:
        # голова
        gotoxy(-100, 0)
        turtle.circle(20)
    elif step == 6:
        # туловище
        draw_line(-100, 0, -100, -50)
    elif step == 7:
        # левая рука
        draw_line(-100, -10, -120, -20)
    elif step == 8:
        # правая рука
        draw_line(-100, -10, -80, -20)
    elif step == 9:
        # левая нога
        draw_line(-100, -50, -120, -60)
    elif step == 10:
        # правая нога
        draw_line(-100, -50, -80, -60)

turtle.speed(0)
x = random.randint(1, 100)

print('Случайное число', x)



gotoxy(-200, 250)
turtle.write("Я загадал число от 1 до 100. \n Попробуй Угадать",
    font=('Arial', 18, 'normal'))

try_count = 0

answer = turtle.textinput('Давать подсказки?', 'Y/N')
hints = False

if answer == 'Y' or answer == 'y':
    hints = True

answer = turtle.textinput('Играть?', 'Y/N')

if answer == 'N' or answer == 'n':
    sys.exit()

while True:
    number = turtle.numinput('Попробуй угадать', 'Число', 0, 0, 100)
    gotoxy(200, 200 - try_count * 12)

    turtle.color('red')
    turtle.write(number)

    if hints:
        gotoxy(250, 200 - try_count * 12)
        if number < x:
            turtle.write('Загаданное число больше')
        elif number > x:
            turtle.write('Загаданное число меньше')

    if number == x:
        gotoxy(-150, 120)
        turtle.color('green')
        turtle.write('Ура', font = ('Arial', 26, 'normal'))
        break
    else:
        gotoxy(-150, 100)
        turtle.color('red')
        turtle.write('Неверно', font = ('Arial', 26, 'normal'))

        try_count += 1
        draw_gibbet(try_count)

        if try_count == 10:
            gotoxy(-150, -200)
            turtle.color('red')
            turtle.write('Вы проиграли!', font = ('Arial', 26, 'normal'))
            break
            
        
