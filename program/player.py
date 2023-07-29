from coordinates import coordinates
import pygame
class player(coordinates):
    def __init__( self):
        coordinates.__init__(self,50,50)
        self.width=22
        self.height=30
        self.vel=10
        self.left=False
        self.right=False
        self.walkCount=0
        self.standCount=0
        self.shot=0
        self.score=0
        self.health=100
        self.hpBar=pygame.Rect(0,900,1280,10)
        self.rect=pygame.Rect(self.x+10,self.y,self.width,self.height)




    def resetHealth(self):
        self.health=200
    def decreaseHealth(self):
        self.health-=1

    def rectOfPlayer(self):
        return (self.x,self.y,self.width,self.height)


    def drawHitbox(self,win):
        self.rect.update(self.x-10,self.y+5,18,18)

    #ANIMATION WALKCOUNT
    def resetWalkCount(self):
        self.walkCount=0
    def incrementWalkCount(self):
        self.walkCount+=1
    def incrementStandCount(self):
        self.standCount+=1
    def resetStandCount(self):
        self.standCount=0
    def getPlayerXY(self):
        return (self.x,self.y)


    #MOVEMENT FUNCTİONS    
    def toLeft(self):
        self.x-=self.vel
    def toRight(self):
        self.x+=self.vel
    def toUp(self):
        self.y-=self.vel
    def toDown(self):
        self.y+=self.vel

        
    def dashToLeft(self):
        self.x-=30
        self.dashTrue()
    def dashToRight(self):
        self.x+=30
        self.dashTrue()

    def dashToUp(self):
        self.y-=30
        self.dashTrue()

    def dashToDown(self):
        self.y+=30
        self.dashTrue()

    def leftTrue(self):
        self.left=True
    def leftFalse(self):
        self.left=False
    def rightTrue(self):
        self.right=True
    def rightFalse(self):
        self.right=False

    def incrementShot(self):
        self.shot+=1

    def incrementScore(self):
        self.score+=1

    def resetScore(self):
        self.score=0

    def updateHealthBar(self):
        updatedBar=128/10*self.health
        self.hpBar.update(0,900,updatedBar,10)