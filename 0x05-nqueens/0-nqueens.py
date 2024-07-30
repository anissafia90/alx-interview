#!/usr/bin/python3
"""
N queens problem
- Approach: Backtracking
    - Use backtracking to find all possible paths
    - Check if the path is valid
        - Check if the column is valid
        - Check if the positive diagonal is valid
        - Check if the negative diagonal is valid
    - Add the queen's location to the path
    - Continue if the path is valid until we reach the end of the board
    - Backtrack if the path is not valid and try another path
    - Add path to the result if we reach the end of the board
- Analysis:
    - Time: O(n!) - n is the number of queens
        - We have n choices for the first queen, n - 1 choices for the
          second queen,n - 2 choices for the third queen, etc.
    - Space: O(n^2) - n is the number of queens
"""

import sys


def n_queens(n):
    """ N queens solution """
    queens, res = [], []
    cols, positive_diag, negative_diag = set(), set(), set()

    def backtrack(row, n, queens):
        """ Backtracking function """
        if row == n:
            res.append(queens[:])
            return
        for col in range(n):
            if (col in cols or row + col in positive_diag or
                    row - col in negative_diag):
                continue
            cols.add(col)
            positive_diag.add(row + col)
            negative_diag.add(row - col)
            queens.append([row, col])
            backtrack(row + 1, n, queens)

            cols.remove(col)
            positive_diag.remove(row + col)
            negative_diag.remove(row - col)
            queens.pop()
    backtrack(0, n, queens)
    return res


def check_args(n):
    """ Check if n is a valid argument """
    if not n.isdigit():
        print("N must be a number")
        exit(1)
    if int(n) < 4:
        print("N must be at least 4")
        exit(1)


def main():
    """ Main function """
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        exit(1)
    n = args[1]
    check_args(n)
    solutions = n_queens(int(n))
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()