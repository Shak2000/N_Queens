def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe"""

    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n, solutions):
    """Recursive function to solve n-Queens using backtracking"""

    # Base case: all queens placed
    if row == n:
        solutions.append([row[:] for row in board])  # Deep copy of solution
        return

    # Try placing queen in each column of current row
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen
            board[row][col] = 'Q'

            # Recursively place queens in next rows
            solve_nqueens(board, row + 1, n, solutions)

            # Backtrack - remove queen
            board[row][col] = '.'


def print_solutions(solutions):
    """Print all solutions in a readable format"""
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for row in solution:
            print(' '.join(row))
        print()


def main():
    print("Welcome to the n-Queens solver!")

    while True:
        user_input = input("Enter an integer board size to see the solver in action or 'quit' to stop the program: ")

        if user_input.lower() == "quit":
            break

        try:
            n = int(user_input)
            if n < 1:
                print("Please enter a positive integer.")
                continue

            # Initialize empty board
            board = [['.' for _ in range(n)] for _ in range(n)]
            solutions = []

            print(f"\nSolving {n}-Queens...")
            solve_nqueens(board, 0, n, solutions)

            if solutions:
                print(f"Found {len(solutions)} solution(s):\n")
                print_solutions(solutions)
            else:
                print(f"No solutions exist for {n}-Queens.\n")

        except ValueError:
            print(f"'{user_input}' is not a valid integer. Please try again.")


if __name__ == "__main__":
    main()
