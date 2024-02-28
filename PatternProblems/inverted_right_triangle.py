num = int(input())

for i in reversed(range(num+1)):
    print("*"*i)
    print(i)

for i in range(num+1):
    print("*"*(num-i))
    print(num-i)