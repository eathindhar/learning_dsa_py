"""
Input: n1 = 4, n2 = 6
Output: 2

Input: n1 = 9, n2 = 8
Output: 1

1 <= n1, n2 <= 1000
"""

n1 = int(input())
n2 = int(input())
gcd = 1
if 1 <= n1 <= 1000 and 1 <= n2 <= 1000:
    if n1>n2:
        div = n2
    else:
        div = n1
    
    for i in range(1,div+1):
        if ((n1%i == 0) and (n2%i == 0)):
            gcd = i

print(gcd)
    
