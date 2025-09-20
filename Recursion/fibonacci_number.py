"""
the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, 
starting from 0 and 1. 
That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Examples:
Input : n = 2
Output : 1
Explanation : F(2) = F(1) + F(0) => 1 + 0 => 1.

Input : n = 3
Output : 2
Explanation : F(3) = F(2) + F(1) => 1 + 1 => 2.

Constraints:
0 <= n <= 20

def fib(self, n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    # b will hold the final F(n) value
    return b


"""

n = int(input())

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(n))