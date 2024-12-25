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
        n = int(input("Enter a number 1 to 9 to choose a square, or enter 0 to have the computer make a move\n"))
        print()

        if(0< n <= 9):
            if(board[n - 1] == 'X' or board[n - 1] == 'O'):
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

def highValue(list):
    size = len(list)
    i = 1
    largeIndex = 0
    while(i < size):
        if(list[i] > list[largeIndex]):
            largeIndex = i
        i += 1
    return largeIndex

def calcMove(board, turn, turnNum):
    #determine if the game has already ended
    if(detWin(turn, board)):
        return 5 ** (11 - turnNum)
    elif(detWin(nextTurn(turn), board)):
        return -5 ** (11 - turnNum)
    elif(turnNum > 9): #tie
        return 1
    
    #tries every possible move to determine overall score of the position
    score = 0
    if(board[0] == '1'):
        testBoard = board.copy()
        testBoard[0] = turn
        #-= because it is calculating whether or not the other person wins
        score -= calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[1] == '2'):
        testBoard = board.copy()
        testBoard[1] = turn
        score -= calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[2] == '3'):
        testBoard = board.copy()
        testBoard[2] = turn
        score -= calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[3] == '4'):
        testBoard = board.copy()
        testBoard[3] = turn
        score -= calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[4] == '5'):
        testBoard = board.copy()
        testBoard[4] = turn
        score -= calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[5] == '6'):
        testBoard = board.copy()
        testBoard[5] = turn
        score -= calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[6] == '7'):
        testBoard = board.copy()
        testBoard[6] = turn
        score -= calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[7] == '8'):
        testBoard = board.copy()
        testBoard[7] = turn
        score -= calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[8] == '9'):
        testBoard = board.copy()
        testBoard[8] = turn
        score -= calcMove(testBoard, nextTurn(turn), turnNum + 1)
    
    return score

def detBestMove(board, turn, turnNum):
    #populates a list of possible moves with -10^100 so if the space is occupied
    #then the scores of non-occupied squares will be higher
    scores = [-10 ** 100] * 9

    #Checks to see if the space is open, and if so, calculates how beneficial that move would be
    if(board[0] == '1'):
        testBoard = board.copy()
        testBoard[0] = turn
        scores[0] = -1* calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[1] == '2'):
        testBoard = board.copy()
        testBoard[1] = turn
        scores[1] = -1* calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[2] == '3'):
        testBoard = board.copy()
        testBoard[2] = turn
        scores[2] = -1* calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[3] == '4'):
        testBoard = board.copy()
        testBoard[3] = turn
        scores[3] = -1* calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[4] == '5'):
        testBoard = board.copy()
        testBoard[4] = turn
        scores[4] = -1* calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[5] == '6'):
        testBoard = board.copy()
        testBoard[5] = turn
        scores[5] = -1* calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[6] == '7'):
        testBoard = board.copy()
        testBoard[6] = turn
        scores[6] = -1* calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[7] == '8'):
        testBoard = board.copy()
        testBoard[7] = turn
        scores[7] = -1* calcMove(testBoard, nextTurn(turn), turnNum + 1)
    if(board[8] == '9'):
        testBoard = board.copy()
        testBoard[8] = turn
        scores[8] = -1* calcMove(testBoard, nextTurn(turn), turnNum + 1)
    
    return highValue(scores)



board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
turn = 'X'
turnNum = 1

while not (turnNum > 9 or detWin('O', board) or detWin('X', board)):
    turn = nextTurn(turn)
    printBoard(board)
    pInput = getInput(board)

    if(pInput == 0):
        pInput = detBestMove(board, turn, turnNum) + 1
    board[pInput - 1] = turn
    turnNum += 1
    clearScreen()

printBoard(board)
if(turnNum > 9):
    print("Draw!")
else:
    print(turn, "'s won!", sep='')