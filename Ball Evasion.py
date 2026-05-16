# -------------------------------------------------------------------------
#   INFO
# -------------------------------------------------------------------------
# Name:         Ball Evasion
# Purpose:      A fun minigame where you drag and click a shape, avoiding the balls
# Programmer:   Kektsune (Includes help from "Bro Code"s tutorials on youtube!)
# Date:         01/16/2026
# -------------------------------------------------------------------------

from tkinter import *
from Ball import *
import random
import time

window = Tk()
window.title("Ball Evasion")


window.attributes('-fullscreen', True)

#Sets constant SCREEN_WIDTH and SCREEN_HEIGHT to the sizes of the window
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()

#Creates canvas
canvas = Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack(fill=BOTH, expand=True)

# ----------------------- WIDGET + VARIABLE SETUP ---------------------- #

title = Label(canvas, text="Welcome to Ball Evasion!", font=("Arial", 24))
canvas.create_window(SCREEN_WIDTH // 2, 50, window=title)

directions = Label(canvas, text="Click and drag the red square to start!", font=("Arial", 16))
canvas.create_window(SCREEN_WIDTH // 2, 100, window=directions)

tag = Label(canvas, text="By Kektsune", font=("Arial", 12))
canvas.create_window(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30, window=tag)

square = Label(canvas, bg='red', width=1, height=1)
canvas.create_window(50, 150, window=square)

gameStarted = False

gameEnded = False

ballCounter = 0

seconds = 0

minutes = 0

hours = 0

# ----------------------- FUNCTIONS ---------------------- #

#When event is triggered on click, begin to track widget positions and mark game started
def drag_start(event): 
    global gameStarted, title, directions

    title.destroy()
    directions.destroy()
    tag.destroy()

    widget = event.widget 
    widget.startX = event.x 
    widget.startY = event.y 
    if(gameStarted == False):
        gameStarted = True
        startGame()
    else:
        print()

#Drags the position of the widget to the location of the mouse and places edge boundaries
def drag_motion(event): 
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y

    w = widget.winfo_width()
    h = widget.winfo_height()

    x = max(2, min(SCREEN_WIDTH - 10, x))
    y = max(2, min(SCREEN_HEIGHT - 20, y))

    widget.place(x=x, y=y)


#Starts the game, running all functions once in itself
def startGame():
    global canvas, balls 

    balls = []

    valueGeneration()
    ballGeneration()
    animate()
    timeKeeper()

#Randomizes some values while keeping some the same
def valueGeneration():
    global rand_xVelocity, rand_yVelocity, rand_xStarting, rand_yStarting, diameter
    rand_xVelocity = random.randint(1,8)
    rand_yVelocity = random.randint(1,8)
    diameter = 10
    rand_xStarting = 0
    rand_yStarting = 0

#Creates a new ball every 5 seconds and tracks the amount
def ballGeneration():
    global ballCounter

    valueGeneration() 
    randomBall = Ball(canvas, rand_xStarting, rand_yStarting, diameter, rand_xVelocity, rand_yVelocity, "black")
    balls.append(randomBall)

    ballCounter += 1

    window.after(5000, ballGeneration)

#Continuously loops the animation and checks for any collision deaths
def animate():
    for ball in balls:
        ball.move()
    deathCheck()
    window.after(10, animate)

#If any of the balls collide with the square/label, call on endGame
def deathCheck():
    square_x1 = square.winfo_x()
    square_y1 = square.winfo_y()
    square_x2 = square_x1 + square.winfo_width()
    square_y2 = square_y1 + square.winfo_height()

    for ball in balls:
        ball_coords = canvas.coords(ball.image) 
        ball_x1, ball_y1, ball_x2, ball_y2 = ball_coords

        if (square_x1 < ball_x2 and square_x2 > ball_x1 and
            square_y1 < ball_y2 and square_y2 > ball_y1):
            endGame()

#Lets the user know they've lost and pulls up their stats on balls on screen and keeps track of survival time
def endGame():
    global gameEnded
    if(gameEnded == False):
        gameEnded = True
        canvas.pack_forget()
        endLabel = Label(window, text="You died! Exiting...", font=("Helvetica", 20))
        endLabel.pack()
        ballCounterLabel = Label(window, text="You survived a total of: " + str(ballCounter) + " balls!", font=("Helvetica", 20))
        ballCounterLabel.pack()
        timerLabel = Label(window, text="Your total time was: " + str(seconds) + " seconds, " + str(minutes) + " minutes, and " + str(hours) + " hours", font=("Helvetica", 20))
        timerLabel.pack()
        window.after(3000, window.destroy)

#Tracks time, resetting seconds and minutes if they reach 60
def timeKeeper():
    global seconds, minutes, hours
    seconds+=1
    if(seconds==60):
        seconds = 0
        minutes += 1
    if(minutes==60):
        minutes = 0
        hours += 1
    window.after(1000, timeKeeper)

#Bind the events to the square label and attaches the functions
square.bind("<Button-1>", drag_start)
square.bind("<B1-Motion>", drag_motion)

window.mainloop()