import turtle                    # import turtle library
import time
import sys
import collections

blockSize = 24

class Coin(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.startScreenX = -250
        self.startScreenY = 250
        self.goto(self.startScreenX-150,self.startScreenY)


class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Grid(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Path(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.startScreenX = -250
        self.startScreenY = 250
        self.stepSize = 24
        self.goto(self.startScreenX-150,self.startScreenY)

    def drawBlock(self, x, y):
        """
        A function that takes x and y coordinates and draws a blue box in it
        """
        self.goto(x,y)
        self.stamp()

    def drawArray(self, arr):
        """
        A function that takes an array of (x,y) coordinates and draws blue boxes in it
        """
        for y in range(len(arr)):
            cord = arr[y]
            xCord = cord[0]
            yCord = cord[1]
            self.drawBlock(xCord, yCord)

class Maze():
    def __init__(self):
        self.bg = turtle.Screen()
        self.bg.bgcolor("black")
        self.bg.setup(750,650)
        self.grid = Grid()
        self.end = End()
        self.coin = Coin()
        self.wall = []
        self.finish = (0,0)
        self.coins = []
        self.startScreenX = -250
        self.startScreenY = 250
        self.startingPos = [0,0]
        self.stepSize = 24

    def setUpMaze(self, border):
        """"
        A function that takes the maze array and sets up the simulator
        """
        for y in range(len(border)):
            for x in range(len(border[y])):
                square = border[y][x]
                screen_x = self.startScreenX + (x * self.stepSize)
                screen_y = self.startScreenY - (y * self.stepSize)
                if square == "+":                     # if grid character contains an +
                    self.grid.goto(screen_x, screen_y)        # move turtle to the x and y location and
                    self.grid.stamp()                         # stamp a copy of the turtle (white square) on the screen
                    self.wall.append((screen_x, screen_y))   # add coordinate to walls list
                elif square == "e":                     # if grid character contains an e
                    self.end.goto(screen_x, screen_y)         # move turtle to the x and y location and
                    self.end.stamp()                          # stamp a copy of the turtle (green square) on the screen
                    self.finish = (screen_x, screen_y)  # add coordinate to finish list
                elif square == "s":                     # if grid character contains an s
                    self.startingPos[0] = screen_x         # edit the values of the starting position
                    self.startingPos[1] = screen_y
                elif square == "x":                     # if the grid character contains an x
                    self.coin.goto(screen_x, screen_y)  # move turtle to the x and y location and
                    self.coin.stamp()  # stamp a copy of the turtle (yellow square) on the screen
                    self.coins.append((screen_x, screen_y))


    def getWall(self):
        """"
        returns an array that includes the coordinates of each tile in the wall
        """
        return self.wall

    def getCoins(self):
        """"
        returns an array that includes the coordinates of each coin in the game
        """
        return self.coins

    def getstartScreenX(self):
        """"
        returns the starting X coordinates of the maze
        """
        return self.startScreenX

    def getstartScreenY(self):
        """"
        returns the starting Y coordinates of the maze
        """
        return self.startScreenY

    def getFinish(self):
        """
        returns an array that contains the end coordinates
        """
        return self.finish

    def getStartingPosition(self):
        """
        returns an array that contains the starting position
        """
        return self.startingPos


    def endProgram(self):
        """
        A function that ends the game
        """
        self.bg.exitonclick()
        sys.exit()

class Character(turtle.Turtle):
    def __init__(self, startingPos):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("green")
        self.right(90)
        self.penup()
        self.speed(0)
        self.goto(startingPos[0], startingPos[1])
        self.stamp()

    def getCurrentX(self):
        """"
        returns the current X coordinate of the turtle
        """
        return(round(self.xcor(),0))

    def getCurrentY(self):
        """"
        returns the current Y coordinate of the turtle
        """
        return(round(self.ycor(),0))

    def getAngle(self):
        """
        returns the angle that the character is facing
        """
        return self.heading()

    def rotateRight(self):
        self.clear()
        self.right(90)

    def rotateLeft(self):
        self.clear()
        self.left(90)

    def moveForward(self):
        self.clear()
        self.forward(24)
        time.sleep(0.1)
