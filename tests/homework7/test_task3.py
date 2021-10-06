from homework7.task3 import tic_tac_toe_checker


def test_unfinished():
    board1 = [['-', '-', 'o'],
              ['-', 'x', 'o'],
              ['x', 'o', 'x']]
    assert tic_tac_toe_checker(board1) == 'unfinished!'


def test_x_wins():
    board2 = [['-', '-', 'o'],
              ['-', 'o', 'o'],
              ['x', 'x', 'x']]
    assert tic_tac_toe_checker(board2) == 'x wins!'


def test_o_wins():
    board2 = [['-', 'x', 'o'],
              ['x', 'o', 'o'],
              ['x', 'x', 'o']]
    assert tic_tac_toe_checker(board2) == 'o wins!'


def test_draw():
    board2 = [['o', 'o', 'x'],
              ['x', 'x', 'o'],
              ['o', 'x', 'o']]
    assert tic_tac_toe_checker(board2) == 'draw!'
