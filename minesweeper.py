"""Command Line Minesweeper"""
import random


def main():
    """Manages functions for playing game of Minesweeper"""
    board_skeleton, size = make_board()
    board_mines = plant_mines(board_skeleton, size)
    print(board_mines)


def make_board():
    """Build board"""
    while True:
        user_input = input("How big of a board? (no less than 10)")
        try:
            if int(user_input) >= 10:
                board_skeleton_size = int(user_input)
                break
            else:
                print("Too small, must be a value of 10 or more.")
        except ValueError:
            print("Not a value.")
    board_skeleton = [[None for x in range(board_skeleton_size)]
                      for y in range(board_skeleton_size)]  # Build 2d array
    return board_skeleton, board_skeleton_size


def plant_mines(board_skeleton, size):
    """Randomly place mines among board based on size and difficulty"""
    difficulty = 0.0
    while True:
        user_input = input("Select Difficulty (1, 2, 3): ")
        try:
            difficulty = float(user_input) * 0.1  # % to determine frequency
            break
        except ValueError:
            print("Not a proper selection.")
    for x in range(size):
        for y in range(size):
            mine = random.random()
            if mine <= difficulty:
                board_skeleton[x][y] = '*'
            else:
                board_skeleton[x][y] = '.'
    return board_skeleton


if __name__ == "__main__":
    main()
