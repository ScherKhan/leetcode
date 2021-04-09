"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
 The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only
 if the given words are sorted lexicographicaly in this alien language.
"""
from typing import List
from string import ascii_lowercase
from itertools import zip_longest

def isAlienSorted(words: List[str], order: str) -> bool:
        # prepate dictionary with mapping letter: order_index
        letter_order = {l:i for i, l in enumerate(order)}
        
        i = 0
        # compare all the pairs of the words if they are position correct
        # if any of the pairs is incorrect then return False
        while i < len(words) - 1:
            word1 = words[i]
            word2 = words[i+1]
            
            # check every letter that it is in right order
            for l1, l2 in zip_longest(word1, word2):
                # If second word is shorter than first one
                if l2 is None:
                    return False
                elif l1 is None:
                    break
                
                if letter_order[l2] == letter_order[l1]:
                    # if letters are the same that's fine
                    continue
                    
                elif letter_order[l2] > letter_order[l1]:
                    # if second word is already higher don't need to check other letters
                    break
                else:
                    # second word is lower that the first one
                    #print(f'Letters {l1}({letter_order[l1]}) and {l2}({letter_order[l2]})')
                    return False

            # go to the next pair            
            i += 1
                
        return True



def isAlienSorted2(words: List[str], order: str) -> bool:
    alphabet = ascii_lowercase[:len(order)]
    translated = [''.join(map(lambda x: alphabet[order.index(x)], word)) for word in words]
    #print(translated, sorted(translated))
    return translated == sorted(translated)


def main():
    print(isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
    assert isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True
    assert isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz") == False
    assert isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz") == False, 'Shorter word must by first'
    assert isAlienSorted(["app","apple"], "abcdefghijklmnopqrstuvwxyz") == True, 'Shorter word is first'
    assert isAlienSorted(["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz") == True
    print('All tests passed')


if __name__ == '__main__':
    main()