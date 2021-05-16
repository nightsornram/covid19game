import pygame
import math
import random
import csv

pygame.init()

screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('Covid 19')
icon = pygame.image.load('icon.png')
covid = pygame.image.load('coronavirus.png')
pygame.display.set_icon(icon)
WIDTH = 1000
HEIGHT = 800

bg = pygame.image.load('bg.png')
start_time = None

############PLAYER############
psize = 128
heart = 3
pimage = pygame.image.load('hand.png')
px = 400
py = HEIGHT-psize
pspeed = 0


def Player(x,y):
	screen.blit(pimage,(x,y))




############ENEMY#############
esize = 128
eimage = pygame.image.load('man.png')
ex = 50
ey = 0
espeed = 5

def Enemy(x,y):
	screen.blit(eimage,(x,y))

##########BOSS###############

bsize = 256
bimage = pygame.image.load('boss.png')
bx = 300
by = 0
bspeed = 5
heartboss = 10

def Boss(x,y):
	screen.blit(bimage,(x,y))


############MULTI ENEMY#############
exlist = []
eylist = []
espeedlist = []
allenemy = 3

for i in range(allenemy):
	exlist.append(random.randint(esize ,WIDTH - esize))
	eylist.append(random.randint(0,100))
	#espeedlist.append(random.randint(1,3))
	espeedlist.append(5)

##########POTION############
poimage = pygame.image.load('potion.png')
posize = 128
pox = random.randint(posize,WIDTH-posize)
poy = 0
pospeed = 5
potiondrop = False
speedlv1 = False
speedlv2 = False
speedlv3 = False

def Potion(x,y):
	screen.blit(poimage,(x,y))

#############MASK#############
msize = 64
mimage = pygame.image.load('mask.png')
mx = -1000
my = -1000
mspeed = 40
mstate = 'ready'

def Fire_Mask(x,y):
	global mstate
	mstate = 'fire'
	screen.blit(mimage,(x,y))

##########COLLISION###################
def isCollision(ecx,ecy,mcx,mcy):
	distance = math.sqrt(math.pow(ecx - mcx,2)+math.pow(ecy - mcy,2))
	if distance < msize + esize:
		return True
	else:
		return False

#########SCORE##########
allscore = 0
font = pygame.font.Font('angsana.ttc',60)
savescore = True

def ShowScore():
	score = font.render('คะแนน: {} คะแนน'.format(allscore),True,(255,255,255))
	heartscore = font.render('หัวใจ: {} ดวง'.format(heart),True,(255,255,255))
	screen.blit(score,(50,10))
	screen.blit(heartscore,(750,10))


###########SHOW TIME###############

counttime = True
resettime = False
besttimelist = []

def ShowTime():
	millis=ticks%1000
	seconds=int(ticks/1000 % 60)
	minutes=int(ticks/60000 % 24)
	out=font.render('{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds),True,(255,255,255))
	screen.blit(out,(50,80))

###########SHOW BEST TIME############### 
def ShowBestTime():
	mil=besttime%1000
	sec=int(besttime/1000 % 60)
	minu=int(besttime/60000 % 24)
	bt=font.render('BestTime : {minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minu, millis=mil, seconds=sec),True,(255,255,255))
	screen.blit(bt,(360,600))

###########SOUND###########

pygame.mixer.music.load('virus.wav')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
laser = pygame.mixer.Sound('laser.wav')
gameoversound = pygame.mixer.Sound('gameover.wav')
winsound = pygame.mixer.Sound('win.wav')

#########SAVE SCORE###########
def SaveScore():
	with open('score.csv', 'a') as file:
		writer = csv.writer(file, lineterminator = "\n")
		writer.writerow([outtext,str(ticks)])


############WIN#############
win = False
trophy = pygame.image.load('trophy.png')
playsoundwin = False
def Win():
	global playsoundwin
	global counttime
	screen.fill((57, 166, 137))
	screen.blit(trophy,(370,70))
	quittext = font.render('Quit',True,(0,0,0))

	if 400 <= mouse[0] <= 600 and 400 <= mouse[1] <= 500:
		pygame.draw.rect(screen,(0,0,0),[390,390,220,120]) 
		pygame.draw.rect(screen,(211, 0, 84),[400,400,200,100]) 
	else:
		pygame.draw.rect(screen,(0,0,0),[390,390,220,120]) 
		pygame.draw.rect(screen,(255, 0, 92),[400,400,200,100])

	screen.blit(quittext , (455,400))

	if playsoundwin == False:
		winsound.play()
		playsoundwin = True
	if counttime == True:
		counttime = False
	



##########GAME OVER#########
start = False
playsound = False
gameover = False
nstate = False
fontover = pygame.font.Font('angsana.ttc',100)
gimage = pygame.image.load('gameover.png')
def GameOver():
	global playsound
	global nstate
	global counttime
	screen.fill((255, 174, 0))
	screen.blit(gimage,(370,70))
	restart = font.render('Restart',True,(0,0,0))
	if 400 <= mouse[0] <= 600 and 400 <= mouse[1] <= 500:
		pygame.draw.rect(screen,(0,0,0),[390,390,220,120]) 
		pygame.draw.rect(screen,(211, 0, 84),[400,400,200,100]) 
	else:
		pygame.draw.rect(screen,(0,0,0),[390,390,220,120]) 
		pygame.draw.rect(screen,(255, 0, 92),[400,400,200,100])

	screen.blit(restart , (447,400))

	if playsound == False:
		gameoversound.play()
		playsound = True
	if nstate == False:
		nstate = True
	if counttime == True:
		counttime = False



starttext = font.render('Start' , True , (0,0,0))

running = True

clock = pygame.time.Clock()
FPS = 30

while running:
	screen.blit(bg,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			running = False

		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_LEFT and start == True:
				if speedlv3 == True:
					mspeed = 70
					pspeed = -23
				elif speedlv2 == True:
					mspeed = 60
					pspeed = -16
				elif speedlv1 == True:
					mspeed = 50
					pspeed = -13
				else:
					mspeed = 40
					pspeed = -10
			if event.key == pygame.K_RIGHT and start == True:
				if speedlv3 == True:
					mspeed = 70
					pspeed = 23
				elif speedlv2 == True:
					mspeed = 60
					pspeed = 16
				elif speedlv1 == True:
					mspeed = 50
					pspeed = 13
				else:
					mspeed = 40
					pspeed = 10

			if event.key == pygame.K_SPACE and start == True:
				if mstate == 'ready':
					laser.play()
					mx = px + 25
					my = HEIGHT-psize
					Fire_Mask(mx,my)

				
			

		if event.type == pygame.KEYUP and start == True :
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				pspeed = 0

		if event.type == pygame.MOUSEBUTTONDOWN:

			if 390 <= mouse[0] <= 610 and 390 <= mouse[1] <= 510 and nstate == False:
				start = True
			if 390 <= mouse[0] <= 610 and 390 <= mouse[1] <= 510 and nstate == True:
				playsound = False
				gameover = False
				allscore = 0
				heart = 3
				ex = random.randint(esize ,WIDTH - esize)
				ey = 0
				espeed = 5
				counttime = True
				resettime = True
				pspeed = 10
				potiondrop = False
				heartboss = 10
				speedlv1 = False
				speedlv2 = False
				speedlv3 = False
				by = 0
				poy = 0
				for i in range(allenemy):
					exlist.append(random.randint(esize ,WIDTH - esize))
					eylist.append(random.randint(0,100))
					espeedlist[i] = 5
				nstate = False
			if 390 <= mouse[0] <= 610 and 390 <= mouse[1] <= 510 and win == True:
				running = False



	mouse = pygame.mouse.get_pos()

	if start == False:
		with open('score.csv', mode='r') as csv_file:
			csv_reader = csv.DictReader(csv_file)
			line_count = 0
			for row in csv_reader:
				if line_count == 0:
					line_count += 1
				besttimelist.append(int(row['ticks']))
				line_count += 1
			besttime = min(besttimelist)
		

		screen.fill((35,62,139))
		screen.blit(covid,(360,50))
		ShowBestTime()
		if 400 <= mouse[0] <= 600 and 400 <= mouse[1] <= 500:
			pygame.draw.rect(screen,(0,0,0),[390,390,220,120]) 
			pygame.draw.rect(screen,(30, 174, 152),[400,400,200,100]) 
		else:
			pygame.draw.rect(screen,(0,0,0),[390,390,220,120]) 
			pygame.draw.rect(screen,(169, 241, 223),[400,400,200,100])

		screen.blit(starttext , (460,400))
		tickstart = pygame.time.get_ticks()


	if start == True:
	###############PLAYER################
		if resettime:
			tickstart = pygame.time.get_ticks()
		if counttime:
			tickstart2 = pygame.time.get_ticks()
			ticks = tickstart2 - tickstart
			resettime = False

		Player(px,py)

		if px <= 0:
			px = 0
			px += pspeed
		elif px >= WIDTH - psize:
			px = WIDTH - psize
			px += pspeed
		else:
			px += pspeed

	###############ENEMY################
		#for i in range(5):
			#Enemy(ex + (i*150),ey)
		#ey += espeed 
		if heart <= 0:
			ey = 1000
			for i in range(allenemy):
				eylist[i] = 1000
			GameOver()
			gameover = True

		if heartboss == 0:
			by = 1000
			if savescore:
				millis=ticks%1000
				seconds=int(ticks/1000 % 60)
				minutes=int(ticks/60000 % 24)
				outtext='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
				SaveScore()
				savescore = False
			Win()
			win = True

		if allscore >= 10 and allscore < 30:
			if potiondrop == True:
				pass
			else: 
				Potion(pox,poy)
				poy += pospeed 
				collisionpotion = isCollision(pox,poy,mx,my)
				if collisionpotion:
					speedlv1 = True
					my = HEIGHT-psize
					mstate = 'ready'
					poy = 0
					pox = random.randint(posize ,WIDTH - posize)
					potiondrop = True

		if allscore >= 30 and allscore < 50:
			if potiondrop == False:
				pass
			else: 
				Potion(pox,poy)
				poy += pospeed 
				collisionpotion = isCollision(pox,poy,mx,my)
				if collisionpotion:
					speedlv2 = True
					my = HEIGHT-psize
					mstate = 'ready'
					poy = 0
					pox = random.randint(posize ,WIDTH - posize)
					potiondrop = False

		if allscore >= 50 and allscore < 60:
			if potiondrop == True:
				pass
			else: 
				Potion(pox,poy)
				poy += pospeed 
				collisionpotion = isCollision(pox,poy,mx,my)
				if collisionpotion:
					speedlv3 = True
					my = HEIGHT-psize
					mstate = 'ready'
					poy = 0
					pox = random.randint(posize ,WIDTH - posize)
					potiondrop = True
				

		if allscore < 20:
			if ey > HEIGHT-esize and gameover == False and win == False:
				heart -= 1
				ex = random.randint(esize ,WIDTH - esize)
				ey = 0
			Enemy(ex ,ey)
			ey += espeed 
			collision = isCollision(ex,ey,mx,my)
			if collision:
				allscore += 1
				my = HEIGHT-psize
				mstate = 'ready'
				ey = 0
				ex = random.randint(esize ,WIDTH - esize)
				espeed += 0.25
	###############MULTI ENEMY#############
		
		if allscore >= 20 and allscore <= 50: 
			for i in range(allenemy):
				if eylist[i] > HEIGHT-esize and gameover == False and win == False:
					heart -= 1
					for i in range(allenemy):
						eylist[i] = random.randint(0,100)

				eylist[i] += espeedlist[i]
				collisionmulti = isCollision(exlist[i],eylist[i],mx,my)
				if collisionmulti:
					allscore += 1
					my = HEIGHT-psize
					mstate = 'ready'
					eylist[i] = random.randint(0,100)
					exlist[i] = random.randint(esize ,WIDTH - esize)
					espeedlist.append(0.25)
				Enemy(exlist[i],eylist[i])


		if allscore > 50:
			if by > HEIGHT-100 and gameover == False and win == False:
				heart -= 3
			by += bspeed 
			collisionboss = isCollision(bx,by,mx,my)
			if collisionboss:
				allscore += 1
				my = HEIGHT-psize
				mstate = 'ready'
				by = 0
				bx = random.randint(esize ,WIDTH - esize)
				bspeed += 1
				heartboss -= 1
			Boss(bx,by)


		if mstate == 'fire':
			Fire_Mask(mx,my)
			my -= mspeed

		if my <= 0 :
			my = HEIGHT-psize
			mstate = 'ready'



		ShowScore()
		ShowTime()
	pygame.display.update()
	
	clock.tick(FPS)