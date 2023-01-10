#Hassan Fakih 101168868

import pygame
pygame.display.init()
scrn_size = (500,500)
scrn = pygame.display.set_mode(scrn_size)

#Colors
DARKBLUE = (0,0,160)
RED = (255,0,0)
GREEN = (0,128,0)
BLACK = (0,0,0)
MAROON = (128,0,0)
BROWN = (165,42,42)
YELLOW = (255,255,0)
LIGHTBLUE = (173,216,230)
LIME = (0,255,0)
WHITE = (255,255,255)

#Drawing

#sky setting the background
scrn.fill(DARKBLUE) #Earth (DarkBlue) RGB: 0, 0, 160
#ground
pygame.draw.rect(scrn, GREEN,(0,385,500,115)) #Green RGB: 0, 128, 0
#house base
pygame.draw.rect(scrn, RED,(70,260,250,125)) #Red RGB: 255, 0, 0
#outline for house front
pygame.draw.rect(scrn, BLACK,(143,298,104,87)) #Black RGB: 0, 0, 0
#house front
pygame.draw.rect(scrn, RED,(145,300,100,85)) #Red RGB: 255, 0, 0
#roof for house base
pygame.draw.polygon(scrn, MAROON,((70,260),(130,150),(260,150),(320,260))) #Maroon RGB: 128, 0, 0
#outline for roof for house front
pygame.draw.polygon(scrn, BLACK,((138,300),(252,300),(195,218))) #Black RGB: 0, 0, 0
#roof for house front
pygame.draw.polygon(scrn, MAROON,((140,300),(250,300),(195,220))) #Maroon RGB: 128, 0, 0
#door
pygame.draw.rect(scrn, BROWN,(175,320,40,65)) #Brown RGB: 165, 42, 42
#door handle
pygame.draw.circle(scrn, YELLOW,(210,355),2) #Yellow RGB: 255, 255, 0
#window to the left
pygame.draw.rect(scrn, LIGHTBLUE,(80,300,45,45)) #LightBlue RGB: 173, 216, 230
#window to the right
pygame.draw.rect(scrn, LIGHTBLUE,(265,300,45,45)) #LightBlue RGB: 173, 216, 230
#cross on window left (horizontal)
pygame.draw.rect(scrn, BLACK,(80,320,45,4)) #Black RGB: 0, 0, 0
#cross on window left (vertical)
pygame.draw.rect(scrn, BLACK,(100,300,4,45)) #Black RGB: 0, 0, 0
#cross on window right (horizontal)
pygame.draw.rect(scrn, BLACK,(265,320,45,4)) #Black RGB: 0, 0, 0
#cross on window right (vertical)
pygame.draw.rect(scrn, BLACK,(285,300,4,45)) #Black RGB: 0, 0, 0
#tree trunk
pygame.draw.polygon(scrn, BROWN, ((360,385),(475,385),(455,365),(445,245),(385,245),(380,365))) #Brown RGB: 165, 42, 42
#tree leaf 1
pygame.draw.ellipse(scrn, LIME, (360,175,110,100)) #Lime RGB: 0, 255, 0
#tree leaf 2
pygame.draw.ellipse(scrn, LIME, (380,155,80,80)) #Lime RGB: 0, 255, 0
#tree leaf 3
pygame.draw.ellipse(scrn, LIME, (340,155,80,80)) #Lime RGB: 0, 255, 0
#tree leaf 4
pygame.draw.ellipse(scrn, LIME, (340,180,80,100)) #Lime RGB: 0, 255, 0
#tree leaf 5
pygame.draw.ellipse(scrn, LIME, (400,180,80,90)) #Lime RGB: 0, 255, 0
#tree leaf 6
pygame.draw.ellipse(scrn, LIME, (380,220,90,70)) #Lime RGB: 0, 255, 0
#moon 
pygame.draw.circle(scrn, WHITE, (90,75),45) #White RGB: 255, 255, 255
#moon shadow
pygame.draw.ellipse(scrn, DARKBLUE,(65,25,90,75)) #Earth (DarkBlue) RGB: 0, 0, 160

#Other
pygame.display.update()
pygame.image.save(scrn, "house_101168868.bmp")
pygame.time.delay(3000)


