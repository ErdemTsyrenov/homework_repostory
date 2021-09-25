"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from collections import Counter
from typing import List


def check_horizontal(board: List[List], symbol: str) -> bool:
    for line in board:
        if Counter(line)[symbol] == len(line):
            return True
    return False


def check_vertical(board: List[List], symbol: str):
    for col in list(zip(*board)):
        if Counter(col)[symbol] == len(col):
            return True
    return False


def check_diags(board: List[List], symbol: str):
    main_diag = [board[i][i] for i in range(len(board))]
    side_diag = [board[-i - 1][i] for i in range(len(board))]
    return Counter(main_diag)[symbol] == len(board) or \
        Counter(side_diag)[symbol] == len(board)


def check_if_x_wins(board: List[List]) -> bool:
    return check_horizontal(board, 'x') or \
           check_vertical(board, 'x') or \
           check_diags(board, 'x')


def check_if_o_wins(board: List[List]) -> bool:
    return check_horizontal(board, 'o') or \
           check_vertical(board, 'o') or \
           check_diags(board, 'o')


def check_if_unfinished(board: List[List]) -> bool:
    for line in board:
        if '-' in line:
            return True
    return False


def tic_tac_toe_checker(board: List[List]) -> str:
    if check_if_x_wins(board):
        return "x wins!"
    elif check_if_o_wins(board):
        return "o wins!"
    elif check_if_unfinished(board):
        return "unfinished!"
    else:
        return "draw!"
