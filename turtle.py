# Original code by Andrew Kuchling amk@magnet.com

import ImageDraw, math

deg2rad = math.pi/180.0

class Turtle:

    ''' A factory class to create and actually return a Turtle object with 
    proper parameters'''

    def __init__(self):
        img = Image.new("RGB", (1000,1000), "white")
        turtle = TurtleDraw(img)
        turtle.setxy((500,500))
        turtle.pendown()
        turtle.sendimg(img)
        return turtle

class TurtleDraw(ImageDraw.ImageDraw):
    def __init__(self, *args):
	apply(ImageDraw.ImageDraw.__init__, (self,)+args)
	self.__x, self.__y, self.__heading = 0.0, 0.0, 90.0
	self.__pendown=1
        self.__img = None

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
	"Move the turtle forward, drawing a line if the pen is down"
	im_x, im_y = self.im.size
	sx, sy = self.__x, self.__y
	distance=float(distance) 
	ex=sx+distance*math.cos(self.__heading*deg2rad)
	ey=sy-distance*math.sin(self.__heading*deg2rad)
	if self.__pendown: self.line( [(sx,sy), (ex,ey)] )
 	self.__x, self.__y = ex, ey
	if not (0<=ex<im_x) or not (0<=ey<im_y):
	    new_ex=ex % im_x ; new_ey=ey % im_y
	    sx=sx + (new_ex-ex) ; sy=sy + (new_ey-ey)
	    if self.__pendown: self.line( [(sx,sy), (new_ex,new_ey)] )
	    self.__x, self.__y = new_ex, new_ey

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
	self.__heading = float(heading) % 360.0

    def distance(self, (x,y)):
	"Return the turtle's distance from the given point"
	return math.sqrt( (x-self.__x)**2 + (y-self.__y)**2 )

    def home(self):
	"Move the turtle to position 0,0"
	self.setxy( (0,0) )

    def sendimg(self, img):
        "Stores the parent image so that teh Turtle can save itself"
        self.img = img

    def wrapup(self, name):
        "Save the image and return the saved image name"
        self.img.save(name)
        

    # Shortcuts
    fd=forward ; rt=right ; lt=left ; bk=backward
