#Implementing Backtracking algorithm.

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(brd):
    find = find_empty(brd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0

    return False


def valid(brd, num, pos):
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    # Check surrounding box
    pos_x = pos[1] // 3
    pos_y = pos[0] // 3

    for i in range(pos_y*3, pos_y*3 + 3):
        for j in range(pos_x * 3, pos_x*3 + 3):
            if brd[i][j] == num and (i,j) != pos:
                return False

    return True


def display_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")


def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)  # row, col

    return None



display_board(board)
solve(board)
print("SOLVED:" + '\n')
display_board(board)
                
    
    
    
