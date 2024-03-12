print("Program Started")
n = int(input())
num_str = ""
count = ord("A")
for i in range(n,0,-1):
    for j in range(i,0,-1):
        num_str = num_str + chr(count) + " "
        count = count + 1
    print(num_str)
    num_str = ""
    count = ord("A")

print("Program Completed")