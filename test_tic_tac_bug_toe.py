import unittest
from unittest.mock import patch
from io import StringIO
from tic_tac_bug_toe import print_board, is_win, tally_wins

class TestTicTacToe(unittest.TestCase):

    def test_print_board(self):
        expected_output = " | | \n-----\n | | \n-----\n | | \n-----\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_board()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_is_win(self):
        board_X = [['X', 'O', 'O'],
                    [' ', 'X', ' '],
                    [' ', ' ', 'X']]
        self.assertTrue(is_win('X', board_X))

        board_O = [['X', 'O', 'O'],
                    ['X', 'O', ' '],
                    ['O', 'X', ' ']]
        self.assertTrue(is_win('O', board_O))

        board_none = [['X', 'O', 'O'],
                        [' ', ' ', ' '],
                        [' ', 'X', ' ']]
        self.assertFalse(is_win('O', board_none))

    def test_tally_wins(self):
        results = [True, True, False, True, False]
        self.assertEqual(tally_wins(results), 3)


if __name__ == '__main__':
    unittest.main()