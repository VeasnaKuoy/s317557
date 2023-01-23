###############

# Student Name: Veasna Kuoy s317557
# Student Name: Ryan Mu s301219

###############

import turtle              # 1. import the modules
import random
import time

wn = turtle.Screen()       # 2. Create a screen
wn.setup(width = 420, height = 420, startx = 0, starty = 0)
turtle1 = turtle.Turtle()    # 3. Create 4 turtles
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtle4 = turtle.Turtle()
landscape = turtle.Turtle()

turtle1.ht()
turtle2.ht()
turtle3.ht()
turtle4.ht()

#Road setup
landscape.speed(3)
landscape.pensize(3)
landscape.ht()       
landscape.up()
landscape.setpos(-200,-200)
landscape.down()
landscape.color("White","DarkGray")

landscape.begin_fill()#landscape.fill(True)
for square in range(2):
    landscape.forward(400)
    landscape.left(90)
    landscape.forward(120)
    landscape.left(90)
landscape.end_fill()#landscape.fill(False)

landscape.up()
landscape.setpos(-200,-200)
for line in range(4):
    landscape.left(90)
    landscape.forward(30)
    landscape.right(90)
    for lot_of_paint in range(10):
        landscape.down()
        landscape.forward(20)
        landscape.up()
        landscape.forward(20)
    landscape.backward(400)
    
landscape.setpos(-200,-200)
landscape.pensize(5)
for line in range(2):
    landscape.down()
    for lot_of_paint in range(20):
        landscape.color("red")
        landscape.forward(10)
        landscape.color("white")
        landscape.forward(10)
    landscape.up()
    landscape.backward(400)  
    landscape.setpos(-200,-80)
    
landscape.setpos(180,-80)
landscape.pensize(8)
landscape.seth(270)
landscape.shape("square")

flag1 = 1                            
for line in range(4):
    landscape.down()
    if ((flag1 % 2) != 1):
        for lot_of_paint in range(10):
            landscape.color("black")
            landscape.forward(6)
            landscape.color("white")
            landscape.forward(6)
    else:
        for lot_of_paint in range(10):
            landscape.color("white")
            landscape.forward(6)
            landscape.color("black")
            landscape.forward(6)
    flag1 = flag1 + 1
    landscape.up()
    landscape.backward(120)  
    landscape.left(90)
    landscape.forward(6)
    landscape.right(90)
    

#Background Colour
wn.bgcolor('skyblue')

#create circle of sun
landscape.goto(-120,100)
landscape.pendown()
landscape.color("yellow","yellow")
landscape.begin_fill()
landscape.circle(20)
landscape.end_fill()
landscape.goto(-100,100)

#create sunrays
landscape.pensize(3)
for i in range(12):
        landscape.forward(80)
        landscape.backward(80)
        landscape.left(30)
landscape.penup()

#Trees
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

x = -200
turtles = [t1,t2,t3,]
for t in turtles:
  t.speed(100)
  t.left(90)
  t.color('brown')
  t.pu()
  x += random.randint(80,100)
  t.goto(x, random.randint(-70,-60))
  t.pd()

#Branch of trees
def branch(turt, branch_len):
  angle = random.randint(22,30)
  sf = random.uniform(0.6,0.8)
  size = int(branch_len /10)
  turt.pensize(size)
  if branch_len < 20:
    turt.color('green')
    turt.stamp()
    turt.color('brown')

  if branch_len > 10:
    turt.forward(branch_len)
    turt.left(angle)
    branch(turt, branch_len*sf)
    turt.right(angle*2)
    branch(turt, branch_len*sf)
    turt.left(angle)
    turt.backward(branch_len)

for t in turtles:
  branch(t,40)

#Turtle color
turtle1.color('Blue')
turtle2.color('Red')
turtle3.color("Yellow")
turtle4.color("purple")

#Getting the turtles ready 
for pointer in [turtle1, turtle2, turtle3, turtle4]:
    pointer.st()
    pointer.up()
    pointer.shape('turtle')

turtle1.goto(-190,-95)
turtle2.goto(-190,-125)
turtle3.setpos(-190,-155)
turtle4.setpos(-190,-185)

turtle1.speed(2)
turtle2.speed(2)
turtle4.speed(2)
turtle3.speed(2)

#Starting the race
landscape.shape("circle")
landscape.color("red")
landscape.setpos(-188,-60)
landscape.seth(0)

for countdown in range(3):
    landscape.st()
    time.sleep(0.5)
    landscape.ht()
    time.sleep(0.5)
   
landscape.color("LawnGreen")
landscape.st()
time.sleep(1.5)
landscape.ht()

turtle1_winner = 0
turtle2_winner = 0
turtle3_winner = 0
turtle4_winner = 0

winners_flag = 0
for i in range(50):
    if (turtle1.xcor()<200):
        turtle1.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (turtle1_winner == 0):
                print("turtle1 is the first place")
                turtle1_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (turtle1_winner == 0):
                print("turtle1 is the second place")
                turtle1_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (turtle1_winner == 0):
                print("turtle1 is the third place")
                turtle1_winner = 1
                winners_flag = 3
        elif (winners_flag == 3):
            if (turtle1_winner == 0):
                print("turtle1 is the fourth place")
                turtle1_winner = 1
                winners_flag = 4
    
    if (turtle2.xcor()<200):
        turtle2.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (turtle2_winner == 0):
                print("turtle2 is the first place")
                turtle2_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (turtle2_winner == 0):
                print("turtle2 is the second place")
                turtle2_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (turtle2_winner == 0):
                print("turtle2 is the third place")
                turtle2_winner = 1
                winners_flag = 3
        elif (winners_flag == 3):
            if (turtle2_winner == 0):
                print("turtle2 is the fourth place")
                turtle2_winner = 1
                winners_flag = 4       
        
    if (turtle3.xcor()<200):
        turtle3.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (turtle3_winner == 0):
                print("turtle3 is the first place")
                turtle3_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (turtle3_winner == 0):
                print("turtle3 is the second place")
                turtle3_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (turtle3_winner == 0):
                print("turtle3 is the third place")
                turtle3_winner = 1
                winners_flag = 3
        elif (winners_flag == 3):
            if (turtle3_winner == 0):
                print("turtle3 is the fourth place")
                turtle3_winner = 1
                winners_flag = 4  
     
    if (turtle4.xcor()<200):
        turtle4.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (turtle4_winner == 0):
                print("turtle4 is the first place")
                turtle4_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (turtle4_winner == 0):
                print("turtle4 is the second place")
                turtle4_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (turtle4_winner == 0):
                print("turtle4 is the third place")
                turtle4_winner = 1
                winners_flag = 3
        elif (winners_flag == 3):
            if (turtle4_winner == 0):
                print("turtle4 is the fourth place")
                turtle4_winner = 1
                winners_flag = 4  
                
wn.exitonclick()