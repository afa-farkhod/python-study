import turtle

s = turtle.Screen()
t = turtle.Turtle() # 'turtle' object

t.color("blue")
t.penup()
t.goto(-110, -25)
t.pendown()
t.circle(45)

t.color("black")
t.penup()
t.goto(0, -25)
t.pendown()
t.circle(45)

t.color("red")
t.penup()
t.goto(110, -25)
t.pendown()
t.circle(45)

t.color("brown")
t.penup()
t.goto(-55, -75)
t.pendown()
t.circle(45)

t.color("green")
t.penup()
t.goto(55, -75)
t.pendown()
t.circle(45)

s.mainloop()
