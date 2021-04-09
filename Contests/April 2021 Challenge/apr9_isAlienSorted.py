"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
 The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only
 if the given words are sorted lexicographicaly in this alien language.
"""
from typing import List
from string import ascii_lowercase

def isAlienSorted(words: List[str], order: str) -> bool:
    alphabet = ascii_lowercase[:len(order)]
    translated = [''.join(map(lambda x: alphabet[order.index(x)], word)) for word in words]
    #print(translated, sorted(translated))
    return translated == sorted(translated)


def main():
    print(isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
    assert isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True
    assert isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz") == False
    assert isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz") == False
    assert isAlienSorted(["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz") == True
    print('All tests passed')


if __name__ == '__main__':
    main()