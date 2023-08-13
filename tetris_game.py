import pygame
import sys
from game import Game
from colors import Colors
pygame.init()

title_font=pygame.font.Font(None,40)
score_surface=title_font.render("Score ",True,Colors.WHITE)
next_surface=title_font.render("Next",True,Colors.WHITE)
game_over_surface=title_font.render("GAME OVER",True,Colors.WHITE)

score_rect=pygame.Rect(320,55,170,60)
next_rect=pygame.Rect(320,215,170,180)

WIDTH=500
HEIGHT=620

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Python Tetris") #Used for giving title

clock=pygame.time.Clock() #Used to control the frame rate of the game

game=Game()
GAME_UPDATE=pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,600)

while True:
    for event in pygame.event.get():
        if event==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if game.game_over==True:
                game.game_over=False
                pygame.time.wait(500)
                game.reset()
            if event.key==pygame.K_LEFT and game.game_over==False:
                game.move_left()
            if event.key==pygame.K_RIGHT and game.game_over==False:
                game.move_right()
            if event.key==pygame.K_DOWN and game.game_over==False:
                game.move_down()
                game.update_score(0,1)
            if event.key==pygame.K_UP and game.game_over==False:
                game.rotate()
        if event.type==GAME_UPDATE and game.game_over==False:
            game.move_down()
                
    score_value_surface=title_font.render(str(game.score),True,Colors.WHITE)
    screen.fill(Colors.DARKBLUE)
    screen.blit(score_surface,(365,20,50,50)) #block image transfer 
    screen.blit(next_surface,(375,180,50,50))
    if game.game_over==True:
        screen.blit(game_over_surface,(320,450,50,50))

    pygame.draw.rect(screen,Colors.LIGHTBLUE,score_rect,0,10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,centery = score_rect.centery))

    pygame.draw.rect(screen,Colors.LIGHTBLUE,next_rect,0,10)

    game.draw(screen)
    pygame.display.update()

    clock.tick(60) #runs 60 times a second