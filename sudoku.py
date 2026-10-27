import random
import sys
from typing import List, Optional, Tuple

class Sudoku:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solution = [[0 for _ in range(9)] for _ in range(9)]
    
    def is_valid(self, board: List[List[int]], num: int, row: int, col: int) -> bool:
        # Check row
        for x in range(9):
            if board[row][x] == num:
                return False
        # Check column
        for x in range(9):
            if board[x][col] == num:
                return False
        # Check box
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True
    
    def solve(self, board: List[List[int]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, num, i, j):
                            board[i][j] = num
                            if self.solve(board):
                                return True
                            board[i][j] = 0
                    return False
        return True
    
    def generate_puzzle(self, difficulty: str = 'medium') -> None:
        # Generate full solution
        self.fill_board(self.solution)
        # Copy solution to board
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.solution[i][j]
        # Remove cells based on difficulty
        if difficulty == 'easy':
            cells_to_remove = 40
        elif difficulty == 'hard':
            cells_to_remove = 55
        else:  # medium
            cells_to_remove = 45
        
        count = 0
        while count < cells_to_remove:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if self.board[i][j] != 0:
                self.board[i][j] = 0
                count += 1
    
    def fill_board(self, board: List[List[int]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    # Randomize numbers
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if self.is_valid(board, num, i, j):
                            board[i][j] = num
                            if self.fill_board(board):
                                return True
                            board[i][j] = 0
                    return False
        return True
    
    def print_board(self, board: Optional[List[List[int]]] = None) -> None:
        if board is None:
            board = self.board
        print("+-------+-------+-------+")
        for i in range(9):
            print("|", end="")
            for j in range(9):
                if board[i][j] == 0:
                    print(" .", end="")
                else:
                    print(f" {board[i][j]}", end="")
                if j % 3 == 2:
                    print(" |", end="")
            print()
            if i % 3 == 2:
                print("+-------+-------+-------+")
    
    def get_hint(self) -> bool:
        # Find first empty cell and fill with solution
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    self.board[i][j] = self.solution[i][j]
                    return True
        return False
    
    def check_solution(self) -> bool:
        # Check if current board is complete and valid
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
                num = self.board[i][j]
                # Temporarily remove to check
                self.board[i][j] = 0
                if not self.is_valid(self.board, num, i, j):
                    self.board[i][j] = num
                    return False
                self.board[i][j] = num
        return True

def main():
    game = Sudoku()
    print("SUDOKU GAME")
    print("=" * 20)
    
    # Select difficulty
    print("\nSelect difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    while True:
        try:
            choice = input("\nEnter choice (1-3): ").strip()
            if choice == '1':
                game.generate_puzzle('easy')
                break
            elif choice == '2':
                game.generate_puzzle('medium')
                break
            elif choice == '3':
                game.generate_puzzle('hard')
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            sys.exit()
    
    print(f"\nPuzzle generated! (Difficulty: {['Easy', 'Medium', 'Hard'][int(choice)-1]})")
    
    while True:
        game.print_board()
        print("\nOptions:")
        print("1. Make a move")
        print("2. Get a hint")
        print("3. Check solution")
        print("4. Show solution")
        print("5. New game")
        print("6. Quit")
        
        try:
            choice = input("\nEnter choice (1-6): ").strip()
            
            if choice == '1':
                try:
                    row = int(input("Enter row (1-9): ")) - 1
                    col = int(input("Enter column (1-9): ")) - 1
                    num = int(input("Enter number (1-9): "))
                    
                    if 0 <= row <= 8 and 0 <= col <= 8 and 1 <= num <= 9:
                        if game.board[row][col] == 0:
                            # Check if move is valid
                            if game.is_valid(game.board, num, row, col):
                                game.board[row][col] = num
                                print("Move placed successfully!")
                                if game.check_solution():
                                    print("\n🎉 Congratulations! You solved the puzzle! 🎉")
                                    game.print_board()
                                    sys.exit()
                            else:
                                print("Invalid move! That number conflicts with existing numbers.")
                        else:
                            print("That cell is already filled!")
                    else:
                        print("Invalid input! Please enter numbers between 1-9.")
                except ValueError:
                    print("Invalid input! Please enter valid numbers.")
                except IndexError:
                    print("Invalid input!")
            
            elif choice == '2':
                if game.get_hint():
                    print("Hint added! A cell has been filled with the correct answer.")
                else:
                    print("No empty cells left!")
            
            elif choice == '3':
                if game.check_solution():
                    print("🎉 Congratulations! The puzzle is solved correctly! 🎉")
                else:
                    print("The puzzle is not complete or has errors. Keep trying!")
            
            elif choice == '4':
                print("\nSolution:")
                game.print_board(game.solution)
                input("\nPress Enter to continue...")
            
            elif choice == '5':
                main()
                return
            
            elif choice == '6':
                print("Thanks for playing!")
                sys.exit()
            else:
                print("Invalid choice. Please enter 1-6.")
        
        except KeyboardInterrupt:
            print("\n\nThanks for playing!")
            sys.exit()

if __name__ == "__main__":
    main()
