"""
An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

Input: n = 153
Output: true
Explanation: Number of digits : 3.
1 ^ 3 + 5 ^ 3 + 3 ^ 3 = 1 + 125 + 27 = 153.


Input: n = 12
Output: false
Explanation: Number of digits : 2.
1 ^ 2 + 2 ^ 2 = 1 + 4 = 5.

Constraints:
0 <= n <= 5000

"""

n = int(input())

if 0 <= n <= 5000 :
    n_str = str(n)
    pow = len(n_str)
    total = sum(int(digit) ** pow for digit in n_str)
    if total == n:
        print("true")
    else:
        print("false")
else:
    print("false")