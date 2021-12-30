import pygame
import time
import random
from pygame import mixer
import pickle
#Initialization of the library pygame
pygame.init() 
#initizalization of pygame's sound library
pygame.mixer.init()
#Defining parameters for window size
window_length=800
window_height=800
#Differnt colors for easy use
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
#Parameters for the window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_length, window_height))
#fps controller
fps = pygame.time.Clock()
#playing background music
mixer.music.load("sounds/backgroundmusic.wav")
mixer.music.set_volume(0.4)
mixer.music.play(-1)
#sound effects
deathsound=pygame.mixer.Sound('sounds/gameover.wav')
eatsound=pygame.mixer.Sound('sounds/crunch.wav')
#defining the postion of the snake
snake_position=[100,50]
#body of the snake
snake_body=[
[100,50],
[90,50],
[80,50],
[70,50]
]
#fruit position
fruit_position=[
random.randrange(1,(window_length//10))*10,
random.randrange(1,(window_height//10))*10
]
fruit_spawn=True
#defining snake speed
snake_speed=15
#default snake direction is right
direction='RIGHT'
change_to=direction
#initial score
score=0
#defining score function
def show_score(choice,color,font,size):
    #creating font
    score_font=pygame.font.SysFont('Sans',20)
    #creating a display for the surface object for the score
    score_surface=score_font.render('Score: '+str(score),True,color)
    #creating a rectangular object for the text surface object
    score_rect=score_surface.get_rect()
    #displaying the text
    game_window.blit(score_surface,score_rect)
#defining game over function
def game_over():
    my_font=pygame.font.SysFont('Sans',50)
    #creating text surface for text to be drawn
    game_over_surface=my_font.render('Your score is: '+str(score),True,red)
    game_over_rect=game_over_surface.get_rect()
    deathsound.play()
    #position of the window
    game_over_rect.midtop=(window_length/2,window_height/4)
    #blit function draws text on screen
    game_window.blit(game_over_surface,game_over_rect)
    pygame.display.flip()
    #after 2 seconds the program closes
    time.sleep(2)
    #deactivation the pygame lib
    pygame.quit()
    #quits the program
    quit()

#main function
while True:

    #key events/ input fuctions from keyboard
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                change_to='UP'
            if event.key==pygame.K_DOWN:
                change_to='DOWN'
            if event.key==pygame.K_LEFT:
                change_to='LEFT'
            if event.key==pygame.K_RIGHT:
                change_to='RIGHT'
    #For a bug that occurs when you press two keys simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    #implementing core game mechanics
    #score incrementing when collided with "FRUIT"
    #also growth mechanic of the snake
    snake_body.insert(0,list(snake_position))
    if snake_position[0]==fruit_position[0] and snake_position[1]==fruit_position[1]:
        score+=1
        eatsound.play()
        snake_speed+=2
        fruit_spawn=False
    else:
        snake_body.pop()
    if not fruit_spawn:
        fruit_position=[
            random.randrange(1,(window_length//10))*10,
            random.randrange(1,(window_height//10))*10]
    fruit_spawn=True
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window,green,pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(game_window,red,pygame.Rect(fruit_position[0],fruit_position[1],10,10))

    #game over 
    if snake_position[0]<0 or snake_position[0]>window_length-10:
        game_over()
    if snake_position[1]<0 or snake_position[1]>window_height-10:
        game_over()
    #touching the snake body
    for block in snake_body[1:]:
        if snake_position[0]==block[0] and snake_position[1]==block[1]:
            game_over()
    #dispalying score
    show_score(1,white,'sans',20)
    with open('score.dat','rb') as file:
        v=pickle.load(file)
        if(score>v):
         with open('score.dat','wb') as file:
          pickle.dump(score,file)
    # refreshs game screen
    pygame.display.update()
    #fps
    fps.tick(snake_speed)