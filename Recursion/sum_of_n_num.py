n = int(input())
sum0 = 0

# by loop
for i in range(1, n + 1):
    sum0 = sum0 + i
print("By Loop: ",sum0)

# by formula
sum1 = int(n * (n + 1) / 2)
print("By Formula: ",sum1)

# by recursion - Functional Way

def sum_n_f(i):
    if i == 0:
        return 0
    return i+sum_n_f(i-1)

sum2 = sum_n_f(n)
print("By Recursion Functional way: ",sum2)

# by recursion - Parameterized way

def sum_n_p(i, sum):
    if i==0:
        return sum
    return sum_n_p(i-1,sum+i)

sum3 = sum_n_p(n,0)
print("By Recursion Parameter way: ",sum3)