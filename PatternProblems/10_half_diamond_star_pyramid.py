print("Program Started")
n = int(input())
num_str = ""
for i in range(0,2*n+1):
    if i <= n:
        num_str = num_str + "*"*(i+1)
        print(num_str)
        num_str=""
    else:
        num_str = num_str + "*"*((2*n-i)+1)
        print(num_str)
        num_str=""

print("Program Completed")