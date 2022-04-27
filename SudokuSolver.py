#Implementing Backtracking algorithm.

board = [
    [7,8,0,4,0,0,1,2,0],
    [7,8,0,4,0,0,1,2,0],
    [7,8,0,4,0,0,1,2,0],
    [7,8,0,4,0,0,1,2,0],
    [7,8,0,4,0,0,1,2,0],
    [7,8,0,4,0,0,1,2,0],
    [7,8,0,4,0,0,1,2,0],
    [7,8,0,4,0,0,1,2,0],
    [7,8,0,4,0,0,1,2,0]
]


def display_board(board):
    
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - -", end ="")#
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print (" | ", end = "")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")
                
                
def find_empty(board):
    for i in range(len(board)):
        for j in range (len(board[0])):
            if board[i][j] == 0:
                return (i,j) #row, column
                
    
    
    
