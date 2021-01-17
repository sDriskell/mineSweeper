"""Original Minesweeper project from COMP151; OBSOLETE"""
import random


def game():
    """Play game of minesweeper"""
    board = makeBoard()
    board = plantMines(board)
    board = placeNumbers(board)
    reveal = makeReveal()
    printBoard(board, reveal)
    while not won(board, reveal):
        y = int(input("Give me a X value:"))
        x = int(input("Give me a Y value:"))
        while not (x <= 9 and y <=9 and x >= 0 and y >= 0):
            print("Not a proper grid; try again!")
            y = int(input("Give me a X value:"))
            x = int(input("Give me a Y value:"))
        reveal[x][y] = True
        if board[x][y] == "*":
            print("Boom!")
            return 0
        else:
            printBoard(board, reveal)


def makeBoard():
    """Currently builds a 10x10 board"""
    board = ["."]
    board = board * 10
    for i in range(10):
        board[i] = ["."] * 10
    return board


def plantMines(board):
    """Randomly places mines throughout board"""
    mine = 0
    for x in range(10):
          for y in range(10):
              mine = random.random()
              if mine <= 0.1:
                  board[x][y] = "*"
              else:
                  board[x][y] = "."
    return board


def printBoard(board, reveal):
    """Display board in X's to hide mines"""
    for x in range(10):
        for y in range(10):
            if reveal[x][y] == False:
                print("X", end="")
            else:
                print(board[x][y], end="")
        print()


def makeReveal():
    """Tracks if part of board has been displayed or not using boolean values"""
    reveal = [False]
    reveal = reveal * 10
    for i in range(10):
        reveal[i] = [False] * 10
    return reveal


def placeNumbers(board):
    """Tallys nearby mines and places number value for player"""
    for x in range(10):
        for y in range(10):
            mineCount = 0
            if board[x][y] == "*":
                board[x][y] = "*"
            if board [x][y] == "." and x == 0 and y < 9:
                if board[x+1][y+1] == "*":
                   mineCount = mineCount + 1
                if board[x][y+1] == "*" :
                    mineCount = mineCount + 1
                if board[x][y-1] == "*":
                    mineCount = mineCount + 1
                if board[x+1][y-1] == "*":
                    mineCount = mineCount + 1
                if board[x+1][y] == "*":
                    mineCount = mineCount + 1
                board[x][y] = mineCount
            if board[x][y] == "." and x == 9 and y < 9:
                if board[x-1][y] == "*":
                    mineCount = mineCount + 1
                if board[x-1][y-1] == "*":
                    mineCount = mineCount + 1
                if board[x-1][y+1] == "*":
                    mineCount = mineCount + 1
                if board[x][y+1] == "*" :
                    mineCount = mineCount + 1
                if board[x][y-1] == "*":
                    mineCount = mineCount + 1
                board[x][y] = mineCount
            if board[x][y] == "." and y == 0 and x < 9:
                if board[x-1][y] == "*":
                    mineCount = mineCount + 1
                if board[x-1][y+1] == "*":
                    mineCount = mineCount + 1
                if board[x+1][y+1] == "*":
                   mineCount = mineCount + 1
                if board[x][y+1] == "*" :
                    mineCount = mineCount + 1
                if board[x+1][y] == "*":
                    mineCount = mineCount + 1
                board[x][y] = mineCount
            if board[x][y] == "." and y == 9 and x < 9:
                if board[x-1][y] == "*":
                    mineCount = mineCount + 1
                if board[x-1][y-1] == "*":
                    mineCount = mineCount + 1
                if board[x][y-1] == "*":
                    mineCount = mineCount + 1
                if board[x+1][y-1] == "*":
                    mineCount = mineCount + 1
                if board[x+1][y] == "*":
                    mineCount = mineCount + 1
                board[x][y] = mineCount
            if board[x][y] == "." and x > 0 and x < 9 and y > 0 and y < 9:
                if board[x-1][y] == "*":
                    mineCount = mineCount + 1
                if board[x-1][y-1] == "*":
                    mineCount = mineCount + 1
                if board[x-1][y+1] == "*":
                    mineCount = mineCount + 1
                if board[x+1][y+1] == "*":
                   mineCount = mineCount + 1
                if board[x][y+1] == "*" :
                    mineCount = mineCount + 1
                if board[x][y-1] == "*":
                    mineCount = mineCount + 1
                if board[x+1][y-1] == "*":
                    mineCount = mineCount + 1
                if board[x+1][y] == "*":
                    mineCount = mineCount + 1
                board[x][y] = mineCount
            if board[x][y] == "." and x == 9 and y == 9:
                if board[x-1][y] == "*":
                    mineCount = mineCount + 1
                if board[x-1][y-1] == "*":
                    mineCount = mineCount + 1
                if board[x][y-1] == "*":
                    mineCount = mineCount + 1
                board[x][y] = mineCount
    return board

def won(board, reveal):
    """Tracks if game has been won yet or not"""
    for x in range(10):
        for y in range(10):
            if board[x][y] != "*" or board[x][y] != True:
                return False
            else:
                print("You won!")
                return True


if __name__ == "__main__":
    game()

