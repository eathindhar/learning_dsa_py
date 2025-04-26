#Input: n = 25
#Output: 52
#Input: n = 123
#Output: 321


def reverse_func(n):
    rev_num = ""
    while n>0:
        temp = n % 10
        rev_num = rev_num+str(temp)
        n=int(n/10)
    return int(rev_num)

n = int(input())

if n == 0:
    print(n)
elif n<0:
    n=n*-1
    rnum = reverse_func(n) *-1
    print(rnum)
else:
    rnum = reverse_func(n)
    print(rnum)
    

