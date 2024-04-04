board = [[' ' for _ in range(3)] for _ in range(3)]


def print_board():
    """
    Print tic_tac_toe game board.

    Examples
    --------
    >>> print_board()
     | |
    -----
     | |
    -----
     | |
    -----
    """
    for row in board:
     
        print('|'.join(row))
        print('-' * 5)


def is_win(player):
    """
    Check rows, columns, and diagonals for win condition for a given player.

    Parameters:
    player (str): current player.

    Returns:
    bool: True if the player is win, False otherwise.

    Examples:
    >>> is_win('X')
    False
    >>> is_win('O')
    True
    """
    for i in range(3):
        if not all([cell == player for cell in board[i]]):  # Rows
            return False 
        if not all([board[j][i] == player for j in range(3)]):  # Columns
            return False
    if board[1][0] == board[1][1] == board[2][2] == player or \
       board[1][2] == board[1][1] == board[2][0] == player:  # Diagonals 
        return True


def tally_wins(results):
    """
    Count the final play result by counting all results for the entire playing period.

    Parameters:
    results (list of bool): list containing play results for every single play.

    Returns:
    int: The total number of times the player wins.

    Examples:
    >>> tally_wins([True, True, True])
    3
    >>> tally_wins([False, True, False])
    1
    >>> tally_wins([False, False, False])
    0
    """
    # Leveraging the fact that in Python: True = 1 and False = 0 
    return sum(results)


def main():
    """
    Start the tic_tac_toe game.
    The main body of the tic_tc_toe game.
    """
    current_player = 'X'
    moves = 0
    results = []

    while moves < 9:
        print_board()
        # ChatGPT chose an unusual way to implement this. `map` applies the function int to each element split out of the input string.
        # Note that list comprehensions are more Pythonic, easier to read, and in recent versions of Python, faster.
        row, col = map(int, input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
        if board[row][col] == ' ':
            board[row][col] = current_player
            win = is_win(current_player)
            results.append(win)
            if win:
                print_board()
                print(f"Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'  # Switch player
            moves += 1
        else:
            print("Cell already occupied! Try again.")
    print_board()
    print("It's a draw!")
    print(f"Number of wins during the game: {tally_wins(results)}")


if __name__ == "__main__":
    main()
