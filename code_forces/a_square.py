test_cases = int(input())

for i in range(test_cases):
    a,b,c,d = input().split(' ')
    if a == b == c == d:
        print("YES")
    else:
        print("NO")


