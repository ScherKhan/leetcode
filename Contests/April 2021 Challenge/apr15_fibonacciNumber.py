"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number
 is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""
import time


def fib(n: int) -> int:
    if n in [0, 1]:
            return n
        
    return fib(n-1) + fib(n-2)


def main():
    start_time = time.time()
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(30) == 832040
    assert fib(15) == 610
    assert fib(4) == 3
    print(f'All tests passed. Took {time.time() - start_time:.3f} seconds')


if __name__ == '__main__':
    main()