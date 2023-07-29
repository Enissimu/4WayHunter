import pygame
import sys
from imageLoader import *
from player import player	
from trajectory import trajectory
from pawn import pawn
from random import randrange
class win(object):
	def __init__(self,windowWidth,windowHeight):
		self.windowHeight=windowHeight
		self.windoWidth=windowWidth

		self.win=pygame.display.set_mode((self.windoWidth,self.windowHeight))
		self.font = pygame.font.SysFont("comicsans", 30, True)
		self.player=player()

		self.runs()
	

	def redrawGameWindow(self,bullets,pawns,start):
		self.win.blit(backgrounds[0], (0,0))
		text = self.font.render("Score: "+str(self.player.score), 1, (0,0,0)) 
		self.win.blit(text, (225, 10))
		self.player.drawHitbox(self.win)
		self.player.updateHealthBar()
		pygame.draw.rect(self.win,(255,0,0),self.player.hpBar)
		if not start:
			text = self.font.render("Shoot once and press b to start", False, (255,255,255)) 
			self.win.blit(text, (250, 240))

		if  self.player.health<0:
			text = self.font.render("Press R to Respawn", False, (255,255,255)) 
			self.win.blit(text, (250, 240))
		else:
			pass
		if len(pawns):
			for i in pawns:
				i.draw(self.win)
		if self.player.shot>0:

			#self.win.blit(shootAnim[0], self.player.getPlayerXY()) SHOOT ANIMATION GET THE PROJECTILE FROM ORIGINAL PNGS PLACE IT ACCORDING TO WHETEVR IF ITS LEFT OR RIGHGT
			for bullet in bullets:
				bullet.draw(self.win)
		if self.player.standCount+1>=40:
			self.player.resetStandCount()
		if self.player.walkCount+1>=40:
			self.player.resetWalkCount()
		if self.player.left:#leftd

			self.win.blit(leftAnim[self.player.walkCount//5], self.player.getPlayerXY())
			self.player.incrementWalkCount()
		elif  self.player.right:#right
			self.win.blit(rightAnim[self.player.walkCount//5], self.player.getPlayerXY())
			self.player.incrementWalkCount()
		else:
			self.win.blit(idleAnim[self.player.standCount//8], self.player.getPlayerXY())
			self.player.incrementStandCount()
		#idle
		pygame.display.update()

	def runs(self):
		DASHRES=pygame.USEREVENT+1
		PAWNSPAWN=pygame.USEREVENT+2
		pygame.time.set_timer(DASHRES,5000)
		pygame.time.set_timer(PAWNSPAWN,100)
		on=True
		clock = pygame.time.Clock()
		pawns=[]
		bullets=[]
		start=False
		#VARIABLES
		
		veloc=self.player.vel
		width,height=self.player.width,self.player.height
	




		#pygame_icon = pygame.image.load('others/damaged0.png')
		#pygame.display.set_icon(pygame_icon)

		pygame.display.set_caption("4WayHunter")
	

		while on:
			clock.tick(40)

			for event in pygame.event.get():
				if event.type==pygame.MOUSEBUTTONDOWN and self.player.health>0:
					bullet=trajectory(self.player.x+3,self.player.y,self.player.left,self.player.right)
					bullet.vectoralDirection(pygame.mouse.get_pos(),125)
					bullets.append(bullet)
					self.player.incrementShot()
				if event.type==PAWNSPAWN and start:
					if randrange(0,10)<6 and len(pawns)<20:
						randx,randy=randrange(0,self.windoWidth),randrange(0,self.windowHeight)

						if(randx==self.player.x   and self.player.y==randy):
								pass
						pawnE=pawn(randx,randy)
						pawnE.setDirect(self.player.x,self.player.y)
						pawns.append(pawnE)

				if event.type== pygame.QUIT:
					on=False
					pygame.quit()
					quit()




			keys=pygame.key.get_pressed()

			if self.player.health<0  and keys[pygame.K_r]:
				self.player.resetHealth()
				self.player.resetScore()
				bullets.clear()
				pawns.clear()




			for j in pawns:
				if (j.x < self.windoWidth and j.x > 0 ) and (j.y<self.windowHeight and j.y>0):
					j.vectoralDirection(self.player.getPlayerXY(),49)
					j.move()
					if pygame.Rect.colliderect(self.player.rect,j.rect):
						self.player.decreaseHealth()
				else:
					pawns.pop(pawns.index(j))
			if self.player.shot>0:
				for i in bullets:
					if (i.x < self.windoWidth and i.x > 0 ) and (i.y<self.windowHeight and i.y>0):
						i.move()
						for j in pawns:
							if pygame.Rect.colliderect(i.rect,j.rect):
								pawns.pop(pawns.index(j))
								bullets.pop(bullets.index(i))
								self.player.incrementScore()
								break
					else:
						bullets.pop(bullets.index(i))

			#PLAYER MOVE

			if keys[pygame.K_b]:
				start=True 

			if keys[pygame.K_a] and self.player.x>veloc:
					self.player.toLeft()
					self.player.leftTrue()
					self.player.rightFalse() 
					self.player.incrementWalkCount()


			elif keys[pygame.K_d] and self.player.x<self.windoWidth-width - veloc:
					self.player.toRight()
					self.player.leftFalse()
					self.player.rightTrue()
					self.player.incrementWalkCount()

			else:
				self.player.resetWalkCount()
				self.player.rightFalse()
				self.player.leftFalse()

			if keys[pygame.K_s] and self.player.y<self.windowHeight-height-veloc:
					self.player.toDown()
					self.player.incrementWalkCount()
					self.player.rightTrue()

			if keys[pygame.K_w] and self.player.y>veloc:
				self.player.toUp()
				self.player.incrementWalkCount()
				self.player.rightTrue()
			self.redrawGameWindow(pawns,bullets,start)












