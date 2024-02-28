num = int(input())
num_str = ""
for i in range(1,num+1):
    for j in range(1,i+1):
        num_str = num_str+str(j)
    print(num_str)
    num_str = ""