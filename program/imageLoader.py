import os
import pygame
cwd = os.getcwd()
upCwd=os.path.abspath(os.path.join(cwd, os.pardir))
dir_list = os.listdir(upCwd+"/others")
os.chdir(upCwd)
backgrounds,leftAnim,rightAnim,deathAnim,idleAnim=([] for i in range(5))
for i in dir_list:
	i="others/"+i
	if("bglight" in i):
		backgrounds.append(pygame.image.load(i))
	if("movel" in i):
		leftAnim.append(pygame.image.load(i))
	elif("mover" in i):
		rightAnim.append(pygame.image.load(i))
	elif("death" in i):
		deathAnim.append(pygame.image.load(i))
	elif("idle" in i):	
		idleAnim.append(pygame.image.load(i))	
pygame.init()
traject=pygame.image.load('others/trajectory.png')
pawnImage=pygame.image.load('others/pawn.png')

