"""
File: game_counter.py
Author: Brett Jackson <bjack3@gmail.com>
Version: 3.5.0

<DESCRITION>

"""

# ==============================================================================
from itertools import product
from game_board import GameBoard
from collections import defaultdict


# ------------------------------------------------------------------------------
def test_move(board, row, col, results=None, move=1):
    """TODO

    Args:
        TODO

    Returns:
        TODO

    Example:
        TODO

    """
    # create default for results if needed
    if results is None:
        results = defaultdict(int)

    # if illegal move, back out
    if not board.make_move(row, col):
        return results

    ## print('  '*move, 'move:', move, ': ', row, col)

    if board.winner() is not None:
        ## print('  '*move, '  ', move, 'winner!')
        ## board.print()
        results[move] += 1
    elif move == 9:
        ## print('  '*move, '  draw!')
        ## board.print()
        results['draw'] += 1
    else:
        for _row, _col in product(range(3), range(3)):
            if _row == row and _col == col:
                continue
            results = test_move(board, _row, _col, results, move+1)

    # undo this move
    board.board[row][col] = None
    board.next_move()
    return results


# ==============================================================================
if __name__ == '__main__':
    board = GameBoard()
    results = None
    for _row, _col in product(range(3), range(3)):
        print('First move:', _row, _col)
        results = test_move(board, _row, _col, results)
    total = sum(results.values())

    for _game_result in sorted(results.keys(), key=lambda x: str(x)):
        print('Game result: {} - number games: {} - fraction: {}'.format(
                _game_result,
                results[_game_result],
                round(results[_game_result]/total, 2)))

