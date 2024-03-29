import tkinter
import math

class Board:
    def __init__(self, x, y, width, height, canvas, cWidth, cHeight, tag, reboundSurface, maxSpeed = 4):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvas = canvas
        self.cWidth = cWidth
        self.cHeight = cHeight
        self.tag = tag
        self.reboundSurface = reboundSurface
        self.maxSpeed = maxSpeed

        self.drawFlag = False
        self.lose = 0
        self.isTouchBall = False
        self.touchBall = None

    def turnLeft(self, distance=1):
        if (distance > self.maxSpeed):
            distance = self.maxSpeed
        elif (distance < 0):
            distance = 0
        if (self.reboundSurface == "up"):
            if (self.x - distance >= 0):
                self.x -= distance
        elif (self.reboundSurface == "down"):
            if (self.x + self.width <= self.cWidth):
                self.x += distance
        elif (self.reboundSurface == "left"):
            if (self.y + self.height <= self.cHeight):
                self.y += distance
        elif (self.reboundSurface == "right"):
            if (self.y - distance >= 0):
                self.y -= distance
    def turnRight(self, distance=1):
        if (self.reboundSurface == "down"):
            if (self.x - distance >= 0):
                self.x -= distance
        elif (self.reboundSurface == "up"):
            if (self.x + self.width <= self.cWidth):
                self.x += distance
        elif (self.reboundSurface == "right"):
            if (self.y + self.height <= self.cHeight):
                self.y += distance
        elif (self.reboundSurface == "left"):
            if (self.y - distance >= 0):
                self.y -= distance

    def draw(self):
        if (self.drawFlag):
            self.canvas.delete(self.tag)
        self.canvas.create_rectangle(self.x, self.y, self.x + self.width, 
                                     self.y + self.height, 
                                     fill="black",
                                     tag = self.tag)
        self.drawFlag = True
    
    def ballOnLR(self, ball):
        if (self.reboundSurface == "left"):
            if (self.y + self.height < ball.y):
                return (0, self.y + self.height - ball.y)
            elif (self.y > ball.y):
                return (0, self.y - ball.y)
            else:
                return (self.y + self.height - ball.y, 0)
        elif (self.reboundSurface == "right"):
            if (self.y > ball.y):
                return (0, ball.y - self.y)
            elif (self.y + self.height < ball.y):
                return (0, ball.y - (self.y + self.height))
            else:
                return (ball.y - self.y, 0)
        elif (self.reboundSurface == "up"):
            if (self.x > ball.x):
                return (0, ball.x - self.x)
            elif (self.x + self.width < ball.x):
                return (0, ball.x - (self.x + self.width))
            else:
                return (ball.x - self.x, 0)
        elif (self.reboundSurface == "down"):
            if (self.x + self.width < ball.x):
                return (0, self.x + self.width - ball.x)
            elif (self.x > ball.x):
                return (0, self.x - ball.x)
            else:
                return (self.x + self.width - ball.x, 0)
    
    def ballOnUD(self, ball):
        if (self.reboundSurface == "right"):
            return (ball.x - ball.r) - (self.x + self.width) 
        elif (self.reboundSurface == "left"):
            return self.x - (ball.x + ball.r)
        elif (self.reboundSurface == "up"):
            return self.y - (ball.y + ball.r)
        elif (self.reboundSurface == "down"):
            return (ball.y - ball.r)- (self.y + self.height)
    
    def getLRBloak(self):
        if (self.reboundSurface == "left"):
            return (self.cHeight - (self.y+self.height), self.y)
        elif (self.reboundSurface == "right"):
            return (self.y, self.cHeight - (self.y + self.height))
        elif (self.reboundSurface == "up"):
            return (self.x, self.cWidth - (self.x + self.width))
        elif (self.reboundSurface == "down"):
            return (self.cWidth - (self.x + self.width), self.x)

class Ball:
    def __init__(self, x, y, r, canvas, cWidth, cHeight, tag, moveDirection = 0.0, speed = 1, maxSpeed = 3):
        self.x = x
        self.y = y
        self.r = r
        self.canvas = canvas
        self.cWidth = cWidth
        self.cHeight = cHeight
        self.tag = tag
        self.drawFlag = False
        self.moveDirection = moveDirection
        self.speed = speed
        self.maxSpeed = maxSpeed
        self.useful = True
    
    def draw(self):
        if (self.drawFlag):
            self.canvas.delete(self.tag)
            self.drawFlag = False
        if (self.useful):
            self.canvas.create_oval(self.x - self.r, self.y - self.r, 
                                    self.x + self.r, self.y + self.r,
                                    fill="red", outline="red",
                                    tag = self.tag)
            self.drawFlag = True
    
    def move(self):
        if (self.speed > self.maxSpeed):
            self.speed = self.maxSpeed
        elif (self.speed < 0):
            self.speed = 0
        self.x += self.speed * math.cos(self.moveDirection)
        self.y += self.speed * math.sin(self.moveDirection)
        if (self.x < 0):
            self.x += self.cWidth
        elif (self.x > self.cWidth):
            self.x -= self.cWidth
        if (self.y < 0):
            self.y += self.cHeight
        elif (self.y > self.cHeight):
            self.y -= self.cHeight
