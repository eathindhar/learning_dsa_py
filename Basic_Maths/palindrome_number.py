"""
Input: n = 121
Output: true

Input: n = 123
Output: false

0 <= n <= 5000
n will contain no leading zeroes except when it is 0 itself.
"""

n = int(input())

rev = str(n)[::-1]
if str(n) == rev :
    print("true")
else :
    print("false")
