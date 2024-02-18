import pygame
import time
import os
import re

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
    images['small-' + imagename] = pygame.transform.scale(images[imagename], (screenSize/4, screenSize/4))
    images['small-large-' + imagename] = pygame.transform.scale(images[imagename], (screenSize/4+screenSize/16, screenSize/4+screenSize/16))

# Play music
pygame.mixer.music.set_volume(1)
pygame.mixer.music.load('assets/Skystones.mp3')
pygame.mixer.music.play(-1)

# Set the hands
hand = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]

# Set the board
board = [[images['skystone-empty'], images['skystone-empty'], images['skystone-empty']], [images['skystone-empty'], images['skystone-empty'], images['skystone-empty']], [images['skystone-empty'], images['skystone-empty'], images['skystone-empty']]]
boardColor = [[5, 0, 25], [5, 0, 25], [5, 0, 25], [5, 0, 25], [5, 0, 25], [5, 0, 25], [5, 0, 25], [5, 0, 25], [5, 0, 25]]

# Set the turn
turn = 0

# Set the page
page = [[images['skystone-spiderling1-0100'], images['skystone-spiderling2-0200'], images['skystone-spiderling3-0300-a'], images['skystone-chompy1-0001'], images['skystone-chompy2-0001-e'], images['skystone-chompy3-1011-e'], images['skystone-frigid1-0010-w'], images['skystone-frigid2-0020-w'], images['skystone-frigid3-0121-w'], images['skystone-enfuego1-1000-f'], images['skystone-enfuego2-2000-f'], images['skystone-enfuego3-3101-f'], images['skystone-lance1-1001'], images['skystone-lance2-2002'], images['skystone-lance3-3003'], images['skystone-lance4-3113'], images['skystone-mohawk1-1100'], images['skystone-mohawk2-2200'], images['skystone-mohawk3-3300'], images['skystone-mohawk4-3311'], images['large-skystone-spiderling1-0100'], images['large-skystone-spiderling2-0200'], images['large-skystone-spiderling3-0300-a'], images['large-skystone-chompy1-0001'], images['large-skystone-chompy2-0001-e'], images['large-skystone-chompy3-1011-e'], images['large-skystone-frigid1-0010-w'], images['large-skystone-frigid2-0020-w'], images['large-skystone-frigid3-0121-w'], images['large-skystone-enfuego1-1000-f'], images['large-skystone-enfuego2-2000-f'], images['large-skystone-enfuego3-3101-f'], images['large-skystone-lance1-1001'], images['large-skystone-lance2-2002'], images['large-skystone-lance3-3003'], images['large-skystone-lance4-3113'], images['large-skystone-mohawk1-1100'], images['large-skystone-mohawk2-2200'], images['large-skystone-mohawk3-3300'], images['large-skystone-mohawk4-3311'], images['small-skystone-spiderling1-0100'], images['small-skystone-spiderling2-0200'], images['small-skystone-spiderling3-0300-a'], images['small-skystone-chompy1-0001'], images['small-skystone-chompy2-0001-e'], images['small-skystone-chompy3-1011-e'], images['small-skystone-frigid1-0010-w'], images['small-skystone-frigid2-0020-w'], images['small-skystone-frigid3-0121-w'], images['small-skystone-enfuego1-1000-f'], images['small-skystone-enfuego2-2000-f'], images['small-skystone-enfuego3-3101-f'], images['small-skystone-lance1-1001'], images['small-skystone-lance2-2002'], images['small-skystone-lance3-3003'], images['small-skystone-lance4-3113'], images['small-skystone-mohawk1-1100'], images['small-skystone-mohawk2-2200'], images['small-skystone-mohawk3-3300'], images['small-skystone-mohawk4-3311'], images['small-large-skystone-spiderling1-0100'], images['small-large-skystone-spiderling2-0200'], images['small-large-skystone-spiderling3-0300-a'], images['small-large-skystone-chompy1-0001'], images['small-large-skystone-chompy2-0001-e'], images['small-large-skystone-chompy3-1011-e'], images['small-large-skystone-frigid1-0010-w'], images['small-large-skystone-frigid2-0020-w'], images['small-large-skystone-frigid3-0121-w'], images['small-large-skystone-enfuego1-1000-f'], images['small-large-skystone-enfuego2-2000-f'], images['small-large-skystone-enfuego3-3101-f'], images['small-large-skystone-lance1-1001'], images['small-large-skystone-lance2-2002'], images['small-large-skystone-lance3-3003'], images['small-large-skystone-lance4-3113'], images['small-large-skystone-mohawk1-1100'], images['small-large-skystone-mohawk2-2200'], images['small-large-skystone-mohawk3-3300'], images['small-large-skystone-mohawk4-3311']], [images['skystone-mace1-0011'], images['skystone-mace2-0022'], images['skystone-mace3-0033'], images['skystone-mace4-1133'], images['skystone-archer1-1010'], images['skystone-archer2-2020'], images['skystone-archer3-3030'], images['skystone-blaster1-0101'], images['skystone-blaster2-0202'], images['skystone-blaster3-0303'], images['skystone-jouster1-2101'], images['skystone-jouster2-3101'], images['skystone-jouster3-3202'], images['skystone-jouster4-3212'], images['skystone-jouster5-3222'], images['skystone-shield1-0121'], images['skystone-shield2-0131'], images['skystone-shield3-0232'], images['skystone-shield4-1232'], images['skystone-shield5-2232'], images['large-skystone-mace1-0011'], images['large-skystone-mace2-0022'], images['large-skystone-mace3-0033'], images['large-skystone-mace4-1133'], images['large-skystone-archer1-1010'], images['large-skystone-archer2-2020'], images['large-skystone-archer3-3030'], images['large-skystone-blaster1-0101'], images['large-skystone-blaster2-0202'], images['large-skystone-blaster3-0303'], images['large-skystone-jouster1-2101'], images['large-skystone-jouster2-3101'], images['large-skystone-jouster3-3202'], images['large-skystone-jouster4-3212'], images['large-skystone-jouster5-3222'], images['large-skystone-shield1-0121'], images['large-skystone-shield2-0131'], images['large-skystone-shield3-0232'], images['large-skystone-shield4-1232'], images['large-skystone-shield5-2232'], images['small-skystone-mace1-0011'], images['small-skystone-mace2-0022'], images['small-skystone-mace3-0033'], images['small-skystone-mace4-1133'], images['small-skystone-archer1-1010'], images['small-skystone-archer2-2020'], images['small-skystone-archer3-3030'], images['small-skystone-blaster1-0101'], images['small-skystone-blaster2-0202'], images['small-skystone-blaster3-0303'], images['small-skystone-jouster1-2101'], images['small-skystone-jouster2-3101'], images['small-skystone-jouster3-3202'], images['small-skystone-jouster4-3212'], images['small-skystone-jouster5-3222'], images['small-skystone-shield1-0121'], images['small-skystone-shield2-0131'], images['small-skystone-shield3-0232'], images['small-skystone-shield4-1232'], images['small-skystone-shield5-2232'], images['small-large-skystone-mace1-0011'], images['small-large-skystone-mace2-0022'], images['small-large-skystone-mace3-0033'], images['small-large-skystone-mace4-1133'], images['small-large-skystone-archer1-1010'], images['small-large-skystone-archer2-2020'], images['small-large-skystone-archer3-3030'], images['small-large-skystone-blaster1-0101'], images['small-large-skystone-blaster2-0202'], images['small-large-skystone-blaster3-0303'], images['small-large-skystone-jouster1-2101'], images['small-large-skystone-jouster2-3101'], images['small-large-skystone-jouster3-3202'], images['small-large-skystone-jouster4-3212'], images['small-large-skystone-jouster5-3222'], images['small-large-skystone-shield1-0121'], images['small-large-skystone-shield2-0131'], images['small-large-skystone-shield3-0232'], images['small-large-skystone-shield4-1232'], images['small-large-skystone-shield5-2232']], [images['skystone-riveter1-1012'], images['skystone-riveter2-1013'], images['skystone-riveter3-2023'], images['skystone-riveter4-2123'], images['skystone-riveter5-2223'], images['skystone-jawbreaker1-1210'], images['skystone-jawbreaker2-1310'], images['skystone-jawbreaker3-2320'], images['skystone-jawbreaker4-2321'], images['skystone-jawbreaker5-2322'], images['skystone-bot1-1010'], images['skystone-bot2-1111'], images['skystone-bot3-2121'], images['skystone-bot4-2222'], images['skystone-bot5-3232'], images['skystone-bot6-3333'], images['skystone-duelist-4000'], images['skystone-boom-0400'], images['skystone-duke-0040'], images['skystone-sniper-0004'], images['large-skystone-riveter1-1012'], images['large-skystone-riveter2-1013'], images['large-skystone-riveter3-2023'], images['large-skystone-riveter4-2123'], images['large-skystone-riveter5-2223'], images['large-skystone-jawbreaker1-1210'], images['large-skystone-jawbreaker2-1310'], images['large-skystone-jawbreaker3-2320'], images['large-skystone-jawbreaker4-2321'], images['large-skystone-jawbreaker5-2322'], images['large-skystone-bot1-1010'], images['large-skystone-bot2-1111'], images['large-skystone-bot3-2121'], images['large-skystone-bot4-2222'], images['large-skystone-bot5-3232'], images['large-skystone-bot6-3333'], images['large-skystone-duelist-4000'], images['large-skystone-boom-0400'], images['large-skystone-duke-0040'], images['large-skystone-sniper-0004'], images['small-skystone-riveter1-1012'], images['small-skystone-riveter2-1013'], images['small-skystone-riveter3-2023'], images['small-skystone-riveter4-2123'], images['small-skystone-riveter5-2223'], images['small-skystone-jawbreaker1-1210'], images['small-skystone-jawbreaker2-1310'], images['small-skystone-jawbreaker3-2320'], images['small-skystone-jawbreaker4-2321'], images['small-skystone-jawbreaker5-2322'], images['small-skystone-bot1-1010'], images['small-skystone-bot2-1111'], images['small-skystone-bot3-2121'], images['small-skystone-bot4-2222'], images['small-skystone-bot5-3232'], images['small-skystone-bot6-3333'], images['small-skystone-duelist-4000'], images['small-skystone-boom-0400'], images['small-skystone-duke-0040'], images['small-skystone-sniper-0004'], images['small-large-skystone-riveter1-1012'], images['small-large-skystone-riveter2-1013'], images['small-large-skystone-riveter3-2023'], images['small-large-skystone-riveter4-2123'], images['small-large-skystone-riveter5-2223'], images['small-large-skystone-jawbreaker1-1210'], images['small-large-skystone-jawbreaker2-1310'], images['small-large-skystone-jawbreaker3-2320'], images['small-large-skystone-jawbreaker4-2321'], images['small-large-skystone-jawbreaker5-2322'], images['small-large-skystone-bot1-1010'], images['small-large-skystone-bot2-1111'], images['small-large-skystone-bot3-2121'], images['small-large-skystone-bot4-2222'], images['small-large-skystone-bot5-3232'], images['small-large-skystone-bot6-3333'], images['small-large-skystone-duelist-4000'], images['small-large-skystone-boom-0400'], images['small-large-skystone-duke-0040'], images['small-large-skystone-sniper-0004']], [images['skystone-bomber-2310-a'], images['skystone-bowler-2202-e'], images['skystone-fiend-2121-f'], images['skystone-armored-1131-w'], images['skystone-punk-2103-m'], images['skystone-grenade-0321-t'], images['skystone-runner-2121-l'], images['skystone-wanderer-1212-u'], images['skystone-dragonet-1322-a'], images['skystone-golem-2222-e'], images['skystone-brewer-3122-f'], images['skystone-mutticus-1331-w'], images['skystone-crackler-2321-m'], images['skystone-juggernaut-0133-t'], images['skystone-goliath-4101-l'], images['skystone-gargantula-0141-u'], images['skystone-trogmander-1222-m'], images['skystone-ultron-2222-t'], images['skystone-axecutioner-3333'], images['skystone-CONQUERTRON-4444'], images['large-skystone-bomber-2310-a'], images['large-skystone-bowler-2202-e'], images['large-skystone-fiend-2121-f'], images['large-skystone-armored-1131-w'], images['large-skystone-punk-2103-m'], images['large-skystone-grenade-0321-t'], images['large-skystone-runner-2121-l'], images['large-skystone-wanderer-1212-u'], images['large-skystone-dragonet-1322-a'], images['large-skystone-golem-2222-e'], images['large-skystone-brewer-3122-f'], images['large-skystone-mutticus-1331-w'], images['large-skystone-crackler-2321-m'], images['large-skystone-juggernaut-0133-t'], images['large-skystone-goliath-4101-l'], images['large-skystone-gargantula-0141-u'], images['large-skystone-trogmander-1222-m'], images['large-skystone-ultron-2222-t'], images['large-skystone-axecutioner-3333'], images['large-skystone-CONQUERTRON-4444'], images['small-skystone-bomber-2310-a'], images['small-skystone-bowler-2202-e'], images['small-skystone-fiend-2121-f'], images['small-skystone-armored-1131-w'], images['small-skystone-punk-2103-m'], images['small-skystone-grenade-0321-t'], images['small-skystone-runner-2121-l'], images['small-skystone-wanderer-1212-u'], images['small-skystone-dragonet-1322-a'], images['small-skystone-golem-2222-e'], images['small-skystone-brewer-3122-f'], images['small-skystone-mutticus-1331-w'], images['small-skystone-crackler-2321-m'], images['small-skystone-juggernaut-0133-t'], images['small-skystone-goliath-4101-l'], images['small-skystone-gargantula-0141-u'], images['small-skystone-trogmander-1222-m'], images['small-skystone-ultron-2222-t'], images['small-skystone-axecutioner-3333'], images['small-skystone-CONQUERTRON-4444'], images['small-large-skystone-bomber-2310-a'], images['small-large-skystone-bowler-2202-e'], images['small-large-skystone-fiend-2121-f'], images['small-large-skystone-armored-1131-w'], images['small-large-skystone-punk-2103-m'], images['small-large-skystone-grenade-0321-t'], images['small-large-skystone-runner-2121-l'], images['small-large-skystone-wanderer-1212-u'], images['small-large-skystone-dragonet-1322-a'], images['small-large-skystone-golem-2222-e'], images['small-large-skystone-brewer-3122-f'], images['small-large-skystone-mutticus-1331-w'], images['small-large-skystone-crackler-2321-m'], images['small-large-skystone-juggernaut-0133-t'], images['small-large-skystone-goliath-4101-l'], images['small-large-skystone-gargantula-0141-u'], images['small-large-skystone-trogmander-1222-m'], images['small-large-skystone-ultron-2222-t'], images['small-large-skystone-axecutioner-3333'], images['small-large-skystone-CONQUERTRON-4444']]]
pageNo = 0

# Run until the user asks to quit
firstPress = True
firstPress1 = True
running = True
gameRunning = False
while running:
   
    # Did the user click the window close button?
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
             running = False

    screen.fill((25, 15, 85))

    # Draw the page
    idx = 0
    idy = 0

    for i in page[pageNo]:
        if idy < 4:
            write = page[pageNo][0:20]

            mouse = pygame.mouse.get_pos()
            if mouse[1] < screenSize*4:
                write[int(mouse[0]/screenSize)+5*int(mouse[1]/screenSize)] = page[pageNo][int(mouse[0]/screenSize)+5*int(mouse[1]/screenSize)+20]

                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if firstPress:
                            hand[hand.index(0)] = page[pageNo][int(mouse[0]/screenSize)+5*int(mouse[1]/screenSize)]
                            hand[hand.index(10)] = page[pageNo][int(mouse[0]/screenSize)+5*int(mouse[1]/screenSize)+20]
                            hand[hand.index(100)] = page[pageNo][int(mouse[0]/screenSize)+5*int(mouse[1]/screenSize)+40]
                            hand[hand.index(1000)] = page[pageNo][int(mouse[0]/screenSize)+5*int(mouse[1]/screenSize)+60]
                            firstPress = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        firstPress = True
                    if event.type == pygame.KEYDOWN:
                        if firstPress1:
                            if event.key == pygame.K_LEFT:
                                pageNo -= 1
                                if pageNo < 0:
                                    pageNo = 3
                            if event.key == pygame.K_RIGHT:
                                pageNo += 1
                                if pageNo > 3:
                                    pageNo = 0
                            firstPress1 = False
                    if event.type == pygame.KEYUP:
                        firstPress1 = True

            screen.blit(write[idx+5*idy], (idx*screenSize, idy*screenSize))

            # If the hand is over a stone, highlight it
            mouse = pygame.mouse.get_pos()
            write = hand[20:40]
            # Awful code. Put random stuff here till it worked
            if mouse[1] > screenSize*4 and mouse[0] < screenSize*1.25:
                write[int(mouse[0]/screenSize*4)] = hand[int(mouse[0]/screenSize*4)+30]
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        hand[int(mouse[0]/screenSize*4)] = 0
                        hand[int(mouse[0]/screenSize*4)+10] = 10                       
                        hand[int(mouse[0]/screenSize*4)+20] = 100
                        hand[int(mouse[0]/screenSize*4)+30] = 1000
            elif mouse[1] > screenSize*4 and mouse[0] > screenSize*3.75:
                write[int((mouse[0]-screenSize*2.5)/screenSize*4)] = hand[int(mouse[0]/screenSize*4)+20]
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        hand[int((mouse[0]-screenSize*2.5)/screenSize*4)] = 0
                        hand[int((mouse[0]-screenSize*2.5)/screenSize*4)+10] = 10
                        hand[int((mouse[0]-screenSize*2.5)/screenSize*4)+20] = 100
                        hand[int((mouse[0]-screenSize*2.5)/screenSize*4)+30] = 1000

            # Draw the hands
            if write[0] not in [0, 10, 100, 1000]:
                screen.blit(write[0], (0, screenSize*4))
            if write[1] not in [0, 10, 100, 1000]:
                screen.blit(write[1], (screenSize*0.25, screenSize*4))
            if write[2] not in [0, 10, 100, 1000]:
                screen.blit(write[2], (screenSize*0.5, screenSize*4))
            if write[3] not in [0, 10, 100, 1000]:
                screen.blit(write[3], (screenSize*0.75, screenSize*4))
            if write[4] not in [0, 10, 100, 1000]:
                screen.blit(write[4], (screenSize, screenSize*4))
            if write[5] not in [0, 10, 100, 1000]:
                screen.blit(write[5], (screenSize*3.75, screenSize*4))
            if write[6] not in [0, 10, 100, 1000]:
                screen.blit(write[6], (screenSize*4, screenSize*4))
            if write[7] not in [0, 10, 100, 1000]:
                screen.blit(write[7], (screenSize*4.25, screenSize*4))
            if write[8] not in [0, 10, 100, 1000]:
                screen.blit(write[8], (screenSize*4.5, screenSize*4))
            if write[9] not in [0, 10, 100, 1000]:
                screen.blit(write[9], (screenSize*4.75, screenSize*4))

            idx += 1
            if idx == 5:
                idx = 0
                idy += 1

    # Flip the display
    pygame.display.flip()

    if not 0 in hand:
        gameRunning = True

    while gameRunning:     

        # Did the user click the window close button?
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                gameRunning = False
   
        # Draw the board
        screen.fill((25, 15, 85))
        pygame.draw.polygon(screen, (boardColor[0]), [(screenSize-screenSize/16, screenSize/4), (screenSize*2-screenSize/16, screenSize/4), (screenSize*2-screenSize/16, screenSize+screenSize/4), (screenSize-screenSize/16, screenSize+screenSize/4)])
        pygame.draw.polygon(screen, (boardColor[1]), [(screenSize*2, screenSize/4), (screenSize*3, screenSize/4), (screenSize*3, screenSize+screenSize/4), (screenSize*2, screenSize+screenSize/4)])
        pygame.draw.polygon(screen, (boardColor[2]), [(screenSize*3+screenSize/16, screenSize/4), (screenSize*4+screenSize/16, screenSize/4), (screenSize*4+screenSize/16, screenSize+screenSize/4), (screenSize*3+screenSize/16, screenSize+screenSize/4)])

        pygame.draw.polygon(screen, (boardColor[3]), [(screenSize-screenSize/16, screenSize*21/16), (screenSize*2-screenSize/16, screenSize*21/16), (screenSize*2-screenSize/16, screenSize*37/16), (screenSize-screenSize/16, screenSize*37/16)])
        pygame.draw.polygon(screen, (boardColor[4]), [(screenSize*2, screenSize*21/16), (screenSize*3, screenSize*21/16), (screenSize*3, screenSize*37/16), (screenSize*2, screenSize*37/16)])
        pygame.draw.polygon(screen, (boardColor[5]), [(screenSize*3+screenSize/16, screenSize*21/16), (screenSize*4+screenSize/16, screenSize*21/16), (screenSize*4+screenSize/16, screenSize*37/16), (screenSize*3+screenSize/16, screenSize*37/16)])

        pygame.draw.polygon(screen, (boardColor[6]), [(screenSize-screenSize/16, screenSize*38/16), (screenSize*2-screenSize/16, screenSize*38/16), (screenSize*2-screenSize/16, screenSize*54/16), (screenSize-screenSize/16, screenSize*54/16)])
        pygame.draw.polygon(screen, (boardColor[7]), [(screenSize*2, screenSize*38/16), (screenSize*3, screenSize*38/16), (screenSize*3, screenSize*54/16), (screenSize*2, screenSize*54/16)])
        pygame.draw.polygon(screen, (boardColor[8]), [(screenSize*3+screenSize/16, screenSize*38/16), (screenSize*4+screenSize/16, screenSize*38/16), (screenSize*4+screenSize/16, screenSize*54/16), (screenSize*3+screenSize/16, screenSize*54/16)])


        # Draw the stones
        screen.blit(board[0][0], (screenSize-screenSize/16, screenSize/4))
        screen.blit(board[0][1], (screenSize*2, screenSize/4))
        screen.blit(board[0][2], (screenSize*3+screenSize/16, screenSize/4))
        screen.blit(board[1][0], (screenSize-screenSize/16, screenSize*21/16))
        screen.blit(board[1][1], (screenSize*2, screenSize*21/16))
        screen.blit(board[1][2], (screenSize*3+screenSize/16, screenSize*21/16))
        screen.blit(board[2][0], (screenSize-screenSize/16, screenSize*38/16))
        screen.blit(board[2][1], (screenSize*2, screenSize*38/16))
        screen.blit(board[2][2], (screenSize*3+screenSize/16, screenSize*38/16))

        # If the hand is over a stone, highlight it
        mouse = pygame.mouse.get_pos()
        if screenSize*52/16 < mouse[1]:
            write = hand[0+5*turn:5+5*turn]
            write[int(mouse[0]/screenSize)] = hand[int(mouse[0]/screenSize)+5*turn+10]

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key in range(49, 58):
                        keyPressed = event.key - 49
                        if board[keyPressed//3][keyPressed%3] == images['skystone-empty'] and hand[int(mouse[0]/screenSize)+5*turn] != images['skystone-empty']:
                            board[keyPressed//3][keyPressed%3] = hand[int(mouse[0]/screenSize)+5*turn]
                            boardColor[keyPressed] = [50*(1-turn), 0, 50*turn+25]
                            hand[int(mouse[0]/screenSize)+5*turn] = images['skystone-empty']
                            hand[int(mouse[0]/screenSize)+5*turn+10] = images['skystone-empty']

                            print(re.findall(r'\d{4}', hand[int(mouse[0]/screenSize)+5*turn]))
                    
                            # Switch players
                            if turn == 0:
                                turn = 1
                            else:
                                turn = 0
        else:
            write = hand[0+5*turn:5+5*turn]

        # Draw the hand
        screen.blit(write[0], (0, screenSize*52/16))
        screen.blit(write[1], (screenSize, screenSize*52/16))
        screen.blit(write[2], (screenSize*2, screenSize*52/16))
        screen.blit(write[3], (screenSize*3, screenSize*52/16))
        screen.blit(write[4], (screenSize*4, screenSize*52/16))

        # Flip the display
        pygame.display.flip()