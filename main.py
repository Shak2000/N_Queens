class Board:
    def __init__(self, n):
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.n = n

    def is_safe(self, row, col):
        """Check if placing a queen at (row, col) is safe"""

        # Check column
        for i in range(self.n):
            if i != row and self.board[i][col] == 'Q':
                return False

        # Check upper left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check lower left diagonal
        i, j = row + 1, col - 1
        while i < self.n and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i += 1
            j -= 1

        # Check upper right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < self.n:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        # Check lower right diagonal
        i, j = row + 1, col + 1
        while i < self.n and j < self.n:
            if self.board[i][j] == 'Q':
                return False
            i += 1
            j += 1

        return True

    def is_valid_board_state(self):
        """Check if the current board state is valid (no queens attack each other)"""
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == 'Q':
                    # Temporarily remove this queen to check if position is safe
                    self.board[row][col] = '.'
                    is_safe = self.is_safe(row, col)
                    self.board[row][col] = 'Q'
                    if not is_safe:
                        return False
        return True

    def find_next_empty_position(self, start_row=0):
        """Find the next empty position starting from start_row"""
        for row in range(start_row, self.n):
            for col in range(self.n):
                if self.board[row][col] == '.':
                    return row, col
        return None, None

    def count_queens_in_row(self, row):
        """Count queens in a specific row"""
        return sum(1 for col in range(self.n) if self.board[row][col] == 'Q')

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

    def solve_from_current_state(self):
        """Solve n-Queens from the current board state"""

        # First check if current state is valid
        if not self.is_valid_board_state():
            return []

        # Count existing queens
        existing_queens = sum(row.count('Q') for row in self.board)

        # If we already have n queens, check if it's a valid solution
        if existing_queens == self.n:
            return [row[:] for row in self.board] if self.is_valid_board_state() else []

        # Find which rows still need queens
        rows_with_queens = set()
        for row in range(self.n):
            if any(self.board[row][col] == 'Q' for col in range(self.n)):
                rows_with_queens.add(row)

        # If any row has more than one queen, it's invalid
        for row in range(self.n):
            if self.count_queens_in_row(row) > 1:
                return []

        # Start solving from the first empty row
        return self._solve_recursive_from_state(0)

    def _solve_recursive_from_state(self, row):
        """Recursive helper for solving from current state"""

        # Base case: processed all rows
        if row == self.n:
            # Check if we have exactly n queens
            total_queens = sum(row.count('Q') for row in self.board)
            return [row[:] for row in self.board] if total_queens == self.n else []

        # If this row already has a queen, move to next row
        if any(self.board[row][col] == 'Q' for col in range(self.n)):
            return self._solve_recursive_from_state(row + 1)

        # Try placing a queen in each column of this row
        for col in range(self.n):
            if self.is_safe(row, col):
                # Place queen
                self.board[row][col] = 'Q'

                # Recursively solve remaining rows
                result = self._solve_recursive_from_state(row + 1)

                # If solution found, return it
                if result:
                    return result

                # Backtrack - remove queen
                self.board[row][col] = '.'

        # No solution found
        return []

    def solve_nqueens_once(self, row):
        """Solve n-Queens from current board state (wrapper for backward compatibility)"""
        return self.solve_from_current_state()

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
