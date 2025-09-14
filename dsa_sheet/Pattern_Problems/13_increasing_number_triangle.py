""""

13. 13_increasing_number_triangle.py
    1
    2  3
    4  5  6
    7  8  9  10
    11  12  13  14  15
    16  17  18  19  20  21

"""

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