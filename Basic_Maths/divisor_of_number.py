"""

Input: n = 6
Output = [1, 2, 3, 6]
Explanation: The divisors of 6 are 1, 2, 3, 6.

Input: n = 8
Output: [1, 2, 4, 8]
Explanation: The divisors of 8 are 1, 2, 4, 8.

Constraints:
1 <= n <= 1000

"""

n = int(input())
arr = []

if 1 <= n <= 1000:
    for i in range(1,int(n/2)+1):
        if n%i==0:
            arr.append(i)
    arr.append(n)
else:
    arr.append(0)

print(arr)