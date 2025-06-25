class Board:
    def __init__(self, n):
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.n = n

    def is_safe(self, row, col):
        """Check if placing a queen at (row, col) is safe"""

        # Check column
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False

        # Check upper left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check upper right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < self.n:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def solve_nqueens(self, row, solutions):
        """Recursive function to solve n-Queens using backtracking"""

        # Base case: all queens placed
        if row == self.n:
            solutions.append([row[:] for row in self.board])  # Deep copy of solution
            return

        # Try placing queen in each column of current row
        for col in range(self.n):
            if self.is_safe(row, col):
                # Place queen
                self.board[row][col] = 'Q'

                # Recursively place queens in next rows
                self.solve_nqueens(row + 1, solutions)

                # Backtrack - remove queen
                self.board[row][col] = '.'

    def solve_nqueens_once(self, row):
        """Recursive function to solve n-Queens using backtracking, but return only one solution"""

        # Base case: all queens placed, and return the solution
        if row == self.n:
            return [row[:] for row in self.board]

        # Try placing queen in each column of current row
        for col in range(self.n):
            if self.is_safe(row, col):
                # Place queen
                self.board[row][col] = 'Q'

                # Recursively place queens in next rows
                new_board = self.solve_nqueens_once(row + 1)

                # Backtrack - remove queen
                self.board[row][col] = '.'

                # if a solution has been found, then return it
                if len(new_board) > 0:
                    return new_board

        # if a solution has not been found, then return an empty list
        return []

    def print_solutions(self, solutions):
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
            chessboard = Board(int(user_input))
            if chessboard.n < 1:
                print("Please enter a positive integer.")
                continue

            # Initialize empty solutions
            solutions = []

            print(f"\nSolving {chessboard.n}-Queens...")
            chessboard.solve_nqueens(0, solutions)

            if solutions:
                print(f"Found {len(solutions)} solution(s):\n")
                chessboard.print_solutions(solutions)
            else:
                print(f"No solutions exist for {chessboard.n}-Queens.\n")

        except ValueError:
            print(f"'{user_input}' is not a valid integer. Please try again.")


if __name__ == "__main__":
    main()
