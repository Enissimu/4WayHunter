import os, sys
import pygame

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from imageLoader import traject

from coordinates import coordinates

class trajectory(coordinates):
	def __init__(self,x,y,left,right):
		coordinates.__init__(self,x,y)
		self.left=left
		self.right=right
		self.directx=0
		self.directy=0
		self.hitbox=(self.x-10,self.y+5,18,18)
		self.rect=pygame.Rect(self.x-10,self.y+5,18,18)

	def draw(self,win):
		self.rect.update(self.x-10,self.y+5,18,18)
		win.blit(traject,(self.x-8,self.y+8))
