board=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                return i, j

def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(sudoku[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j % 8 == 0 and j != 0:
                print(str(sudoku[i][j]) + " ")
            else:
                print(str(sudoku[i][j]) + " ", end="")

def check(sudoku, n, position):
    #Row
    for i in range(len(sudoku[0])):
        if sudoku[position[0]][i] == n and position[1] != 0:
            return False
    #Column
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == n and position[0] != 0:
            return False
    #Square
    sq_x = position[0] // 3
    sq_y = position[1] // 3
    for i in range(sq_x * 3, sq_x * 3 + 3):
        for j in range(sq_y * 3, sq_y * 3 + 3):
            if sudoku[i][j] == n and (i, j) != position:
                return False
    
    return True

def solve(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        row, column = find
    for i in range(1, 10):
        if(check(sudoku, i, (row, column))):
            sudoku[row][column] = i
            if solve(sudoku):
                return True
            sudoku[row][column] = 0
    return False


print(print_sudoku(board))
solve(board)
print("***********************")
print("***********************")
print("***********************")
print("***********************")
print(print_sudoku(board))