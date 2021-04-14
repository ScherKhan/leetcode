"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may 
not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""

from typing import List, Tuple
import time

directions = [(1, 0),  #S
              (0, 1),  #E
              (-1, 0), #N
              (0, -1)] #W

m, n = 0, 0
visited = []

def longestIncreasingPath(matrix: List[List[int]]) -> int:
    global m, n
    m = len(matrix)
    n = len(matrix[0])
    longest_path = []
    cell_to_path = dict()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) not in longest_path:
                path = _dfs(i, j, matrix, cell_to_path)
                if len(path) > len(longest_path):
                    longest_path = path
    return len(longest_path)


def _dfs(r, c, matrix, cell_to_path):
    if (r, c) not in cell_to_path:
        cell_to_path[(r, c)] = [(r, c)]
        # finding longest path so far
        path = [(r, c)]
        for d in directions:
            if can_go(r, c, d) and matrix[r][c] < matrix[r + d[0]][c + d[1]]:
                path = _dfs(*move(r, c, d), matrix, cell_to_path)
                # update dictionary with max path
                if len(cell_to_path.get((r, c))) < len(path) + 1:
                    cell_to_path[(r, c)] = [(r, c)] + path

    return cell_to_path[(r, c)]


def move(r: int, c: int, direction: Tuple[int, int]) -> Tuple[int, int]:
    return (r + direction[0], c + direction[1])

def can_go(r: int, c: int, direction: Tuple[int, int]) -> bool:
    r1, c1 = move(r, c, direction)

    return can_go_to(r1, c1)


def can_go_to(r: int, c: int) -> bool:
    global m, n
    return 0 <= r < m and 0 <= c < n

def main():
    start_time = time.time()
    assert longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]) == 4
    assert longestIncreasingPath([[1]]) == 1
    assert longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]) == 4
    assert longestIncreasingPath([[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[0,0,0,0,0,0,0,0,0,0]]) == 70
    assert longestIncreasingPath([[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]) == 140
    print(f"Testing took {time.time() - start_time:.3f} seconds")
    print('All tests passed')


if __name__ == '__main__':
    main()
    