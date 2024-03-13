print("Program Started")
n = int(input())
num_str = ""
list = []
for i in range(1,n):
    num_str = num_str + "*" * (i)
    num_str = num_str + " " * (n-i)
    num_str = num_str + " " * (n-i)
    num_str = num_str + "*" * (i)
    list.append(num_str)
    num_str=""

for i in range(n):
    num_str = num_str + "*" * (n-i)
    num_str = num_str + " " * (i)
    num_str = num_str + " " * (i)
    num_str = num_str + "*" * (n-i)
    list.append(num_str)
    num_str=""

for i in list:
    print(i)

print("Program Completed")