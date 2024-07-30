import sys

def print_solution(board):
    """Prints the board with queens placed."""
    for row in board:
        print(''.join('Q' if cell else '.' for cell in row))

def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]."""
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    
    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j]:
            return False
        i -= 1
        j += 1
    
    return True

def solve_nqueens(board, row):
    """Uses backtracking to solve the N-Queens problem."""
    n = len(board)
    if row >= n:
        print_solution(board)
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = True
            solve_nqueens(board, row + 1)
            board[row][col] = False

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[False] * n for _ in range(n)]
    solve_nqueens(board, 0)

if __name__ == "__main__":
    main()
