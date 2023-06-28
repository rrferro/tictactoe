import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
winner = None
game_running = True


# print game board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# printBoard(board)
# take player input
def player_input(boardpa):
    inp = int(input("Enter a number from 1 - 9 that represents the position\n"))
    if 1 <= inp <= 9 and boardpa[inp - 1] == "-":
        boardpa[inp - 1] = current_player
    else:
        print("That position is already taken")
        player_input(boardpa)


# check for win or tie
def check_horizontal_win(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def check_vertical_win(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def check_diagonal_win(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def computer(boardpa):
    while current_player == "0":
        position = random.randint(0, 8)
        if boardpa[position] == "-":
            boardpa[position] = "0"
            switch_player()


def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("It's a tie!!!")
        game_running = False


def check_win():
    global game_running
    if check_diagonal_win(board) or check_vertical_win(board) or check_horizontal_win(board):
        print(f"The winner is {winner}")
        game_running = False
        print_board(board)
        exit()


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "0"
    else:
        current_player = "X"


while game_running:
    print_board(board)
    player_input(board)
    if check_win():
        print_board(board)
        break
    check_tie(board)
    switch_player()
    computer(board)
    check_win()
    check_tie(board)
