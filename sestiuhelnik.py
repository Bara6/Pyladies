from turtle import forward, left, right, penup, pendown, exitonclick

for i in range(6):
    
    for j in range(6):
        forward(40)
        left(60)
    left(120)
    penup()
    forward(40)
    right(60)
    pendown()

exitonclick()

