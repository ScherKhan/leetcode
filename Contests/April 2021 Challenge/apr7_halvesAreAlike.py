vowels = 'euioa'


def halvesAreAlike(s: str) -> bool:
    one, two = s[:len(s)//2].lower(), s[len(s)//2:].lower()

    return countVowels(one) == countVowels(two)


def countVowels(s: str) -> int:
    count = 0
    for c in s:
        count += [0, 1][c in vowels]
    return count



def main():
    assert halvesAreAlike('somethin') == False
    assert halvesAreAlike('book') == True
    assert halvesAreAlike('textbook') == False
    assert halvesAreAlike('MerryChristmas') == False
    assert halvesAreAlike('AbCdEfGh') == True
    assert halvesAreAlike('aaaaEEEE') == True
    assert halvesAreAlike('aB') == False
    print('All tests passed')


if __name__ == '__main__':
    main()