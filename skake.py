import pygame
import random

pygame.init()
dis_height = 600
dis_width = 800
dis=pygame.display.set_mode((dis_width,dis_height))

white = (255, 255, 255)
yellow = (255, 255, 25)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 50, 255)

pygame.display.set_caption('SnakePY')

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("calibri", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [20, dis_height/2])

def score_draw(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
def snake_draw(snake_Nlist,snake_block):
    for x in snake_Nlist:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def gameloop():
    game_over = False
    game_close = False
    direction = 'rigth'

    x1 = dis_width/2
    y1 = dis_height/2

    x1n = 0
    y1n = 0

    snake_Nlist = []
    snake_size = 1

    foodx = round(random.randrange(10,dis_height-10)/10) * 10
    foody = round(random.randrange(10,dis_width-10)/10) * 10

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost:( Q-Quit or P-Play", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction!='right':
                    x1n = -snake_block
                    y1n = 0
                    direction = 'left'
                elif event.key == pygame.K_RIGHT and direction!='left':
                    x1n = snake_block
                    y1n = 0
                    direction = 'right'
                elif event.key == pygame.K_DOWN and direction!='up':
                    x1n = 0
                    y1n = snake_block
                    direction = 'down'
                elif event.key == pygame.K_UP and direction!='down':
                    x1n = 0
                    y1n = -snake_block
                    direction = 'up'
            if x1 >= dis_width or x1<0 or y1 >= dis_height or y1 <0:
                game_close = True

            x1 += x1n
            y1 += y1n

            dis.fill(blue)

            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_Nlist.append(snake_Head)

            if len(snake_Nlist) > snake_size:
                del snake_Nlist[0]
            
            for i in snake_Nlist[:-1]:
                if i == snake_Head:
                    game_close = True
 
            snake_draw(snake_Nlist, snake_block)
 
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                snake_size += 1

            score = (snake_size * 10) - 10
            score_draw(score)

            pygame.display.update()

    pygame.quit()
    quit()
 
gameloop()