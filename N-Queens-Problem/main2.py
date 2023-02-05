import random
from copy import deepcopy
from math import exp

board_size = 0


def print_board(board):
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end=' ')
        print()


def place_queens(board):
    count = 0
    while count < board_size:
        row = random.randint(0, board_size - 1)
        col = count
        board[row][col] = 1
        count += 1


def get_queens(board):
    position_q = []
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 1:
                x = i, j
                position_q.append(x)
    return position_q


def attacking_queens(board):
    positions = get_queens(board)
    attacks = 0
    for i in range(len(positions)):
        queen_position = positions[i]
        for j in range(len(positions)):
            if i != j:
                others = positions[j]
                if others[0] == queen_position[0]:
                    attacks += 1

                x_others, y_others = others[0], others[1]

                x = deepcopy(queen_position[0])
                y = deepcopy(queen_position[1])

                while x >= 0 and y >= 0:
                    x -= 1
                    y -= 1
                    if x == x_others and y == y_others:
                        attacks += 1

                x = deepcopy(queen_position[0])
                y = deepcopy(queen_position[1])

                while x < board_size and y < board_size:
                    x += 1
                    y += 1
                    if x == x_others and y == y_others:
                        attacks += 1

                x = deepcopy(queen_position[0])
                y = deepcopy(queen_position[1])

                while x < board_size and y >= 0:
                    x += 1
                    y -= 1
                    if x == x_others and y == y_others:
                        attacks += 1

                x = deepcopy(queen_position[0])
                y = deepcopy(queen_position[1])

                while x >= 0 and y < board_size:
                    x -= 1
                    y += 1
                    if x == x_others and y == y_others:
                        attacks += 1

    return int(attacks / 2)


def expand_board(board, positions):
    boards = []
    for i in range(len(positions)):
        x = deepcopy(positions[i][0])
        y = deepcopy(positions[i][1])
        for j in range(board_size):
            if x != j:
                b = deepcopy(board)
                b[x][y] = 0
                b[j][y] = 1
                boards.append(b)
    return boards


def move_queen(board):
    random_col = random.randint(0, len(board) - 1)
    random_row = random.randint(0, len(board) - 1)
    for row, col in get_queens(board):
        if col == random_col:
            while row == random_row:
                random_row = random.randint(0, len(board) - 1)
            b = deepcopy(board)
            b[random_row][col], b[row][col] = b[row][col], b[random_row][col]
            return b


def minboard(boards):
    boards.sort(key=attacking_queens)
    return boards[0]


# Hill Climbing


def hill_climbing(board):
    moves = 0
    while True:
        moves += 1
        positions = get_queens(board)
        h = attacking_queens(board)
        boards = expand_board(board, positions)
        min_board = minboard(boards)
        min_h = attacking_queens(min_board)
        if min_h >= h:
            return board, moves, h
        elif min_h == 0:
            return min_board, moves, min_h
        else:
            board = min_board


# Simulated Annealing


def simulated_annealing(board, max_t):
    b = board
    moves = 0
    for t in range(1, max_t):
        T = ((t + 1) / max_t)
        moves += 1
        b_h = attacking_queens(b)
        neighbour = move_queen(b)
        neighbour_h = attacking_queens(neighbour)
        delta = neighbour_h - b_h
        e = (-delta) / T
        if e < 0:
            b = neighbour
        try:
            if random.uniform(0, 1) < exp(e):
                b = neighbour
        except:
            pass
        if neighbour_h == 0:
            return neighbour, moves
    return b, moves


def main():
    global board_size
    board_size = int(input("Number of Queens: "))

    board = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append(0)
        board.append(row)

    print("Initial board:\n")

    place_queens(board)
    print_board(board)

    print("\n Hill Climbing")
    result, moves, h = hill_climbing(board)
    print_board(result)

    print("\nattacks: ", h)
    print("moves: ", moves)

    print("\n Simulated Annealing")
    max_t = 100000
    result, moves = simulated_annealing(board, max_t)
    print_board(result)

    print("\nattacks: ", attacking_queens(result))
    print("moves: ", moves)


if __name__ == "__main__":
    main()


# Genetic Algorithm

n = 8
population = 500
current = []
new = []

print("\n Genetic Algorithm")


def random_(rows, queens):
    generation_list = []
    for i in range(rows):
        gene = []
        for j in range(queens):
            gene.append(random.randint(1, n))
        gene.append(0)
        generation_list.append(gene)
    return generation_list


def fitness(population_list):
    i = 0
    conflict = 0
    while i < len(population_list):
        j = 0
        x = 0
        while j < n:
            l = j + 1
            while l < n:
                if population_list[i][j] == population_list[i][l]:
                    x += 1
                if abs(j - l) == abs(population_list[i][j] - population_list[i][l]):
                    x += 1
                l += 1
            j += 1
        population_list[i][len(population_list[j]) - 1] = x
        i += 1
    for i in range(len(population_list)):
        min = i
        for j in range(i, len(population_list)):
            if population_list[j][n] < population_list[min][n]:
                min = j
        temp = population_list[i]
        population_list[i] = population_list[min]
        population_list[min] = temp
    return population_list


def cross_over(generation_list):
    for i in range(0,len(generation_list), 2):
        z = 0
        new1 = []
        new2 = []
        while z<n:
            if(z<n//2):
                new1.append(generation_list[i][z])
                new2.append(generation_list[i+1][z])
            else:
                new1.append(generation_list[i+1][z])
                new2.append(generation_list[i][z])
            z+=1
        new1.append(0)
        new2.append(0)
        generation_list.append(new1)
        generation_list.append(new2)
    return generation_list


def mutation(generation_list):
    muted_list=[]
    i = 0
    while i<population//2:
        new_rand = random.randint(population//2,population-1)
        if new_rand not in muted_list:
            muted_list.append(new_rand)
            generation_list[new_rand][random.randint(0,n-1)]=random.randint(1,n-1)
            i+=1
    return generation_list


current_generation = random_(population,n)
current_generation = fitness(current_generation)
epoch = 1
while True:
    print("Epoch ",epoch)
    current_generation = current_generation[0:population//2]
    new_generation = cross_over(current_generation)
    new_generation = mutation(new_generation)
    current_generation = new_generation
    current_generation = fitness(current_generation)
    if current_generation[0][n] == 0:
        print("Solution Found: ", current_generation[0])
        break
    else:
        print("Best Solution: ", current_generation[0])
    epoch+=1