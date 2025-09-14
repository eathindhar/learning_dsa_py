""""

21. 21_hollow_rectangle.py
    ******
    *    *
    *    *
    *    *
    *    *
    ******

"""

print("Program Started")
n = int(input())
num_str = ""
for i in range(n):
    if i == 0 or i == n-1:
        num_str = num_str+"*"*(n)
    else:
        num_str = num_str+"*"+" "*(n-2)+"*"
    print(num_str)
    num_str=""

print("Program Completed")