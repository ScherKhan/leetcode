"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may 
not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""

from typing import List

directions = [(1, 0),
                (0, 1),
                (-1, 0),
                (0, -1)]



def longestIncreasingPath(matrix: List[List[int]]) -> int:
    return 0


def main():
    print(longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
    print('All tests passed')


if __name__ == '__main__':
    main()
    