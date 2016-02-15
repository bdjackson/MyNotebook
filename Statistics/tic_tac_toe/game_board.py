"""
File: game_board.py
Author: Brett Jackson <bjack3@gmail.com>
Version: 3.5.0

Game board class for tic tac toe studies

"""

# ==============================================================================
class GameBoard(object):
    """Simple class to keep track of a tic tac toe game board

    """
    # --------------------------------------------------------------------------
    def __init__(self):
        """Constructor for GameBoard class. This initializes an empty board

        Args:
            Nothing

        Returns:
            Nothing

        Example:
            TODO

        """
        self.board = [[None]*3 for _ in range(3)]
        self.current_move = 'x'


    # --------------------------------------------------------------------------
    def print(self):
        """Print the current state of the board

        Args:
            Nothing

        Returns:
            Nothing

        Example:
            TODO

        """
        print('\n-----\n'.join(['|'.join([' ' if _element is None else _element
                                          for _element in _row])
                                for _row in self.board]))
        print()


    # --------------------------------------------------------------------------
    def make_move(self, row, col):
        """make move for the next player

        Args:
            row (int): row for next move
            col (int): col for next move

        Returns:
            bool: was the move successful

        Example:
            TODO

        """
        if col<0 or col>len(self.board) or row<0 or row>len(self.board[0]):
            print('invalid space')
            return False

        if self.board[row][col] is not None:
            return False

        self.board[row][col] = self.current_move
        self.next_move()

        return True


    # --------------------------------------------------------------------------
    def next_move(self):
        """TODO

        Args:
            TODO

        Returns:
            TODO

        Example:
            TODO

        """
        self.current_move = 'x' if self.current_move == 'o' else 'o'


    # --------------------------------------------------------------------------
    def winner(self):
        """Is this game won? If yes, who is the winner

        Args:
            Nothing

        Returns:
            str: Winner if the game has been won. Else, None

        Example:
            TODO

        """
        if self.__test_elements__([(0,0), (0,1), (0,2)]):
            return self.board[0][0]
        if self.__test_elements__([(1,0), (1,1), (1,2)]):
            return self.board[1][0]
        if self.__test_elements__([(2,0), (2,1), (2,2)]):
            return self.board[2][0]

        if self.__test_elements__([(0,0), (1,0), (2,0)]):
            return self.board[0][0]
        if self.__test_elements__([(0,1), (1,1), (2,1)]):
            return self.board[0][1]
        if self.__test_elements__([(0,2), (1,2), (2,2)]):
            return self.board[1][2]

        if self.__test_elements__([(0,0), (1,1), (2,2)]):
            return self.board[0][0]
        if self.__test_elements__([(0,2), (1,1), (2,0)]):
            return self.board[0][2]

        return None

    # --------------------------------------------------------------------------
    def __test_elements__(self, elements):
        """Test a list of elements to determine if they are all the same and
            not filled by None values

        Args:
            elements (list): List of tuples (row, col) of the elements to be
                             tested

        Returns:
            bool: Do the elements match or not?

        Example:
            TODO

        """
        if len(elements) == 0:
            return False

        first = self.board[elements[0][0]][elements[0][1]]
        if first is None:
            return False

        for _next in elements:
            next_value = self.board[_next[0]][_next[1]]
            if next_value is None or next_value != first:
                return False

        return True


# ==============================================================================
if __name__ == '__main__':
    board = GameBoard()
    print('the winner is:', board.winner())
    board.print()

    board.make_move(0,0)
    print('the winner is:', board.winner())
    board.print()

    board.make_move(1,0)
    print('the winner is:', board.winner())
    board.print()

    board.make_move(1,0)
    print('the winner is:', board.winner())
    board.print()

    board.make_move(1,1)
    print('the winner is:', board.winner())
    board.print()

    board.make_move(0,0)
    print('the winner is:', board.winner())
    board.print()

    board.make_move(0,1)
    print('the winner is:', board.winner())
    board.print()

    board.make_move(2,2)
    print('the winner is:', board.winner())
    board.print()
