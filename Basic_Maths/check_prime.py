"""

Input: n = 5
Output: true
Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

Input: n = 8
Output: false
Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number.

Constraints:
1 <= n <= 5000

"""

n = int(input())
for i in range(2, int(n / 2)):
    if n % i == 0:
        print("not prime")
    else:
        print("prime")
