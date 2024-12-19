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

def getInput():
    n = -1
    while (0 > n or n > 9):
        n = int(input("Enter a number 1 to 9\n"))
        print()
    return n

def clearScreen():
    print()
    print()
    print()

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
printBoard(board)
input = getInput()

if(input == -1):
    #1
    clearScreen()
    board = ['X', 'X', 'X', '4', '5', '6', '7', '8', '9']
    printBoard(board)
    print(detWin('X', board))
    #2
    clearScreen()
    board = ['1', '2', '3', 'X', 'X', 'X', '7', '8', '9']
    printBoard(board)
    print(detWin('X', board))
    #3
    clearScreen()
    board = ['1', '2', '3', '4', '5', '6', 'X', 'X', 'X']
    printBoard(board)
    print(detWin('X', board))

    #4
    clearScreen()
    board = ['X', '2', '3', 'X', '5', '6', 'X', '8', '9']
    printBoard(board)
    print(detWin('X', board))
    #5
    clearScreen()
    board = ['1', 'X', '3', '4', 'X', '6', '7', 'X', '9']
    printBoard(board)
    print(detWin('X', board))
    #6
    clearScreen()
    board = ['1', '2', 'X', '4', '5', 'X', '7', '8', 'X']
    printBoard(board)
    print(detWin('X', board))

    #7
    clearScreen()
    board = ['X', '2', '3', '4', 'X', '6', '7', '8', 'X']
    printBoard(board)
    print(detWin('X', board))
    #8
    clearScreen()
    board = ['1', '2', 'X', '4', 'X', '6', 'X', '8', '9']
    printBoard(board)
    print(detWin('X', board))

    #9
    clearScreen()
    board = ['1', '2', 'X', '4', 'X', '6', '7', '8', '9']
    printBoard(board)
    print(detWin('X', board))

