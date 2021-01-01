import numpy as np

rows = 6
cols = 7
board = np.zeros((rows, cols))
game_over = False
turn = 0

def is_valid_column(board, col):
	return board[rows - 1][col] == 0


def drop_piece(board, col, piece):
	for r in range(rows):
		if board[r][col] == 0:
			row = r
			break
	board[row][col] = piece

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


while not game_over:
	if turn % 2 == 0:
		# player 1 turn
		col = int(input("Player 1 Please Pick a Column: "))
		if (is_valid_column(board, col)):
			drop_piece(board, col - 1, 1)
			if (is_win_move(board, 1)):
				game_over = True
				print("Player 1 Wins!")
		else: 
			turn -= 1
	else:
		# player 2 turn
		col = int(input("Player 2 Please Pick a Column: "))
		if (is_valid_column(board, col)):
			drop_piece(board, col - 1, 2)
			if (is_win_move(board, 2)):
				game_over = True
				print("Player 2 Wins!")
		else: 
			turn -= 1
	print(np.flip(board, 0))
	print()
	turn += 1
