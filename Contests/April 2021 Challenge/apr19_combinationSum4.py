"""
Given an array of distinct integers nums and a target integer target, return the number of possible 
combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.
"""
import time
from typing import List

def combinationSum4(nums: List[int], target: int) -> int:
    return 0

def main():
    start_time = time.time()
    assert combinationSum4([1,2,3], 4) == 7
    assert combinationSum4([9], 3) == 0
    print(f'All tests passed. Took {time.time() - start_time:.3f} seconds')


if __name__ == '__main__':
    main()