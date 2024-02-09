import pygame
import os

pygame.init()

# Set up the drawing window
screenSize = 176
screen = pygame.display.set_mode([screenSize*5, screenSize*4.25])
pygame.display.set_caption('Skystones')

#Load all images
path = 'C:/Users/treha/projects/skystones/assets'
filenames = [f for f in os.listdir(path) if f.endswith('.png')]
images = {}
for name in filenames:
    imagename = os.path.splitext(name)[0] 
    images[imagename] = pygame.image.load(os.path.join(path, name)).convert_alpha()
    images[imagename] = pygame.transform.scale(images[imagename], (screenSize, screenSize))
    images['large-' + imagename] = pygame.transform.scale(images[imagename], (screenSize+screenSize/16, screenSize+screenSize/16))

# Play music
pygame.mixer.music.set_volume(1)
pygame.mixer.music.load('assets/Skystones.mp3')
pygame.mixer.music.play(-1)

# Set the hands
hand = [images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['large-skystone-CONQUERTRON-4444'], images['large-skystone-CONQUERTRON-4444'], images['large-skystone-CONQUERTRON-4444'], images['large-skystone-CONQUERTRON-4444'], images['large-skystone-CONQUERTRON-4444'], images['large-skystone-CONQUERTRON-4444'], images['large-skystone-CONQUERTRON-4444'], images['large-skystone-CONQUERTRON-4444'], images['large-skystone-CONQUERTRON-4444'], images['large-skystone-CONQUERTRON-4444']]
write = [images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444'], images['skystone-CONQUERTRON-4444']]

# Run until the user asks to quit
running = True
while running:
   
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
   
    # Draw the board
    screen.fill((20, 15, 25))
    pygame.draw.polygon(screen, (100, 100, 100), [(screenSize-screenSize/16, screenSize/4), (screenSize*2-screenSize/16, screenSize/4), (screenSize*2-screenSize/16, screenSize+screenSize/4), (screenSize-screenSize/16, screenSize+screenSize/4)])
    pygame.draw.polygon(screen, (100, 100, 100), [(screenSize*2, screenSize/4), (screenSize*3, screenSize/4), (screenSize*3, screenSize+screenSize/4), (screenSize*2, screenSize+screenSize/4)])
    pygame.draw.polygon(screen, (100, 100, 100), [(screenSize*3+screenSize/16, screenSize/4), (screenSize*4+screenSize/16, screenSize/4), (screenSize*4+screenSize/16, screenSize+screenSize/4), (screenSize*3+screenSize/16, screenSize+screenSize/4)])

    pygame.draw.polygon(screen, (100, 100, 100), [(screenSize-screenSize/16, screenSize*21/16), (screenSize*2-screenSize/16, screenSize*21/16), (screenSize*2-screenSize/16, screenSize*37/16), (screenSize-screenSize/16, screenSize*37/16)])
    pygame.draw.polygon(screen, (100, 100, 100), [(screenSize*2, screenSize*21/16), (screenSize*3, screenSize*21/16), (screenSize*3, screenSize*37/16), (screenSize*2, screenSize*37/16)])
    pygame.draw.polygon(screen, (100, 100, 100), [(screenSize*3+screenSize/16, screenSize*21/16), (screenSize*4+screenSize/16, screenSize*21/16), (screenSize*4+screenSize/16, screenSize*37/16), (screenSize*3+screenSize/16, screenSize*37/16)])

    pygame.draw.polygon(screen, (100, 100, 100), [(screenSize-screenSize/16, screenSize*38/16), (screenSize*2-screenSize/16, screenSize*38/16), (screenSize*2-screenSize/16, screenSize*54/16), (screenSize-screenSize/16, screenSize*54/16)])
    pygame.draw.polygon(screen, (100, 100, 100), [(screenSize*2, screenSize*38/16), (screenSize*3, screenSize*38/16), (screenSize*3, screenSize*54/16), (screenSize*2, screenSize*54/16)])
    pygame.draw.polygon(screen, (100, 100, 100), [(screenSize*3+screenSize/16, screenSize*38/16), (screenSize*4+screenSize/16, screenSize*38/16), (screenSize*4+screenSize/16, screenSize*54/16), (screenSize*3+screenSize/16, screenSize*54/16)])


    # Draw the stones
    screen.blit(images['skystone-lance1-1001'], (screenSize-screenSize/16, screenSize/4))
    screen.blit(images['skystone-lance4-3113'], (screenSize*2, screenSize/4))
    screen.blit(images['skystone-lance4-3113'], (screenSize*3+screenSize/16, screenSize/4))
    screen.blit(images['skystone-lance4-3113'], (screenSize-screenSize/16, screenSize*21/16))
    screen.blit(images['skystone-CONQUERTRON-4444'], (screenSize*2, screenSize*21/16))
    screen.blit(images['skystone-lance2-2002'], (screenSize*3+screenSize/16, screenSize*21/16))
    screen.blit(images['skystone-lance3-3003'], (screenSize-screenSize/16, screenSize*38/16))
    screen.blit(images['skystone-lance4-3113'], (screenSize*2, screenSize*38/16))
    screen.blit(images['skystone-CONQUERTRON-4444'], (screenSize*3+screenSize/16, screenSize*38/16))

    turn = 0

    # If the hand is over a stone, highlight it
    mouse = pygame.mouse.get_pos()
    if screenSize*52/16 < mouse[1] < screenSize*4.25:
        write = hand[0+5*turn:5+5*turn]
        write[int(mouse[0]/screenSize)] = hand[int(mouse[0]/screenSize)+5*turn+10]

    else:
        write = hand[0+5*turn:5+5*turn]

    # Draw the hands
    screen.blit(write[0], (0, screenSize*52/16))
    screen.blit(write[1], (screenSize, screenSize*52/16))
    screen.blit(write[2], (screenSize*2, screenSize*52/16))
    screen.blit(write[3], (screenSize*3, screenSize*52/16))
    screen.blit(write[4], (screenSize*4, screenSize*52/16))

    # Flip the display
    pygame.display.flip()