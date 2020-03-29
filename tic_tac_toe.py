# Programmer: Matthew Landes
# Date:		  March 15, 2020


board = {'top_left': ' ', 'top_middle': ' ', 'top_right': ' ', 
         'mid_left': ' ', 'mid_middle': ' ', 'mid_right': ' ',
		 'low_left': ' ', 'low_middle': ' ', 'low_right': ' '}
		 
board_key = list(board.keys())

print('')
print('')
print('Positions on the board')
print('')
print(board_key[0] + ' | ' + board_key[1] + ' | ' + board_key[2])
print('--------' + ' + ' + '----------' + ' + ' + '---------')
print(board_key[3] + ' | ' + board_key[4] + ' | ' + board_key[5])
print('--------' + ' + ' + '----------' + ' + ' + '---------') 
print(board_key[6] + ' | ' + board_key[7] + ' | ' + board_key[8])
print('')

def print_board(board):
	print(board['top_left'] + ' | ' + board['top_middle'] + ' | ' + board['top_right'])
	print('--+---+--')
	print(board['mid_left'] + ' | ' + board['mid_middle'] + ' | ' + board['mid_right'])
	print('--+---+--')
	print(board['low_left'] + ' | ' + board['low_middle'] + ' | ' + board['low_right'])
	return
	
def check_winner(board):
	if ((((board['top_left'] == board['mid_left'])     & (board['top_left'] == board['low_left'])     & (board['top_left'] != ' ')))   |
	   (((board['top_middle'] == board['mid_middle']) & (board['top_middle'] == board['low_middle']) & (board['top_middle'] != ' '))) |
	   (((board['top_right'] == board['mid_right'])   & (board['top_right'] == board['low_right'])   & (board['top_right'] != ' ')))  |
	   (((board['top_left'] == board['top_middle'])   & (board['top_left'] == board['top_right'])    & (board['top_left'] != ' ')))   |
	   (((board['mid_left'] == board['mid_middle'])   & (board['mid_left'] == board['mid_right'])    & (board['mid_left'] != ' ')))   |
	   (((board['low_left'] == board['low_middle'])   & (board['low_left'] == board['low_right'])    & (board['low_left'] != ' ')))   |
	   (((board['top_left'] == board['mid_middle'])   & (board['top_left'] == board['low_right'])    & (board['top_left'] != ' ')))   |
	   (((board['low_left'] == board['mid_middle'])   & (board['low_left'] == board['top_right'])    & (board['low_left'] != ' ')))):
		winner = True
	else:
		winner = False
	return winner
	   
turn = 'X'

round = 1
while round <= 9:
	print_board(board)
	print('Turn for ' + turn + '. Move on which space?')
	move = input()
	while (move not in board_key) | (board.get(move, 'Bad') != ' '):
		if move not in board_key:
			print('Did not recognize position. Please enter a valid position')
			move = input()
		else:
			print('Space is not available.  Please select another postion')
			move = input()
	board[move] = turn
	if check_winner(board):
		print('Congratulations ' + turn + ' on winning the game!')
		break
	
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
	round += 1

if round > 9:
	print('Game is a draw!')

print_board(board)
