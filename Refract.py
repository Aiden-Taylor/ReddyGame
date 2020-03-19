import pygame, sys, random, time, math
from pygame.locals import *
pygame.init()

#setup
area = pygame.display.set_mode((800, 600))
red=(255, 0, 0)
black=(0, 0, 0)
blu=(11, 99, 239)
orange=(255, 200, 0)
white=(255, 255, 255)
yellow=(255, 238, 0)
dedred=(130, 0, 0)
diamond=(160, 160, 160)
glass=(139, 160, 193)
fps = 30
clock=pygame.time.Clock()
run=True
x=100
y=100
a=0
b=0
c=0
d=0
one=0
two=0
three=0
four=0
count=0
count2=0
count3=0
count4=0
countinvin=0
angle=0
ratio=1/1.5
start=0
diff=50
lives=5
location=0
heart=pygame.image.load("heart.png")
josh= pygame.image.load("josh.png")
josh2=pygame.image.load("josh2.png")
pygame.display.set_caption('Reddy For School')
pygame.display.set_icon(heart)

#def text/input
def text_objects(text, font, color):
  textSurface = font.render(text, True, color)
  return textSurface, textSurface.get_rect()
def display_message_corner(text, size, xcoord, ycoord, color):
  largeText = pygame.font.Font('freesansbold.ttf',size)
  TextSurf, TextRect = text_objects(text, largeText, color)
  TextRect.topleft = (xcoord,ycoord)
  area.blit(TextSurf, TextRect)
  pygame.display.update()
def display_message_center(text, size, xcoord, ycoord, color):
  largeText = pygame.font.Font('freesansbold.ttf',size)
  TextSurf, TextRect = text_objects(text, largeText, color)
  TextRect.center = (xcoord,ycoord)
  area.blit(TextSurf, TextRect)
  pygame.display.update()
def wait_for_input():
  pygame.event.get()
  i=False
  while i==False:
    time.sleep(.1)
    for event in (pygame.event.get()):
      if event.type==KEYDOWN:
        i=True
      if event.type==QUIT:
        pygame.quit()
        sys.exit()

#init game
display_message_center("Are You REDDY For School?", 50, 400, 300, white)
time.sleep(1)
display_message_center("(Use arrow keys & enter)", 25, 400, 350, white)
wait_for_input()
area.fill(black)
display_message_corner("Difficulty:", 25, 0, 0, white)
i=False
display_message_corner("Easy", 25, 0, 45, white)
display_message_corner("Medium", 25, 100, 45, white)
display_message_corner("Hard", 25, 250, 45, white)

#Choosing diff
while i==False:
  for event in pygame.event.get():
    if event.type==KEYDOWN and event.key==K_LEFT:
      location+=-1
      if location>3:
        location=1
      if location<1:
        location=3
    if event.type==KEYDOWN and event.key==K_RIGHT:
      location+=1
      if location>3:
        location=1
      if location<1:
        location=3
    if location==1:
      display_message_corner("Easy", 25, 0, 45, yellow)
      display_message_corner("Medium", 25, 100, 45, white)
      display_message_corner("Hard", 25, 250, 45, white)
    if location==2:
      display_message_corner("Medium", 25, 100, 45, yellow)
      display_message_corner("Easy", 25, 0, 45, white)
      display_message_corner("Hard", 25, 250, 45, white)
    if location==3:
      display_message_corner("Hard", 25, 250, 45, yellow)
      display_message_corner("Easy", 25, 0, 45, white)
      display_message_corner("Medium", 25, 100, 45, white)
    if location==0:
      display_message_corner("Easy", 25, 0, 45, white)
      display_message_corner("Medium", 25, 100, 45, white)
      display_message_corner("Hard", 25, 250, 45, white)
    if event.type==KEYDOWN and event.key==K_RETURN and location!=0:
      i=True
if location==1:
  display_message_corner("You chose: Easy", 25, 0, 95, white)
  diff=50
elif location==3:
  display_message_corner("You chose: Hard", 25, 0, 95, white)
  diff=10
else:
  display_message_corner("You chose: Medium", 25, 0, 95, white)
  diff=25
location=0

#story
wait_for_input()
area.fill(black)
display_message_corner("One Day... Josh Awakens From His Slumber", 25, 0, 0, white)
wait_for_input()
display_message_corner("As he prepares for the day, something seems off...", 25, 0, 25, white)
wait_for_input()
display_message_corner("He feels... shorter", 25, 0, 50, white)
wait_for_input()
display_message_corner("Has he been shrinking?", 25, 0, 75, white)
wait_for_input()
display_message_corner("Oh Well.", 100, 0, 100, white)
wait_for_input()
area.fill(black)
display_message_corner("On his way to school, he feels something at the pit of his stomach", 25, 0, 0, white)
wait_for_input()
display_message_corner("The streets are eerily empty...", 25, 0, 25, white)
wait_for_input()
display_message_corner("Oh Well.", 100, 0, 100, white)
wait_for_input()
area.fill(black)
display_message_corner("Once he gets to school, there are strikingly few students", 25, 0, 0, white)
wait_for_input()
display_message_corner("Perhaps there's a walkout today.", 25, 0, 25, white)
wait_for_input()
display_message_corner("Oh Well.", 100, 0, 100, white)
wait_for_input()
area.fill(black)
display_message_corner("The bell rings.", 50, 0, 0, white)
wait_for_input()
display_message_corner("Josh starts on his way to class.", 25, 0, 50, white)
wait_for_input()
area.fill(black)
display_message_corner("He trips as he's walking to V48", 25, 0, 0, white)
wait_for_input()
display_message_corner("It's as if the universe doesn't want him to go...", 25, 0, 25, white)
wait_for_input()
display_message_corner("Oh Well.", 100, 0, 100, white)
wait_for_input()
area.fill(black)
display_message_corner("He enters the room at the same time as Joey Palacios", 25, 0, 0, white)
wait_for_input()
display_message_corner("This seems like a bad sign...", 25, 0, 25, white)
wait_for_input()
display_message_corner("Oh Well.", 100, 0, 100, white)
wait_for_input()
area.fill(black)
display_message_corner('As Mr. Clarion sees Joey, he immediately yells "You are killing me, Joey!"', 20, 0, 0, white)
wait_for_input()
display_message_corner("What do you pick up?", 25, 0, 20, white)
wait_for_input()
display_message_corner("Water Bottle", 25, 0, 45, white)
display_message_corner("Glass Bust of Clarion's Head... Dont't ask", 25, 250, 45, white)
display_message_corner("Huge Diamond", 25, 150, 70, white)

#choosing I.O.R
i=False
while i==False:
  for event in pygame.event.get():
    if event.type==KEYDOWN and event.key==K_RIGHT:
      location=-1
    if event.type==KEYDOWN and event.key==K_LEFT:
      location=1
    if event.type==KEYDOWN and event.key==K_DOWN:
      location=2
    if location==1:
      display_message_corner("Water Bottle", 25, 0, 45, yellow)
      display_message_corner("Glass Bust of Clarion's Head... Dont't ask", 25, 250, 45, white)
      display_message_corner("Huge Diamond", 25, 150, 70, white)
    if location==-1:
      display_message_corner("Glass Bust of Clarion's Head... Dont't ask", 25, 250, 45, yellow)
      display_message_corner("Water Bottle", 25, 0, 45, white)
      display_message_corner("Huge Diamond", 25, 150, 70, white)
    if location==2:
      display_message_corner("Huge Diamond", 25, 150, 70, yellow)
      display_message_corner("Water Bottle", 25, 0, 45, white)
      display_message_corner("Glass Bust of Clarion's Head... Dont't ask", 25, 250, 45, white)
    if location==0:
      display_message_corner("Water Bottle", 25, 0, 45, white)
      display_message_corner("Glass Bust of Clarion's Head... Dont't ask", 25, 250, 45, white)
      display_message_corner("Huge Diamond", 25, 150, 70, white)
    if event.type==KEYDOWN and event.key==K_RETURN and location!=0:
      i=True
if location==1:
  display_message_corner("You chose: Water Bottle", 25, 0, 95, white)
  ratio=1/1.3
  color=blu
  trans=0
elif location==2:
  display_message_corner("You chose: Huge Diamond", 25, 0, 95, white)
  ratio=1/2.4
  color=diamond
  trans=0
else:
  display_message_corner("You chose: Glass Bust of Clarion's Head", 25, 0, 95, white)
  ratio=1/1.5
  color=glass
  trans=100

#more story
wait_for_input()
area.fill(black)
display_message_corner("Mr. Clarion throws some lab equiptment at Joey...", 25, 0, 0, white)
wait_for_input()
display_message_corner("He misses! The battery hits you in the head 300 m/s", 25, 0, 25, white)
wait_for_input()
display_message_corner("As you lose  consciousness, you can't help but think to yourself...", 25, 0, 50, white)
wait_for_input()
display_message_corner("Oh Well.", 100, 0, 100, white)
wait_for_input()
area.fill(black)
display_message_corner("What?", 25, 0, 0, white)
wait_for_input()
area.blit(josh, (350,250))
pygame.display.update()
wait_for_input()
display_message_corner("You're tiny, trapped in the item you were holding!", 25, 0, 25, white)
wait_for_input()
area.fill(black)
display_message_corner("It appears that Mr. Clarion is shooting lasers at Joey now.", 25, 0, 0, white)
wait_for_input()
display_message_corner("DODGE.", 200, 0, 100, white)
wait_for_input()
area.fill(black)
while run==True: #Main Game Loop
  area.fill(black)
  pygame.draw.rect(area, color, (0, 150, 800, 450))
  count+=1
  count2+=1
  count3+=1
  countinvin+=1

#input management
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
      one=1
    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
      two=1
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
      three=1
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
      four=1
    if event.type == pygame.KEYUP and event.key==pygame.K_UP:
      one=0
    if event.type == pygame.KEYUP and event.key==pygame.K_DOWN:
      two=0
    if event.type == pygame.KEYUP and event.key==pygame.K_LEFT:
      three=0
    if event.type == pygame.KEYUP and event.key==pygame.K_RIGHT:
      four=0
    if one==0 or two==0:
      b=-10*one+10*two
    if three==0 or four==0:
      a=-10*three+10*four
    if three==1 and four==1:
      a=0
    if one==1 and two==1:
      b=0
    if event.type==QUIT:
      pygame.quit()
      sys.exit()
  if x<=-25:
    a=0
    x+=10
  if x>=725:
    a=0
    x-=10
  if y<=125:
    b=0
    y+=10
  if y>=500:
    b=0
    y-=10
  x+=a
  y+=b
  if a!=0 or b!=0:
    c+=1
  if c==5:
    d=1
  if c==10:
    d=0
    c=0
  pygame.draw.rect(area, white, (x+33, y+27, 40, 73))

#josh blit
  if d==0:
    area.blit(josh, (x,y))
  if d==1:
    area.blit(josh2, (x,y))
  if count==diff:
    count=0

#Lasers
  if count==1:
    angle=random.randint(-50, 50)
    x1=random.randint(150, 650)
    x2=(math.tan(math.radians(angle))*150+x1)
    x3=(math.tan(math.radians(angle*ratio))*450+x2)
  pygame.draw.line(area, red, (x1, 0), (x2, 150), 10) #main red
  if count>=diff//4:
    pygame.draw.line(area, red, (x2, 150), (x3, 600), 10) #refracted red
  if count==diff//3:
    angle2=random.randint(-50, 50)
    x4=random.randint(150, 650)
    x5=(math.tan(math.radians(angle2))*150+x4)
    x6=(math.tan(math.radians(angle2*ratio))*450+x5)
  if count2>=diff//2:
    pygame.draw.line(area, orange, (x4, 0), (x5, 150), 10) #main orange
  if (count>=2*diff/3 or count<diff//3) and count2>=diff//3:
    pygame.draw.line(area, orange, (x5, 150), (x6, 600), 10) #refracted orange
  if countinvin>30 and count3>100 and (x+73-x2)!=0 and (x3-x2)!=0 and (x+33-x2)!=0:
    if math.atan((y+27-150)/(x+73-x2))<=math.atan(450/(x3-x2)) and math.atan(450/(x3-x2))<=math.atan((y+100-150)/(x+33-x2)):
      lives-=1
      countinvin=0

#hitbox
  if countinvin>30 and count3>100 and (x+73-x5)!=0 and (x6-x5)!=0 and (x+33-x5)!=0:
    if math.atan((y+27-150)/(x+73-x5))<=math.atan(450/(x6-x5)) and math.atan(450/(x6-x5))<=math.atan((y+100-150)/(x+33-x5)):
      lives-=1
      countinvin=0
  area.blit(heart, (10,10))

#lives
  if lives<=0:
    run=False
  if lives>=2:
    area.blit(heart, (31,10))
  if lives>=3:
    area.blit(heart, (52,10))
  if lives>=4:
    area.blit(heart, (73,10))
  if lives==5:
    area.blit(heart, (94,10))

#end of loop
  pygame.display.update()

  clock.tick(fps)
#endgame
time.sleep(1)
area.fill(black)
display_message_center("Game over", 125, 400, 300, dedred)
time.sleep(2)
wait_for_input()
pygame.quit()
sys.exit()
