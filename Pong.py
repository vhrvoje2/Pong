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
ballSpeed = 0.6

#p1 paddle
paddleImg1 = pygame.image.load(r'D:\Git\Pong\paddle.png')
paddle1X = 350
paddle1Y = 580
paddle1XChange = 0
score1 = 0

def paddle1(x, y):
    screen.blit(paddleImg1, (x, y))

#p2 paddle
paddleImg2 = pygame.image.load(r'D:\Git\Pong\paddle.png')
paddle2X = 350
paddle2Y = 0
paddle2XChange = 0
score2 = 0

def paddle2(x, y):
    screen.blit(paddleImg2, (x, y))

#ball
ballImg = pygame.image.load(r'D:\Git\Pong\ball.png')
ballX = 375
ballY = 275
ballXChange = ballSpeed
ballYChange = ballSpeed

def ball(x, y):
    screen.blit(ballImg, (x, y))

def distance1(ballX, ballY, paddle1X, paddle1Y):
    for xCord1 in range(int(paddle1X), int(paddle1X+100)):
        ballXTemp = ballX + 25
        ballYTemp = ballY + 25
        distance = math.sqrt((math.pow(ballXTemp-xCord1, 2)) + (math.pow(ballYTemp-paddle1Y,2)))
        if distance <= 25:
            return True
    return False

def distance2(ballX, ballY, paddle2X, paddle2Y):
    for xCord2 in range(int(paddle2X+100), int(paddle2X), -1):
        paddle2Ytemp = paddle2Y + 20
        ballXTemp = ballX + 25
        ballYTemp = ballY + 25
        distance = math.sqrt((math.pow(ballXTemp-xCord2, 2)) + (math.pow(ballYTemp-paddle2Ytemp,2)))
        if distance <= 25:
            return True
    return False

# def collision(ballX, BallY, paddle1X, paddle1Y, paddle2X, paddle2Y):
#     for xCord1 in range(int(paddle1X), int(paddle1X+100)):
#         ballXTemp = ballX + 25
#         ballYTemp = ballY + 25
#         distance = math.sqrt((math.pow(ballXTemp-xCord1, 2)) + (math.pow(ballYTemp-paddle1Y,2)))
#         if distance <= 25:
#             return True

#     for xCord2 in range(int(paddle2X+100), int(paddle2X), -1):
#         paddle2Ytemp = paddle2Y + 20
#         ballXTemp = ballX + 25
#         ballYTemp = ballY + 25
#         distance = math.sqrt((math.pow(ballXTemp-xCord2, 2)) + (math.pow(ballYTemp-paddle2Ytemp,2)))
#         if distance <= 25:
#             return True
    
#     return False

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
    
    #score
    if ballY <= -50:
        score1 += 1
        ballX = 375
        ballY = 275
        print(score1)
    elif ballY >= 650:
        score2 += 1
        ballX = 375
        ballY = 275
        print(score2)

    #bounce off sides
    if ballX <= 0:
        ballX = 0
        ballXChange = ballSpeed
    elif ballX >= 750:
        ballX = 750
        ballXChange = -ballSpeed

    #bounce off paddle
    if distance1(ballX, ballY, paddle1X, paddle1Y) or distance2(ballX, ballY, paddle2X, paddle2Y):
        ballYChange = (-1)*ballYChange
        while distance1(ballX, ballY, paddle1X, paddle1Y) or distance2(ballX, ballY, paddle2X, paddle2Y):
            ballY += ballYChange
            ballX += ballXChange

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