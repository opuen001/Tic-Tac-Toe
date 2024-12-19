int = __builtins__.int

def printBoard(board):
    print(board[0], " | ", board[1], " | ", board[2])
    print("-------------")
    print(board[3], " | ", board[4], " | ", board[5])
    print("-------------")
    print(board[6], " | ", board[7], " | ", board[8])

def detWin(letter, board):
    # Horizontals
    if ((board[0] == letter and board[1] == letter and board[2] == letter)
    or (board[3] == letter and board[4] == letter and board[5] == letter)
    or (board[6] == letter and board[7] == letter and board[8] == letter)):
        return True
    # Verticals
    elif((board[0] == letter and board[3] == letter and board[6] == letter)
    or (board[1] == letter and board[4] == letter and board[7] == letter)
    or (board[2] == letter and board[5] == letter and board[8] == letter)):
        return True
    # Diagonals
    elif((board[0] == letter and board[4] == letter and board[8] == letter)
    or (board[2] == letter and board[4] == letter and board[6] == letter)):
        return True
    else:
        return False

def getInput(board):
    n = -1

    while (0 > n or n > 9):
        n = int(input("Enter a number 1 to 9\n"))
        print()

        if(0<= n <= 9):
            if(board[n - 1] == 'X' or board[n-1] == 'O'):
                print("That square is taken, please choose another")
                n = -1 #so that the while loop runs again
            
    return n

def clearScreen():
    print()
    print()
    print()

def nextTurn(turn):
    if(turn == 'O'):
        return 'X'
    else:
        return 'O'

def gameOver(board):
    if(detWin('O', board) or detWin('X', board)):
        return True
    else:
        return ((board[0] != '1') and (board[1] != '2') and (board[2] != '3')
                and (board[3] != '4') and (board[4] != '5') and (board[5] != '6')
                and (board[6] != '7') and (board[7] != '8') and (board[8] != '9'))

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
gameEnd = False
turn = 'X'

while not (gameEnd):
    turn = nextTurn(turn)
    printBoard(board)
    pInput = getInput(board)
    board[pInput - 1] = turn

    gameEnd = gameOver(board)

printBoard(board)
print(turn, "'s won!", sep='')