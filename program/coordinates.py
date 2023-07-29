from math import sqrt

class coordinates(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.directy=0
		self.directx=0
		self.walkCount=0

	def returnXY(self):
		return (self.x,self.y)
	
	def move(self):
		self.x+=self.directx
		self.y+=self.directy

	def vectoralDirection(self,direct,vel):	
		movex=self.x-direct[0]
		movey=self.y-direct[1]#100=y^2*float^2+y^2    200=y'2(float'2+1)  # x/y = (movex/movey)float x=y*float
		try:
			ratio=(movex/movey)		
			if movey<0:
				self.directy=sqrt(vel/( pow(ratio,2)+1))
				self.directx=self.directy*ratio
			else:
				self.directy=-sqrt(vel/( pow(ratio,2)+1))
				self.directx=self.directy*ratio
		except Exception as e:
			print("you got hit")