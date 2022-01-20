import turtle


def hardmap():
    hardmap = turtle.Screen()
    hardmap.bgcolor("black")
    hardmap.setup(900,800)
    ss = turtle.Turtle()
    ss.color("orange")
    ss.pensize(4)
    ss.speed(0)
    ss.penup()
    ss.goto(450,400)
    ss.pendown()
    ss.goto(450,25)
    ss.penup()
    ss.goto(450,-25)
    ss.pendown()
    ss.right(90)
    ss.goto(450,-400)

    ss.left(90)
    ss.goto(-450,-400)
    ss.right(90)
    ss.goto(-450,400)
    ss.left(90)
    ss.goto(450,400)
    ss.left(180)
    ss.goto(-400,400)
    ss.left(90)
    ss.goto(-400,25)
    ss.penup()
    ss.goto(-400,-25)
    ss.pendown()
    ss.goto(-400,-400)
    ss.penup()
    ss.goto(-350,350)
    ss.pendown()
    ss.goto(-350,-350)
    ss.penup()
    ss.goto(-300,-400)
    ss.left(180)
    ss.pendown()
    ss.goto(-300,-250)
    ss.penup()
    ss.goto(-300,-200)
    ss.pendown()
    ss.goto(-300,200)
    ss.penup()
    ss.goto(-300,250)
    ss.pendown()
    ss.goto(-300,400)
    ss.right(90)
    ss.goto(-100,400)
    ss.left(90)
    ss.goto(-100,250)
    ss.left(90)
    ss.goto(-300,250)
    ss.penup()
    ss.goto(-300,200)
    ss.pendown()
    ss.right(180)
    ss.goto(-100,200)
    ss.right(90)
    ss.goto(-100,-200)
    ss.right(90)
    ss.goto(-300,-200)
    ss.left(90)
    ss.penup()
    ss.goto(-300,-250)
    ss.left(90)
    ss.pendown()
    ss.goto(-100,-250)
    ss.left(90)
    ss.goto(-100,-400)
    ss.penup()
    ss.goto(-50,-400)
    ss.pendown()
    ss.goto(-50,-25)
    ss.penup()
    ss.goto(-50,25)
    ss.pendown()
    ss.goto(-50,400)
    ss.penup()
    ss.goto(0,350)
    ss.pendown()
    ss.goto(0,-350)
    ss.right(90)
    ss.goto(250,-350)
    ss.penup()
    ss.goto(300,-350)
    ss.pendown()
    ss.goto(450,-350)
    ss.left(180)
    ss.goto(300,-350)
    ss.right(90)
    ss.goto(300,-300)
    ss.left(90)
    ss.goto(50,-300)
    ss.left(90)
    ss.goto(50,-25)
    ss.penup()
    ss.left(180)
    ss.goto(50,25)
    ss.pendown()
    ss.goto(50,300)
    ss.right(90)
    ss.goto(300,300)
    ss.left(90)
    ss.goto(300,350)
    ss.right(90)
    ss.goto(450,350)
    ss.penup()
    ss.goto(0,350)
    ss.pendown()
    ss.goto(250,350)
    ss.penup()
    ss.goto(50,25)
    ss.pendown()
    ss.goto(200,25)
    ss.penup()
    ss.goto(50,-25)
    ss.pendown()
    ss.goto(200,-25)
    ss.penup()
    ss.goto(250,-250)
    ss.pendown()
    ss.goto(250,250)
    ss.penup()
    ss.goto(300,25)
    ss.pendown()
    ss.goto(300,250)
    ss.right(90)
    ss.goto(450,250)
    ss.penup()
    ss.goto(300,-25)
    ss.pendown()
    ss.goto(300,-250)
    ss.goto(450,-250)
    ss.hideturtle()
    pen = turtle.Turtle()
    pen.color("white")
    pen.penup()
    pen.goto(0,450)
    tank1 = turtle.Turtle()
    tank2 = turtle.Turtle()
    tank1.color("red")
    tank2.color("blue")
    tank1.shape("turtle")
    tank2.shape("turtle")
    tank1.penup()
    tank2.penup()
    tank1.goto(-425,400)
    tank2.goto(-425,-400)
    tank1.pendown()
    tank2.pendown()
    tank1.right(90)
    tank2.left(90)


    tank1.penup()
    tank2.penup()

    def turnr1():
        tank1.right(90)

    turtle.listen()
    turtle.onkey(turnr1, "Right")

    def turnl1():
        tank1.left(90)
    turtle.listen()
    turtle.onkey(turnl1,"Left")

    


    def turnr2():
        tank2.right(90)

    turtle.listen()
    turtle.onkey(turnr2, "d")


    def turnl2():
        tank2.left(90)
    turtle.listen()
    turtle.onkey(turnl2,"a")

    def forward1():
        if 440 <= tank1.xcor() <= 460 and 25 <= tank1.ycor() <= 400:
            tank1.goto(-440,390)
        elif 440 <= tank1.xcor() <= 460 and -200 <= tank1.ycor() <= -50:
            tank1.goto(-440,390)
        elif tank1.xcor() <= -450:
            tank1.goto(-425,395)
        elif tank1.ycor() >= 400:
            tank1.goto(-425,395)
        elif tank1.ycor() <= -400:
            tank1.goto(-425,395)
        elif -410 <= tank1.xcor() <= -390 and 25 <= tank1.ycor() <= 400:
            tank1.goto(-425,395)
        elif -410 <= tank1.xcor() <= -390 and -400 <= tank1.ycor() <= -25:
            tank1.goto(-425,395)
        elif -360 <= tank1.xcor() <= -340 and -350 <= tank1.ycor() <= 350:
            tank1.goto(-425,395)
        elif -310 <= tank1.xcor() <= -290 and 250 <= tank1.ycor() <= 400:
            tank1.goto(-425,395)
        elif -310 <= tank1.xcor() <= -290 and -200 <= tank1.ycor() <= 200:
            tank1.goto(-425,395)
        elif -310 <= tank1.xcor() <= -290 and -400 <= tank1.ycor() <= -250:
            tank1.goto(-425,395)
        elif -310 <= tank1.xcor() <= -290 and -400 <= tank1.ycor() <= -250:
            tank1.goto(-425,395)
        elif -110 <= tank1.xcor() <= -90 and -400 <= tank1.ycor() <= -250:
            tank1.goto(-425,395)
        elif -110 <= tank1.xcor() <= -90 and -400 <= tank1.ycor() <= -250:
            tank1.goto(-425,395)
        elif -110 <= tank1.xcor() <= -90 and -400 <= tank1.ycor() <= -250:
            tank1.goto(-425,395)
        elif -110 <= tank1.xcor() <= -90 and -400 <= tank1.ycor() <= -250:
            tank1.goto(-425,395)
        elif -60 <= tank1.xcor() <= -40 and 25 <= tank1.ycor() <= 400:
            tank1.goto(-425,395)
        elif -60 <= tank1.xcor() <= -40 and -400 <= tank1.ycor() <= -25:
            tank1.goto(-425,395)
        elif -10 <= tank1.xcor() <= 10 and -350 <= tank1.ycor() <= 350:
            tank1.goto(-425,395)
        elif 40 <= tank1.xcor() <= 60 and 25 <= tank1.ycor() <= 300:
            tank1.goto(-425,395)
        elif 40 <= tank1.xcor() <= 60 and -300 <= tank1.ycor() <= -257:
            tank1.goto(-425,395)
        elif 290 <= tank1.xcor() <= 310 and 300 <= tank1.ycor() <= 350:
            tank1.goto(-425,395)
        elif 290 <= tank1.xcor() <= 310 and 25 <= tank1.ycor() <= 250:
            tank1.goto(-425,395)
        elif 290 <= tank1.xcor() <= 310 and -250 <= tank1.ycor() <= -25:
            tank1.goto(-425,395)
        elif 290 <= tank1.xcor() <= 310 and -350 <= tank1.ycor() <= -300:
            tank1.goto(-425,395)
        elif 290 <= tank1.xcor() <= 310 and 300 <= tank1.ycor() <= 350:
            tank1.goto(-425,395)
        elif 40 <= tank1.xcor() <= 60 and -250 <= tank1.ycor() <= -25:
            tank1.goto(-425,395)
        elif 40 <= tank1.xcor() <= 60 and 25 <= tank1.ycor() <= 250:
            tank1.goto(-425,395)
        elif -300 <= tank1.xcor() <= -100 and -210 <= tank1.ycor() <= -190:
            tank1.goto(-425,395)
        elif -300 <= tank1.xcor() <= -100 and -260 <= tank1.ycor() <= -240:
            tank1.goto(-425,395)
        elif -300 <= tank1.xcor() <= -100 and 190 <= tank1.ycor() <= 210:
            tank1.goto(-425,395)
        elif -300 <= tank1.xcor() <= -100 and 240 <= tank1.ycor() <= 260:
            tank1.goto(-425,395)
        elif 50 <= tank1.xcor() <= 200 and 15 <= tank1.ycor() <= 35:
            tank1.goto(-425,395)
        elif 50 <= tank1.xcor() <= 200 and -35 <= tank1.ycor() <= -15:
            tank1.goto(-425,395)
        elif 50 <= tank1.xcor() <= 300 and -310 <= tank1.ycor() <= -290:
            tank1.goto(-425,395)
        elif 50 <= tank1.xcor() <= 300 and 290 <= tank1.ycor() <= 310:
            tank1.goto(-425,395)
        elif 0 <= tank1.xcor() <= 250 and 340 <= tank1.ycor() <= 360:
            tank1.goto(-425,395)
        elif 0 <= tank1.xcor() <= 250 and -360 <= tank1.ycor() <= -340:
            tank1.goto(-425,395)
        elif 300 <= tank1.xcor() <= 450 and 340 <= tank1.ycor() <= 360:
            tank1.goto(-425,395)
        elif 300 <= tank1.xcor() <= 450 and -360 <= tank1.ycor() <= -340:
            tank1.goto(-425,395)
        elif 300 <= tank1.xcor() <= 450 and 240 <= tank1.ycor() <= 260:
            tank1.goto(-425,395)
        elif 300 <= tank1.xcor() <= 450 and -260 <= tank1.ycor() <= -240:
            tank1.goto(-425,395)
        elif 240 <= tank1.xcor() <= 260 and -250 <= tank1.ycor() <= 250:
            tank1.goto(-425,395)
        elif 240 <= tank1.xcor() <= 260 and -250 <= tank1.ycor() <= 250:
            tank1.goto(-425,395)
        elif 290 <= tank1.xcor() <= 310 and -350 <= tank1.ycor() <= -300:
            tank1.goto(-425,395)
        elif 290 <= tank1.xcor() <= 310 and 300 <= tank1.ycor() <= 350:
            tank1.goto(-425,395)
        elif 445 <= tank1.xcor() <= 470 and -50 <= tank1.ycor() <= 50:
            pen.write("Congratulations!", font=("Arial", 40, "normal"))
        
            
    
            
        
        

        
        
        
        
        
        
        

    
        tank1.forward(25)

    turtle.listen()
    turtle.onkey(forward1, "Up")

    def forward2():
        tank2.forward(30)

    turtle.listen()
    turtle.onkey(forward2, "w")

    

def easymap():
    easyscreen2=turtle.Screen()
    easyscreen2.bgcolor("yellow")
    easyscreen2.setup(900,800)
    ss = turtle.Turtle()
    ss.speed(0)
    ss.pensize(4)
    ss.penup()
    ss.goto(450,400)
    ss.pendown()
    ss.right(90)
    ss.goto(450,50)
    ss.penup()
    ss.goto(450,-50)
    ss.pendown()
    ss.goto(450,-400)
    ss.left(90)
    ss.goto(-450,-400)
    ss.right(90)
    ss.goto(-450,400)
    ss.left(90)
    ss.goto(450,400)
    ss.left(180)
    ss.goto(-350,400)
    ss.left(90)
    ss.penup()
    ss.goto(-350,300)
    ss.pendown()
    ss.goto(-350,-300)
    ss.penup()
    ss.goto(-250,-400)
    ss.pendown()
    ss.goto(-250,-50)
    ss.penup()
    ss.goto(-250,50)
    ss.pendown()
    ss.goto(-250,400)
    ss.goto(-250,50)
    ss.goto(-200,50)
    ss.penup()
    ss.goto(-250,-50)
    ss.pendown()
    ss.goto(-200,-50)
    ss.penup()
    ss.goto(-100,-300)
    ss.pendown()
    ss.goto(-100,300)
    ss.goto(100,300)
    ss.penup()
    ss.goto(200,400)
    ss.pendown()
    ss.goto(200,50)
    ss.penup()
    ss.goto(200,-50)
    ss.pendown()
    ss.goto(200,-400)
    ss.penup()
    ss.goto(100,-300)
    ss.goto(-100,-300)
    ss.pendown()
    ss.goto(100,-300)
    ss.penup()
    ss.goto(200,-200)
    ss.pendown()
    ss.goto(0,-200)
    ss.penup()
    ss.goto(0,200)
    ss.pendown()
    ss.goto(200,200)
    ss.penup()
    ss.goto(350,300)
    ss.pendown()
    ss.goto(350,-300)
    ss.hideturtle()
    pen = turtle.Turtle()
    pen.color("white")
    pen.penup()
    pen.goto(0,450)
    tank1 = turtle.Turtle()
    tank2 = turtle.Turtle()
    tank1.color("red")
    tank2.color("blue")
    tank1.shape("turtle")
    tank2.shape("turtle")
    tank1.penup()
    tank2.penup()
    tank1.goto(-425,400)
    tank2.goto(-425,-400)
    tank1.pendown()
    tank2.pendown()
    tank1.right(90)
    tank2.left(90)


    tank1.penup()
    tank2.penup()

    def turn1():
        if -360 <= tank1.xcor() <= -340 and -300 <= tank1.ycor()<= 300:
            tank1.goto(-450,400)
    
        tank1.right(90)

    turtle.listen()
    turtle.onkey(turn1, "Right")


    def turn2():
        tank2.right(90)

    turtle.listen()
    turtle.onkey(turn2, "d")

    def forward1():
        if tank1.xcor() < -450:
            tank1.goto(-440,390)
        elif 440 <= tank1.xcor() <= 460 and 50 <= tank1.ycor() <= 400:
            tank1.goto(-440,390)
        elif 440 <= tank1.xcor() <= 460 and -400 <= tank1.ycor() <= -50:
            tank1.goto(-440,390)
        elif tank1.ycor() >= 400:
            tank1.goto(-440,390)
        elif tank1.ycor() <= -400:
            tank1.goto(-440,390)
            
        elif -360 <= tank1.xcor() <= -340 and -300 <= tank1.ycor()<= 300:
            tank1.goto(-440,390)
        
        elif -260 <= tank1.xcor() <= -240 and -400 <= tank1.ycor()<= -50:
            tank1.goto(-440,390)
        elif -260 <= tank1.xcor() <= -240 and 50 <= tank1.ycor()<= 400:
            tank1.goto(-440,390)
        elif -200 <= tank1.xcor() <= -250 and 45 <= tank1.ycor() <= 55:
            tank1.goto(-440,390)
        elif -200 <= tank1.xcor() <= -250 and -55 <= tank1.ycor() <= -45:
            tank1.goto(-440,390)
        elif -110 <= tank1.xcor() <= -90 and -300 <= tank1.ycor()<= 300:
            tank1.goto(-440,390)
        elif -55 <= tank1.ycor() <= -45 and -250 <= tank1.xcor() <= -200:
            tank1.goto(-440,390)
        elif 45 <= tank1.ycor() <= 55 and 200 <= tank1.xcor() <= 250:
            tank1.goto(-440,390)
        elif 200 <= tank1.xcor() <= 250 and 45 <= tank1.ycor() <= 55:
            tank1.goto(-440,390)
        elif 190 <= tank1.xcor() <= 210 and -400 <= tank1.ycor() <= -50:
            tank1.goto(-440,390)
        elif 190 <= tank1.xcor() <= 210 and 50 <= tank1.ycor() <= 400:
            tank1.goto(-440,390)
        elif 340 <= tank1.xcor() <= 360 and -300 <= tank1.ycor() <= 300:
            tank1.goto(-440,390)
        elif 445 <= tank1.xcor() <= 470 and -50 <= tank1.ycor() <= 50:
            pen.write("Congratulations!", font=("Arial", 40, "normal"))
        elif -50 <= tank1.xcor() <= 100 and 290 <= tank1.ycor() <= 310:
            tank1.goto(-440,390)
        elif -50 <= tank1.xcor() <= 100 and -310 <= tank1.ycor() <= -290:
            tank1.goto(-440,390)
        elif 0 <= tank1.xcor() <= 100 and 190 <= tank1.ycor() <= 210:
            tank1.goto(-440,390)
        elif 0 <= tank1.xcor() <= 100 and -210 <= tank1.ycor() <= -190:
            tank1.goto(-440,390)
        
        else:
            tank1.forward(15)
            
        
        tank1.forward(15)
    turtle.listen()
    turtle.onkey(forward1, "Up")

    def forward2():
        tank2.forward(30)

    turtle.listen()
    turtle.onkey(forward2, "w")

map = int(input("Please enter 1 for easy map or 2 for hard map: "))
if map == 1:
    easymap()
elif map == 2:
    hardmap()
