from ctypes import alignment
from hashlib import new
from multiprocessing.spawn import old_main_modules
import turtle
import random
import time

screen = turtle.Screen()
screen.title('Snake Game')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('turquoise')

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#score
score = 0
delay = 0.1

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30,30)

oldFruit = []

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score :",align="center",font=("Courier",24,"bold"))

#define how to move
def snakeGoUp():
    if snake.direction != "down":
        snake.direction = "up"

def snakeGoDown():
    if snake.direction != "up":
        snake.direction = "down"

def snakeGoLeft():
    if snake.direction != "right":
        snake.direction = "left"

def snakeGoRight():
    if snake.direction != "left":
        snake.direction = "right"

def snakeMove():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

#keyboard bindings
screen.listen()
screen.onkeypress(snakeGoUp, "Up")
screen.onkeypress(snakeGoDown, "Down")
screen.onkeypress(snakeGoLeft, "Left")
screen.onkeypress(snakeGoRight, "Right")

#main loop
while True:
        screen.update()
            #snake and fruit collisions
        if snake.distance(fruit)< 20:
                x = random.randint(-290,270)
                y = random.randint(-240,240)
                fruit.goto(x,y)
                scoring.clear()
                score+=1
                scoring.write("Score:{}".format(score),align="center",font=("Courier",24,"bold"))
                delay-=0.001

                #creating new ball
                newFruit = turtle.Turtle()
                newFruit.speed(0)
                newFruit.shape('square')
                newFruit.color('red')
                newFruit.penup()
                oldFruit.append(newFruit)

        #adding ball to snake
        for i in range (len(oldFruit)-1,0,-1):
                a = oldFruit[i-1].xcor()
                b = oldFruit[i-1].ycor()

                oldFruit[i].goto(a,b)

        if len(oldFruit)>0:
                a= snake.xcor()
                b = snake.ycor()
                oldFruit[0].goto(a,b)

        snakeMove()

        #snake and border collision
        if snake.xcor()>280 or snake.xcor()< -300 or snake.ycor()>240 or snake.ycor()<-240:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('turquoise')
                scoring.goto(0,0)
                scoring.write("Game Over \nYour Score is {}".format(score), align="center", font=("Courier", 24, "bold"))

        #snake collision
        for food in oldFruit:
                if food.distance(snake) < 20:
                    time.sleep(1)
                    screen.clear()
                    screen.bgcolor('turquoise')
                    scoring.goto(0,0)
                    scoring.write("Game Over \nYour Score is {}".format(score, align="center", font=("Courier", 24, "bold")))




        time.sleep(delay)

turtle.Terminator()
