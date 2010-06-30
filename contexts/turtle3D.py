
import sys
import random
import math
import string
import copy
import datetime
import time
import os

# conversion from degrees to radians for math trig functions
deg2rad = math.pi/180.00

class turtle3D:
	"""
	initializes the turtle
	"""
	def __init__(self, size=(1000, 1000), bg="black", start=(2500,3500), *args):
		# initial position, heading, and thickness
		self.__x, self.__y, self.__z, self.__heading, self.__thickness = 0.0, 0.0, 0.0, (0,0), 5
		# minimum thickness of the line (default "0.01")
		self.minThickness = 0.01
		# viewing angle of the camera
		self.camAngle = 38
		# stack holding positon, heading, and thickness
		self.__orientation_stack = []
		# name of the temporary folder and .pov file (default "test")
		self.name = "test"
		# whether the pen is currently drawing
		# 1 = drawing, 0 = not drawing (default "1")
		self.__pendown = 1
		# curvature of the pen
		# 0 = straight, 3 = particularly curvy (default "0")
		self.__curvature = 0
		# stack holding the colors
		self.__colorStack = []
		# used for the creation of sphere splines for drawing
		self.spheres = []
		# sets up the initial .pov file
		self.fileOut = open("./povrayContent/testingPov."+self.name+".pov", 'w')
		# current color in <red, green, blue, opacity>
		# all values between 0 and 1 inclusive
		self.__color = "pigment{rgbf <1,1,1,0>}"
		# variables for animation
		self.animated = False
		self.ani_index = 0
		# sets the camera's initial position, look, and rotation
		self.camera = (500,0,0,0,0,0,0,0,0)
		# sets the camera's depth of field
		# aperture of 0 turns it off
		self.dof = (0,0,0,0,0)
		# adds header information to the .pov file
		self.setupPov()
		
	"""
	sets up pov-ray
	"""
	def setupPov(self):
		self.fileOut.write(" #version 3.6;\n #include \"colors.inc\"    \n")
		self.fileOut.write(" #include \"textures.inc\"   \n\n")
		self.setupBg(0,0,0)
		self.setupCam()
		distx = 600
		disty = 600
		distz = 600
		# sets light sources in a rectangular prism
		self.addLS(-distx, disty, distz)
		self.addLS(-distx, disty, -distz)
		self.addLS(-distx, -disty, distz)
		self.addLS(-distx, -disty, -distz)
		self.addLS(distx, disty, distz)
		self.addLS(distx, disty, -distz)
		self.addLS(distx, -disty, distz)
		self.addLS(distx, -disty, -distz)
		
	"""
	adds a light source to space
	"""
	def addLS(self,x,y,z):
		self.fileOut.write("light_source {\n<"+str(x)+", "+str(y)+", "+str(z)+">\n color White \n  shadowless\n")
		self.fileOut.write("adaptive 2 }\n\n")

	"""
	changes the camera's x,y,z position by adding to the current x,y,z position
	"""
	def changeCamPosition(self, dx, dy, dz):
		dx, dy, dz = float(dx),float(dy),float(dz)
		self.camera=(self.camera[0]+dx, self.camera[1]+dy, self.camera[2]+dz, self.camera[3], self.camera[4], self.camera[5],self.camera[6], self.camera[7], self.camera[8])
		
	"""
	changes the camera's x,y,z look by adding to the current x,y,z look
	"""
	def changeCamLook(self, dx, dy, dz):
		dx,dy,dz = float(dx),float(dy),float(dz)
		self.camera=(self.camera[0], self.camera[1], self.camera[2], self.camera[3]+dx, self.camera[4]+dy, self.camera[5]+dz, self.camera[6], self.camera[7], self.camera[8])
    	
	"""
	changes the camera's x,y,z rotation by adding to the current x,y,z rotation
	"""
	def rotateCamera(self, dx, dy, dz):
		dx,dy,dz = float(dx),float(dy),float(dz)
		self.camera=(self.camera[0], self.camera[1], self.camera[2], self.camera[3], self.camera[4], self.camera[5], self.camera[6]+dx, self.camera[7]+dy, self.camera[8]+dz)
		
	"""
	sets the camera's depth of field
	aperture determines the depth of the sharpness zone (default "0")
		larger apertures give a lot of blurring
		narrow apertures give a wide zone of sharpness
	the center of the focal point is given by the vector <xFoc,yFoc,zFoc> (default <0,0,0>)
	blur samples determine specify the maximum number of rays to use for each pixel (default "0")
	"""
	def setDepthOfField(self, aperture, xFoc, yFoc, zFoc, samples):
		self.dof=(float(aperture),float(xFoc),float(yFoc),float(zFoc),float(samples))
		
	"""
	changes the camera's depth of field by adding to the current depth of field's aperture size and x,y,z focal point
	"""
	def changeDepthOfField(self, da, dx, dy, dz):
		self.dof=(self.dof[0]+float(da),self.dof[1]+float(dx),self.dof[2]+float(dy),self.dof[3]+float(dz),self.dof[4])

	"""
	sets the camera's position, look, and rotation
	"""
	def setCamera(self, xPos, yPos, zPos, xLook, yLook, zLook, xRotate, yRotate, zRotate):	
		self.camera=(float(xPos), float(yPos), float(zPos), float(xLook), float(yLook), float(zLook), float(xRotate), float(yRotate), float(zRotate))
		self.updateCamera("./povrayContent/testingPov."+self.name+".pov")

	"""
	updates the camera in the .pov file with the new values
	"""
	def updateCamera(self, filename):
		mod = open(filename).readlines()
		for i in range(len(mod)-1):
			if "camera" in mod[i]:
				mod[i] = "camera {\n angle "+str(self.camAngle)+"\n location <"+str(self.camera[0])+","+str(self.camera[1])+","+str(self.camera[2])+">\n right x*image_width/image_height\n look_at <"+str(self.camera[3])+","+str(self.camera[4])+","+str(self.camera[5])+">\n rotate <"+str(self.camera[6])+","+str(self.camera[7])+","+str(self.camera[8])+">"
				if self.dof[0] != 0:
					mod[i] += "\n focal_point <"+str(self.dof[1])+", "+str(self.dof[2])+", "+str(self.dof[3])+">\n aperture "+str(self.dof[0])+"\n blur_samples "+str(self.dof[4])
				mod[i] += "\n}"
				del mod[i+1:i+7]
				break
		out = open(filename, "w")
		out.writelines(mod)
		out.close()
		
	"""
	sets up the camera's code in the .pov file
	"""
	def setupCam(self):
		self.fileOut.write("camera {\n angle 38\n location <"+str(self.camera[0])+","+str(self.camera[1])+","+str(self.camera[2])+">\n right x*image_width/image_height\n look_at <"+str(self.camera[3])+","+str(self.camera[4])+","+str(self.camera[5])+">\n rotate <"+str(self.camera[6])+","+str(self.camera[7])+","+str(self.camera[8])+">")
		if self.dof[0] != 0:
			self.fileOut.write("\n focal_point <"+str(self.dof[1])+", "+str(self.dof[2])+", "+str(self.dof[3])+">\n aperture "+str(self.dof[0])+"\n blur_samples "+str(self.dof[4]))
		self.fileOut.write("\n}\n")
		
	"""
	sets up the background color of the space
	""" 
	def setupBg(self, r, g, b):
		self.fileOut.write("background   { color rgb <"+str(r)+", "+str(g)+", "+str(b)+"> } \n")
		
	"""
	adds the sphere spline based on the given color
	"""
	def renderSS(self, color):
		self.fileOut.write("sphere_sweep{\n linear_spline \n "+str(len(self.spheres))+",\n")
		for i in range(len(self.spheres)):
			x,y,z,r = self.spheres[i]
			self.fileOut.write("<"+str(x)+", "+str(y)+", "+str(z)+">, "+str(r)+"\n")
		self.fileOut.write("texture{ \n "+color+" \n")
		self.fileOut.write("finish{ \n ambient .1 \n \n}")
		self.fileOut.write("\n}")
		(self.fileOut).write("}\n\n")
		
	"""
	moves the pen forward by given distance
	"""
	def forward(self, distance):
		# do nothing if the thickness is below the minimum value
		if self.__thickness<self.minThickness:
			return
		# creates the curvy nature of the spline
		dTheta = ((self.__curvature*100)*random.random()-self.__curvature*50)/float(distance)
		dPhi = ((self.__curvature*100)*random.random()-self.__curvature*50)/float(distance)
		x, y, z = self.__x, self.__y, self.__z
		radius = float(self.__thickness)
		theta,phi = self.__heading
		# spheres of the spline
		self.spheres = []
		self.spheres.append((x,y,z,radius))
		for i in range(int(distance)):
			dx = math.sin((theta + dTheta) * deg2rad) * math.cos((phi + dPhi) * deg2rad)
			dy = math.sin((theta + dTheta) * deg2rad) * math.sin((phi + dPhi) * deg2rad)
			dz = math.cos((theta + dTheta) * deg2rad)
			x = dx + x
			y = dy + y
			z = dz + z
			theta = dTheta + theta
			phi = dPhi + phi
			self.spheres.append((x,y,z,radius))
		# add splines if pen is down
		if self.__pendown:
			self.renderSS(self.__color)
		# set the new x,y,z position and heading
		self.__x, self.__y, self.__z, self.__heading = x, y, z, (theta,phi)
		
	"""
	moves the pen backwards by given distance
	"""
	def backward(self, distance):
		# do nothing if the thickness is below the minimum value
		if self.__thickness<self.minThickness:
			return
		# creates curvy nature of spline
		dTheta = ((self.__curvature*100)*random.random()-self.__curvature*50)/float(distance)
		dPhi = ((self.__curvature*100)*random.random()-self.__curvature*50)/float(distance)
		x, y, z = self.__x, self.__y, self.__z
		radius = float(self.__thickness)
		theta,phi = self.__heading
		# spheres of the spline
		self.spheres = []
		self.spheres.append((x,y,z,radius))
		for i in range(int(distance)):
			dx = math.sin((theta + dTheta) * deg2rad) * math.cos((phi + dPhi) * deg2rad)
			dy = math.sin((theta + dTheta) * deg2rad) * math.sin((phi + dPhi) * deg2rad)
			dz = math.cos((theta + dTheta) * deg2rad)
			x = x - dx
			y = y - dy
			z = z - dz
			theta = dTheta + theta
			phi = dPhi + phi
			self.spheres.append((x,y,z,radius))
		# add spline if pen is down
		if self.__pendown:
			self.renderSS(self.__color)
		# set the new x,y,z position and heading
		self.__x, self.__y, self.__z, self.__heading = x, y, z, (theta,phi)
	
	"""
	changes the pen's heading at the current x,y,z position by a inclination theta and an azimuth phi
	works just like spherical coordinates
	"""
	def turn(self, dTheta, dPhi):
		# do nothing if the thickness is below the minimum value
		if self.__thickness<self.minThickness:
			return
		# number of steps to create a smoother curve
		steps = 10
		dTheta = float(dTheta)/steps
		dPhi = float(dPhi)/steps
		x, y, z = self.__x, self.__y, self.__z
		radius = float(self.__thickness)
		# spheres of the spline
		self.spheres = []
		self.spheres.append((x,y,z,radius))
		theta,phi = self.__heading
		for i in range(steps):
			dx = math.sin((theta + dTheta) * deg2rad) * math.cos((phi + dPhi) * deg2rad)
			dy = math.sin((theta + dTheta) * deg2rad) * math.sin((phi + dPhi) * deg2rad)
			dz = math.cos((theta + dTheta) * deg2rad)
			x = dx + x
			y = dy + y
			z = dz + z
			theta = dTheta + theta
			phi = dPhi + phi
			self.spheres.append((x,y,z,radius))
		# add spline if pen is down
		if self.__pendown:
			self.renderSS(self.__color)
		# set the new x,y,z position and heading
		self.__x, self.__y, self.__z, self.__heading = x, y, z, (theta,phi)
		
	"""
	turns the pen at the current x,y,z position in at a random angle between the given minimum and maximum theta and phi values
	works just like spherical coordinates
	"""
	def turn_range(self, minTheta, minPhi, maxTheta, maxPhi):
		dTheta, dPhi = random.random()*(float(maxTheta)-float(minTheta))+float(minTheta), random.random()*(float(maxPhi)-float(minPhi))+float(minPhi)
		self.turn(dTheta,dPhi)
		
	"""
	turns the pen at the current x,y,z position at a random angle based on the normal distribution given by the given mean and standard deviations of theta and phi
	works just like spherical coordinates
	"""
	def turn_normal(self, meanTheta, stdevTheta, meanPhi, stdevPhi):
		dTheta, dPhi = random.normalvariate(float(meanTheta), float(stdevTheta)), random.normalvariate(float(meanPhi), float(stdevPhi))
		self.turn(dTheta, dPhi)
		
	"""
	turns the pen at the current x,y,z position at a random angle based on the gaussian distribution given by the given mean and standard deviations of theta and phi
	works just like spherical coordinates
	random.gauss is slightly faster than random.normalvariate but is not thread safe
	"""
	def turn_gauss(self, meanTheta, stdevTheta, meanPhi, stdevPhi):
		dTheta, dPhi = random.gauss(float(meanTheta), float(stdevTheta)), random.gauss(float(meanPhi), float(stdevPhi))
		self.turn(dTheta, dPhi)
		
	"""
	creates a dot at the current x,y,z position with a radius between the given minimum and maximum radii
	"""
	def draw_dot(self, minRadius, maxRadius):
		radius = float(minRadius) + (random.random()*(float(maxRadius)-float(minRadius)))
		x, y, z = self.__x, self.__y, self.__z
		# create dot in .pov file
		self.fileOut.write("sphere {\n<"+str(x)+", "+str(y)+", "+str(z)+">, "+str(radius))
		self.fileOut.write("\ntexture{"+ self.__color+"\n} \n \n finish{\ndiffuse 0.3\n ambient 0.0\nreflection 0.8}}\n\n\n")
		
	"""
	creates a dot at the current x,y,z position with a radius based on a normal distribution given by the given mean and standard deviation of the radius
	"""
	def draw_dot_normal(self, meanRadius, stdevRadius):
		radius = random.normalvariate(float(meanRadius), float(stdevRadius))
		x, y, z = self.__x, self.__y, self.__z
		# create dot in .pov file
		self.fileOut.write("sphere {\n<"+str(x)+", "+str(y)+", "+str(z)+">, "+str(radius))
		self.fileOut.write("\ntexture{"+ self.__color+"\n} \n \n finish{\ndiffuse 0.3\n ambient 0.0\nreflection 0.8}}\n\n\n")
		
	"""
	creates a dot at the current x,y,z position with a radius based on a gaussian distribution given by the given mean and standard deviation of the radius
	random.gauss is slightly faster than random.normalvariate but is not thread safe
	"""
	def draw_dot_gauss(self, meanRadius, stdevRadius):
		radius = random.gauss(float(meanRadius), float(stdevRadius))
		x, y, z = self.__x, self.__y, self.__z
		# create dot in pov file
		self.fileOut.write("sphere {\n<"+str(x)+", "+str(y)+", "+str(z)+">, "+str(radius))
		self.fileOut.write("\ntexture{"+ self.__color+"\n} \n \n finish{\ndiffuse 0.3\n ambient 0.0\nreflection 0.8}}\n\n\n")
		
	"""
	creates a cylinder of given height and radius parallel to the current heading
	"""
	def draw_cylinder(self, radius, height):
		theta,phi = self.__heading
		# creates cylinder in .pov file
		self.fileOut.write("cylinder {\n<"+str(self.__x)+", "+str(self.__y)+", "+str(self.__z)+">,<"+str(self.__x+float(height)*math.sin(theta*deg2rad)*math.cos(phi*deg2rad))+", "+str(self.__y+float(height)*math.sin(theta*deg2rad)*math.sin(phi*deg2rad))+", "+str(self.__z+float(height)*math.cos(theta*deg2rad))+">,"+str(radius))
		self.fileOut.write("\ntexture {\n"+self.__color+"\n}\n\nfinish{ ambient 0.1 }\n}\n\n\n")
		# sets the x,y,z position to the current x,y,z position plus the height of the cylinder
		self.__x, self.__y, self.__z = self.__x+float(height)*math.sin(theta*deg2rad)*math.cos(phi*deg2rad), self.__y+float(height)*math.sin(theta*deg2rad)*math.sin(phi*deg2rad), self.__z+float(height)*math.cos(theta*deg2rad)
		
	"""
	creates a cylinder of given height and radius perpendicular to the current heading
	"""
	def draw_cylinder_perp(self, radius, height):
		theta,phi = self.__heading
		# sets the center of the cylinder
		x, y, z = self.__x+float(radius)*math.sin(theta*deg2rad)*math.cos(phi*deg2rad), self.__y+float(radius)*math.sin(theta*deg2rad)*math.sin(phi*deg2rad), self.__z+float(radius)*math.cos(theta*deg2rad)
		# creates cylinder in .pov file
		self.fileOut.write("cylinder {\n<"+str(x+float(height)/2.0*math.sin((theta+90)*deg2rad)*math.cos((phi+90)*deg2rad))+", "+str(y+float(height)/2.0*math.sin((theta+90)*deg2rad)*math.sin((phi+90)*deg2rad))+", "+str(z+float(height)/2.0*math.cos((theta+90)*deg2rad))+">,<"+str(x-float(height)/2.0*math.sin((theta+90)*deg2rad)*math.cos((phi+90)*deg2rad))+", "+str(y-float(height)/2.0*math.sin((theta+90)*deg2rad)*math.sin((phi+90)*deg2rad))+", "+str(z-float(height)/2.0*math.cos((theta+90)*deg2rad))+">,"+str(radius))
		self.fileOut.write("\ntexture {\n"+self.__color+"\n}\n\nfinish{ ambient 0.1 }\n}\n\n\n")
		# sets the x,y,z position to the current x,y,z position plus the diameter of the cylinder
		self.__x, self.__y, self.__z = x+float(radius)*math.sin(theta*deg2rad)*math.cos(phi*deg2rad), y+float(radius)*math.sin(theta*deg2rad)*math.sin(phi*deg2rad), z+float(radius)*math.cos(theta*deg2rad)
		
	"""
	takes a snapshot of the current ray-traced image and saves it into the temporary directory
	"""
	def processFrame(self):
		self.fileOut.close()
		tempName = self.name
		self.animated = True
		# creates a temporary folder for all the images
		os.system("mkdir ./povrayContent/"+tempName)
		# creates the .pov files and images for each snap shot that is needed
		if self.ani_index<10:
			povname = "./povrayContent/"+tempName+"/tempPov.000"+str(self.ani_index)+".pov"
			pngname = "./povrayContent/"+tempName+"/tempPng.000"+str(self.ani_index)+".png"
		if self.ani_index>=10 and self.ani_index<100:
			povname = "./povrayContent/"+tempName+"/tempPov.00"+str(self.ani_index)+".pov"
			pngname = "./povrayContent/"+tempName+"/tempPng.00"+str(self.ani_index)+".png"
		if self.ani_index>=100:
			povname = "./povrayContent/"+tempName+"/tempPov.0"+str(self.ani_index)+".pov"
			pngname = "./povrayContent/"+tempName+"/tempPng.0"+str(self.ani_index)+".png"
		if self.ani_index>=1000:
			povname = "./povrayContent/"+tempName+"/tempPov."+str(self.ani_index)+".pov"
			pngname = "./povrayContent/"+tempName+"/tempPng."+str(self.ani_index)+".png"
		
		# copies the latest .pov file to the main directory
		os.system("cp povrayContent/testingPov."+tempName+".pov "+povname)
		self.updateCamera(povname)

		os.system("povray -I"+povname+" -O"+pngname+" +L/usr/share/povray-3.6/include +A +Q9 -J -H900 -W1600 +A -D ")
		os.system("rm "+povname)

		self.ani_index+=1
		self.fileOut = open("./povrayContent/testingPov."+tempName+".pov", 'a')
	
	"""
	lifts the pen up
	movement no longer draws splines
	"""
	def penup(self):
		self.__pendown=0
		
	"""
	puts the pen back down
	movement draws splines
	"""
	def pendown(self):
		self.__pendown=1
		
	"""
	sets the x position of the pen
	"""
	def setx(self, x):
		self.__x = float(x)
		
	"""
	sets the y position of the pen
	"""
	def sety(self, y):
		self.__y = float(y)
		
	"""
	sets the z position of the pen
	"""
	def setz(self, z):
		self.__z = float(z)
		
	"""
	sets the heading of the pen
	"""
	def seth(self, theta, phi):
		# values are modulo 360 because despite theta being between 0 and 180 or -90 and 90, there is no good way to represent -90 except by -90%360 = 270 while still having values like 630 be valid
		self.__heading = ((float(theta) % 360.0),(float(phi) % 360.0))
		
	"""
	sets the thickness of the pen
	"""
	def sett(self, thickness):
		self.__thickness = float(thickness)
		
	"""
	sets the thickness of the pen to a value between given minimum and maximum thicknesses
	"""
	def sett_range(self, minThickness, maxThickness):
		self.__thickness = random.random()*(float(maxThickness)-float(minThickness))+float(minThickness)
		
	"""
	sets the thickness of the pen based on a normal distribution given by the given mean and standard deviation
	"""
	def sett_normal(self, meanThickness, stdevThickness):
		self.__thickness = random.normalvariate(float(meanThickness), float(stdevThickness))
		
	"""
	sets the thickness of the pen based on a gaussian distribution given by the given mean and standard deviation
	random.gauss is slightly faster than random.normalvariate but is not thread safe
	"""
	def sett_gauss(self, meanThickness, stdevThickness):
		self.__thickness = random.gauss(float(meanThickness), float(stdevThickness))
		
	"""
	changes the thickness by adding the given value to the current thickness
	"""
	def change_t(self, delta_t):
		self.__thickness = self.__thickness+(float(delta_t))
		
	"""
	changes the thickness by the given percent of the current thickness
	"""
	def change_t_percent(self, percent):
		self.__thickness = self.__thickness*(float(percent)/100.0)
		
	"""
	sets the curvature of the pen
	0 gives straight lines
	larger values give curvier lines
	"""
	def set_curvature(self, curvature_in):
		self.__curvature = float(curvature_in)
		
	"""
	saves the current x,y,z position, heading, and thickness of the pen to the stack
	"""
	def save_point(self):
		self.__orientation_stack.append((self.__x, self.__y, self.__z, self.__heading, self.__thickness))
		
	"""
	pops the latest x,y,z position, heading, and thickness from the stack
	"""
	def restore_point(self):
		self.__x, self.__y, self.__z, self.__heading, self.__thickness = self.__orientation_stack.pop()
		
	"""
	restores x,y,z position, heading, and thickness from the beginning of the stack
	"""
	def restore_all_begin(self):
		self.__x, self.__y, self.__z, self.__heading, self.__thickness = self.__orientation_stack.pop(0)
		
	"""
	saves the current color to the stack
	"""
	def save_color(self):
		self.__colorStack.append(self.__color)
		
	"""
	pops the latest color from the stack
	"""
	def restore_color(self):
		self.__color = self.__colorStack.pop()
		
	"""
	restores the color from the beginning of the stack
	"""
	def restore_color_begin(self):
		self.__color = self.__colorStack.pop(0)
		
	"""
	sets the current color to a random color with given alpha value
	alpha value between 0 and 255 inclusive
	values less than 0 or greater than 255 will default to 0 or 255 respectively
	"""
	def set_color_random(self, f):
		if f<0:
			f = 0
		if f>255:
			f = 255
		red, green, blue, f = random.random(), random.random(), random.random(), float(f)/255.0
		self.__color = "pigment{rgbf <" + str(red) + "," + str(green) + "," + str(blue) + "," + str(f)+">}"
        
	"""
	sets the current color to a random color with given alpha value
	alpha value between 0 and 1 inclusive
	values less than 0 or greater than 1 will default to 0 or 1 respectively
	"""
	def set_color_dec_random(self, f):
		if f<0:
			f = 0
		if f>1:
			f = 1
		red, green, blue = random.random(), random.random(), random.random()
		self.__color = "pigment{rgbf <" + str(red) + "," + str(green) + "," + str(blue) + "," + str(f)+">}"
		
	"""
	sets the current color to a random color in given range with given alpha value
	all values between 0 and 255 inclusive
	values less than 0 or greater than 255 will default to 0 or 255 respectively
	"""
	def set_color_random_ranged(self, r1, g1, b1, f1, r2, g2, b2, f2):
		if r1<0:
			r1 = 0
		if g1<0:
			g1 = 0
		if b1<0:
			b1 = 0
		if f1<0:
			f1 = 0
		if r2<0:
			r2 = 0
		if g2<0:
			g2 = 0
		if b2<0:
			b2 = 0
		if f2<0:
			f2 = 0
		if r1>255:
			r1 = 255
		if g1>255:
			g1 = 255
		if b1>255:
			b1 = 255
		if f1>255:
			f1 = 255
		if r2>255:
			r2 = 255
		if g2>255:
			g1 = 255
		if b2>255:
			b2 = 255
		if f2>255:
			f2 = 255
		red, green, blue, f= random.random()*(float(r2)/255.0-float(r1)/255.0)+float(r1)/255.0, random.random()*(float(g2)/255.0-float(g1)/255.0)+float(g1)/255.0, random.random()*(float(b2)/255.0-float(b1)/255.0)+float(b1)/255.0, random.random()*(float(f1)/255.0-float(f2)/255.0)+float(f1)/255.0
		self.__color = "pigment{rgbf <" + str(red) + "," + str(green) + "," + str(blue) + "," + str(f)+">}"
		
	"""
	sets the current color to a random color in given range with given alpha value
	all values between 0 and 1 inclusive
	values less than 0 or greater than 1 will default to 0 or 1 respectively
	"""
	def set_color_dec_random_ranged(self, r1, g1, b1, f1, r2, g2, b2, f2):
		if r1<0:
			r1 = 0
		if g1<0:
			g1 = 0
		if b1<0:
			b1 = 0
		if f1<0:
			f1 = 0
		if r2<0:
			r2 = 0
		if g2<0:
			g2 = 0
		if b2<0:
			b2 = 0
		if f2<0:
			f2 = 0
		if r1>1:
			r1 = 1
		if g1>1:
			g1 = 1
		if b1>1:
			b1 = 1
		if f1>1:
			f1 = 1
		if r2>1:
			r2 = 1
		if g2>1:
			g1 = 1
		if b2>1:
			b2 = 1
		if f2>1:
			f2 = 1
		red, green, blue, f= random.random()*(float(r2)-float(r1))+float(r1), random.random()*(float(g2)-float(g1))+float(g1), random.random()*(float(b2)-float(b1))+float(b1), random.random()*(float(f1)-float(f2))+float(f1)
		self.__color = "pigment{rgbf <" + str(red) + "," + str(green) + "," + str(blue) + "," + str(f)+">}"
		
	"""
	sets the current color based on the given red, green, blue, and alpha values
	all values between 0 and 255 inclusive
	values less than 0 or greater than 255 will default to 0 or 255 respectively
	"""
	def set_color(self, red, green, blue, f):
		if red<0:
			red = 0
		if green<0:
			green = 0
		if blue<0:
			blue = 0
		if f<0:
			f = 0
		if red>255:
			red = 255
		if green>255:
			green = 255
		if blue>255:
			blue = 255
		if f>255:
			f = 255
		red, green, blue, f = float(red)/255.0, float(green)/255.0, float(blue)/255.0, float(f)/255.0
		self.__color = "pigment{rgbf <" + str(red) + "," + str(green) + "," + str(blue) + "," + str(f)+">}"

	"""
	sets the current color based on the given red, green, blue, and alpha values
	all values between 0 and 1 inclusive
	values less than 0 or greater than 1 will default to 0 or 1 respectively
	"""
	def set_color_dec(self, red, green, blue, f):
		red, green, blue, f = float(red), float(green), float(blue), float(f)
		if red<0:
			red = 0
		if blue<0:
			blue = 0
		if green<0:
			green = 0
		if f<0:
			f = 0
		if red>1:
			red = 1
		if blue>1:
			blue = 1
		if green>1:
			green = 1
		if f>1:
			f = 1
		self.__color = "pigment{rgbf <" + str(red) + "," + str(green) + "," + str(blue) + "," + str(f)+">}"
		
	"""
	alters the current color by adding the given red, green, blue, and alpha values to the current color
	all values are between 0 and 255
	"""
	def alter_color(self, r_in, g_in, b_in, f_in):
		try:
			Dred, Dgreen, Dblue, Dfilter = float(r_in)/255.0, float(g_in)/255.0, float(b_in)/255.0, float(f_in)/255.0
			red, green, blue, f = self.getRGB(self.__color)
			self.set_color_dec((float(red)+Dred),(float(green)+Dgreen),(float(blue)+Dblue), (float(f)+Dfilter))
		except Exception, val:
			print val
			
	"""
	alters the current color by adding the given red, green, blue, and alpha values to the current color
	all values are between 0 and 1
	"""
	def alter_color_dec(self, r_in, g_in, b_in, f_in):
		try:
			Dred, Dgreen, Dblue, Dfilter = float(r_in), float(g_in), float(b_in), float(f_in)
			red, green, blue, f = self.getRGB(self.__color)
			self.set_color_dec((float(red)+Dred),(float(green)+Dgreen),(float(blue)+Dblue), (float(f)+Dfilter))
		except Exception, val:
			print val
		
	"""
	sets the texture to the given texture name
	you cannot have a color and a texture at the same time
	"""
	def set_texture(self, textureIn):
		self.__color = textureIn
		
	"""
	gets the current red, green, blue, and alpha values
	"""
	def getRGB(self, color):
		color = color.strip('pigment{rgbf <>}')
		colors = color.split(',')
		return colors
		
	"""
	compiles all created images into an avi if animated otherwise a single image
	"""
	def wrapup(self, name):
		self.fileOut.close()
		if self.animated:
			os.system("ffmpeg -qscale 4 -r 18 -b 9600 -i ./povrayContent/"+self.name+"/tempPng.%04d.png "+name)
			
		if not self.animated:
			os.system("mv povrayContent/testingPov." + self.name +".pov ./povrayContent/" + name + ".pov")
			os.system("povray -I./povrayContent/" + name + ".pov -O./" + name + " +A +Q9 -J -H500 -W500 -D")
			self.__init__()
