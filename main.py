import turtle, math 

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color("green")
for i in range(0,628) :
    t = i/50.0

    # draw a flower
    k = 6 
    x = 100*math.cos(k*t)*math.cos(t)
    y = 100*math.cos(k*t)*math.sin(t)
        
    if(not math.isnan(y)) :
        pen.goto(x, y)
        pen.pendown()
