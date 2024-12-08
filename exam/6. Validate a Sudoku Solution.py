#Write a function that validates whether a given Sudoku board is solved correctly. The board is represented as a 2D array of size 9x9. A valid solution must meet these conditions:
#Each row contains numbers 1–9 without repetition.
#Each column contains numbers 1–9 without repetition.
#Each 3x3 subgrid contains numbers 1–9 without repetition.
def is_valid_set(nums):
    nums=[num for num in nums if nums != '.']
    return len(nums)==len (set(nums))and all(1 < int(num)<9 for num in nums)

def is_valid_sudoku(board):
    for i in range(9):
        if not is_valid_set(board[i]):
            return False
        if not is_valid_set([board[j][i]for j in range(9)]):
            return False
        
        if not is_valid_set([board[r][c]for r in range(i // 3 * 3, i // 3 * 3 + 3)
                             for c in range(i % 3 * 3, i % 3 * 3 + 3)]):
            return False
    return True    
        
