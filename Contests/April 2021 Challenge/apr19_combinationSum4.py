"""
Given an array of distinct integers nums and a target integer target, return the number of possible 
combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.
"""
import time
from typing import List


def combinationSum4(nums: List[int], target: int) -> int:
    # solution from forum
    # top down solution
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if num <= i: dp[i] += dp[i - num]
    return dp[target]


_cache = dict()


def combinationSum4_1(nums: List[int], target: int) -> int:
    # MINE solution: veeery slow
    nums = [i for i in nums if i <= target]
    if _cache.get((tuple(nums), target)):
        return _cache.get((tuple(nums), target))
    count = 0
    for el in nums:
        if el == target:
            count += 1
        else:
            comb = combinationSum4(nums, target - el)
            _cache[(tuple(nums), target - el)] = comb
            count  += comb
    return count


def main():
    start_time = time.time()
    #print(combinationSum4([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], 31))
    assert combinationSum4([1,2,3], 4) == 7
    assert combinationSum4([9], 3) == 0
    assert combinationSum4([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], 31) == 1073741824
    print(f'All tests passed. Took {time.time() - start_time:.3f} seconds')


if __name__ == '__main__':
    main()