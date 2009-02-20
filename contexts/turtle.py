# Original code by Andrew Kuchling amk@magnet.com

import Image, ImageDraw, math

deg2rad = math.pi/180.0

#class turtle:
#
#    ''' A factory class to create and actually return a Turtle object with 
#    proper parameters'''

#    def __init__(self):
#        img = Image.new("RGB", (1000,1000), "white")
#        turtle = TurtleDraw(img)
#        turtle.setxy((500,500))
#        turtle.pendown()
#        turtle.sendimg(img)


class turtle(ImageDraw.ImageDraw):
    def __init__(self, size=(1000, 1000), bg="black", start=(650,650), *args):
        self.__img = Image.new("RGB", size, bg)
#        ImageDraw.ImageDraw.__init__(self, self.__img)
	apply(ImageDraw.ImageDraw.__init__, (self,self.__img, )+args)
        
	self.__x, self.__y, self.__heading, self.thickness = 0.0, 0.0, 90.0, 5
        self.__state_stack = [(self.__x, self.__y, self.__heading)]
	self.__pendown=1
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

    def ahead(self, distance):
        "Moves the turtle ahead, but doesn't put down a line"
        self.__pendown = 0
        self.forward(distance)

    def behind(self, distance):
        "Moves the turtle behind without drawing a line"
        self.__pendown = 0
        self.backward(distance)
        
    def penup(self): 
	"Raise the pen from the paper"
	self.__pendown=0    

    def pendown(self): 
	"Lower the pen to the paper"
	self.__pendown=1

    def thickness(self, thick):
        "Changes the thickness of the line drawn TO the given amount"
        self.__thickness = thickness

    def thicken(self, amt):
        "Changes the thickness of the line BY the given amount"
        self.__thickness = self.__thickness + float(amt)
        if self.__thickness < 0:
            self.__thickness = 1

    def color(self, color):
        "Changes the color of the pen"
        self.ink_color = color
    def save(self):
        "Save the turtle's current position and heading to a stack"
        self.__state_stack.append((self.__x, self.__y, self.__heading, self.__thickness, self.__color))

    def restore(self):
        "Sets the turtle's position and heading to the last saved set"
        self.__x, self.__y, self.__heading, self.thickness, self.__color = self.__state_stack.pop()

    def restore_without(self, *args):
        "Restore the turtle's position without the properties specified by the entered numbers"
        optlist = [1,2,3,4,5]
        x, y, h, th, col = self.__state_stack.pop()
        for num in optlist:
            if not num in args:
                if num==1: self.__x = x
                elif num==2: self.__y = y
                elif num==3: self.__heading = h
                elif num==4: self.__thickness = th
                elif num==5: self.__color = col

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
        self.__img = img

    def wrapup(self, name):
        "Save the image and return the saved image name"
        self.__img.save(name)
        self.__init__()
        

    # Shortcuts
    fd=forward ; rt=right ; lt=left ; bk=backward
