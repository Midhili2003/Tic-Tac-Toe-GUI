import pygame
from pygame.locals import*

#initialize pygame
pygame.init()

#assigning screenwidth and screenheight
screen_width = 300
screen_height = 300

#define colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#define variables
line_width = 6
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False

#define font
font = pygame.font.SysFont(None, 40)

#create play again rectangle
again_rect = Rect(screen_width // 2 - 80,screen_height // 2, 160, 54)

#create screen
game_board = pygame.display.set_mode((screen_width, screen_height))

#title
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("Tictactoe.png")
pygame.display.set_icon(icon)

def draw_grid():
    bg = (250,200,190)  #define background colour
    grid = (50,50,50)    #define grid line colour
    game_board.fill(bg)
    for i in range(1,3):
        pygame.draw.line(game_board, grid, (0, i*100), (screen_width, i*100), line_width)
        pygame.draw.line(game_board, grid, (i*100, 0), (i*100, screen_height), line_width)
for i in range(3):
    row = [0]*3
    markers.append(row)
print(markers)

def draw_markers():
    pos_x = 0
    for m in markers:
        pos_y = 0
        for p in m:
            if p == 1:
                pygame.draw.line(game_board, green, (pos_x*100 + 15, pos_y*100 + 15), (pos_x*100 + 85, pos_y*100 + 85), line_width)
                pygame.draw.line(game_board, green, (pos_x*100 + 15, pos_y*100 + 85), (pos_x*100 + 85, pos_y*100 + 15), line_width)
            if p == -1:
                pygame.draw.circle(game_board, red, (pos_x*100 + 50, pos_y*100 + 50), 38, line_width)
            pos_y += 1
        pos_x += 1
def check_winner():
    global winner
    global game_over
    pos_y = 0
    for i in markers:
        #check columns
        if sum(i) == 3:
            winner = 1
            game_over = True
        if sum(i) == -3:
            winner = 2
            game_over = True
            
        #check rows
        if markers[0][pos_y] + markers[1][pos_y] + markers[2][pos_y] == 3:
            winner = 1
            game_over = True
        if markers[0][pos_y] + markers[1][pos_y] + markers[2][pos_y] == -3:
            winner = 2
            game_over = True
        pos_y += 1

        #check cross
        if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
            winner = 1
            game_over = True
        if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
            winner = 2
            game_over = True
        
                    
def draw_winner(winner):
    win_text = " Player " + str(winner) + " wins! "
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(game_board, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    game_board.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = "Play Again!"
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(game_board, green,again_rect)
    game_board.blit(again_img, (screen_width // 2 - 80, screen_height //2 + 10))
    

#main loop
run = True
while run:
    draw_grid()
    draw_markers()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x//100][cell_y//100] == 0:
                    markers[cell_x//100][cell_y//100] = player
                    player*= -1
                    check_winner()
                
    if game_over == True and (winner == 1 or winner == 2):
        draw_winner(winner)
   
    #check for mouseclick to see if user has clickd on play again
    if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
        clicked = True
    if event.type == pygame.MOUSEBUTTONUP and clicked == True:
        clicked = False
        pos = pygame.mouse.get_pos()
        if again_rect.collidepoint(pos):
            #reset variables
            markers = []
            pos = []
            player = 1
            winner = 0
            game_over = False
        for x in range(3):
            row = [0]*3
            markers.append(row)
    pygame.display.update()

pygame.quit()
            
