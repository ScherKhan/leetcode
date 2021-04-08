"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could 
represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

"""
from typing import List

def letterCombinations(digits: str) -> List[str]:
    pass


def main():
    assert letterCombinations('23') == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert letterCombinations('') == [], 'Empty input'
    assert letterCombinations('2') == ['a', 'b', 'c'], 'Sinble digit'
    print('All tests passed')


if __name__ == '__main__':
    main()