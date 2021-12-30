import sys, pygame
pygame.init()
pygame.key.set_repeat(10)

size = width, height = 640, 440
xspeed = 2
yspeed = 2
black = [0,0,0]
white = [255,255,255]
font = pygame.font.SysFont("Comic Sans",50)
renderedText3 = font.render("Player 1 wins!",1,white)
renderedText4 = font.render("Game Over!",1,white)
renderedText5 = font.render("Press Q to Quit, or R to Restart",1,white)
renderedText6 = font.render("Player 2 wins!",1,white)
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
ballrect.left = width/2

paddle1 = pygame.Rect(10,10,10,50)
paddle2 = pygame.Rect(620,10,10,50)
score1 = 0
score2 = 0

gameover = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w]:
                paddle1.top = paddle1.top - 5
            if keys [pygame.K_s]:
                paddle1.top = paddle1.top + 5
            keys=pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                paddle2.top=paddle2.top-5
            if keys[pygame.K_DOWN]:
                paddle2.top=paddle2.top+5
                ## r to restart and q to quit
            if gameover:
                if keys[pygame.K_r]:
                    gameover=False
                    paddle1 = pygame.Rect(10,10,10,50)
                    paddle2 = pygame.Rect(620,10,10,50)
                    score1 = 0
                    score2 = 0
                    xspeed = 2
                    yspeed = 2
                if keys[pygame.K_q]:
                    pygame.quit()
                    sys.exit()
    ## increase speed
    ballrect.left = ballrect.left+xspeed
    ballrect.top = ballrect.top+yspeed
    if ballrect.colliderect(paddle1) and xspeed<0:
        xspeed = xspeed * -1.1
    if ballrect.colliderect(paddle2) and xspeed>0:
        xspeed = xspeed * -1.1
    if ballrect.left < 0:
        ballrect.left=width/2+100
        ## player 2 score
        score1 = score1 + 1
        xspeed=2
        yspeed=2
    if ballrect.right > width:
        ballrect.right=width/2+100
        ## player 1 score
        score2 = score2 + 1
        xspeed= 2
        yspeed=2
    if ballrect.top < 0 or ballrect.bottom > height:
        yspeed = yspeed * -1.1

    if gameover:
        yspeed=0
        xspeed=0
    
    screen.fill(black)
    ## player 2 wins
    if score1 ==10:
        gameover = True
        screen.blit(renderedText6,(300,height/2+50))
        screen.blit(renderedText4,(300,height/2-150))
        screen.blit(renderedText5,(100,height/2))

        
    ## player 1 wins
    if score2 == 10:
        gameover = True
        screen.blit(renderedText6,(300,height/2+50))
        screen.blit(renderedText4,(300,height/2-150))
        screen.blit(renderedText5, (100,height/2))

        

  
    screen.blit(ball, ballrect)
    pygame.draw.rect(screen, white, paddle1,0)
    pygame.draw.rect(screen, white, paddle2,0)
    renderedText = font.render("Player 1: "+str(score2),1,white)
    renderedText2 = font.render("Player 2: "+str(score1),1,white)
    screen.blit(renderedText, (width/2-175,10))
    screen.blit(renderedText2, (width/2+50,10))
    pygame.display.flip()
    pygame.time.wait(10)

