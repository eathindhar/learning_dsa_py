n = int(input())

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    
    return ans

print(factorial(n))


def factorial_r(i):
    if i ==0:
        return 1
    return i * factorial_r(i-1)

print(factorial_r(n))