# Sudoku Game

A Python implementation of the classic Sudoku puzzle game with a command-line interface.

## Features

- Generate puzzles at three difficulty levels: Easy, Medium, and Hard
- Interactive CLI gameplay
- Move validation to prevent invalid placements
- Hint system to help when stuck
- Solution checker
- Option to view the complete solution

## How to Play

Run the game with:

`ash
python sudoku.py
`

1. Select your difficulty level (Easy/Medium/Hard)
2. Use the menu to make moves, get hints, or check your progress
3. Fill in all empty cells with numbers 1-9 following Sudoku rules
4. Each row, column, and 3x3 box must contain all numbers 1-9 exactly once

## Controls

- Make a move: Enter row, column, and number
- Get a hint: Reveals one correct cell
- Check solution: Validates your current progress
- Show solution: Displays the complete solved puzzle
- New game: Start a fresh puzzle
- Quit: Exit the game
