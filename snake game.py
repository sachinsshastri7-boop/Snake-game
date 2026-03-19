import turtle
import time
import random


delay=0.1
score=0
high_score=0
#set up the screen
wn=turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0) #it turns off the animation in te screen   #the first 7 lines of the code is for the screen

#snake head
head=turtle.Turtle()
head.speed(0) #it keeps the speed of the snake as fast as possible
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0) #the place where the snake will start
head.direction ="stop"

#snake food
food=turtle.Turtle()
food.speed(0) #it keeps the speed of the snake as fast as possible
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100) #the place where the snake will start

segments=[]
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier",24,"normal"))

#Functions
def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction!="up":
       head.direction="down"
def go_right():
    if head.direction!="left":
        head.direction="right"
def go_left():
    if head.direction!="right":
        head.direction="left"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#key bindings

wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")


#main game loop
while True:
    wn.update()
    #check for the collision in the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
       time.sleep(1)
       head.goto(0,0)
       head.direction="stop"

       #hide the segments because it was reappearing even thought the game finished
       for segment in segments:
           segment.goto(1000,1000)
        
        #clear the elements in the segment
       segments.clear()
       
       #resetting the score
       score=0

       #reset the delay
       delay=0.1
       #updating the score list
       pen.clear()
       pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    

    #check for the collision with the food
    if head.distance(food)<20:
        #move food to a random place
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("grey")
        new_segment.shape("square")
        new_segment.penup()
        segments.append(new_segment)
        #shorten the delay
        delay-=0.001

        #Increase the score
        score+=10

        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    
    #move the end segments first in the reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move the segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)


    move()
    #check for the head collision
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

       #hide the segments because it was reappearing even thought the game finished
            for segment in segments:
                segment.goto(1000,1000)
        
        #clear the elements in the segment
            segments.clear()
        #reset the score
            score=0
        #updating the score list
            pen.clear()
            pen.write("Score {} High Score {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    
    time.sleep(delay) #to delay the action
wn.mainloop()  #it will keep the screen open for us