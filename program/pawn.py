from coordinates import coordinates
import os, sys
import pygame



parent = os.path.abspath('.')
sys.path.insert(1, parent)

from imageLoader import pawnImage


parent = os.path.abspath('.')
sys.path.insert(1, parent)

class pawn(coordinates):
	def __init__(self,x,y):
		coordinates.__init__(self,x,y)
		self.vel=8
		self.direct=0
		self.width=30
		self.height=40
		self.hitbox=(self.x-5,self.y,self.width,self.height)
		self.rect=pygame.Rect(self.x-10,self.y+5,self.height,self.width)




	def draw(self,win):
		self.rect.update(self.x-5,self.y,self.width,self.height)
		win.blit(pawnImage, self.returnXY())

	def setDirect(self,x,y):
		self.direct=0
