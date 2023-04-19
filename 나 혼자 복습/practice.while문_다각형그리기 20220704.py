#while문 다각형 그리기 연습문제

import turtle

t = turtle.Turtle()

shape = int(input('몇각형을 그릴건가요 >>> '))

i =0

while i <= shape:
    t.forward(150)
    t.right(360/shape)
    i = i + 1
