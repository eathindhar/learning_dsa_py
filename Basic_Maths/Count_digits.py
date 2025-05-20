"""
Input: n = 5
Output: true
Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

Input: n = 8
Output: false
Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number.

1 <= n <= 5000
"""




def check_prime(n):
    if n == 0 or n == 1:
        return False
    elif n ==2 or n ==3:
        return True
    elif n%2 ==0 or n%3 ==0:
        return False
    i = 5
    while i*i <= n:
        if n%i==0 or n%(i+2) == 0:
            return False
        i += 6
    return True


n = int(input())

is_prime = check_prime(n)

if is_prime:
    print("Prime")
else :
    print("Not Prime")