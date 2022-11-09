from turtle import forward, left, penup, pendown, exitonclick, shape

shape('turtle')

n = 9
mezera = 10

delka = 1
for i in range (10*n):
    delka = delka + (mezera/n)
    forward(delka)        
    left(360/n)

exitonclick()