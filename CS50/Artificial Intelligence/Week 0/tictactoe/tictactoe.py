"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                counter += 1
            elif board[i][j] == O:
                counter -= 1

    if counter == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions_set.append((i, j))

    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for sign in [X, O]:
        for i in range(3):
            if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
                return sign
            elif board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
                return sign

        if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return sign
        elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
            return sign

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in range(3):
            if EMPTY in board[i]:
                return False

        return True

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)

    if won == X:
        return 1
    elif won == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if len(actions(board)) == 9:
        action = actions(board)
        return action[random.randint(0, len(actions(board)) - 1)]

    if terminal(board):
        return None

    best_move = None

    if player(board) == X:
        best_score = -1
    else:
        best_score = 1

    for action in actions(board):
        if player(board) == X:
            score = minimize(result(board, action))

            if score >= best_score:
                best_move = action
                best_score = score
        else:
            score = maximize(result(board, action))

            if score <= best_score:
                best_move = action
                best_score = score

    return best_move


def maximize(board):
    if terminal(board):
        return utility(board)

    score = -1

    for action in actions(board):
        score = max(score, minimize(result(board, action)))

    return score

def minimize(board):
    if terminal(board):
        return utility(board)

    score = 1

    for action in actions(board):
        score = min(score, maximize(result(board, action)))

    return score
