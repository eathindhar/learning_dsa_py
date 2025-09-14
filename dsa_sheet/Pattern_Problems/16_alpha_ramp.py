""""

16. 16_alpha_ramp.py
    A 
    B B
    C C C
    D D D D
    E E E E E
    F F F F F F

"""

print("Program Started")
n = int(input())
num_str = ""
count = ord("A")
for i in range(1,n+1):
    for j in range(1,i+1):
        num_str = num_str + chr(count) + " "
    print(num_str)
    num_str = ""
    count = count + 1

print("Program Completed")