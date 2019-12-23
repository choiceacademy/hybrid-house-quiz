from turtle import *
t =  Turtle()
t.speed(50)
colors=['red', 'black', 'yellow', 'black']
t.color("black")
t.hideturtle()
t.begin_fill()
t.hideturtle()
bgcolor("black")
t.end_fill()
for x in range(100):
  t.color(colors[x % 4])
  t.pendown()
  t.write("GRYFFINDOR!",  align="center", font = ("Arial", "50" , "bold"))
