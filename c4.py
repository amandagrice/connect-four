import numpy as np
import pygame
import math

rows = 6
cols = 7
board = np.zeros((rows, cols))
game_over = False
turn = 0

slot_width = 100
board_width = cols * slot_width
board_height = (rows + 1) * slot_width
board_size = (board_width, board_height)

red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
white = (0, 0, 0)
offset = 100
radius = int(slot_width / 2 - 5)

def draw_board(board):
	print("called draw board")
	pygame.draw.rect(window, white, (0, 0, board_width, slot_width))
	for c in range(cols):
		for r in range(rows):
			rect = (c * slot_width, r * slot_width + offset, slot_width, slot_width)
			c1 = (int(c * slot_width + slot_width / 2), int(r * slot_width + offset + slot_width / 2))
			pygame.draw.rect(window, blue, rect)
			pygame.draw.circle(window, white, c1, radius)
	for c in range(cols):
		for r in range(rows):
			c2 = (int(c * slot_width + slot_width / 2), board_height - int(r * slot_width + slot_width / 2))
			if board[r][c] == 1:
				pygame.draw.circle(window, red, c2, radius)
			elif board[r][c] == 2:
				pygame.draw.circle(window, yellow, c2, radius)
	pygame.display.update()

def is_valid_column(board, col):
	return board[rows - 1][col] == 0


def drop_piece(board, col, piece):
	for r in range(rows):
		if board[r][col] == 0:
			row = r
			break
	board[row][col] = piece
	draw_board(board)

def is_win_move(board, piece):
	# horizontal check
	for c in range(cols - 3):
		for r in range(rows):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True
	# vertical check
	for c in range(cols):
		for r in range(rows - 3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True
	# diagonal check
	for c in range(cols - 3):
		for r in range(rows - 3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True
	for c in range(cols - 3):
		for r in range(3, rows):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True


pygame.init()
window = pygame.display.set_mode(board_size)
pygame.display.set_caption("Connect Four")
draw_board(board)

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.MOUSEBUTTONDOWN:	
			print(event.pos)
			posx = event.pos[0]
			if turn % 2 == 0:
				# player 1 turn
				col = math.floor(posx / slot_width)
				if (is_valid_column(board, col)):
					drop_piece(board, col, 1)
					if (is_win_move(board, 1)):
						game_over = True
						print("Player 1 Wins!")
				else: 
					turn -= 1
			else:
				# player 2 turn
				col = math.floor(posx / slot_width)
				if (is_valid_column(board, col)):
					drop_piece(board, col, 2)
					if (is_win_move(board, 2)):
						game_over = True
						print("Player 2 Wins!")
				else: 
					turn -= 1
			print(np.flip(board, 0))
			print()
			turn += 1
