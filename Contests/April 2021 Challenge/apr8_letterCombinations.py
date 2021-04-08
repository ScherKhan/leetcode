"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could 
represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

"""
from typing import List

mapping = {2: 'abc', 
           3: 'def',
           4: 'ghi', 
           5: 'jkl', 
           6: 'mno',
           7: 'pqrs', 
           8: 'tuv', 
           9: 'wxyz'}

def letterCombinations(digits: str) -> List[str]:
    combs = []
    for digit in digits:
        letters = mapping[int(digit)]
        if len(combs) == 0:
            combs = [l for l in letters]
        else:
            combs = [comb + l for comb in combs for l in letters]

    return combs


def main():
    print(letterCombinations('23'))
    assert letterCombinations('23') == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert letterCombinations('') == [], 'Empty input'
    assert letterCombinations('2') == ['a', 'b', 'c'], 'Single digit'
    print('All tests passed')


if __name__ == '__main__':
    main()