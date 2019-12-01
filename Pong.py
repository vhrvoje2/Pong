import pygame
import math
import random
from pygame import mixer

pygame.init()

#screen and title
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

#global atributes
paddleSpeed = 0.7
ballSpeed = 0.5

#p1 paddle
paddleImg1 = pygame.image.load(r'D:\Git\Pong\paddle.png')
paddle1X = 350
paddle1Y = 580
paddle1XChange = 0

def paddle1(x, y):
    screen.blit(paddleImg1, (x, y))

#p2 paddle
paddleImg2 = pygame.image.load(r'D:\Git\Pong\paddle.png')
paddle2X = 350
paddle2Y = 0
paddle2XChange = 0

def paddle2(x, y):
    screen.blit(paddleImg2, (x, y))

#ball
ballImg = pygame.image.load(r'D:\Git\Pong\ball.png')
ballX = 375
ballY = 0
ballXChange = ballSpeed
ballYChange = ballSpeed

def ball(x, y):
    screen.blit(ballImg, (x, y))

running = True
#main lopp
while running:
    #screen color
    screen.fill((255, 255, 255))

    #event checks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #move p1 paddle right
                paddle1XChange += paddleSpeed
            if event.key == pygame.K_LEFT:
                #move p1 paddle left
                paddle1XChange -= paddleSpeed
            if event.key == pygame.K_d:
                #move p2 paddle left
                paddle2XChange += paddleSpeed
            if event.key == pygame.K_a:
                #move p2 paddle right
                paddle2XChange -= paddleSpeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle1XChange = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                paddle2XChange = 0

    #ball movement
    ballX += ballXChange
    ballY += ballYChange
    
    #bounce off sides
    if ballX <= 0:
        ballX = 0
        ballXChange = ballSpeed
    elif ballX >= 750:
        ballX = 750
        ballXChange = -ballSpeed

    #bounce off paddle
    if ballY <= 0:
        ballY = 0
        ballYChange = ballSpeed
    elif ballY >= 550:
        ballY= 550
        ballYChange = -ballSpeed

    #paddle movement
    paddle1X += paddle1XChange
    paddle2X += paddle2XChange

    #off screen checks
    if paddle1X <= 0:
        paddle1X = 0
    elif paddle1X >= 700:
        paddle1X = 700

    if paddle2X <= 0:
        paddle2X = 0
    elif paddle2X >= 700:
        paddle2X = 700

    #draw on screen
    paddle1(paddle1X, paddle1Y)
    paddle2(paddle2X, paddle2Y)
    ball(ballX, ballY)
    pygame.display.update()
