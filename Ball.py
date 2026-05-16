# -------------------------------------------------------------------------
#   INFO
# -------------------------------------------------------------------------
# Name:         Ball
# Purpose:      The blueprint for all of the balls created in "Ball Evasion"
# Programmer:   Kektsune (Includes help from "Bro Code"s tutorials on youtube!)
# Date:         01/16/2026
# -------------------------------------------------------------------------

class Ball:

    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,x + diameter, y + diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image, self.xVelocity, self.yVelocity)