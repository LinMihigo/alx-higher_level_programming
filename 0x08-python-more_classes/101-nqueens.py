#!/usr/bin/env python3
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col] without
        being attacked.

    Args:
        board (list of list of int): The N×N chessboard.
        row (int): Row index.
        col (int): Column index.

    Returns:
        bool: True if it is safe to place a queen, False otherwise.
    """

    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve(board, col, solutions):
    """Recursively solves the N Queens puzzle using backtracking.

    Args:
        board (list of list of int): The N×N chessboard.
        col (int): The current column being processed.
        solutions (list of list of list of int): A list to store all
            the solutions.

    Returns:
        None
    """

    if col == len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve(board, col + 1, solutions)
            board[i][col] = 0


def nqueens(N):
    """Solve the N Queens puzzle and print all solutions.

    Args:
        N (int): The size of the chessboard (N×N) and number of queens.

    Returns:
        None
    """

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve(board, 0, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(N)
