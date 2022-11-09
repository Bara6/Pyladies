from turtle import forward, left, right, penup, pendown, exitonclick

penup()
left(90)
forward(180)
pendown()

delka = 40
for i in range (1, 19):
    for j in range (4):
        forward(delka)
        left(90)
    left(20)
#namaluje kytku

right(180)
forward(100)
left(90)

listek = 10
for m in range (1, 6):
    listek = listek + 5
    for k in range (2):    
        left(100)
        for l in range(1, 5):
            forward(listek)
            left(20)

    right(180)
   

    for k in range (2):     
        right(100)
        for l in range(1, 5):
            forward(listek)
            right(20)

    left(90)
    forward(80)
    left(90)

exitonclick()