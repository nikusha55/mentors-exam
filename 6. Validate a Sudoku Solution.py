def is_valid_sudoku(board):
   
    for row in board:
        if not is_valid_group(row):
            return False

    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_group(column):
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(board[row + i][col + j])
            if not is_valid_group(subgrid):
                return False

    return True

def is_valid_group(group):

    filtered_group = [num for num in group if num != 0]
    return len(filtered_group) == len(set(filtered_group)) and all(1 <= num <= 9 for num in filtered_group)

