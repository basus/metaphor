from PIL import Image
from PIL import ImageTk
from PIL import ImageDraw
from PIL import ImageColor
import sys
import random
import math
import string
import copy
import datetime
import os

deg2rad = math.pi/180.0

class BranchContext(ImageDraw.ImageDraw):

    def __init__(self, size=(10000, 10000), bg="black", start=(2500,3500), *args):
        print "hello"
        self.__img = Image.new("RGB", size, bg)
        apply(ImageDraw.ImageDraw.__init__, (self,self.__img, )+args)
        self.__x, self.__y, self.__heading, self.__thickness = 0.0, 0.0, 90.0, 5
        self.__orientation_stack = []
        self.__pendown = 1
        self.__curvature = 1.2
        self.__colorStack = []
        self.__leafStack = []
        self.__leaf_color = "rgb(36,90,14)"
        self.setxy(start)

    def tell(self):
        "Return the turtle's X,Y position and heading"
        return (self.__x, self.__y, self.__heading)

    def right(self, amount):
        "Turn the turtle to the right"
        self.__heading=(self.__heading - amount) % 360.0

    def left(self, amount):
        "Turn the turtle to the left"
        self.__heading=(self.__heading + amount) % 360.0

    def backward(self, distance):
        "Move the turtle backward, drawing a line if the pen is down"
        self.forward(-distance)

    def forward(self, distance):
        if self.__thickness<0:
            return
        #print self.__color
        degrees = random.random()
        degrees = degrees*(self.__curvature*10*2)-self.__curvature*10 
        coordList = []
        x, y = self.__x, self.__y
        steps = distance
        radius = int(self.__thickness)
        dd = float(degrees)/steps
        direction = self.__heading
        if degrees>0:
            #Handles curve to the left
            for i in range(steps):
                    # Determines the next x and y values
                    dx = math.cos((direction + dd) * deg2rad)
                    dy = math.sin((direction + dd) * deg2rad)
                    # Updates x, y and direction
                    x = dx + x
                    y = -dy + y
                    direction = direction + dd
                    if self.__pendown:
                        self.ellipse([(x-radius, y-radius), (x+radius, y+radius)], fill=self.__color)
        if degrees<0:
             #Handles a curve to the right     
             for i in range(steps):    
                    # Determines the next x and y values
                    dx = math.cos((direction + dd) * deg2rad)
                    dy = math.sin((direction + dd) * deg2rad)
                    # Updates x, y and direction
                    x = dx + x
                    y = -dy + y
                    direction = direction + dd
                    if self.__pendown:
                        self.ellipse([(x-radius, y-radius), (x+radius, y+radius)], fill=self.__color)
                    
        self.__x, self.__y, self.__heading = x, y, direction    
        return

    def turn(self, degrees):
        if self.__thickness<0:
            return
        degrees = int(degrees)
        coordList = []
        x, y = self.__x, self.__y
        steps = 100
        radius = int(self.__thickness)
        dd = float(degrees)/steps
        direction = self.__heading
        if degrees>0:
            #Handles curve to the left
            for i in range(steps):
                    # Determines the next x and y values
                    dx = math.cos((direction + dd) * deg2rad)
                    dy = math.sin((direction + dd) * deg2rad)
                    # Updates x, y and direction
                    x = dx + x
                    y = -dy + y
                    direction = direction + dd
                    if self.__pendown:
                        self.ellipse([(x-radius, y-radius), (x+radius, y+radius)], fill=self.__color)
        if degrees<0:
             #Handles a curve to the right     
             for i in range(steps):    
                    # Determines the next x and y values
                    dx = math.cos((direction + dd) * deg2rad)
                    dy = math.sin((direction + dd) * deg2rad)
                    # Updates x, y and direction
                    x = dx + x
                    y = -dy + y
                    direction = direction + dd
                    if self.__pendown:
                        self.ellipse([(x-radius, y-radius), (x+radius, y+radius)], fill=self.__color)
                    
        self.__x, self.__y, self.__heading = x, y, direction
        
    def leaf(self, angle, lengthMax, width, widest):
        widestPoint = float(widest)
        widthMax = float(width)
        color = self.__leaf_color
        x,y = self.__x, self.__y
        h = self.__heading + int(angle)
        length = float(lengthMax)-(random.random() * float(lengthMax)/2)
        dd = random.random()*4
        frontDRadius = (widthMax/(length * widestPoint)) * 4
        backDRadius = (widthMax/(length - (length*widestPoint))) * 4
        radius = 1
        for i in range(length):
            self.ellipse([(x-radius, y-radius), (x+radius, y+radius)], fill = color)
            if (i<(length*widestPoint)) and (i%4==0):
                radius += frontDRadius
            if (i>(length*widestPoint)) and (i%4==0):
                radius -= backDRadius
            # Determines the next x and y values
            dx = math.cos((h + dd) * deg2rad)
            dy = math.sin((h + dd) * deg2rad)
            # Updates x, y and direction
            x = dx + x
            y = -dy + y
            
    def set_leaf_color(self, red, green, blue):
        if red<0:
            red = 0
        if blue<0:
            blue = 0
        if green<0:
            green = 0
        self.__leaf_color = "rgb(" + str(red) + "," + str(green) + "," + str(blue) + ")"

    def alter_leaf_color(self, r_in, g_in, b_in):
        Dred, Dgreen, Dblue = int(r_in), int(g_in), int(b_in),
        red, green, blue = self.getRGB(self.__leaf_color)
        self.set_leaf_color((int(red)+Dred),(int(green)+Dgreen),(int(blue)+Dblue))

        
    def penup(self):
        "Raise the pen from the paper"
        self.__pendown=0    

    def pendown(self): 
        "Lower the pen to the paper"
        self.__pendown=1

    def setxy(self, t): 
        "Set the turtle's X and Y position"
        im_x, im_y = self.im.size
        x,y = t
        x,y = float(x) % im_x, float(y) % im_y
        self.__x, self.__y = x,y

    def setx(self, x): 
        "Set the turtle's X position"
        im_x, im_y = self.im.size
        self.__x = float(x) % im_x

    def sety(self, y): 
        "Set the turtle's Y position"
        im_x, im_y = self.im.size
        self.__y = float(y) % im_y

    def seth(self, heading):
        "Set the turtle's heading"
        self.__heading = (float(heading) % 360.0)
                
    def change_h(self, change_h):
        self.__heading = self.__heading + (float(change_h))
        
    def sett(self, thickness):
        self.__thickness = thickness
        
    def change_t(self, i):
        self.__thickness = self.__thickness+(float(i))

              
    def set_curvature(self, curvature_in):
        self.__curvature = float(curvature_in)
        
    def set_ink(self, color):
        self.ink_color = color

    def distance(self, (x,y)):
        "Return the turtle's distance from the given point"
        return math.sqrt( (x-self.__x)**2 + (y-self.__y)**2 )

    def home(self):
        "Move the turtle to position 0,0"
        self.setxy( (0,0) )

    def save_point(self):
        "Save the turtle's current position and heading to a stack"
        self.__orientation_stack.append((self.__x, self.__y, self.__heading, self.__thickness))

    def restore_point(self):
        "Sets the turtle's position and heading to the last saved set"
        self.__x, self.__y, self.__heading, self.__thickness = self.__orientation_stack.pop()
        
    def save_color(self):
        self.__colorStack.append(self.__color)
        self.__leafStack.append(self.__leaf_color)
        #print self.__colorStack
        
    def restore_color(self):
        self.__color = self.__colorStack.pop()
        self.__leaf_color = self.__leafStack.pop()
        
    def set_color(self, red, green, blue):
        if red<0:
            red = 0
        if blue<0:
            blue = 0
        if green<0:
            green = 0
        self.__color = "rgb(" + str(red) + "," + str(green) + "," + str(blue) + ")"
        
    def alter_color(self, r_in, g_in, b_in):
        try:
            Dred, Dgreen, Dblue = int(r_in), int(g_in), int(b_in),
            red, green, blue = self.getRGB(self.__color)
            self.set_color((int(red)+Dred),(int(green)+Dgreen),(int(blue)+Dblue))
        except Exception, val:
            print val
            
    def getRGB(self, color):
        color = color.strip('rgb()')
        colors = color.split(',')
        return colors     
        
    def sendimg(self, img):
        "Stores the parent image so that teh Turtle can save itself"
        self.__img = img

    def saveData(self):
        "Writes all the point data to a file."
        f = open('./contexts/pointData', 'w')
        f.write(""+str(self.__x) + '\n' + str(self.__y) + '\n' + str(self.__heading) + '\n' + str(self.__thickness) + '\n' + str(self.__color))
        
    def loadData(self):
        f = open('./contexts/pointData', 'r')
        self.__x = float(f.readline())
        self.__y = float(f.readline())
        self.__heading = float(f.readline())
        self.__thickness = float(f.readline())
        self.__color = f.readline()
        
    def wrapup(self, name):
        "Save the image and return the saved image name"
        print 'writeup'
        self.__img.save(name)
        self.__init__()
        

    # Shortcuts
    fd=forward ; rt=right ; lt=left ; bk=backward
