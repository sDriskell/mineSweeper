"""Command Line Minesweeper"""
import random


def main():
    """Manages functions for playing game of Minesweeper"""
    board_skeleton, size = make_board()
    board_mines = plant_mines(board_skeleton, size)
    board_answer = place_numbers(board_mines, size)
    board_reveal = make_reveal(size)
    game(board_answer, board_reveal, size)


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
            difficulty = float(user_input) * 0.1  # % of mines on board
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


def place_numbers(board_mines, size):
    """Tally nearby mines and place number value for player to discover"""
    for x in range(size):
        for y in range(size):
            mine_count = 0
            if board_mines[x][y] == ".":
                if x == 0 and y < size - 1:
                    if board_mines[x + 1][y + 1] == "*" or \
                            board_mines[x][y + 1] == "*" or \
                            board_mines[x][y - 1] == "*" or \
                            board_mines[x + 1][y - 1] == "*" or \
                            board_mines[x + 1][y] == "*":
                        mine_count += 1
                    board_mines[x][y] = mine_count
                if x == size - 1 and y < size - 1:
                    if board_mines[x - 1][y] == "*" or \
                            board_mines[x - 1][y - 1] == "*" or \
                            board_mines[x - 1][y + 1] == "*" or \
                            board_mines[x][y + 1] == "*" or \
                            board_mines[x][y - 1] == "*":
                        mine_count += 1
                    board_mines[x][y] = mine_count
                if x < size - 1 and y == 0:
                    if board_mines[x - 1][y] == "*" or \
                            board_mines[x - 1][y + 1] == "*" or \
                            board_mines[x + 1][y + 1] == "*" or \
                            board_mines[x][y + 1] == "*" or \
                            board_mines[x + 1][y] == "*":
                        mine_count += 1
                    board_mines[x][y] = mine_count
                if x < size - 1 and y == size - 1:
                    if board_mines[x - 1][y] == "*" or \
                            board_mines[x - 1][y - 1] == "*" or \
                            board_mines[x][y - 1] == "*" or \
                            board_mines[x + 1][y - 1] == "*" or \
                            board_mines[x + 1][y] == "*":
                        mine_count += 1
                    board_mines[x][y] = mine_count
                if 0 < x < size - 1 and 0 < y < size - 1:
                    if board_mines[x - 1][y] == "*" or \
                            board_mines[x - 1][y - 1] == "*" or \
                            board_mines[x - 1][y + 1] == "*" or \
                            board_mines[x + 1][y + 1] == "*" or \
                            board_mines[x][y + 1] == "*" or \
                            board_mines[x][y - 1] == "*" or \
                            board_mines[x + 1][y - 1] == "*" or \
                            board_mines[x + 1][y] == "*":
                        mine_count += 1
                    board_mines[x][y] = mine_count
                if x == size - 1 and y == size - 1:
                    if board_mines[x - 1][y] == "*" or \
                            board_mines[x - 1][y - 1] == "*" or \
                            board_mines[x][y - 1] == "*":
                        mine_count += 1
                    board_mines[x][y] = mine_count
    for x in range(size):
        for y in range(size):
            if board_mines[x][y] == 0:
                board_mines[x][y] = '.'
    return board_mines


def make_reveal(size):
    """Tracks if part of board is visible to user or not using boolean values"""
    # Build 2d array of False bool flag
    return [[False for x in range(size)] for y in range(size)]


def print_board(board_answer, board_reveal, size):
    """Track and display the board as the player will see it"""
    for x in range(size):
        for y in range(size):
            if board_reveal[x][y] is False:
                print("X", end='')
            else:
                print(board_answer[x][y], end='')
        print()


def won(board_answer, board_reveal, size):
    """Track if game has been won or lost during play"""
    for x in range(size):
        for y in range(size):
            if board_answer[x][y] != '*' or board_reveal[x][y] is not True:
                return False
            else:
                print("You won!")
                return True


def game(board_answer, board_reveal, size):
    """Play and manage game of minesweeper"""
    # used in conjunction to display results for user
    print_board(board_answer, board_reveal, size)
    # TODO: build game loop
    while not won(board_answer, board_reveal, size):
        while True:
            x = input("Give me a X coordinate: ")
            y = input("Give me a Y coordinate: ")
            try:
                x = int(x)
                y = int(y)
                break
            except ValueError:
                print("Not a proper coordinate.")
        board_reveal[x][y] = True
        if board_answer[x][y] == '*':
            print("Boom!")
            return 0
        else:
            print_board(board_answer, board_reveal, size)


if __name__ == "__main__":
    main()
