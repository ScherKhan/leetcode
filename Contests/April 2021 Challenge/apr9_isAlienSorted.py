"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
 The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only
 if the given words are sorted lexicographicaly in this alien language.
"""
from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    pass


def main():
    print(isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
    print('All tests passed')


if __name__ == '__main__':
    main()