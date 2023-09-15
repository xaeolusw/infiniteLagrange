import sys
import time

SIZE = 5
total = 0


def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()


def patrol(board, row, col, step=1):
    if row >= 0 and row < SIZE and \
        col >= 0 and col < SIZE and \
        board[row][col] == 0:
        board[row][col] = step
        if step == SIZE * SIZE:
            global total
            total += 1
            print(f'第{total}种走法: ')
            # print_board(board)
            test_pos (board, row, col)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0

def test_pos (board, row, col):
    if row - 2 >= 0 and row - 2 < SIZE :
       if col - 1 >=0 and col - 1 < SIZE:
           if board[row - 2][col - 1] == 1:
               print_board(board)
       elif col + 1 >= 0 and col + 1 < SIZE:
           if board[row - 2][col + 1] == 1:
               print_board(board)
    elif row - 1 >= 0 and row - 1 < SIZE :
       if col - 2 >=0 and col - 2 < SIZE:
           if board[row - 1][col - 2] == 1:
               print_board(board)
       elif col + 2 >= 0 and col + 2 < SIZE:
           if board[row - 1][col + 2] == 1:
               print_board(board)
    elif row + 1 >= 0 and row + 1 < SIZE :
       if col - 2 >=0 and col - 2 < SIZE:
           if board[row + 1][col - 2] == 1:
               print_board(board)
       elif col + 2 >= 0 and col + 2 < SIZE:
           if board[row + 1][col + 2] == 1:
               print_board(board)
    elif row + 2 >= 0 and row + 2 < SIZE :
       if col - 1 >=0 and col - 1 < SIZE:
           if board[row + 2][col - 1] == 1:
               print_board(board)
       elif col + 1 >= 0 and col + 1 < SIZE:
           if board[row + 2][col + 1] == 1:
               print_board(board)

  
def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            patrol(board, i, j)


if __name__ == '__main__':
    main()