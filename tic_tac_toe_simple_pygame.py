import pygame, sys
from pygame.locals import *

#initialize pygame modules
pygame.init()

#initialize window for display
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe')

#define colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)

#define height and width of cell
width=200
height=200

#default values for game
game_count = 0
player = True
BOARD_SIZE = 3
board = []

#check_for_end_of_game - check if the current player won
#player - current player number(1 or 2)
#rect - current rect in which the player clicked
#returns:
#	True - if the current player won, else False
def check_for_end_of_game(player, rect):
	#Row wise check
	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE-1):
			if (board[i][j] != board[i][j+1]):
				break
		if j==BOARD_SIZE-2 and board[i][j] == board[i][j+1] and board[i][j] == player:
			#player won, strike through the combination
			pygame.draw.line(window, blue, (50, rect.top+100), (550, rect.top+100), 3)
			pygame.display.update()
			return True

	#Column wise check
	for j in range(BOARD_SIZE):
		for i in range(BOARD_SIZE-1):
			if (board[i][j] != board[i+1][j]):
				break
		if (i==BOARD_SIZE -2 and board[i][j] == board[i+1][j] and board[i][j] == player):
			pygame.draw.line(window, blue, (rect.left+100, 50), (rect.left+100, 550), 3)
			pygame.display.update()
			return True

	#Right diagonal wise check
	for i in range(BOARD_SIZE-1):
		if (board[i][i] != board[i+1][i+1]):
			break
	if (i==BOARD_SIZE-2 and board[i][i] == board[i+1][i+1] and board[i][i] == player):
		pygame.draw.line(window, blue, (50, 50), (550, 550), 3)
		pygame.display.update()
		return True

	#Left diagonal wise check
	for i, j in zip(range(BOARD_SIZE-1), range(BOARD_SIZE-1, 0, -1)):
		if (board[i][j] != board[i+1][j-1]):
			break
	if (j==1 and board[i][j] == board[i+1][j-1] and board[i][j] == player):
		pygame.draw.line(window, blue, (550, 50), (50, 550), 3)
		pygame.display.update()
		return True

	return False

#re-draw the screen and display text
def display_text(text):
	pygame.time.wait(4000)
	window.fill(black)
	myfont = pygame.font.SysFont('Times New Roman', 35, True)
	textsurface = myfont.render(text, False, yellow)
	window.blit(textsurface,(50,200))
	pygame.display.update()
	pygame.time.wait(4000)

#create board matrix
for i in range(BOARD_SIZE):
	board.append([])
	for j in range(BOARD_SIZE):
		board[i].append(0)

# main game loop
while True:
	#draw game grid
	rect_1 = pygame.draw.rect(window,white, [0,0,width,height] , 1)
	rect_2 = pygame.draw.rect(window,white, [0,200,width,height] , 1)
	rect_3 = pygame.draw.rect(window,white, [0,400,width,height] , 1)
	rect_4 = pygame.draw.rect(window,white, [200,0,width,height] , 1)
	rect_5 = pygame.draw.rect(window,white, [200,200,width,height] , 1)
	rect_6 = pygame.draw.rect(window,white, [200,400,width,height] , 1)
	rect_7 = pygame.draw.rect(window,white, [400,0,width,height] , 1)
	rect_8 = pygame.draw.rect(window,white, [400,200,width,height] , 1)
	rect_9 = pygame.draw.rect(window,white, [400,400,width,height] , 1)
	rect_list = [[rect_1, rect_4, rect_7], [rect_2, rect_5, rect_8], [rect_3, rect_6, rect_9]]

	pygame.display.update()

	#check for events and take actions accordingly
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type ==  MOUSEBUTTONDOWN:
			mouse_coordinates = pygame.mouse.get_pos()
			#get the rect and pos in which user clicked
			for i in range(BOARD_SIZE):
				for j in range(BOARD_SIZE):
					if rect_list[i][j].collidepoint(mouse_coordinates):
						rect = rect_list[i][j]
						x, y = i, j
			#check if the box is already used
			if board[x][y] != 0:
				print("Box already used")
				continue

			if player:
				board[x][y] = 1
				pygame.draw.line(window, red, (rect.left+50, rect.top+50), (rect.left+150, rect.top+150), 3)
				pygame.draw.line(window, red, (rect.left+150, rect.top+50), (rect.left+50, rect.top+150), 3)
			else:
				board[x][y] = 2
				pygame.draw.circle(window, yellow, (rect.left+100, rect.top+100), 65)
			pygame.display.update()

			game_count += 1
			if check_for_end_of_game(1 if(player) else 2, rect):
				winner = "Congratulations... Player " + (str(1) if(player) else str(2)) + " Wins"
				display_text(winner)
				pygame.quit()
				sys.exit()

			player = not(player)
			if (game_count == BOARD_SIZE*BOARD_SIZE):
				display_text("Game Tie!! Thanks for playing")
				pygame.quit()
				sys.exit()
