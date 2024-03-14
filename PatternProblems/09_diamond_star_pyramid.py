print("Program Started")
n = int(input())
num_str = ""
# upper pyramid
for i in range(0,n):
    num_str = num_str+" "*(n-i)
    num_str = num_str+"*"*((i*2)+1)
    print(num_str)
    num_str=""

for i in range(n,0,-1):
    num_str = num_str+" "*(n-i+1)
    num_str = num_str+"*"*((i-1)*2+1)
    print(num_str)
    num_str = ""
print("Program Completed")