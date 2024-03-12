n = int(input())
num_str = ""
for i in range(1,n+1):
    for j in range(1,i+1):
        num_str = num_str+str(i)
    print(num_str)
    num_str = ""