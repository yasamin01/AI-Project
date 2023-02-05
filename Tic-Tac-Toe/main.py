player, opponent = 'x', 'o'

def Move_Left(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ''):
                return True
    return False


def winner(b):
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == player):
                return 10
            elif (b[row][0] == opponent):
                return -10

    for col in range(3):
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
            if (b[0][col] == player):
                return 10
            elif (b[0][col] == opponent):
                return -10

    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        if (b[0][0] == player):
            return 10
        elif (b[0][0] == opponent):
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):
        if (b[0][2] == player):
            return 10
        elif (b[0][2] == opponent):
            return -10

    return 0


def minimax(board, depth, Max):
    score = winner(board)
    if(score == 10):
        return score

    if(score == -10):
        return score

    if(Move_Left(board) == False):
        return 0

    if(Max):
        best = -1000
        for i in range(3):
            for j in range(3):
                if(board[i][j] == ''):
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not Max))
                    board[i][j] = ''
        return best

    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if(board[i][j] == ''):
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not Max))
                    board[i][j] = ''

        return best


def Best_Move(board):
    bestScore = -1000
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ''):
                board[i][j] = player
                score = minimax(board, 0, False)
                board[i][j] = ''
                if(score > bestScore):
                    bestMove = (i, j)
                    bestScore = score

    print("Score of the best Move:", bestScore)

    return bestMove


board = [

    ['x', 'o', 'x'],

    ['o', 'o', 'x'],

    ['', '', '']
]

best_move = Best_Move(board)

print("Optimal Move:")

print("Row:", best_move[0], " Col:", best_move[1])


