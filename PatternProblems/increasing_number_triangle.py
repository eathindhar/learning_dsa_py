print("Program Started")
n = int(input())
num_str = ""
count = 1
for i in range(1,n+1):
    for j in range(0,i):
        num_str = num_str + str(count) + " "
        count = count + 1
    print(num_str)
    num_str=""


print("Program Completed")