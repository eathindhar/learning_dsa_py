""""

14. 14_increasing_letter_triangle.py
    A
    A B
    A B C
    A B C D
    A B C D E
    A B C D E F

"""

print("Program Started")
n = int(input())
num_str = ""
count = ord('A')
for i in range(1,n+1):
    for j in range(1,i+1):
        num_str = num_str + chr(count)
        count = count + 1
    print(num_str)
    num_str=""
    count = ord("A")

print("Program Completed")